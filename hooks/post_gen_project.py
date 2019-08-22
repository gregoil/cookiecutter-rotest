import os

if __name__ == '__main__':
    os.system("cd {{ cookiecutter.project_slug }}")
    os.system("python manage.py migrate --settings={{ cookiecutter.project_slug }}.settings")
