# Stage 1: Сборка приложения
FROM node:18-alpine AS builder

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы package.json и package-lock.json
COPY frontend/package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем остальные файлы проекта
COPY frontend/ .

# Собираем Nuxt.js приложение
RUN npm run build

# Stage 2: Запуск Nginx для сервинга приложения
FROM nginx:alpine

# Копируем собранные файлы на сервер
COPY --from=builder /app/.output/public /usr/share/nginx/html

# Копируем Nginx конфигурацию
COPY ../nginx.conf /etc/nginx/nginx.conf

# Открываем порт 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
