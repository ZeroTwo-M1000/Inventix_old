# Inventix

> Добро пожаловать в репозиторий проекта **Inventix**. Это полнофункциональное приложение создано с использованием **FastAPI**, **Prisma** и **Vue**. Сайт предназачен для комании **LabMedia**.

## Обзор
Этот репозиторий содержит исходный код и инфраструктуру для вашего веб-приложения, включая бэкенд на **FastAPI**, фронтенд использующий **Vue** и базу данных **PostgreSQL** с использованием **Prisma**.

## Предварительные требования
Для работы с этим проектом вам потребуются следующие инструменты:
- **Python** 3.8 или выше
- **Node.js** и **yarn**
- **PostgreSQL**
- **Poetry** для управления зависимостями **Python**

_Убедитесь, что все эти инструменты установлены и доступны в вашем **PATH**._

## Локальная установка и запуск

### 1. Клонирование репозитория
Склонируйте репозиторий на вашу машину:

```
git clone https://github.com/ZeroTwo-M1000/Inventix.git
```

### 2. Настройка
Для настройки проекта выполните команду:

```
make setup
```

> **Важно**: После запуска команды `make setup`, откройте файл `.env` в директории `src` и убедитесь, что переменные среды заданы корректно для вашей локальной среды.

### 3. Настройка базы данных
Запустите миграции и создайте структуру базы данных с помощью следующей команды:

```
make setup-prisma
```

### 4. Запуск серверов разработки

#### Бэкенд
Чтобы запустить сервер разработки бэкенда, используйте команду:

```
make api-dev
```

Сервер будет доступен по адресу: `http://localhost:8000`

#### Фронтенд
Для запуска сервера фронтенда выполните:

```
make client-dev
```

Фронтенд будет доступен на `http://localhost:5173`

## Справочник по командам
Вот некоторые полезные команды, определенные в `Makefile`:

- `make setup`: Инициализация проекта
- `make api-dev`: Запуск локального сервера разработки бэкенда
- `make client-dev`: Запуск локального сервера разработки фронтенда
- `make client-build`: Сборка продакшн версии фронтенда
- `make create-env`: Создание заготовки файла энвайронментов (.env)
- `make create-media`: Создание директории для медиафайлов
- `make create-logs`: Создание директории для логов
- `make setup-prisma`: Запуск миграций для базы данных через Prisma
