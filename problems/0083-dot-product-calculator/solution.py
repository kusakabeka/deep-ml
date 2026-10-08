import numpy as np

def calculate_dot_product(vec1, vec2):
	dot_prod = 0
	for i in range(len(vec1)):
		dot_prod += (vec1[i] * vec2[i])
	return dot_prod