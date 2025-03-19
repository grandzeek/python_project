import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load the dataset (Replace 'your_dataset.csv' with your actual file)
    df = pd.read_csv('your_dataset.csv')
    
    # Display the first few rows
    print("First 5 rows of the dataset:")
    print(df.head())
    
    # Display dataset info
    print("\nDataset Info:")
    print(df.info())
    
    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Fill or drop missing values
    df = df.fillna(df.mean())  # Filling missing values with column mean
except FileNotFoundError:
    print("Error: Dataset file not found.")
    exit()

# Task 2: Basic Data Analysis
print("\nBasic Statistics:")
print(df.describe())

# Group by a categorical column (Replace 'CategoryColumn' with actual column name)
if 'CategoryColumn' in df.columns:
    group_mean = df.groupby('CategoryColumn')['NumericalColumn'].mean()
    print("\nMean values per category:")
    print(group_mean)

# Task 3: Data Visualization
plt.figure(figsize=(12,6))

# Line Chart (Replace 'TimeColumn' and 'ValueColumn' with actual names)
plt.subplot(2,2,1)
df.plot(x='TimeColumn', y='ValueColumn', kind='line', title='Trend Over Time')

# Bar Chart (Replace 'CategoryColumn' and 'NumericalColumn')
plt.subplot(2,2,2)
df.groupby('CategoryColumn')['NumericalColumn'].mean().plot(kind='bar', title='Category Comparison')

# Histogram (Replace 'NumericalColumn')
plt.subplot(2,2,3)
df['NumericalColumn'].plot(kind='hist', title='Histogram of a Numerical Column', bins=20)

# Scatter Plot (Replace 'NumericalColumn1' and 'NumericalColumn2')
plt.subplot(2,2,4)
sns.scatterplot(x=df['NumericalColumn1'], y=df['NumericalColumn2'])
plt.title('Scatter Plot')

plt.tight_layout()
plt.show()
