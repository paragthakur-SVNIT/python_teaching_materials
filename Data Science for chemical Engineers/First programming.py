# Starter Kit: First Lecture - Data Science for Chemical Engineers

# =============================
# 1. Importing Basic Libraries
# =============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =============================
# 2. Sample Dataset (Synthetic)
# =============================
# Simulated dataset: Flow Rate vs Temperature vs Viscosity
np.random.seed(0)
n = 100
flow_rate = np.random.uniform(10, 100, n)
temperature = np.random.uniform(20, 80, n)
# Assume viscosity depends on temperature inversely and slightly on flow
viscosity = 1000 / (temperature + 10) + 0.05 * flow_rate + np.random.normal(0, 2, n)

# Create DataFrame
data = pd.DataFrame({
    'Flow Rate (L/min)': flow_rate,
    'Temperature (°C)': temperature,
    'Viscosity (cP)': viscosity
})

# =============================
# 3. Initial Data Exploration
# =============================
print("\nFirst five rows of the dataset:")
print(data.head())

print("\nBasic statistics:")
print(data.describe())

# =============================
# 4. Data Visualization
# =============================
sns.set(style="whitegrid")
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.scatterplot(x='Temperature (°C)', y='Viscosity (cP)', data=data)
plt.title('Viscosity vs Temperature')

plt.subplot(1, 2, 2)
sns.scatterplot(x='Flow Rate (L/min)', y='Viscosity (cP)', data=data)
plt.title('Viscosity vs Flow Rate')

plt.tight_layout()
plt.show()

# =============================
# 5. Linear Regression Example (Preview)
# =============================
X = data[['Temperature (°C)', 'Flow Rate (L/min)']]
y = data['Viscosity (cP)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
rmse = mean_squared_error(y_test, predictions, squared=False)

print("\nModel Coefficients:")
print(f"Intercept: {model.intercept_:.2f}")
print(f"Temperature Coefficient: {model.coef_[0]:.2f}")
print(f"Flow Rate Coefficient: {model.coef_[1]:.2f}")
print(f"RMSE on Test Set: {rmse:.2f} cP")
