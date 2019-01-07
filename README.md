# Moon

Инструкция по развертыванию. Копировал с своего sh скрипта, постарался описать, что отличается в Linux

## Backend

#### Под brew install и brew services понимается утилита установки пакетов и ctl-сервис
#### В Arch Linux это pacman -S и systemctl

Установка необходимых пакетов в систему:

```bash
brew install python3 postgresql nginx
```

На Linux также может потребоваться пакет python3-pip или python-pip

Настраиваем postrgres и создаем базу данных

```bash
su - postgres
initdb -D /var/lib/postgres/data
psql 
postgres=# create database note;
```

Настраиваем nginx

#### В Linux вместо /usr/local/etc/nginx подразумевается /etc/nginx

В /usr/local/etc/nginx/nginx.conf комментируем стандартную дерективу server
Вместо нее пишем:

```nginx
include /usr/local/etc/nginx/conf.d/*;
```

Разворачиваем конфиг nginx:

```bash
mkdit /usr/local/etc/nginx/conf.d
cd /usr/local/etc/nginc/conf.d
vim moon.conf
```

Вставляем содержимое конфига:

```nginx
upstream frontend {
  server 127.0.0.1:8080;
}

upstream backend {
  server 127.0.0.1:8000;
}

server {
  listen 80;
  server_name moon.local;

  location /api {
    proxy_pass http://backend/;
    proxy_set_header Host 127.0.0.1;
  }

  location / {
    proxy_pass http://frontend/;
    proxy_set_header Host 127.0.0.1;
  }
}
```

Перезупускаем nginx

```
brew services restart nginx
```

Клонируем проект, создаем виртуальное окружение

```bash
cd backend
python3 -m venv env
```

Установка зависимостей python

```bash
./env/bin/pip3 install -r requirements.txt
```

Запуск миграций alembic:

```bash
./env/bin/alembic upgrade head
```

Для запуска dev-окружения:
```bash
./dev.sh
```

Для запуска под production:
```bash
./prod.sh
```

## Frontend

Устанавливаем в систему npm и nodejs:

```bash
brew install npm nodejs
```

Устанавливаем vue-cli:

```bash
npm install -g vue-cli
```

Устанавливаем зависимости проекта:

```bash
cd frontend
npm install
```

Для запуска dev-окружения:

```bash
npm run serve
```

Для сборки под production:

```bash
npm run build
```


