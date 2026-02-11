# Дипломный проект  Автоматизация тестов МТС (Shop MTS)

Проект содержит авто тесты для интернет магазина МТС
Реализованы UI тесты (Selenium) и API тесты (Requests)

###  Документация по ручному тестированию
1 Финальный проект https://kirov.yonote.ru/share/023b0aa0-512b-4742-b927-447fc3ff82cb
2 Отчет о тестировании https://kirov.yonote.ru/share/94064e88-5216-4e2d-bc1d-0c692b2b0197

## Запуск тестов

### 1. Установка зависимостей
pip install -r requirements.txt

### 2. Режимы запуска
pytest          # Все тесты
pytest -m ui    # Только UI
pytest -m api   # Только API