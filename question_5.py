import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = np.random.normal(loc=0, scale=1, size=1000)
x = np.arange(1000)
plt.figure(figsize=(10, 5))
plt.scatter(x, data, color='blue', alpha=0.6, s=10)
plt.title("Scatter Plot of 1000 Normally Distributed Random Numbers")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.show()
df = pd.DataFrame({"Index": x,"Value": data})
print("First 20 values:")
print(df.head(20).to_string(index=False))
