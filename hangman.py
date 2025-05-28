import random

words = ("red", 'yellow', 'green', 'blue', 'brown', 'pink', 'purple', 'black')


#ASCII ART
hangman_art = {0:('   ',
                  '   ',
                  '   '), 
               1:(' O ',
                  '   ',
                  '   '), 
               2:(' O ',
                  ' | ',
                  '   '), 
               3:(' O ',
                  '/| ',
                  '   '), 
               4:(' O ',
                  '/|\\',
                  '   '), 
               5:(' O ',
                  '/|\\',
                  '/  '), 
               6:(' O ',
                  '/|\\',
                  '/ \\ ')}