### initialisation
import random
error = 0																	#number of try
chance = 6

abc = ['a','b','c','d','e','f','g','h','i',
	'j','k','l','m','n','o','p','q','r','s',
	't','u','v','w','x','y','z']											# array of letter

word = ['whats','the','use','of','feeling','blue']							# array of words

letter_try = []																# array of guessed letter

man = ['1','2','3','4','5','6']																	#array for the disign of thee hangman
woman = ['01','02','03','04','05','06']																	#array for the disign of the hangwoman

guess = 'a'
one_more = 'yes'															#initialisation of the loop to retry
play_word = []

while one_more == 'yes' :
	nb_word = random.randint(0,5)											#choose a random number
	to_guess = word[nb_word]												#choose the word from the random number
	game = list(to_guess)													#list the word
	for i in range (len(game)) :
		play_word.append('_')												#affichage du mot play_word
	perso = input('do you want to hang a man or a woman')					#choose a man or a woman
	print (to_guess)
	while chance > 0 and "".join(play_word) !=  to_guess:							#loop while the player can still play
		print (to_guess)																
		print ('You have try',letter_try)									#show the letter who have been used
		print ('You have the right to make up to', chance, 'errors')			
		#print (play_word)													#show the hangpeople
		print("".join(play_word))
		guess = input('Guess a letter:')									#take in count the letter to guess
		letter_try.append(guess)
		
		if guess in to_guess:
			for char in enumerate(game) :
				if guess == game[char[0]]:					
					play_word[char[0]] = guess
		else:	
			chance -= 1
		
	one_more = input('Do you want to continue : yes/no')					#change the variable if the player want to continue
print ('Thanks for playing =)')