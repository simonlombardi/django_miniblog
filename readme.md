## Pasos para levantar el proyecto

1. clonar el repositorio: 
~~~
git clone https://github.com/simonlombardi/django_miniblog.git
~~~
2. crear entorno virtual:
~~~
python3 -m venv venv
~~~
3. activar entorno virtual:
~~~
source venv/bin/activate
~~~
4. instalar dependencias:
~~~
pip install -r requirements.txt
~~~
5. moverser hacia el directorio que se creó:
~~~
cd django_miniblog
~~~
6. generar migracion:
~~~
python3 manage.py migration
~~~
7. correr el pryecto
~~~
python3 manage.py runserver
~~~




