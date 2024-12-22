from django.core.management.base import BaseCommand
from transport.models import State

class Command(BaseCommand):
    help = 'Populate the State model with Nigerian states and their numerical values.'

    def handle(self, *args, **kwargs):
        states_data = [
            ("Adamawa", 1), ("Borno", 2), ("Yobe", 3), ("Sokoto", 4), 
            ("Kebbi", 5), ("Katsina", 6), ("Kano", 7), ("Jigawa", 8), 
            ("Zamfara", 9), ("Taraba", 10), ("Gombe", 11), ("Plateau", 12), 
            ("Niger", 13), ("Kogi", 14), ("Kaduna", 15), ("Benue", 16), 
            ("Oyo", 17), ("Osun", 18), ("Ekiti", 19), ("Ondo", 20), 
            ("Edo", 21), ("Imo", 22), ("Anambra", 23), ("Abia", 24), 
            ("Enugu", 25), ("Ebonyi", 26), ("Rivers", 27), ("Bayelsa", 28),
            ("Cross River", 29), ("Akwa Ibom", 30), ("Delta", 31), 
            ("Lagos", 32), ("Ogun", 33), ("Nasarawa", 34), ("Kwara", 35),
            ("Taraba", 36)
        ]
        
        for name, code in states_data:
            State.objects.create(name=name, code=code)

        self.stdout.write(self.style.SUCCESS('Successfully populated states'))
