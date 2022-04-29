# Django Course is an educational platform where everybody can learn something new 💻​📕​
<hr/>

### App features:
- Display list of all available course;
- Order course by parameters;
- Join/Leave course;
- Download a course files;
- Display list of student's courses;
- JWT Authentication;
- Database transaction;
- Create/Update/Delete course (only for admin);
- Test coverage;
- API Documentation;

### Stack:
- Python
- Django Rest
- Postgresql

<hr/>

### Installation:
1. Create & activate venv
2. Install requirements.txt
```python
pip install -r requirements.txt
```
3. Change **.env** file
````dotenv
SECRET_KEY=
DEBUG=
DB_NAME=
DB_USER=
DB_PASS=
DB_HOST=
DB_PORT=
````
4. Make migrations
```python
python manage.py makemigrations
python manage.py migrate
```
5. Run application
```python
python manage.py runsever
```
6. Run tests
```
python manage.py test .
```
7. Check test coverage
```python
coverage run --source='.' python manage.py test .
coverage report
```
<hr/>

### Endpoints:

- Get all courses (GET)
```
http://localhost:8000/api/v1/course/
```
- Get detail info about course (GET)
```
http://localhost:8000/api/v1/course/detail/<slug>/
```
- Get all courses sort by price (GET)
```
http://localhost:8000/api/v1/course?price=lowest/
http://localhost:8000/api/v1/course?price=highest/
```
- Get all courses sort by date (GET)
```
http://localhost:8000/api/v1/course?date=newest/
http://localhost:8000/api/v1/course?date=oldest/
```
- Get all courses sort by popularity (GET)
```
http://localhost:8000/api/v1/course?popularity=up/
http://localhost:8000/api/v1/course?popularity=down/
```
- Get all student's courses (GET)
```
http://localhost:8000/api/v1/course/my-courses/
```
- Join student to course (POST)
```
http://localhost:8000/api/v1/course/join/<slug>/
```
- Download a course files (GET)
```
http://localhost:8000/api/v1/course/download/<slug>/
```
- Remove student from course (POST)
```
http://localhost:8000/api/v1/course/remove/<slug>/
```
- Create new course (POST) (only admin)
```
http://localhost:8000/api/v1/course/new/
```
- Update course (PUT) (only admin)
```
http://localhost:8000/api/v1/course/update/<slug>/
```
- Delete course (DELETE) (only admin)
```
http://localhost:8000/api/v1/course/delete/<slug>/
```
- Swagger
```
http://localhost:8000/api/v1/swagger/
```
<hr/>

### Structure:

```
core
+---core
¦   ¦   __init__.py
¦   ¦   asgi.py
¦   ¦   settings.py
¦   ¦   urls.py
¦   ¦   wsgi.py
+---course
¦    +   migrations
¦    ¦   ¦    __init__.py
¦    +   tests
¦    ¦   ¦   __init__.py
¦    ¦   ¦   test_serializers.py
¦    ¦   ¦   test_urls.py
¦    ¦   __init__.py
¦    ¦   admin.py
¦    ¦   apps.py
¦    ¦   models.py
¦    ¦   serializers.py
¦    ¦   services.py
¦    ¦   urls.py
¦    ¦   view.py
     manage.py
README.md
requirements.txt
```
