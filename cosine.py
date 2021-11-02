# Python code below
# Use print("messages...") to debug your solution.
import numpy as np

def euclidean(vector1, vector2):
    return np.sqrt(np.dot((vector1 - vector2).T, (vector1 - vector2)))


def cosine(vector1, vector2):
	return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))