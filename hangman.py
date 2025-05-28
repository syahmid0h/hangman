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

def display_hint(hint):
    pass

def display_answer(answer):
    pass

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    

if __name__ == "__main__":
    main()