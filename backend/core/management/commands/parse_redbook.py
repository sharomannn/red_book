import os
import re

import requests
from bs4 import BeautifulSoup
from django.conf import settings  # Нужно для MEDIA_ROOT
from django.core.management.base import BaseCommand
from requests.exceptions import RequestException, SSLError

from core.consts import CATEGORY
from core.models import Family, Order, RedBookEntry, Section

# Словарь для сопоставления категорий по первым двум словам
category_mapping = {
    '1-я категория.': CATEGORY.ENDANGERED_SPECIES,
    '2-я категория.': CATEGORY.VULNERABLE_SPECIES,
    '3-я категория.': CATEGORY.RARE_SPECIES,
    '4-я категория.': CATEGORY.UNKNOWN_SPECIES,
    '5-я категория.': CATEGORY.RECOVERING_SPECIES,
}

# Базовый URL для скачивания страниц
BASE_URL = 'https://cicon.ru'


class Command(BaseCommand):
    help = 'Скачивание и парсинг HTML файлов для Красной книги'

    def add_arguments(self, parser):
        parser.add_argument('directory_path', type=str, help='Путь к директории для сохранения HTML файлов')

    def handle(self, *args, **kwargs):
        directory_path = kwargs['directory_path']
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        # Задаём список ссылок для скачивания
        links = [
            '/spisok-pt-mosobl.html',
            '/malaya-poganka-mosobl.html',
            '/podicepsgrisegena-mo.html',
            '/upper-ford-near.html',
            '/cap_bily.html',
            '/ciconia_nigra_mosobl.html',
            '/anser_anser_mo.html',
            '/anser_erythropus_mo.html',
            '/cygnus_cygnus_mo.html',
            '/anas_strepera_mo.html',
            '/northern_pintails.html',
            '/skopa-mo.html',
            '/osoed-mo.html',
            '/milvus_migrans_govinda.html',
            '/northern_hen_harrier.html',
            '/pallid_harrier_mo.html',
            '/harrier_female.html',
            '/zmeeyad-mo.html',
            '/booted_eagle_mo.html',
            '/greater_Sspotted_eagle.html',
            '/aquila_pomarina_orlik.html',
            '/aquila_chrysaetos.html',
            '/haliaeetus_albicilla.html',
            '/falco_cherrug_mo.html',
            '/falco_peregrinus_mo.html',
            '/falco_columbarius_male.html',
            '/falco_vespertinus_mo.html',
            '/willow_grouse_standing.html',
            '/grus_grus_mo.html',
            '/pastushok-mo.html',
            '/porzana_parva.html',
            '/haematopus_ostralegus.html',
            '/common_greenshank.html',
            '/travnik-mo.html',
            '/tringa_stagnatilis.html',
            '/xenus_cinereus.html',
            '/philomachus_pugnax.html',
            '/gallinago_media.html',
            '/kronshep-mo.html',
            '/limosa_limosa.html',
            '/malaya-chaika.html',
            '/chlidoniasLeucopterus.html',
            '/sterna_albifrons.html',
            '/columbaoenas.html',
            '/bubo_bubo_mo.html',
            '/centro_provinciale.html',
            '/domovoi-sich-mo.html',
            '/surnia-ulula.html',
            '/strix_uralensis_mo.html',
            '/strix_nebulosa.html',
            '/coracias-garrulus-mo.html',
            '/alcedo-atthis-mo.html',
            '/common_hoopoe.html',
            '/picus-viridis-mo.html',
            '/sedoi-dyatel-mo.html',
            '/dendrocopos_medius.html',
            '/dendrocopos_leucotos_mo.html',
            '/picoides-tridactylus-mo.html',
            '/ullula-arborea-mo.html',
            '/lanius-excubitor-mo.html',
            '/nucifraga-caryocatactes-mo.html',
            '/seggenrohrsaenger_hand.html',
            '/sylvia_nisoria.html',
            '/remiz_pendulinus.html',
            '/parus-cyanus-mo.html',
            '/sadovay-ovsyanka.html',
            '/emberiza-aureola.html',
        ]

        # Скачиваем и сохраняем HTML файлы
        for link in links:
            self.download_html(link, directory_path)

        # После скачивания файлов, начинаем парсинг
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path) and file_path.endswith('.html'):
                # Парсинг и сохранение каждого HTML файла
                self.parse_and_save_html(file_path)

    def download_html(self, link, save_dir):
        """Функция для скачивания HTML файла с тайм-аутом и обработкой ошибок."""
        url = BASE_URL + link
        try:
            response = requests.get(url, timeout=10)  # Тайм-аут 10 секунд
            response.raise_for_status()  # Возбудит исключение, если статус код не 200
            filename = os.path.join(save_dir, os.path.basename(link) + '.html')
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(response.text)
            self.stdout.write(self.style.SUCCESS(f'Скачан файл: {filename}'))
        except (RequestException, SSLError) as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при скачивании {url}: {e}'))

    def parse_and_save_html(self, file_path):
        """Парсит HTML файл и обновляет или сохраняет данные в базу."""
        try:
            # Открываем и парсим файл
            with open(file_path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')

            # Извлекаем название и латинское название
            name_tag = soup.find('h1')
            if name_tag:
                name = name_tag.get_text(strip=True)
            else:
                self.stdout.write(self.style.WARNING(f'Название не найдено в файле {file_path}'))
                name = 'Неизвестное название'

            pre_tag = soup.find('pre')
            if pre_tag:
                pre_text_lines = pre_tag.get_text(strip=True).split('\n')
                latin_name = pre_text_lines[1].strip() if len(pre_text_lines) > 1 else 'Неизвестное латинское название'
            else:
                self.stdout.write(self.style.WARNING(f'Латинское название не найдено в файле {file_path}'))
                latin_name = 'Неизвестное латинское название'

            # Проверка категории статуса
            status_paragraph = None
            for paragraph in soup.find_all('p'):
                if 'Cтатус' in paragraph.get_text():
                    status_paragraph = paragraph
                    break

            if status_paragraph:
                status_text = status_paragraph.get_text(strip=True).replace('Cтатус.', '').strip()
                category_key = ' '.join(status_text.split()[:2])  # Первые два слова
                category = category_mapping.get(category_key, CATEGORY.UNKNOWN_SPECIES)
            else:
                self.stdout.write(self.style.WARNING(f'Категория не найдена в файле {file_path}'))
                category = CATEGORY.UNKNOWN_SPECIES

            # Проверка на отряд и семейство
            if pre_tag and len(pre_text_lines) >= 5:
                order_name = pre_text_lines[3].split(' - ')[0].strip()
                family_name = pre_text_lines[4].split(' - ')[0].strip()
            else:
                order_name = 'Неизвестный отряд'
                family_name = 'Неизвестное семейство'

            order_obj, _ = Order.objects.get_or_create(name=order_name)
            family_obj, _ = Family.objects.get_or_create(name=family_name, order=order_obj)

            # Проверяем наличие навигации для секции
            section_nav = soup.find('nav')
            if section_nav:
                section_links = section_nav.find_all('a')
                section_name = section_links[-1].get_text(strip=True) if section_links else 'Неизвестная секция'
            else:
                section_name = 'Неизвестная секция'
            section_obj, _ = Section.objects.get_or_create(name=section_name)

            # Ищем секцию "Распространение" с частичным совпадением
            distribution_section = soup.find('h3', text=re.compile('Распространение', re.IGNORECASE))
            description_html = ''
            if distribution_section:
                description_html += str(distribution_section)
            else:
                self.stdout.write(self.style.WARNING(f'Секция "Распространение" не найдена в файле {file_path}'))

            # Ищем секцию "Источники информации" с частичным совпадением
            sources_section = soup.find('h4', text=re.compile('Источники информации', re.IGNORECASE))
            recommendation_section = soup.find(
                'h4', text=re.compile('Рекомендации по разведению в неволе', re.IGNORECASE)
            )

            # Определяем секцию завершения описания (либо Источники, либо Рекомендации)
            end_section = sources_section or recommendation_section

            if end_section:
                # Собираем текст до конца раздела с описанием
                for tag in distribution_section.find_all_next():
                    if tag == end_section:
                        break
                    description_html += str(tag)
                description_html += str(end_section)

                # Если после секции "Рекомендации по разведению в неволе" есть абзац, включаем его
                if recommendation_section:
                    next_paragraph = recommendation_section.find_next('p')
                    if next_paragraph:
                        description_html += str(next_paragraph)
            else:
                # Если не найдено ни одной из секций, собираем до конца значимых секций, но не включаем рекламу и прочие блоки
                stop_tags = [
                    'aside',
                    'footer',
                    'script',
                    'div',
                    'form',
                    'nav',
                ]  # Теги, которые сигнализируют конец значимого контента
                for tag in distribution_section.find_all_next():
                    if tag.name in stop_tags:
                        break
                    description_html += str(tag)

            # Проверка на изображение
            image_tag = soup.find('img', class_='image-art')
            image_path = None
            if image_tag:
                image_url = image_tag['src']
                if image_url.startswith('/'):  # Проверяем, если путь относительный
                    image_url = BASE_URL + image_url  # Добавляем базовый URL
                image_name = os.path.basename(image_url)

                # Директория для изображений (используем settings.MEDIA_ROOT)
                image_dir = os.path.join(settings.MEDIA_ROOT, 'red_book_images')
                os.makedirs(image_dir, exist_ok=True)  # Создаем директорию, если она не существует

                # Скачиваем и сохраняем изображение
                try:
                    image_response = requests.get(image_url, timeout=10)
                    if image_response.status_code == 200:
                        image_path = os.path.join(image_dir, image_name)
                        with open(image_path, 'wb') as out_file:
                            out_file.write(image_response.content)
                        self.stdout.write(self.style.SUCCESS(f'Изображение сохранено: {image_path}'))
                    else:
                        self.stdout.write(
                            self.style.ERROR(
                                f'Ошибка загрузки изображения {image_url}, статус код: {image_response.status_code}'
                            )
                        )
                except (RequestException, SSLError) as e:
                    self.stdout.write(self.style.ERROR(f'Ошибка при скачивании изображения {image_url}: {e}'))

            # Сохранение данных в базу: обновление или создание записи
            entry, created = RedBookEntry.objects.update_or_create(
                name=name,  # Используем уникальное название как критерий поиска
                defaults={
                    'latin_name': latin_name,
                    'category': category,
                    'order': order_obj,
                    'family': family_obj,
                    'section': section_obj,
                    'description': description_html if description_html else 'Описание не найдено',
                    'image': image_path if image_path else None,
                },
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Создана новая запись для {name}.'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Обновлена запись для {name}.'))

        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Ошибка обработки файла {file_path}: {e}'))
