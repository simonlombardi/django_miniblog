from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help = 'Te saludo'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            'nombre',
            type=str,
            help='Tu nombre para que te diga hola'
        )

    def handle(self, *args, **kwargs):
        nombre = kwargs['nombre']
        print(f'HOLA {nombre}')