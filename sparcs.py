import pandas as pd
import matplotlib.pyplot as plt

## dataset loading
df = pd.read_csv('/Users/sarahdancyger/Desktop/WE Fall 507 Williams Python+R/SPARCS_2022.csv')

## field separation
df_subset = df[['Age Group', 'Gender', 'Length of Stay', 'Total Charges', 'Total Costs', 'Type of Admission']]

stats = df_subset[['Length of Stay', 'Total Charges', 'Total Costs']].describe()

print("Basic Descriptive Statistics:")
print(stats)

age_group_counts = df_subset['Age Group'].value_counts()
gender_counts = df_subset['Gender'].value_counts()
admission_counts = df_subset['Type of Admission'].value_counts()

print("\nAge Group Distribution:")
print(age_group_counts)
print("\nGender Distribution:")
print(gender_counts)
print("\nType of Admission Distribution:")
print(admission_counts)

## Histogram : Length of stay
plt.figure(figsize=(10, 5))
plt.hist(df_subset['Length of Stay'], bins=20, edgecolor='black', color='lightgreen')
plt.title('Histogram of Length of Stay')
plt.xlabel('Length of Stay (Days)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('length_of_stay_histogram.png')
plt.show()

## Boxplot  : Total charges
plt.figure(figsize=(10, 5))
plt.boxplot(df_subset['Total Charges'], patch_artist=True)
plt.title('Boxplot of Total Charges')
plt.ylabel('Total Charges')
plt.tight_layout()
plt.savefig('total_charges_boxplot.png')
plt.show()

## Barplot : Type of Admission
plt.figure(figsize=(10, 5))
age_group_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('age_group_distribution.png')
plt.show()

