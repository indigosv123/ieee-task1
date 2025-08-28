import numpy as np

matrix = np.random.randint(1, 101, size=(5, 5))

print("OG Matrix:")
print(matrix)

minv = np.min(matrix)
maxv = np.max(matrix)
normalized = (matrix - minv) / (maxv - minv)

print("Normalized Matrix:")
print(normalized)

middle33 = normalized[1:4, 1:4]
print("Middle 3x3 Matrix:")
print(middle33)


row1 = middle33[0, :]
rowend= middle33[:, -1]   

print("First row of 3x3:", row1)
print("Last column of 3x3:", rowend)

# Step 5: Compute dot product
dot_product = np.dot(row1, rowend)
print("Dot Product:", dot_product)
