# **Автотесты БИБЛ** 
* Репозиторий проекта автоматизации тестирования БИБЛ.
* Основной функционал проекта: UI скрипты на `python` с использованием библиотеки `playwright`.
* [**План и описание**](https://stash.bars-open.ru/projects/EDUTEST/repos/edu-test/browse) нюансов автоматизации в репозитории edu-test
* [**Инструкции**](https://stash.bars-open.ru/projects/EDUTEST/repos/edu-test/browse/docs) в репозитории edu-test/docs
    * [**`PLAN.md`**](https://stash.bars-open.ru/projects/EDUTEST/repos/edu-test/browse/docs/PLAN.md) - Общий план автоматизации тестирования
    * [**`PYTHON.md`**](https://stash.bars-open.ru/projects/EDUTEST/repos/edu-test/browse/docs/PYTHON.md) - Инструкция по установке и эксплуатации языка `python`
    * [**`IDE.md`**](https://stash.bars-open.ru/projects/EDUTEST/repos/edu-test/browse/docs/IDE.md) - Инструкция по установке и эксплуатации сред разработок
    * [**`GIT.md`**](https://stash.bars-open.ru/projects/EDUTEST/repos/edu-test/browse/docs/GIT.md) - Инструкция по установке и эксплуатации системы управления версиями `git`
    * [**`CODE.md`**](https://stash.bars-open.ru/projects/EDUTEST/repos/edu-test/browse/docs/CODE.md) - Инструкция по правилам написания кода
    * [**`TERMINAL.md`**](https://stash.bars-open.ru/projects/EDUTEST/repos/edu-test/browse/docs/TERMINAL.md) - Инструкция по запуску и эксплуатации командной строки \ терминала
    * [**`MD.md`**](https://stash.bars-open.ru/projects/EDUTEST/repos/edu-test/browse/docs/MD.md) - Инструкция по написанию файлов-инструкция с расширением `.md` в формате `markdown` разметки
* [**Задача**](https://jira.bars.group/browse/EDUBOOKS-233) автоматизации тестирования:
* [**Чек-лист**](https://conf.bars.group/pages/viewpage.action?pageId=305480188) тестирования БИБЛ
* [**Jenkins**](https://jenkins.edu.bars.group/view/%D0%90%D0%B2%D1%82%D0%BE%D1%82%D0%B5%D1%81%D1%82%D1%8B/) БЦ ОБР пространство Автотесты

## **Контакты команды разработки**
* Руководитель БЦ ОБР: `m.pyshenko` Михаил Пышенко
* Ответственный автоматизации БИБЛ: `d.gromov` Дмитрий Громов

## **Покрытие авто-тестами**
* Покрытие авто-тестами производится чек-листу, ссылка в шапке.
* Покрытие рассчитанно из количественного соотношения 1 к 1 в двух категориях, модули и тест-кейсы.
  * `Модулей`: `40` ; `Кейсов`: `?`
* Реализованно:
    * Модули - `Типы реализованных тестов` - `Техническое имя модуля` - `Кол-во кейсов`:
      * Авторизация - `smoke` - `login` - `2`
      * Асинхронные задачи - 
      * Паспорт библиотеки - 
      * Реестры - `smoke` - `registries` - `0`
        * Библиотечный реестр - 
        * Общий фонд литературы - 
        * Выдача/Сдача экземпляров - 
        * Желаемая литература - 
        * Каталог изданий - 
        * Книгообменный фонд - 
        * Мои заявки на заказ изданий - 
        * Моя литература - 
        * Реестр библиотечных мероприятий - 
        * Реестр читателей - 
      * Справочники и Администрирование - `smoke` - `admin` - `0`
        * Журнал изменений - 
        * Роли и права - 
        * Справочники:
          * Авторы - 
          * Знаки информационной продукции - 
          * Издательства - 
          * Источники поступления - 
          * Классы - 
          * Организации - 
          * Периоды обучения - 
          * Предметы - 
          * Разделы ББК - 
          * Разделы УДК - 
          * Сотрудники - 
          * Типы библиотечных экземпляров - 
          * Ученики - 
          * УМК - 
          * Федеральный перечень учебников - 
      * Отчёты - `smoke` - `reports` - `0`
        * Дневник работы библиотеки - 
        * Книга суммарного отчета - 
        * Расчет коэффициента обеспеченности - 
        * Списанные экземпляры - 
        * Список выданных книг - 
        * Список должников - 
        * Печатная форма библиотечного реестра - 
        * Печатная форма общего фонда литературы - 
        * Формирование потребности в изданиях - 
      * Интеграции `integration` - `0`
        * СГДС интеграция - `smoke` - `sgds_integration` - `0`

* Прочее:
  * `Приемка (accept)`  `Кейсы: 0`;
  * `Логика (api)`      `Кейсы: 0`;
  * `Нагрузка (load)`   `Кейсы: 0`;

## **Архитектура проекта**
* Общая универсальная структура директорий проектов автоматизации описана в [**основном репозитории `edu-test`**](https://stash.bars-open.ru/projects/EDUTEST/repos/edu-test/browse) в разделе `Архитектура проекта`
* Архитектура `edu-test-lib` проекта БИБЛ
```
/edu-test-lib/                                # корневой каталог (репозиторий) проекта авто-тестов БИБЛ
├── /page/                                    # page object модели
│   ├── __init__.py
│   ├── /auth_logout/                     # папка с page object моделью и данными модуля ЛОГИН
│   │   ├── __init__.py
│   │   ├── auth_logout_page.py           # page object класс модуля
│   │   ├── auth_logout_locators.py       # селекторы элементов модулей
│   │   └── auth_logout_data.py           # тестовые данные модуля
│   ├── /registers/                       # папка с page object моделью и данными модуля РЕЕСТРЫ
│   │   ├── __init__.py
│   │   ├── registers_page.py             # page object класс модуля
│   │   ├── registers_locators.py         # селекторы элементов модулей
│   │   └── registers_data.py             # тестовые данные модуля
│   ├── /administration/                  # папка с page object моделью и данными модуля АДМИНИСТРИРОВАНИЕ
│   │   ├── __init__.py
│   │   ├── administration_page.py        # page object класс модуля
│   │   ├── administration_locators.py    # селекторы элементов модулей
│   │   └── administration_data.py        # тестовые данные модуля
│   ├── /reports/                         # папка с page object моделью и данными модуля ОТЧЕТЫ
│   │   ├── __init__.py
│   │   ├── reports_page.py               # page object класс модуля
│   │   ├── reports_locators.py           # селекторы элементов модулей
│   │   └── reports_data.py               # тестовые данные модуля
│   ├── /directories/                     # папка с page object моделью и данными модуля СПРАВОЧНИКИ
│   │   ├── __init__.py
│   │   ├── directories_page.py           # page object класс модуля
│   │   ├── directories_locators.py       # селекторы элементов модулей
│   │   └── directories_data.py           # тестовые данные модуля
│   ├── /integrations/                    # папка с page object моделью и данными модуля ИНТЕГРАЦИИ
│   │   ├── __init__.py
│   │   ├── integrations_page.py          # page object класс модуля
│   │   ├── sgds_integration_page.py      # page object класс модуля СГДС
│   │   ├── integrations_locators.py      # селекторы элементов модулей
│   │   └── integrations_data.py          # тестовые данные модуля
│   └── base_page.py                      # базовый page object класс (основные методы работы со страницей)
├── /test/                                # тестовые сценарии с группировкой по видам
│   ├── __init__.py
│   ├── /smoke/                           # дымы (фронт)
│   │   └── test_module.py
│   ├── /accept/                          # приемка (фронт)
│   │   └── test_module.py
│   ├── /api/                             # апи (бэк)
│   │   └── test_module_api.py
│   ├── /load/                            # нагрузочное (locust)
│   └────── locust_smoke.py
├── /report/                              # отчеты и артефакты (хранятся только локально, в проде подключено хранение в jenkins)
│   ├── /screenshots/                     # скриншоты
│   ├── /allure-results/                  # allure отчеты
│   ├── /pytest-html/                     # pytest отчеты (для прикладывания в задачи)
│   ├── /locust/                          # locust отчеты нагрузочного
│   └── /logs/                            # логи выполнения тестов (pytest cli, logger)
├── /config/                              # конфигурации
│   ├── __init__.py
│   └── logger.py                         # конфигурация логирования (пока не используем)
├── /utils/                               # вспомогательные инструменты (пока не используем)
│   ├── __init__.py
│   ├── /drivers/                         # веб-драйвера и портативные браузеры (пока не используем)
│   ├── actions.py                        # сложные методы и действия на страницах (пока не используем)
│   ├── asserts.py                        # проверки (пока не используем)
│   └── helpers.py                        # вспомогательные элементы (пока не используем)
├── conftest.py                           # фикстуры pytest, allure
├── pytest.ini                            # конфигурация тестов
├── requirements.txt                      # зависимости и пакеты
├── README.md                             # описание проекта
└── .gitignore                            # игнор лист git
```
* Отчеты и артефакты папки `report` только для локального хранения (папка указана в `.gitignore`), в эксплуатации подразумевается хранение артефактов в `jenkins`.

## Запуск
### Ручные запуски тестов
* Предварительно настраивается окружение (requirements.txt)
* Пример команды запуска тестов
```bash
pytest test/smoke --browser=firefox --headless --alluredir=reports/allure-results
```

## **Работа в репозитории**:
* **Пример безопасного workflow в `git`**
```bash
# Перед началом работы актуализируем локальные данные
git pull origin ветка

# После нужных изменений в коде и ревью, сформируйте индексы изменений
git add .

# Проверяем какие файлы изменятся и что нет лишних изменений
git status

# Создание коммита на изменение
git commit -m "Комментарий"

# Отправка изменений на сервер (-u чтобы запомнил ветки, потом можно просто git push)
git push -u origin ветка

#---#---#---#
# Получить последние изменения с удалённого репозитория
git fetch origin
# Переключиться на нужную ветку (если ещё не в ней)
git checkout master  # или другая ветка (feature/branch)
# Жёсткий сброс локальной ветки в точное соответствие с удалённой
git reset --hard origin/master
# Очистить локальные неотслеживаемые файлы (опционально). Если нужно удалить файлы, которые есть локально, но отсутствуют в удалённой ветке:
git clean -fd
```
#### **Подключение к `bitbucket` репозиторию через `git`**:
* Описано в файле [**`GIT.md` в папке `docs`**](https://stash.bars-open.ru/projects/EDUTEST/repos/edu-test/browse/docs/GIT.md) в корневой директории [**основного репозитория `edu-test`**](https://stash.bars-open.ru/projects/EDUTEST/repos/edu-test/browse)
