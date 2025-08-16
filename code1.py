import pandas as pd
import os 

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

# Absolute path
base_dir = r"C:\Users\DELL\Desktop\mlops\DVC"
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "people.csv")
df.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")
