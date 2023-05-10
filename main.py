import pandas as pd

pop_file = 'KEN_1961-2020_population.csv'
gdp_file = 'KEN_1961-2020_GDP.csv'

pop_data = ['year', 'population_percentage_change']
gdp_columns = ['gdp_percentage_change']

pop = pd.read_csv(pop_file)[pop_data]
gdp = pd.read_csv(gdp_file)[gdp_columns]

combined = pd.concat([pop, gdp], axis=1)

print(combined)

combined.to_csv('output_file.csv', index=False)
