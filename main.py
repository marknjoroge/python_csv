import pandas as pd

# Paths to csv files
pop_file = 'https://raw.githubusercontent.com/marknjoroge/python_csv/main/KEN_1961-2020_population.csv' 
gdp_file = 'https://raw.githubusercontent.com/marknjoroge/python_csv/main/KEN_1961-2020_GDP.csv'

# columns to be used
pop_data = ['year', 'population_percentage_change']
gdp_columns = ['gdp_percentage_change']

# read and select columns
pop = pd.read_csv(pop_file, encoding='utf-8')[pop_data]
gdp = pd.read_csv(gdp_file, encoding='utf-8')[gdp_columns]

# combine the two dataframes
combined = pd.concat([pop, gdp], axis=1)
print(combined)

# output to csv
combined.to_csv('output_file.csv', index=False)