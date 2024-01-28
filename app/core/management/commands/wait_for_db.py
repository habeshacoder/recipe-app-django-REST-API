import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError

from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2OpError, OperationalError) as e:
                self.stdout.write("database Unavailable waiting for 1 sec...")
                self.stdout.write(str(e))  # Print the error message
                time.sleep(1)
        self.stdout.write("connection successfully done")
