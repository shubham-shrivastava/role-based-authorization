# Role based Authorization
Simple API to show role based authorization using basic authentication in a virtual news agency. There are 3 groups viz Admin, Editor and Subscriber. Admin can add users belonging to different groups, he can also add, remove or update various news articles. Editor can only do CRUD on Articles whereas subscriber has only readonly access to articles. 

### Running locally

Clone this repo
```sh
$ git clone https://github.com/shubham-shrivastava/role-based-authorization.git
```
Now create the virtualenv of Python3.6 using
```sh
$ virtualenv my_env
```
OR if using conda
```sh
$ conda create --name my_env python=3
```
Activate the environment.
```sh
$ activate my_env
```
or
```sh
$ ./bin/activate
```
Now install requirements using pip. 

```sh
$ pip install -r requirements.txt
```

Create a database and add a superuser. 

```sh
$ python manage.py makemigrations && python manage.py migrate
$ python manage.py createsuperuser
```

Run the app

```sh
$ python manage.py runserver
```
Your application will now be running and you will be able to add users to different groups and perform CRUD on articles. 

### Note : Add groups using admin dashboard (<base_url>/admin) before adding users. You can also use the provided db(username=admin, password=Shubham@25)