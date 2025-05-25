import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

sns.countplot(x='sex', hue='survived', data=df)
plt.title('Survival Count by Gender')
plt.show()

sns.countplot(x='pclass', data=df)
plt.title('Passenger Class Distribution')
plt.show()

sns.histplot(df['age'].dropna(), bins=30, kde=True)
plt.title('Age Distribution of Passengers')
plt.show()

sns.scatterplot(x='age', y='fare', hue='survived', data=df)
plt.title('Fare vs Age (Colored by Survival)')
plt.show()

