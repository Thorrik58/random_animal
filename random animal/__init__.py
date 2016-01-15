from sys import argv
from collections import defaultdict
import random

def random_animal
	adjective_dict = defaultdict(set)
	animal_dict = defaultdict(set)
	letter = argv[1] if argv and len(argv) > 1 else ''
	while not letter:
	    letter = raw_input(
	        "What letter should your animal and adjective start with?\n")
	letter = letter.upper()
	nr_of_runs = input("How many names would you like to generate?\n")
	for _ in range(nr_of_runs):
	    with open("adjectives.txt") as adjectives:
	        for adjective in adjectives:
	            adjective_dict[adjective[0]].add(adjective.rstrip('\n'))
	    with open("animals.txt") as animals:
	        for animal in animals:
	            animal_dict[animal[0]].add(animal.rstrip('\n'))

	    random_adjective = random.sample(adjective_dict[letter], 1)
	    random_animal = random.sample(animal_dict[letter], 1)

	    print random_adjective[0] + ' ' + random_animal[0]
