import logging
from django.core.management.base import BaseCommand
#  , CommandError
import treetaggerwrapper as ttw

class Command(BaseCommand):
    """ Main """
    def handle(self, *args, **options):
        str = "Hello! This is Django batch."
        print("input:" + str)
        tagger = ttw.TreeTagger(TAGLANG='en', TAGDIR='/usr/local/src/tree-tagger')
        tags = tagger.TagText(str)
        #  print("output:" + tags)
        for tag in tags:
            print(tag)
