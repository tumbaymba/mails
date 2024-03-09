## Задание

Курсовая работа состоит из двух частей:
1) «Разработка сервиса»
2) «Доработка сервиса».

## Критерии приемки курсовой: 

* Интерфейс системы содержит следующие экраны: список рассылок, отчет проведенных рассылок отдельно, создание рассылки, удаление рассылки, создание пользователя, удаление пользователя, редактирование пользователя.
* Реализовали всю требуемую логику работы системы.
* Интерфейс понятен и соответствует базовым требованиям системы.
* Все интерфейсы для изменения и создания сущностей, не относящиеся к стандартной админке, реализовали с помощью Django-форм.
* Все настройки прав доступа реализовали верно.
* Использовали как минимум два типа кеширования.
* Решение выложили на GitHub.

## **1. Разработка сервиса**

### Контекст

Чтобы удержать текущих клиентов, часто используют вспомогательные, или «прогревающие», рассылки для информирования и привлечения клиентов.

Разработайте сервис управления рассылками, администрирования и получения статистики.

### Описание задач

Реализуйте интерфейс заполнения рассылок, то есть CRUD-механизм для управления рассылками.
Реализуйте скрипт рассылки, который работает как из командой строки, так и по расписанию.
Добавьте настройки конфигурации для периодического запуска задачи.

### Сущности системы

##### Клиент сервиса:
* контактный email,
* ФИО,
* комментарий.

##### Рассылка (настройки):

* время рассылки;
* периодичность: раз в день, раз в неделю, раз в месяц;
* статус рассылки: завершена, создана, запущена.

##### Сообщение для рассылки:

* тема письма,
* тело письма.

##### Логи рассылки:

* дата и время последней попытки;
* статус попытки;
* ответ почтового сервера, если он был.

Не забудьте про связи между сущностями. Вы можете расширять модели для сущностей в произвольном количестве полей либо добавлять вспомогательные модели.

#### Логика работы системы

После создания новой рассылки, если текущее время больше времени начала и меньше времени окончания, то должны быть выбраны из справочника все клиенты, которые указаны в настройках рассылки, и запущена отправка для всех этих клиентов.
Если создается рассылка со временем старта в будущем, то отправка должна стартовать автоматически по наступлению этого времени без дополнительных действий со стороны пользователя системы.
По ходу отправки сообщений должна собираться статистика (см. описание сущности «сообщение» и «логи» выше) по каждому сообщению для последующего формирования отчетов.
Внешний сервис, который принимает отправляемые сообщения, может долго обрабатывать запрос, отвечать некорректными данными, на какое-то время вообще не принимать запросы. Нужна корректная обработка подобных ошибок. Проблемы с внешним сервисом не должны влиять на стабильность работы разрабатываемого сервиса рассылок.

### ‍Рекомендации

Реализовать интерфейс можно с помощью UI kit Bootstrap.
Для работы с периодическими задачами можно использовать либо crontab-задачи в чистом виде, либо изучить дополнительно библиотеку: https://pypi.org/project/django-crontab/
‍Периодические задачи — задачи, которые повторяются с определенной частотой, которая задается расписанием.

‍crontab — классический демон, который используется для периодического выполнения заданий в определенное время. Регулярные действия описываются инструкциями, помещенными в файлы crontab и в специальные каталоги.

Служба crontab не поддерживается в Windows, но может быть запущена через WSL. Поэтому если вы работаете на этой ОС, то решите задачу запуска периодических задач с помощью библиотеки apscheduler: https://pypi.org/project/django-apscheduler/.

Подробную информацию, что такое crontab-задачи, найдите самостоятельно.

## **2. Доработка сервиса**

### Контекст

Сервис по управлению рассылками пользуется популярностью, однако запущенный MVP уже не удовлетворяет потребностям бизнеса.

Доработайте ваше веб-приложение. 
А именно: 
1. разделите права доступа для различных пользователей
2. добавьте раздел блога для развития популярности сервиса в интернете.

### Описание задач

1. Расширьте модель пользователя для регистрации по почте, а также верификации.
2. Добавьте интерфейс для входа, регистрации и подтверждения почтового ящика.
3. Реализуйте ограничение доступа к рассылкам для разных пользователей.
4. Реализуйте интерфейс менеджера.
5. Создайте блог для продвижения сервиса.
6. Используйте для наследования модель AbstractUser.

### Функционал менеджера

1.  Может просматривать любые рассылки.
2.  Может просматривать список пользователей сервиса.
3.  Может блокировать пользователей сервиса.
4.  Может отключать рассылки.
5.  Не может редактировать рассылки.
6.  Не может управлять списком рассылок.
7.  Не может изменять рассылки и сообщения.

### Функционал пользователя

Весь функционал дублируется из первой части курсовой работы. 
Но теперь нужно следить за тем, чтобы пользователь не мог случайным образом изменить чужую рассылку и мог работать только со своим списком клиентов и со своим списком рассылок.

### Продвижение

### Блог

Реализуйте приложение для ведения блога.
При этом отдельный интерфейс реализовывать не требуется, но необходимо настроить административную панель для контент-менеджера.

В сущность блога добавьте следующие поля:

1. заголовок,
2. содержимое статьи,
3. изображение,
4. количество просмотров,
5. дата публикации.
6. Главная страница


### Главная страница 

Реализуйте главную страницу в произвольном формате, но обязательно отобразите следующую информацию:

1. количество рассылок всего,
2. количество активных рассылок,
3. количество уникальных клиентов для рассылок,
4. 3 случайные статьи из блога.

### Кеширование

Для блога и главной страницы самостоятельно выберите, какие данные необходимо кешировать, а также каким способом необходимо произвести кеширование.

# Установка и использование (для Windows)
1. Клонируйте репозиторий.
2. Создайте и активируйте виртуальное окружение.
3. Для работы программы необходимо установить зависимости, указанные в файле requirements.txt
   pip install -r requirements.txt (показано для (venv)).
4. Создайте файл .env. Введите туда свои настройки как указано в файле .env.sample.
5. Создайте базу данных ( Например, через консоль: 1) psql -U postgres; 2) create database online_studing; 3) выход: \q)
6. Сделайте и примените миграции.
6.1 python manage.py makemigrations
6.2 python manage.py migrate
7. Можете загрузить тестовые данные:
7.1 python manage.py loaddata data_blog.json
7.2 python manage.py loaddata data_mails.json
либо создать свои.
8. Создайте суперпользователя: python manage.py csu
9. Запустите сервер: python manage.py runserver
10. Зарегистрируйтесь на проекте, cоздайте своих клиентов, сообщения и саму рассылку. После создание рассылки нужно вызвать команду в терминале python manage.py runapscheduler
11. Настройка для кеша.
Перед тем как использовать пакет redis внутри Django, не забудьте установить БД Redis.
Для этого:
в Linux используется команда 
sudo apt install redis
или 
sudo yum install redis,
в macOS — команда 
brew install redis,
в случае с Windows воспользуйтесь инструкцией: https://redis.io/docs