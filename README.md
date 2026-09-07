# Python Programming Course

Practice exercises and small demo projects written while learning Python, from basic syntax through web development with Django.

## Features

The exercises are organized by topic, roughly in the order they were learned:

- Core language: data structures, operators, conditionals, loops, functions, OOP, modules, error handling, file handling, advanced function features, iterators, generators
- Web scraping and browser automation with Selenium and BeautifulSoup
- Data analysis and visualization with NumPy, Pandas, and Matplotlib
- Relational and NoSQL databases: MySQL, SQLite, and MongoDB
- A small desktop GUI application built with PyQt5
- A Django web application (a movie catalog with user registration, login, and messaging)

## Tech stack

- Python 3
- Selenium, BeautifulSoup, Requests
- NumPy, Pandas, Matplotlib
- MySQL Connector, SQLite3, PyMongo
- PyQt5
- Django 2.2

## Installation

```bash
git clone <this-repo-url>
cd python-kursu-master
pip install -r requirements.txt
```

Some modules need extra setup:

- **Selenium (module 14)**: download `chromedriver` and/or `geckodriver` matching your installed browser version and place them in `src/14-selenium-web-automation/`, or point Selenium at wherever you installed them. These binaries are not included in the repo.
- **MySQL (module 18)**: requires a local MySQL server; update the placeholder password in the connection scripts with your own.
- **MongoDB (module 19)**: requires a local MongoDB instance or your own MongoDB Atlas connection string in `mongodb-connections.py`.
- **Pandas (module 16)**: `datasets/youtube-ing.csv` is not included (51 MB) because of its size — the other, smaller sample datasets in that folder are included.

## Usage

Each file under `src/` is a standalone script or small project meant to be run and read on its own, e.g.:

```bash
python src/04-loops/for-demo.py
```

The Django project is run the usual way:

```bash
cd src/21-django-movie-catalog/catalog
python manage.py migrate
python manage.py runserver
```

The PyQt5 apps are run directly, e.g.:

```bash
python src/20-desktop-app-pyqt5/calculator.py
```

## Project structure

```
src/
├── 01-python-objects-and-data-structures/
├── 02-operators/
├── 03-conditional-statements/
├── 04-loops/
├── 05-functions/
├── 06-object-oriented-programming/
├── 07-modules/
├── 08-errors-and-exception-handling/
├── 09-file-handling/
├── 10-advanced-functions/
├── 11-iterators/
├── 12-generators/
├── 13-advanced-modules/
├── 14-selenium-web-automation/
├── 15-numpy/
├── 16-pandas/
├── 17-matplotlib/
├── 18-sql-databases/
├── 19-nosql-mongodb/
├── 20-desktop-app-pyqt5/
└── 21-django-movie-catalog/
```

## Limitations

- These are learning exercises, not production code — error handling, input validation, and security practices are minimal in places (e.g. the Django `SECRET_KEY` is a placeholder and must be replaced before any real deployment).
- The Selenium scripts (module 14) depend on specific page layouts (XPath selectors) of third-party sites at the time they were written and will likely need updating to still work.
- The MySQL and MongoDB scripts expect a local database that isn't included; you need to set one up yourself and update the connection details.

## About

This project was a simple self-study exercise I built in high school (2020) to develop my computer/programming skills through courses I was taking at the time. It was reorganized and cleaned up in 2026 for public release.

> 📝 TODO: add the course/resource that inspired this project

## License

MIT — see [LICENSE](LICENSE).
