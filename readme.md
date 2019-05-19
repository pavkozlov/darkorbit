# PyDOBot

Утилита, написанная на языке программировния Python, помогающая в прокачке в онлайн игре Darkorbit.

## Начало

Эта инструкция поможет вам скопировать проект и запустить на вашем компьютере.

###История изменений
#####v0.1
* Добавлена автризация и парсинг основной информации со страницы (уридиум, кредиты, опыт, честь, ID, уровень)
#####v0.2
* Оптимизирован и улучшен код
* Добавлен парсинг имеющихся в сайлебе ресурсов и их колличества
* Добавлен парсинг модулей скайлеба (название и уровень)
* Добавлены юнит тесты
######В разработке
* Сохранение результатов работы в файл / базу данных
* Автоматический запуск обновления модулей скайлеба (с анализом их приоритетности в файле config.py, с анализом доступных ресурсов/кредитов/энергии)
* Автоматическая отправка ресурсов на корабль
* GUI/web интерфейс
### Требования

Для работоспособности программы необходимы библиотеки, указанные в requirements.txt

Для автоматической установки:

```
pip install -r reqirements.txt
```

### Запуск

1) Клонируйте репозиторий к себе на компьютер с помощью git clone

2) Откройте config.py в любом удобном текстовом редакторе и укажите логин и пароль

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

## Тесты

Все тесты в папке tests

## Автор

* **Павел Козлов** - [pavkozlov](https://github.com/pavkozlov)

