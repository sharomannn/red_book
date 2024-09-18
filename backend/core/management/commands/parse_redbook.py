import os
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.conf import settings  # Нужно для MEDIA_ROOT
from core.models import RedBookEntry, Order, Family, Section
from core.consts import CATEGORY


# Словарь для сопоставления категорий по первым двум словам
category_mapping = {
    '1-я категория.': CATEGORY.ENDANGERED_SPECIES,
    '2-я категория.': CATEGORY.VULNERABLE_SPECIES,
    '3-я категория.': CATEGORY.RARE_SPECIES,
    '4-я категория.': CATEGORY.UNKNOWN_SPECIES,
    '5-я категория.': CATEGORY.RECOVERING_SPECIES,
}

# Базовый URL для изображений
BASE_URL = "https://cicon.ru"

class Command(BaseCommand):
    help = 'Парсинг HTML файлов для Красной книги'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Путь к HTML файлу')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'Файл {file_path} не найден'))
            return

        # Открываем и парсим файл
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

        # Извлекаем название и латинское название
        name = soup.find('h1').get_text(strip=True)
        latin_name = soup.find('pre').get_text(strip=True).split('\n')[1].strip()

        # Извлечение категории
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
            category = CATEGORY.UNKNOWN_SPECIES

        # Извлекаем названия отряда и семейства
        order_name = soup.find('pre').get_text(strip=True).split('\n')[3].split(' - ')[0].strip()
        family_name = soup.find('pre').get_text(strip=True).split('\n')[4].split(' - ')[0].strip()

        # Получаем или создаем объекты Order и Family
        order_obj, _ = Order.objects.get_or_create(name=order_name)
        family_obj, _ = Family.objects.get_or_create(name=family_name, order=order_obj)

        # Извлечение названия секции
        section_nav = soup.find('nav').find_all('a')[-1].get_text(strip=True)
        section_obj, _ = Section.objects.get_or_create(name=section_nav)

        # Извлечение полезного HTML описания
        distribution_section = soup.find('h3', text='Распространение.')
        sources_section = soup.find('h4', text='Источники информации')

        # Начинаем с включения самого тега <h3> "Распространение."
        description_html = str(distribution_section)

        # Извлечение текста между заголовками "Распространение" и "Источники информации"
        for tag in distribution_section.find_all_next():
            if tag == sources_section:
                break
            description_html += str(tag)

        # Сохранение фото на сервер
        image_tag = soup.find('img', class_='image-art')
        image_path = None
        if image_tag:
            image_url = image_tag['src']
            if image_url.startswith('/'):  # Проверяем, если путь относительный
                image_url = BASE_URL + image_url  # Добавляем базовый URL
            image_name = os.path.basename(image_url)

            # Директория для изображений (используем settings.MEDIA_ROOT)
            image_dir = os.path.join(settings.MEDIA_ROOT, 'red_book_images')
            os.makedirs(image_dir, exist_ok=True)

            # Скачиваем и сохраняем изображение
            image_temp = NamedTemporaryFile(delete=True)
            img_response = requests.get(image_url)
            if img_response.status_code == 200:
                image_temp.write(img_response.content)
                image_temp.flush()

                # Путь к файлу изображения
                image_path = os.path.join(image_dir, image_name)
                with open(image_path, 'wb') as out_file:
                    out_file.write(img_response.content)

        # Сохранение данных в базу
        entry = RedBookEntry(
            name=name,
            latin_name=latin_name,
            category=category,
            order=order_obj,
            family=family_obj,
            section=section_obj,  # Связываем запись с секцией
            description=description_html,  # Сохраняем только извлеченный контент с тегом <h3>
            image=os.path.join('red_book_images', image_name) if image_path else None  # Относительный путь к изображению
        )
        entry.save()

        self.stdout.write(self.style.SUCCESS(f'Запись для {name} успешно сохранена.'))
