# RewardMan Server

> Backend часть проекта

> [!NOTE]
> Веб-приложение для специализированного продвижения достижений пользователей, 
> а также удобного ранжирования их навыков и компетенций.
>
> Система оценивания и социального рейтинга за достижения и личного мнения.

<br>

## Содержание

1. [Введение](./README.md#введение)
2. [Структура репозитория](./README.md#структура-репозитория)
3. [Полезные ссылки](./README.md#полезные-ссылки)
4. [Лицензии и авторства](./README.md#лицензии-и-авторства)
5. [Дополнительно](./README.md#дополнительно)

---

<br><br>

## Введение

RewardMan - WEB приложение, нацеленное на улучшение рабочего процесса путем конкуренции и анонимного социального рейтинга.

Принцип работы проекта заключается преимущественно в том, что WEB приложение постоянно обменивается какой-либо информацией с сервером. Собственно, в большинстве случает в жизни так и происходит.
Для обеспечения наиболее оптимального подхода к решению задачи обмена данными между WEB приложением и сервером, в проекте используется преимущественно *REST API*.

Сервер реализован с использованием python библиотеки (он же framework) Flask.
Он готовит json ответы, сразу после того, как на определенный адрес был сделан GET или POST запрос.

Работа с базой данных пользователей так же происходит на сервере с использованием запросов на сервер и с использованием СУБД SQLAlchemic от библиотеки flask.

---

<br>

## Структура репозитория

Репозиторий разбит на несколько составляющих частей:

1. [**Основная директория с кодом - src**](./src/): нахождение исходного кода сервера, базы данных и всех связующих файлов.
2. [**Директория тестирования - test**](./test/): нахождение всех тестов, которые проверяют работу сервера. Выполнение тестовых операций и систем симулирующих работу пользовательского приложения.
3. [**Файл фильтрации данных в репозитории - .gitignore**](./.gitignore): файл необходим для фильтрации мусора разных надстроек.
4. [**Директория настроек vscode - .vscode**](./.vscode): личные настройки проекта в программе Visual Studio Code.
5. [**Файл лицензий - LICENSE**](./LICENSE): файл с лицензией распространения открытого исходного кода RewardMan.
6. [**Директория документации - doc**](./doc/): здесь находятся файлы с техническим заданием проекта, инструкции по развертыванию приложения и инструкции по пользованию приложением
5. [**Файл лицензий - LICENSE**](./LICENSE): файл с лицензией распространения открытого исходного кода RewardMan.
6. [**Файл настройки стилей - .prettierrc**](./.prettierrc): файл необходим для реализации единой стилистики написания кода через форматеры.

---

<br>

## Полезные ссылки

1. [Официальный сайт Python - python.org](https://www.python.org/)
2. [Официальная документация по python Flask - flask.palletsprojects.com](https://flask.palletsprojects.com/en/stable/)
3. [Официальный сайт React Native reactnative.dev](https://reactnative.dev/)
4. [официальный сайт PyPI - pypi.org](https://pypi.org/project/Flask/)
5. ["Flask (веб-фреймворк)" - wikipedia.org](https://ru.wikipedia.org/wiki/Flask_(веб-фреймворк))
6. ["HTTP-запросы: параметры, методы и коды состояния" - habr.com](https://habr.com/ru/companies/timeweb/articles/853174/)
7. ["REST, что же ты такое? Понятное введение в технологию для ИТ-аналитиков" - habr.com](https://habr.com/ru/articles/590679/)
8. ["Пишем API на Python (с Flask и RapidAPI)" - habr.com](https://habr.com/ru/companies/skillbox/articles/464705/)
9. ["Создание простейшего API" - metani.com](https://metanit.com/python/fastapi/1.12.php)
10. ["Python | Build a REST API using Flask" - geeksforgeeks.org](https://www.geeksforgeeks.org/python-build-a-rest-api-using-flask/)
11. ["Flask для начинающих" - habr.com](https://habr.com/ru/articles/783574/)
12. ["Пишем веб-приложение с НУЛЯ на Python|Flask (API)" - rutube.cu](https://rutube.ru/video/a5de26a2f7ca3eb890eb688a4f3453ca/?r=plemwd)

---

<br>

## Лицензии и авторства

1. [Огур Александр](https://github.com/orgs/Livegress/people/Alexandr-Ogur):
   
   * Backend разработка WEB приложения RewardMan;
   * Развертывание базы данных на сервере;
   * Построения JSON дерева;
   * Логика Flask ответов на запросы от приложения.

2. [Воронов Никита](https://github.com/voronov-nikita):
   
   * Frontend разработка WEB приложения RewardMan;
   * Схема обмена данных между клиентским и серверным приложением;
   * Консультации по backend части;
   * Поднятие и настройка сервера.

---

<br>

## Дополнительно

Основной код приложения разбит на две составляющие: клиентскую часть (WEB-приложение) и серверную часть (API).
Конкретно в этом репозитории представлена серверная часть приложения (backend).

С исходным кодом frontend часть. проекта можно ознакомиться в репозитории [RewardMan](https://github.com/Livegress/RewardMan)

<br><br>
<br><br>


###### 06.12.2024