import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("plots.csv")

features = ["valence", "energy", "danceability"]

for i, feature in enumerate(features, 1):
    plt.figure()
    sns.scatterplot(x=df["Songs"], y=df[f"My_{feature}"], label="My Ratings", color="blue", marker="o", s=100)
    sns.scatterplot(x=df["Songs"], y=df[f"Mmt_{feature}"], label="Class Average", color="green", marker="s", s=100)
    sns.scatterplot(x=df["Songs"], y=df[f"Spotify_{feature}"], label="Spotify Ratings", color="red", marker="^", s=100)
    
    plt.xticks(rotation=90)
    plt.xlabel("Songs")
    plt.ylabel(f"{feature.capitalize()}")
    plt.title(f"Comparison of {feature.capitalize()} Ratings")
    plt.legend()
    plt.tight_layout()
    plt.show()
