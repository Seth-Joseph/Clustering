import csv
import seaborn as sns
import matplotlib.pyplot as plt
import plotly_express as px
from sklearn.cluster import KMeans

rows = []
with open("Star_Data.csv", "r") as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        rows.append(row)


star_data = rows[1:]

mass = []
radius = []

temp_star_data = list(star_data)

for data in temp_star_data:
    planet_gravity = data[5]

    if planet_gravity.lower() == 'unknown':
        star_data.remove(data)

for data in star_data:
    mass.append(data[3])
    radius.append(data[4])

X = []

for idx, mass in enumerate(mass):
  temp_list = [radius[idx], mass]
  X.append(temp_list)

wcss = []

for i in range(1, 11):
  kmeans = KMeans(n_clusters = i, init='k-means++', random_state=42)
  kmeans.fit(X)
  
  wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))

sns.lineplot(range(1, 11), wcss, marker='o', color='red')
plt.title('elbow Methord')
plt.xlabel('no. of cluster')
plt.ylabel('wcss')
plt.show()