import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('titanic')

# Basic info
print("Shape of the dataset:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())

# Summary statistics
print("\nSummary Statistics:\n", df.describe(include='all'))

# Count of survivors
print("\nSurvival Count:\n", df['survived'].value_counts())

# Visual: Survival by gender
sns.countplot(x='survived', hue='sex', data=df)
plt.title("Survival Count by Gender")
plt.show()

