# quiz_API_service

<h2>Описание</h2>

<p>Проект с реализацией сервиса получения и хранения вопросов викторины.</p>
<p>В сервисе реализован API, с возможностью передачи количества вопросов путем POST запроса.
Указанное количество вопросов, в свою очередь, запрашивается с публичного API.</p>
<p> https://jservice.io/api/random?count=1</p>
<p>Имеется возможность получения последнего вопроса, добавленного в базу</p>
<p>Запрос может быть отправлен с содержимым вида {"questions_num": integer}</p>
<p>Пример POST запроса: http://0.0.0.0:8000/q?questions_num=4 </p>
<p>На главной странице http://0.0.0.0:8000/ имеется возможность отправки POST запроса с указанием количества вопросов 
  и с возможностью получения последнего вопроса из базы.</p>

<p>Используется:</p>
<li>django</li>
<li>django-rest-framework</li>
<li>bootstrap4</li>
<li>docker-compose</li>
<li>PostgreSQL</li>

<h2>Установка</h2>

Склонируйте репозиторий
> git clone https://github.com/yutanov/quiz_API_service.git

Перейдите в каталог репозитория
> cd quiz_API_service

Запустите миграции
> docker-compose run web python ./manage.py migrate

Изменените права доступа к файлам
> sudo chown -R $USER:$USER .

Запустите контейнер
> docker-compose up

Перейдите по адресу http://0.0.0.0:8000/

Остановка контейнера
> docker-compose down
