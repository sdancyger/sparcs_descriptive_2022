import pandas as pd
import matplotlib.pyplot as plt

## dataset loading
df = pd.read_csv('/Users/sarahdancyger/Desktop/WE Fall 507 Williams Python+R/SPARCS_2022.csv')

## field separation
df_subset = df[['Age Group', 'Gender', 'Length of Stay', 'Total Charges', 'Total Costs', 'Type of Admission']]

