# PyDOBot

Утилита, написанная на языке программировния Python, помогающая в прокачке в онлайн игре Darkorbit.

## Начало

Эта инструкция поможет вам скопировать проект и запустить на вашем компьютере.

### Требования

Для работоспособности программы необходимы библиотеки:

beautifulsoup4==4.7.1
certifi==2019.3.9
chardet==3.0.4
idna==2.8
requests==2.21.0
soupsieve==1.9.1
urllib3==1.24.3

Для автоматической установки:

```
pip install -r reqirements.txt
```

### Запуск

1) Клонируйте репозиторий к себе на компьютер с помощью git clone

2) Откройте config.py в любом удобном текстовом редакторе и укажите логин и пароль (ковычки обязательны)

```
AUTH = {
    'login': 'ЛОГИН',
    'password': 'ПАРОЛЬ'
}
```

3) Запустите из командной строки main.py

```
python3 main.py
```

4) В случае неверной пары логин+пароль на экране появится предупреждение:

```
Exception: Не верно введён логин и/или пароль
```

5) Если пароль верный, на экран выводится информация об аккаунтее:

```
id : 123456789
sid : bfb2267f1605252bcc
server : ru1
level : 9
exp : 1.600.001
honor : 5.005
uri_count : 25.000
credits_count : 1.500.000

```

## Тесты

В разработке, будут добавлены вместе со следующим релизом

## Автор

* **Павел Козлов** - [pavkozlov](https://github.com/pavkozlov)

