import pandas as pd
import matplotlib.pyplot as plot

dframe = pd.read_csv('cars.csv')

print(dframe.to_html())