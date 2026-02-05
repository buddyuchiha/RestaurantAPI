# Restaurant API

Микросервис для автоматизации бронирования столиков в ресторанах с асинхронным управлением данными, кэшированием и автоматизированным развертыванием.

## Функционал

* Управление бронированием: Создание, отмена и просмотр резервов в реальном времени.
* Контроль доступности: Автоматическая проверка вместимости и статуса столиков при попытке бронирования.
* Аутентификация: Регистрация и вход пользователей для управления личными бронированиями, используя JWT - токены.
* Кэширование: Оптимизация часто запрашиваемых данных (список доступных столов) через Redis.
* Авто-миграции: Автоматическое обновление схемы базы данных через Alembic при старте контейнера.
* REST API: Документированный интерфейс на FastAPI с валидацией входных данных через Pydantic.

<img width="1201" height="719" alt="{F87A9FF1-C1F5-42B1-A9C8-67650857949A}" src="https://github.com/user-attachments/assets/a2422534-9ef4-4dea-962c-63de6f727af7" />

<img width="1207" height="408" alt="{C09738DD-E1DB-4D4D-BB5F-622D62A9399B}" src="https://github.com/user-attachments/assets/574b14b1-2b8b-4317-84bf-b55849fbfff1" />

## Технологии

![Python](https://img.shields.io/badge/-Python_3.14-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/-Redis-DC382D?logo=redis&logoColor=white)
![JWT](https://img.shields.io/badge/-JSON_Web_Tokens-000000?logo=jsonwebtokens&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white)
![Alembic](https://img.shields.io/badge/-Alembic-00A98F?logo=alembic&logoColor=white)
![Pydantic](https://img.shields.io/badge/-Pydantic-E92063?logo=pydantic&logoColor=white)
![Poetry](https://img.shields.io/badge/-Poetry-60A5FA?logo=poetry&logoColor=white)


## Инструкция запуска через Docker Compose

1) Клонировать git-репозиторий

<img width="766" height="288" alt="{A2259520-F15E-4362-9B4B-4BB66D9B7FE5}" src="https://github.com/user-attachments/assets/00eee5a1-3c5f-4e5c-84ab-199d5ee232ec" />

<img width="836" height="188" alt="{347990AF-F622-4C1C-AB33-A351B478A7CB}" src="https://github.com/user-attachments/assets/421237a3-a512-48da-b5f2-1f036a6a52c9" />

2) Открыть проект

<img width="490" height="52" alt="{24AF8491-ADA9-4146-AA9E-7A2546BA1324}" src="https://github.com/user-attachments/assets/1fa0d4b5-1221-40ea-a961-20895c339ffb" />

3) Сконфигурировать .env по шаблону

<img width="1555" height="424" alt="{24FADD0C-7495-4390-AA79-C9706D473A3E}" src="https://github.com/user-attachments/assets/ad15017a-8d5b-49a3-a1f4-29cb243b1a4e" />

4) Выполнить команду docker compose up -d --build

<img width="929" height="217" alt="{779D72B3-5882-4E86-9A40-EA152B9E7A15}" src="https://github.com/user-attachments/assets/2bad6a2d-d173-4fc4-ab4e-bfcee890276e" />

5) Подождать 20 секунд и перейти на: http://127.0.0.1:8000/docs

<img width="1905" height="962" alt="{8AE3102E-0B65-4B5B-A106-7620C60D1581}" src="https://github.com/user-attachments/assets/410dbcd8-7c0b-4eaf-97c6-2c868798a5eb" />

## Инструкция локального запуска

1) Клонировать git-репозиторий

<img width="766" height="288" alt="{A2259520-F15E-4362-9B4B-4BB66D9B7FE5}" src="https://github.com/user-attachments/assets/00eee5a1-3c5f-4e5c-84ab-199d5ee232ec" />

<img width="836" height="188" alt="{347990AF-F622-4C1C-AB33-A351B478A7CB}" src="https://github.com/user-attachments/assets/421237a3-a512-48da-b5f2-1f036a6a52c9" />

2) Открыть проект

