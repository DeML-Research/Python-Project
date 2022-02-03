
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import pandas as pd
import data as dt

# -- TEST 1 : 
# verify that the script is being read
print(dt.dict_test)

# -- TEST 2 :
# verify that installed pandas module works correctly
df_dict_test = pd.DataFrame(dt.dict_test, index=[0, 1])
print(df_dict_test)

# -- TEST 3 :
# verify you can use plotly and visualize plots in jupyter notebook

import chart_studio.plotly as py   # various tools (jupyter offline print)
import plotly.graph_objects as go  # plotting engine

# example data
df = pd.DataFrame({'column_a': [1, 2, 3, 4, 5], 'column_b': [1, 2, 3, 4, 5]})
# basic plotly plot
data = [go.Bar(x=df['column_a'], y=df['column_b'])]
# instruction to view it inside jupyter
py.iplot(data, filename='jupyter-basic_bar')
# (alternatively) instruction to view it in web app of plotly
py.plot(data)

# -- TEST 4 :
# verify you can use plotly and visualize plots in web browser locally

import plotly.io as pio            # to define input-output of plots
pio.renderers.default = "browser"  # to render the plot locally in your default web browser

# basic plotly plot
plot_data = go.Figure(go.Bar(x=df['column_a'], y=df['column_b']))
# instruction to view it in specified render (in this case browser)
plot_data.show()
