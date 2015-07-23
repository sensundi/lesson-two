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

The DBMS' configuration is managed the same was as your own data.

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

 - Describe our schema
 - DRY


