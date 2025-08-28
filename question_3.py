import numpy as np
matrix = np.random.randint(1, 101, size=(5, 5))
print("Original 5x5 Matrix:")
print(matrix)
print("Maximum:", np.max(matrix))
print("Minimum:", np.min(matrix))
print("Mean:", np.mean(matrix))

normalized = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))
print("Normalized Matrix (0–1):")
print(normalized)
print("Flattened and Sorted Array:")
flattened_sorted = np.sort(matrix.flatten())
print(flattened_sorted)

