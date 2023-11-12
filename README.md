# Генератор QR-кодів
Цей простий Python скрипт створює QR-коди за допомогою бібліотеки qrcode. Він дозволяє легко створювати QR-коди для різних URL та зберігати їх у форматі PNG.

# Встановлення
Переконайтеся, що у вас встановлена бібліотека qrcode. Її можна встановити за допомогою команди:
```
pip install qrcode[pil]
```

# Використання
1.Склонуйте репозиторій:
```
git clone https://github.com/kozhydlo/QR-Code-Generator

```
2.Перейдіть у директорію проекту:
```
cd your-repository
```
3.Запустіть скрипт:
```
python your_script_name.py
```

# Функції
`get_qrcode(url='http://google.com', name='default')`
Ця функція створює QR-код для вказаного URL та зберігає його як зображення PNG з заданим ім'ям.

url: URL, для якого повинен бути створений QR-код. За замовчуванням - 'http://google.com'.
name: Ім'я файлу PNG для збереження. За замовчуванням - 'default'.
Повертає повідомлення про успішне створення QR-коду та розташування файлу.

`main()`
Функція main демонструє використання функції get_qrcode, створюючи QR-коди для двох різних URL-адрес - особистого веб-сайту та профілю в Telegram. Ви можете змінювати URL та імена за необхідності.

# Приклад

```from qrcode_generator import get_qrcode

def main():
    print(get_qrcode(url='your link', name='your-name'))
    print(get_qrcode(url='your link', name='your-name'))

if __name__ == '__main__':
    main()
```

Це створить QR-коди для вказаних URL та збереже їх як 'WEBSITE.png' та 'TELEGRAM.png' відповідно.
