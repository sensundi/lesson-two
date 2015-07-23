### MelbDjango School - Lesson Two

Introduction to Django "apps"

---

###  What is a Web Framework?

 - Provides structure for your code
 - Makes common work trivial
 - Lets you focus on the parts special to your project.

1. Protect you from the __DANGEROUS__ things.
2. Protect you from the __TEDIOUS__ things.

---

### Overview of Django

![](./img/django-flow.png)

- Request
- URL patterns
- View
- Response

---

### Creating an `app`

```
    $ ./manage.py startapp times
    $ tree .
    .
    ├── manage.py
    ├── times
    │   ├── admin.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    └── timetracker
        ├── __init__.py
        ├── settings.py
        ├── tests.py
        ├── urls.py
        └── wsgi.py

```

---

### Introduction to Databases

What is a Database?

A Collection of data (usually with some structure).

Database Management System (DBMS) is a program that manages access to and storage of a database.

---

### Database Models

- Flat File
- Record
- Hierarchical
- Network
- Key:Value
- Document
- Relational

---

### Relational Model

Invented in 1969 by Edgar Codd.

Organises data into relvars (tables) of tuples (rows), which contain attributes (columns).

- Tuples within a relvar are unique.
- Tuples have no inherent ordering
- Attributes within a Tuple have no inherent ordering

Each tuple is a statement of truth.

Tuples can express their "relation" to other truths.

---

### Benefits

Users declare the information to store, and what to retrieve, and the DBMS takes care of storage, retrieval, etc.

Removes replication of data, avoiding "update anomalies".

Data integrity is enforced by the Database Management System (DBMS).

The DBMS' configuration is managed the same way as your own data.

---

### Normalising Data

![](./img/normalise1.png)

---

### Normalising Data - Step 1

![](./img/normalise2.png)

---

### Normalising Data - Step 2

![](./img/normalise3.png)

---

### Normalising Data - Step 3

![](./img/normalise4.png)

---

### Normalising Data - Step 4

![](./img/normalise5.png)

---

### Normalising Data - Final

![](./img/normalise6.png)

---

### Models

models.py

```
    from django.db import models

    # Create your models here.
```

---

```
    from django.db import models

    # Create your models here.
    class Entry(models.Model):
        start = models.DateTimeField()
        stop = models.DateTimeField()
        client = models.CharField()
        project = models.CharField()
        description = models.CharField()

```

---

```
    from django.db import models

    from django.utils import timezone

    # Create your models here.
    class Entry(models.Model):
        start = models.DateTimeField(default=timezone.now)
        stop = models.DateTimeField(blank=True, null=True)
        client = models.CharField(max_length=200)
        project = models.CharField(max_length=200)
        description = models.CharField(max_length=200)

```

---

```
$ python manage.py makemigrations
Migrations for 'times':
  0001_initial.py:
    - Create model Entry

```

---

```
$ python manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: messages, staticfiles
  Apply all migrations: times, sessions, contenttypes, admin, auth
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying sessions.0001_initial... OK
  Applying times.0001_initial... OK
```

---
### Let's play!


```
$ python manage.py shell
```
