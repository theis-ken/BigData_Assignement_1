import pandas as pd
import matplotlib.pyplot as plt
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["books_db"]
collection = db["books"]

# Load data into a DataFrame
data = pd.DataFrame(list(collection.find()))

# Price Distribution Histogram
plt.figure(figsize=(10, 6))
plt.hist(data['price'], bins=20, color='blue', edgecolor='black')
plt.title('Price Distribution of Books')
plt.xlabel('Price (£)')
plt.ylabel('Number of Books')
plt.grid(axis='y', alpha=0.75)
plt.show()

# Availability Pie Chart
availability_counts = data['availability'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(availability_counts, labels=availability_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Availability of Books')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
