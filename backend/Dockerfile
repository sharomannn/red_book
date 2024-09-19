# Этап сборки (build stage)
FROM python:3.12-slim as builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc-dev \
    libffi-dev \
    python3-dev

COPY requirements.txt /tmp/
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /tmp/wheels -r /tmp/requirements.txt

# Этап выполнения (final stage)
FROM python:3.12-slim

# Установка необходимых пакетов, минимизация слоев и удаление кэша apt
RUN apt-get update && apt-get install -y --no-install-recommends \
    supervisor \
    vim \
    locales \
    tzdata \
    postgresql-client \
    ffmpeg \
    mc \
    libreoffice \
    poppler-utils \
    && sed -i '/ru_RU.UTF-8/s/^# //g' /etc/locale.gen && locale-gen \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU:ru
ENV LC_ALL ru_RU.UTF-8

# Копирование скомпилированных wheel файлов и установка зависимостей
COPY --from=builder /tmp/wheels /tmp/wheels
RUN pip install --no-cache-dir /tmp/wheels/*

COPY . /opt/app
WORKDIR /opt/app

EXPOSE 80

COPY supervisor/supervisord.conf /etc/supervisor/supervisord.conf
COPY supervisor/serv.conf /etc/supervisor/conf.d/app.conf

VOLUME /data/
VOLUME /conf/
VOLUME /static/
VOLUME /media/
VOLUME /logs/

CMD rm -rf static; ln -s /static static; \
    rm -rf media; ln -s /media media; \
    rm -rf logs; ln -s /logs logs; \
    python manage.py collectstatic --noinput; \
    python manage.py migrate; \
    /usr/bin/supervisord -c /etc/supervisor/supervisord.conf --nodaemon
