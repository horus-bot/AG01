import pandas as pd

marks = [78, 85, 92, 67, 88]
data = {
    "Name": ["Anu", "Rahul", "Meera", "Arjun", "Diya"],
    "Marks": marks
}

df = pd.DataFrame(data)

print("\nStudent Data:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
