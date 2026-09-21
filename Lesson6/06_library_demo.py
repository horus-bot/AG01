import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------
# 1. NumPy
# -----------------------------

marks = np.array([78, 85, 92, 67, 88])

print("Marks:", marks)
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))


# -----------------------------
# 2. Pandas
# ----------------------------

data = {
    "Name": ["Aruna", "Rahul", "Meera", "Arjun", "Diya"],
    "Marks": marks
}

df = pd.DataFrame(data)

print("\nStudent Data:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())


# -----------------------------
# 3. Matplotlib
# -----------------------------


plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()