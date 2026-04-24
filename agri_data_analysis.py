import pandas as pd

# Sample agricultural dataset
data = {
    "Crop": ["Maize", "Rice", "Wheat", "Maize", "Rice"],
    "Soil_pH": [6.5, 5.8, 6.0, 6.8, 5.5],
    "Rainfall_mm": [200, 300, 250, 220, 310],
    "Yield_tons": [3.5, 4.0, 3.8, 3.7, 4.2]
}

df = pd.DataFrame(data)

# Display dataset
print("Dataset:\n", df)

# Average yield by crop
avg_yield = df.groupby("Crop")["Yield_tons"].mean()
print("\nAverage Yield by Crop:\n", avg_yield)

# Filter high yield crops
high_yield = df[df["Yield_tons"] > 3.8]
print("\nHigh Yield Records:\n", high_yield)

# Soil pH analysis
print("\nAverage Soil pH:", df["Soil_pH"].mean())
