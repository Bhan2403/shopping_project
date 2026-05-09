
import pandas as pd

df = pd.read_csv("shopping_behavior_updated.csv")

print(
    df["Frequency of Purchases"]
    .unique()
)