<img width="490" height="52" alt="{24AF8491-ADA9-4146-AA9E-7A2546BA1324}" src="https://github.com/user-attachments/assets/1fa0d4b5-1221-40ea-a961-20895c339ffb" />

3) Сконфигурировать .env по шаблону

<img width="1555" height="424" alt="{24FADD0C-7495-4390-AA79-C9706D473A3E}" src="https://github.com/user-attachments/assets/ad15017a-8d5b-49a3-a1f4-29cb243b1a4e" />

4) Скачать poetry и установить зависимости

<img width="638" height="95" alt="{B3AE7274-8A9E-4A3A-841E-5D8EF3718A57}" src="https://github.com/user-attachments/assets/c5e17a8b-8ae7-487d-a642-28e42f9f23b3" />

Версия Poetry: 2.2.1

<img width="439" height="49" alt="{95E32486-D784-4E8D-98C1-9A480D70EACD}" src="https://github.com/user-attachments/assets/c64234f8-6991-433c-a317-6590fb85c12c" />

5) Выполнить команду docker-compose up -d database redis-cache 

<img width="635" height="94" alt="{674C4DF7-BBB9-409B-97DB-7721D17C0615}" src="https://github.com/user-attachments/assets/e4c884cf-7527-40e6-9067-c794040220ec" />

6) Применить миграции

<img width="677" height="68" alt="{DD1C58AC-622B-48A0-A0EC-1E74AB15C86A}" src="https://github.com/user-attachments/assets/8f2925b0-b080-46df-b7e6-771b8e08860c" />

6) Выполнить команду python -m app.main и перейти на http://127.0.0.1:8000/docs

<img width="725" height="70" alt="{221B42AC-CADC-4F3F-B9B2-778301004D11}" src="https://github.com/user-attachments/assets/b770dee3-437e-4bda-8b61-81ae0394393e" />

<img width="1905" height="962" alt="{8AE3102E-0B65-4B5B-A106-7620C60D1581}" src="https://github.com/user-attachments/assets/410dbcd8-7c0b-4eaf-97c6-2c868798a5eb" />

## Авторизация

1) Зарегистрироваться

<img width="1259" height="551" alt="{FDFE0781-023B-48A5-8AB5-A968FA02F4EC}" src="https://github.com/user-attachments/assets/945556c6-817c-4b57-83df-32d9b56caaf3" />

<img width="1181" height="259" alt="{46471B8A-C8C1-4298-9CBA-325F9047ACE6}" src="https://github.com/user-attachments/assets/7d264d69-5484-4ccd-a8df-81413ff1eb05" />

2) Авторизоваться и получить JWT access token

<img width="1190" height="534" alt="{61B8CF32-08EA-4074-A3EB-0E700C349C81}" src="https://github.com/user-attachments/assets/e6fbdc19-11d2-4aa9-aece-078e132c24fa" />

<img width="1231" height="522" alt="{0D0FC5ED-9C86-42EC-A317-161ACEF91FD6}" src="https://github.com/user-attachments/assets/64953087-8415-4cb1-becc-1c9e535b3af1" />

3) Скопировать его и вставить в поле у кнопки Authorize

<img width="1313" height="589" alt="{9736FF24-DD61-4C46-B49C-1AB71881858E}" src="https://github.com/user-attachments/assets/6cd455b3-60cd-4aad-9629-4f29b822b8e3" />

4) После появится возможность использовать эндпоинты

<img width="1221" height="527" alt="{8889E4A7-7C45-4A9D-A1DA-9D19B18266F3}" src="https://github.com/user-attachments/assets/01dc1e4b-224b-488c-b061-80f39ed46cb2" />

## Конфигурация

Все настройки можно регулировать в .env

<img width="852" height="446" alt="{56B85513-ACDF-446E-AA02-EA1477C4E2F8}" src="https://github.com/user-attachments/assets/32f23a48-a831-4e50-bf1f-ace25f40d8c3" />

<img width="253" height="40" alt="image" src="https://github.com/user-attachments/assets/61946965-cb1d-4705-b800-bd36fd14ad4a" />

