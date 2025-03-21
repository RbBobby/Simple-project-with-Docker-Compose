
# Простой проект с фронтендом и бэкендом с использованием Docker

Этот проект демонстрирует, как создать простое веб-приложение с использованием Docker и Docker Compose. Приложение состоит из двух частей:
- **Фронтенд**: простая HTML-страница с формой, которая отправляет данные на сервер.
- **Бэкенд**: сервер на Python с использованием Flask, который обрабатывает запросы от фронтенда.

## Структура проекта

```
simple_project/
├── backend/
│   ├── app.py                # Бэкенд на Flask
│   ├── Dockerfile            # Dockerfile для бэкенда
│   └── requirements.txt      # Зависимости для Flask
├── frontend/
│   ├── index.html            # HTML-страница с формой
│   ├── style.css             # CSS для стилизации
│   └── Dockerfile            # Dockerfile для фронтенда
├── docker-compose.yml        # Docker Compose конфигурация
└── README.md                 # Документация
```

## Описание

### Фронтенд

Фронтенд состоит из простой HTML-страницы с формой, в которую пользователь может ввести имя и email. Данные из формы отправляются на сервер через POST-запрос. Результат от сервера отображается на странице.

### Бэкенд

Бэкенд написан на Python с использованием Flask. Он предоставляет один эндпоинт `/api/submit`, который принимает данные от формы и возвращает сообщение с введенными данными.

## Как запустить проект

1. Убедитесь, что у вас установлены **Docker** и **Docker Compose**.
2. Клонируйте этот репозиторий на вашу машину:
   ```bash
   git clone https://github.com/RbBobby/Simple-project-with-Docker-Compose.git & cd Simple-project-with-Docker-Compose
   ```
3. Соберите и запустите проект с помощью Docker Compose:
   ```bash
   docker-compose up --build
   ```
   После выполнения этой команды Docker создаст и запустит два контейнера:
   - **Frontend** будет доступен по адресу `http://localhost:8080`.
   - **Backend** работает на порту 5000, но для фронтенда взаимодействие с ним происходит через Docker-сеть.

## Остановка проекта

Чтобы остановить и удалить контейнеры, выполните команду:
```bash
docker-compose down
```

## Примечания

- Если вы хотите изменить код, сделайте это в соответствующих файлах:
  - Фронтенд: `frontend/index.html`, `frontend/style.css`
  - Бэкенд: `backend/app.py`
- После внесения изменений вам нужно пересобрать контейнеры, чтобы они приняли новые изменения:
  ```bash
  docker-compose up --build
  ```
