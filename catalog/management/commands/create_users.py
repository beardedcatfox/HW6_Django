from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help = 'Create random users'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('num_users', type=int, help='Number of users to create')

    def handle(self, *args, **kwargs):
        num_users = kwargs['num_users']
        if num_users < 1 or num_users > 10:
            raise ValueError('Number of users must be between 1 and 10')

        users = []
        fake = Faker()
        for i in range(num_users):
            username = fake.first_name()
            email = fake.email()
            user = User(username=username, email=email)
            users.append(user)

        for pas in users:
            pas.set_password(fake.password())
            User(password=pas)

        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {num_users} users'))
