Это API, которое возвращает текущий курс валюты по отношению к рублю (RUB).

Установка и запуск:
1. Клонируйте репозиторий командой:
    git clone https://github.com/ваш-github-логин/simple-currency-api.git
2. Перейдите в папку с проектом:
    cd simple-currency-api
3. Установите зависимости:
    pip install -r requirements.txt
4. Запустите приложение:
    python app.py

Отправка POST-запроса:
Отправьте POST-запрос на /currency с именем валюты в формате JSON. Пример:
    curl -X POST http://127.0.0.1:5000/currency -H "Content-Type: application/json" -d '{"currency": "USD"}'

Формат ответа:
Ответ содержит курс валюты по отношению к рублю. Пример:
    {
      "currency": "USD",
      "rate_to_rub": 74.50
    }

Тестирование:
Для запуска тестов выполните команду:
    python -m unittest test_app.py