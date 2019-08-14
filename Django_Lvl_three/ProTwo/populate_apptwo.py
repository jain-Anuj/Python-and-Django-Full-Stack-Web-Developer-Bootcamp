import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N = 5):
    for entry in range(N):
        fake_name = fakegen.name().split(" ")
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name = fake_name[0], last_name = fake_name[1], email = fake_email)

if __name__ == '__main__':
    print("Populating Script!")
    populate(20)
    print("Population Complete!!")    
