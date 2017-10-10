import logging
from django.core.management.base import BaseCommand
#  , CommandError

class Command(BaseCommand):
    """ Main """
    def handle(self, *args, **options):
        print( "Hello! Django batch" )