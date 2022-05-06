# quiz_API_service

<h2>Описание</h2>

<p>Проект с реализацией сервиса получения и хранения вопросов викторины.</p>
<br>
<p>В сервисе реализован API, с возможностью передачи количества вопросов путем POST запроса.
<p>Запрос может быть отправлен с содержимым вида {"questions_num": integer}</p>
<p>Пример POST запроса: http://0.0.0.0:8000/q?questions_num=4 </p>
<br>
<p>Указанное количество вопросов, в свою очередь, запрашивается с публичного API.</p>
<p> https://jservice.io/api/random?count=1</p>
<br>
<p>Имеется возможность получения последнего вопроса, добавленного в базу</p>
<p>Пример GET запроса http://0.0.0.0:8000/last </p>
<br>
<p>На главной странице http://0.0.0.0:8000/ имеется возможность отправки POST запроса с указанием количества вопросов 
  и с возможностью получения последнего вопроса из базы.</p>
<br>
<p>Используется:</p>
<li>django</li>
<li>django-rest-framework</li>
<li>bootstrap4</li>
<li>docker-compose</li>
<li>PostgreSQL</li>

<h2>Установка</h2>

<h3>Склонируйте репозиторий</h3>

> git clone https://github.com/yutanov/quiz_API_service.git

<h3>Перейдите в каталог репозитория</h3>

> cd quiz_API_service

<h3>Запустите подтовку контейнера</h3>

> make install

Данная команда выполняет следующие команды:

  <li>Создание контейнера</li>

  > docker-compose build

  <li>Запуск миграции</li>

  > docker-compose run web python ./manage.py migrate

<h3>Запустите контейнер</h3>

> docker-compose up

<h3>Перейдите по адресу</h3>

http://0.0.0.0:8000/

<h3>Остановка контейнера</h3>

> docker-compose down
