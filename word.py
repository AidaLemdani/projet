import random
word = ['whats','the','use','of','feeling','blue']

nb_word = random.randint(0,6)					#choose the word randomly
to_guess = word[nb_word]
print (to_guess)
game = list(to_guess)
print (len(game))