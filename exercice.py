#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	return [max(x) for x in numbers]


def join_integers(numbers):
	#return int(str(numbers[0])+ str(numbers[1]) + str(numbers[2]))
	return int("".join([str(n) for n in numbers]))


def generate_prime_numbers(limit):
	#permiers = liste vide
	primes = [0]
	#nombre = liste des entiers de 2 à limite
	numbers = [i for i in range(2, limit+1)]
	#tant que nombre est non vide faire
	while len(numbers) != 0 :

	# Ajouter à premier le premier entier de nombre
		primes.append(numbers[0])
	# nombres = liste des entiers de nombres non multiples du premier
		numbers = [elem for elem in numbers if elem % numbers[0] != 0]

	#Resultats premiers
	return primes

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	#return [s + str(i) 	for i in range(1, num_combinations + 1) for s in strings if excluded_multiples is None or i % excluded_multiples != 0 ]
	result = []
	for i in range(1, num_combinations + 1):
		for s in strings:
			if excluded_multiples is None or i % excluded_multiples != 0:
				result.append(s + str(i))
	return result


if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))

#for elem in numbers:
	#if elem % numbers[0] != 0:
		#numbers2.append(elem)
#numbers = numbers2