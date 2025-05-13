import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("correlation.csv")
df = df.drop(columns=["Spotify_valence", "Spotify_energy", "Spotify_danceability"])

features = ["valence", "energy", "danceability", "hedonic", "eudaimonic"]
song = df.loc[(df[[f"My_{feature}" for feature in features]] - df[[f"Mmt_{feature}" for feature in features]]).abs().sum(axis=1).idxmax(),"Songs"]
print(f"Song with the largest difference from Class Average): {song}")

correlation_matrix = df.drop(columns=["Songs"]).corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix (My Ratings vs. MMT)")
plt.tight_layout()
plt.show()