import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Data Manipulation with Pandas
data = {'Name': ['John', 'Jane', 'Bob'],
        'Age': [28, 25, 32],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)

# Displaying the DataFrame
print("Original DataFrame:")
print(df)

# Exploratory Data Analysis (EDA) and Data Visualization
# Load a sample dataset
tips = sns.load_dataset('tips')

# Display basic statistics
print("\nBasic Statistics:")
print(tips.describe())

# Visualize the distribution of total bill amounts
plt.figure(figsize=(8, 5))
sns.histplot(tips['total_bill'], bins=20, kde=True)
plt.title('Distribution of Total Bill Amounts')
plt.xlabel('Total Bill Amount')
plt.ylabel('Frequency')
plt.show()

# Visualize the relationship between total bill and tip
plt.figure(figsize=(8, 5))
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill Amount')
plt.ylabel('Tip Amount')
plt.show()

# Implementing Basic Machine Learning Model (Linear Regression)
# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# Make predictions on the test set
y_pred = lin_reg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'\nMean Squared Error: {mse}')

# Visualize the linear regression line
plt.scatter(X_test, y_test, color='blue', label='Actual Data')
plt.plot(X_test, y_pred, color='red', linewidth=3, label='Linear Regression Model')
plt.title('Linear Regression Model')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
