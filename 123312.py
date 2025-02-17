import os
from django.core.management.utils import get_random_secret_key

# Создаем папку проекта
project_name = "myproject"
os.system(f"django-admin startproject {project_name}")

# Переходим в папку проекта
os.chdir(project_name)

# Создаем файл зависимостей
requirements = """
django
psycopg2-binary
django-environ
"""
with open("requirements.txt", "w") as f:
    f.write(requirements)

# Генерируем SECRET_KEY
secret_key = get_random_secret_key()

# Настраиваем .env файл
env_content = f"""
DEBUG=True
SECRET_KEY={secret_key}
DATABASE_NAME=mydb
DATABASE_USER=myuser
DATABASE_PASSWORD=mypassword
DATABASE_HOST=db
DATABASE_PORT=5432
"""
with open(".env", "w") as f:
    f.write(env_content)
    

print("Django проект создан! Теперь установи зависимости и настрой базу данных.")

