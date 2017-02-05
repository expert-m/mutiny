# 42 bugs


## Admin
**Login:** `admin`

**Password:** `test1010`


## Настройка проекта:
1. Открыть проект в PyCharm
2. В `File` > `Settings` > `Project Interpreter` > `Add Local` прописать путь к `venv/bin/python3.5`


## Создание виртуального окружения
1. `sudo pip3 install virtualenv`
2. `virtualenv venv --no-site-packages`
3. `source venv/bin/activate`
4. `pip3 install -r requirements.txt`

**Активация:**
```
source venv/bin/activate
```


## API

* **/api/meetings/** `GET`
* **/api/feedback/** `PUT`
* **/api/comments/** `GET`, `DELETE`
* **/api/messages/** `GET`, `POST` (создать сообщение), `DELETE` (удалить сообщение)
* **/api/subscription/** `POST` (подписаться), `DELETE` (отписаться)
* **/api/posts/** `GET`
* **/api/tags/** `GET`
* **/api/projects/** `GET`, `POST` (присоединится к проекту), `DELETE` (прокинуть проект)
* **/api/auth/** `GET` (вход), `POST` (регистрация), `DELETE` (выход)
* **/api/reset_password/** `PUT`
* **/api/users/** `GET`
* **/api/reviews/** `GET`, `POST`
* **/api/profile/** `GET` (получение профиля текущего пользователя), `PUT` (изменение профиля), `DELETE`
