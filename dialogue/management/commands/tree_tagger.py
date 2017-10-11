import logging, sys
from django.core.management.base import BaseCommand
#  , CommandError
import treetaggerwrapper as ttw

class Command(BaseCommand):
    """ Main """
        print ('Do you have any questions?')
        input_test_word = input('>>>  ')
        print ('your question: ' + input_test_word )
        # tagger
        tagger = ttw.TreeTagger(TAGLANG='en', TAGDIR='/usr/local/src/tree-tagger')
        tags = tagger.TagText(str)
        #  print("output:" + tags)
        for tag in tags:
            print(tag)
