# Salary report

**Простой инструмент для генерации отчётов по зарплатам из CSV-файлов.**

## Структура проекта

```
.
├── reports
│   ├── __init__.py
│   └── payout.py
└── tests
    ├── test_reader.py
    ├── test_payout.py
    └── test_main.py
├── .gitignore
├── data1.cvs
├── data2.cvs
├── data3.cvs
├── main.py
├── models.py
├── reader.py
├── README.md
├── requirements.txt
├── setup.py
```

## Как начать

1. **Клонировать репозиторий и установить зависимости**  
   ```bash
   git clone https://github.com/Exslayder/salary_report.git
   cd salary_report
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   pip install -e 
   ```

2. **Подготовить CSV-файлы**  
   Убедитесь, что в ваших файлах есть как минимум следующие заголовки (в любом порядке):
   - `name`  
   - `department`  
   - `hours_worked`  
   - один из: `hourly_rate`, `rate` или `salary`

   Для тестирования взяты файлы `data1.cvs`, `data2.cvs`, `data3.cvs`

3. **Запустить отчёт**  

   ```bash
   python3 main.py data1.csv data2.csv --report payout
   ```

## Описание кода

- **main.py**  
  Точка входа: парсит аргументы, читает все CSV, вызывает нужный генератор отчёта и выводит результат.

- **reader.py**  
  Содержит функции:
  - чтения строк из файла,
  - разбора заголовков,
  - парсинга строк в объекты `Employee` (без внешних CSV-библиотек).

- **models.py**  
  Определяет класс `Employee` с полями `name`, `department`, `hours_worked`, `hourly_rate` и свойством `payout`.

- **reports/**  
  Пакет с модулями отчётов.  
  - `payout.py`: группирует сотрудников по отделам, выводит детализацию и итог.

- **setup.py**  
  Конфигурация для установки пакета в режиме разработки (`pip install -e .`), регистрация консольного скрипта `payroll-report`.

- **.gitignore**  
  Исключает из репозитория артефакты сборки, виртуальные окружения, кэш.

- **tests/**  
  Набор `pytest`-тестов для основных сценариев:
  - `test_reader.py` — проверка чтения CSV и обработки ошибок.  
  - `test_payout.py` — корректность формата отчёта.  
  - `test_main.py` — запуск, поведение при ошибках.

## Тестирование

```bash
pytest --cov=.
```

- Проверка корректности работы и coverage-отчёт.  
- Целевое покрытие — не менее ~80%.

## Частые вопросы

- **Почему нет зависимости от pandas или csv?**  
  Задача — работать напрямую со строками, без сторонних библиотек.

- **Как добавить новый отчёт?**  
  1. Создайте `reports/<имя>.py` с функцией `generate_<имя>_report(employees: list[Employee]) -> str`.  
  2. Зарегистрируйте её в словаре `REPORTS` в `reports/__init__.py`.

- **Что делать при ошибке «Missing required column»?**  
  Проверьте, что заголовки в CSV указаны правильно и без опечаток.

### Приятного использования!
