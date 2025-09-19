# CV Generator

A Django-based web application for generating professional CVs (resumes) dynamically.

## Features
- User-friendly interface for CV creation
- Dynamic templates for resume generation
- Modular Django app structure
- SQLite database for data storage

## Project Structure
```
db.sqlite3
manage.py
cv_generator/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    urls.py
    views.py
    migrations/
resume/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
    templates/
        resume/
            base.html
```

## Getting Started

### Prerequisites
- Python 3.8+
- Django 4.x

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/zohaibk22/cv-gen.git
   cd cv-gen
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install django
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Access the app at `http://127.0.0.1:8000/`
- Follow the prompts to generate your CV

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
