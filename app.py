#### THIS IS A COPY -- DELETE AND REPLACE ALL



######### Import your libraries #######
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State

import pandas as pd
import numpy as np
import os
import plotly as py
import plotly.graph_objs as go
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#init_notebook_mode(connected=True)


###### Define your variables #####
tabtitle = "Daniel's Project 9!"
sourceurl = 'https://www.kaggle.com/datasets/mylesoneill/game-of-thrones?select=character-deaths.csvb'
githublink = 'https://github.com/daniel-varela-3/ds-project-8'

Region = pd.DataFrame({'Allegiances': ['Arryn', 'Baratheon', 'Greyjoy', 'Lannister', 'Martell',"Night's Watch",'None','Stark','Targaryen','Tully','Tyrell','Wildling'], 'Westeros Location': ['East', 'East', 'West', 'West', 'South',"North",'None','North','East','Midwest','West','North']})
royalty = pd.DataFrame({'Allegiances': ['Targaryen', 'Baratheon', 'Lannister','Stark'], 'Number of Kings/Queens': [18,3,1,1]})

# list of columns 
analysis_list=['Death Counts', 'Number of Kings/Queens']


###### Import a dataframe #######
df = pd.read_csv("data/asoiaf_book_deaths.csv")


###### Make changes to dataframe #####
# df['Death Chapter'].fillna(666, inplace=True)
# df['Death Year'].fillna(666, inplace=True)
# df['Book of Death'].fillna(666, inplace=True)
# df['Book Intro Chapter'].fillna(666, inplace=True)

# df2 = df[df['Death Chapter'] != 666]
# df2["Allegiances"] = df2["Allegiances"].str.replace("House ","")
# df2["Death Count"] = 1

# df2_grouped = df2.groupby("Allegiances").count().reset_index()
# df2_grouped["Death Count"] = df2_grouped["Death Year"] 
# deaths_by_allegiance = df2_grouped[["Allegiances","Death Count"]]

# df3 = pd.merge(deaths_by_allegiance, Region, how="left",left_on="Allegiances",right_on="Allegiances")

# df4 = pd.merge(df3, royalty, how = "left", left_on="Allegiances",right_on="Allegiances")
# df4['Number of Kings/Queens'].fillna(0, inplace=True)
# df4.sort_values(by=['Death Count'], inplace=True)



########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1('Stats of Ice and Fire'),
    html.Div([
        html.Div([
                html.H6('Select a statistic for your analysis:'),
                dcc.Dropdown(
                    id='options-drop',
                    options=[{'label': i, 'value': i} for i in analysis_list],
                    value='Death Counts'
                ),
        ], className='two columns'),
        html.Div([dcc.Graph(id='figure-1'),
            ], className='ten columns'),
    ], className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


######### Interactive callbacks go here #########
# @app.callback(Output('display-value', 'figure'),
#               [Input('dropdown', 'value')])
# def display_value(continuous_var):
    
#     #grouped_mean=df.groupby(['Embarked', 'Cabin Class'])[continuous_var].mean()  #### I Think I need to bring in calcs into here
    
#     # bring DF, group by X,Y columns... and find mean of Z olumn (which is input to function)
#     location_grouped = df4.groupby(["Westeros Location"])[continuous_var].sum()
#     location_results = pd.DataFrame(location_grouped)
    
#     #results=pd.DataFrame(grouped_mean)
    
#     # Create a bar chart
#     mydata1 = go.Bar(
#         x=location_results.index,
#         y=location_results[continuous_var],
#         #name='Port Cherbourg',
#         marker=dict(color=color1)
#     )
   
#     mylayout = go.Layout(
#         title='Bar chart',
#         xaxis = dict(title = 'Region'), # x-axis label
#         yaxis = dict(title = str(continuous_var)), # y-axis label

#     )
#     fig = go.Figure(data=[mydata1], layout=mylayout)
#     return fig

############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
