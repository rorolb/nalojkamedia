import json
import requests

# Объявляем url на который будет отправляться данные
url = "deepseek.com"

# Формируем post данные требуемые для отправки формы
post_data = {'ContactForm[subject]': 'Трансфер', 'ContactForm[name]': 'Даниил Аль', 'ContactForm[phone]': '7318293112', 'ContactForm[email]': 'pocecuyoro@cliptik.net', 'ContactForm[body]': 'Test'}

# Количество запросов
lime = 5
# Количество выполненных запросов
inc = 0

while lime > inc:
    # Выполняем запрос
    r = requests.post(url, data=post_data)
    # Декодируем json который пришел к нам в ответ
    data = json.loads(r.text)

    # Проверяем статус ответа, если true тогда пишем в консоль ОК
    # если false то выводим содержимое ответа в консоль и прерываем цикл
    if data['status']:
        inc += 1
        print('OK')
    else:
        print(r.text)
        break
