import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import base64
import json
import dash_auth
from dash.dependencies import Input, Output, State



#--------------------Preparation

#load file
fileku = pd.read_excel('topclub.xlsx',sheet_name='Sheet1')
file2 = pd.read_csv('gapminderDataFiveYear.csv')
file3 = pd.read_csv('mpg.csv')
file4 = pd.read_csv('wheels.csv')


#make filter
list_filter = fileku['Club Name'].sort_values().unique()
filter1 = []
for i in list_filter:
    filter1.append({'label':i,'value':i})



#make filter2
list_filter2 = file2['year'].sort_values().unique()
filter2 = []
for j in file2['year'].sort_values().unique():
    filter2.append({'label':str(j),'value':j})
    
#make filter3
list_filter3 = file3.columns
filter3 = []
for k in list_filter3:
    filter3.append({'label':k,'value':k})
    
#make filter4
list_filter4 = file4['wheels'].unique()
filter4 = [{'label':i,'value':i} for i in file4['wheels'].unique()]
list_filter4b = file4['color'].unique()
filter4b = [{'label':i,'value':i} for i in file4['color'].unique()]
    
#make plot1
data1 = [go.Scatter(x=file4['color'],
                    y=file4['wheels'],
                    dy=1,
                    mode='markers',
                    marker={'size':12,
                            'color':'rgb(51,204,153)',
                            'line':{'width':2}})]
layout1 = go.Layout(title='Wheels & Colors Scatterplot',
                    xaxis={'title':'Color'},
                    yaxis={'title':'# of Wheels',
                           'nticks':3},
                    hovermode='closest')
fig1 = go.Figure(data1,layout1)


#make foot note
markdown_text = '''
This is Masco's Python Page
'''


#make file5 from several var
np.random.seed(10)          # for reproducible results
x1 = np.linspace(0.1,5,50)  # left half
x2 = np.linspace(5.1,10,50) # right half
y = np.random.randint(0,50,50) # 50 random points

df1 = pd.DataFrame({'x': x1, 'y': y})
df2 = pd.DataFrame({'x': x1, 'y': y})
df3 = pd.DataFrame({'x': x2, 'y': y})

file5 = pd.concat([df1,df2,df3])

#make plot2
data2 = [go.Scatter(x = file5['x'],
                    y = file5['y'],
                    mode = 'markers')]
layout2 = go.Layout(title = 'Random Scatterplot',
                    hovermode='closest')
fig2 = go.Figure(data2,layout2)


#make authorization
user =[['username','password'],['Masco','888']]





#delete unused var
del(i,j,k)
del(data1,layout1)
del(data2,layout2)
del(x1,x2,y,df1,df2,df3)











#--------------------Designing

app = dash.Dash()
server = app.server

#authentication for sign in page
auth = dash_auth.BasicAuth(app,user)





#function for load picture
def encode_image(image_file):
    encoded = base64.b64encode(open(image_file,'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())








app.layout = html.Div([ 
    
    
    
    
    

    #1.DCC - Input Text
    
    html.Div(html.Label('1. DCC - Input Text'),style={'font-weight':'bold',
                                                      'font-size':30,
                                                      'margin-bottom':'30px'}),
    
    
    
    html.Div(html.Label('Simple Input Text'),style={'font-weight':'bold',
                                                    'font-size':18,
                                                    'margin-bottom':'10px'}),
    
    html.Div(dcc.Input(id='input1',value='input your name here',type='text',
                       style={'margin-bottom':'10px'})),
    
    html.Div(id='output1',style={'margin-bottom':'30px',
                                 'border':'double',
                                 'width':'50%'}),
    
    
    
    html.Div(html.Label('Input Text with Button'),style={'font-weight':'bold',
                                                         'font-size':18,
                                                         'margin-bottom':'10px'}),
    html.Div(dcc.Input(id='input1B',value='',type='text',style={'margin-bottom':'10px',
                                                                'font-size':20})),
    html.Button(id='button1B',n_clicks=0,children='Submit',style={'font-size':20}),
    html.Div(id='output1B',style={'margin-bottom':'100px',
                                  'border':'double',
                                  'width':'50%'}),
    
    
    
    
    
    
    #2.DCC - Dropdown
    
    html.Div(html.Label('2. DCC - Dropdown'),style={'font-weight':'bold',
                                                    'font-size':30,
                                                    'margin-bottom':'30px'}),
    
    
    
    html.Div(html.Label('Simple Dropdown'),style={'font-weight':'bold',
                                                   'font-size':18,
                                                   'margin-bottom':'10px'}),
    
    html.Div(dcc.Dropdown(options=filter1,value=list_filter[-1]),
             style={'margin-bottom':'30px',
                    'width':'20%'}),
    
    

    html.Div(html.Label('One Dropdown with Plot'),style={'font-weight':'bold',
                                                         'font-size':18,
                                                         'margin-bottom':'10px'}),
    
    html.Div(dcc.Dropdown(id='input2B',options=filter2,value=list_filter2.min()),
             style={'margin-bottom':'10px',
                    'width':'10%'}),
    
    html.Div(dcc.Graph(id='output2B'),
             style={'margin-bottom':'30px'}),
    
    
    
    html.Div(html.Label('Two Dropdown with Plot'),style={'font-weight':'bold',
                                                         'font-size':18,
                                                         'margin-bottom':'10px'}),
    
    html.Div([html.Div(html.Label('X-Axis',style={'font-style':'italic'}),
                       style={'width':'30%',
                              'display':'inline-block'}),
              html.Div(html.Label('Y-Axis',style={'font-style':'italic'}),
                       style={'width':'30%',
                              'display':'inline-block'})]),
    
    html.Div([html.Div(dcc.Dropdown(id='input2C',options=filter3,value=list_filter3[0]),
                       style={'width':'30%',
                              'display':'inline-block'}),
              html.Div(dcc.Dropdown(id='input2Cb',options=filter3,value=list_filter3[1]),
                       style={'width':'30%',
                              'display':'inline-block'})]),
    
    html.Div(dcc.Graph(id='output2C'),
             style={'margin-bottom':'50px'}),
    
    
    
    
    
    
    #3.DCC - Radio Items
    
    html.Div(html.Label('3. DCC - Radio Items'),style={'font-weight':'bold',
                                                       'font-size':30,
                                                       'margin-bottom':'30px'}),
    
    
    
    html.Div(html.Label('Simple Radio Items'),style={'font-weight':'bold',
                                                     'font-size':18,
                                                     'margin-bottom':'10px'}),
    html.Div(dcc.RadioItems(options=filter1,value=list_filter[0]),
             style={'margin-bottom':'30px'}),
    
    
    
    html.Div(html.Label('2 Radio Items with Picture'),style={'font-weight':'bold',
                                                             'font-size':18,
                                                             'margin-bottom':'10px'}),
    html.Div([
        dcc.RadioItems(id='input3',options=filter4,value=list_filter4[0]),
        html.Div(id='output3'),
        html.Hr(),
        dcc.RadioItems(id='input3b',options=filter4b,value=list_filter4b[0]),
        html.Div(id='output3b'),
        html.Img(id='output3c',src='children',height=300),
        ],style={
            'fontFamily':'helvetica',
            'fontSize':18,
            'margin-bottom':'50px'
            }),
    
            
            

    
    
    #4.DCC - Slider
    
    html.Div(html.Label('4. DCC - Slider'),style={'font-weight':'bold',
                                                  'font-size':30,
                                                  'margin-bottom':'30px'}),
    
    
    
    html.Div(html.Label('Simple Slider'),style={'font-weight':'bold',
                                                'font-size':18,
                                                'margin-bottom':'10px'}),
    
    html.Div(dcc.Slider(min=-10,max=10,step=1,value=3,
                        marks={i: i for i in range(-10,10)}),
             style={'margin-bottom':'50px'}),
    


    

    
    
    
    
    
    #5.Interacting with Viz
    
    html.Div(html.Label('5. Interacting with Viz'),style={'font-weight':'bold',
                                                          'font-size':30,
                                                          'margin-bottom':'30px'}),
    
    
    
    html.Div(html.Label('Hover Over Data'),style={'font-weight':'bold',
                                                  'font-size':18,
                                                  'margin-bottom':'10px'}),
    
    html.Div([html.Div(dcc.Graph(id='input5',figure=fig1),
                       style={'width':'30%',
                              'display':'inline-block'}),
              html.Div([html.Img(id='output5', src='children', height=300)],
                       style={'paddingTop':35,
                              'display':'inline-block',
                              'margin-bottom':'20px'})]),
    
    
    
    html.Div(html.Label('Click Data'),style={'font-weight':'bold',
                                             'font-size':18,
                                             'margin-bottom':'10px'}),
    
    html.Div([html.Div(dcc.Graph(id='input5B',figure=fig1),
                       style={'width':'30%',
                              'display':'inline-block'}),
              html.Div([html.Img(id='output5B', src='children', height=300)],
                       style={'paddingTop':35,
                              'display':'inline-block',
                              'margin-bottom':'20px'})]),
    
    
    
    html.Div(html.Label('Selection Data'),style={'font-weight':'bold',
                                                  'font-size':18,
                                                  'margin-bottom':'10px'}),
    
    html.Div([html.Div([dcc.Graph(id='input5C',figure=fig2)],
                       style={'width':'30%',
                              'display':'inline-block'}),
              html.Div([html.H1(id='output5C',style={'paddingTop':25})],
                       style={'width':'30%',
                              'display':'inline-block',
                              'verticalAlign':'top',
                              'margin-bottom':'50px'})]),
    
    
    
    
    








    #6.Live Updating
    
    html.Div(html.Label('6. Live Updating'),style={'font-weight':'bold',
                                                   'font-size':30,
                                                   'margin-bottom':'30px'}),
    
    
    
    html.Div(html.Label('Simple Live Update'),style={'font-weight':'bold',
                                                     'font-size':18,
                                                     'margin-bottom':'10px'}),
    
    html.Div([html.Label(id='output6'),
              dcc.Interval(id='input6',interval=2000,n_intervals=0)],
             style={'margin-bottom':'100px',
                    'border-style':'dashed',
                    'width':'30%'}),





    
    
    html.Div([dcc.Markdown(markdown_text)],style={'font-style':'italic',
                                                  'text-align':'center'}),
    html.Div(html.Label('©2021'),style={'text-align':'center'}),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ])
            
            
    
            













#--------------------Executing

#1.DCC - Input Text

#1

@app.callback(Output(component_id='output1',component_property='children'),
              [Input(component_id='input1',component_property='value')])

def callback1(input_value):
    return "You entered: {}".format(input_value)



#1B

@app.callback(Output(component_id='output1B',component_property='children'),
              [Input(component_id='button1B',component_property='n_clicks')],
              [State(component_id='input1B',component_property='value')])
def callback1B(n_clicks,number):
    return 'You typed {}.. You clicked button {} times..'.format(number,n_clicks)















#2.DCC - Dropdown

#2B

@app.callback(Output(component_id='output2B',component_property='figure'),
               [Input(component_id='input2B',component_property='value')])

def callback2(selected_year):
    filtered_file2=file2[file2['year']==selected_year]
    
    data=[]
    for continent_name in filtered_file2['continent'].unique():
        file2_by_continent=filtered_file2[filtered_file2['continent']==continent_name]
        data.append(go.Scatter(
            x=file2_by_continent['gdpPercap'],
            y=file2_by_continent['lifeExp'],
            mode='markers',
            marker={'size':15},
            name=continent_name,
            opacity=0.7
            ))
    
    layout=go.Layout(title='Scatter Plot with Dropdown',
                     xaxis={'title':'GDP Per Cap','type':'log'},
                     yaxis={'title':'Life Expectancy'})

    return {'data':data,'layout':layout}
        


#2C

@app.callback(Output(component_id='output2C',component_property='figure'),
              [Input(component_id='input2C',component_property='value'),
               Input(component_id='input2Cb',component_property='value')])

def callback3(x_axis,y_axis):
    
    data=[go.Scatter(x=file3[x_axis],
                     y=file3[y_axis],
                     text=file3['name'],
                     mode='markers',
                     marker={'size':15,
                             'opacity':0.5,
                             'line':{'width':0.5,
                                     'color':'white'}})]
    
    layout=go.Layout(title='Scatter Plot with 2 Dropdowns',
                     xaxis={'title':x_axis},
                     yaxis={'title':y_axis},
                     hovermode='closest')
    
    return {'data':data,'layout':layout}


'''
    return {'data':[go.Scatter(x=x_axis,
                     y=y_axis,
                     name=file3['name'],
                     mode='markers',
                     marker={'size':15})],
            'layout':go.Layout(title='Scatter Plot with 2 Dropdowns',
                     xaxis={'title':x_axis},
                     yaxis={'title':y_axis})}
'''















#3.DCC - Radio Items

#3

@app.callback(Output(component_id='output3',component_property='children'),
              [Input(component_id='input3',component_property='value')])
def callback4(wheels_value):
    return "You chose: {}".format(wheels_value)

@app.callback(Output(component_id='output3b',component_property='children'),
              [Input(component_id='input3b',component_property='value')])
def callback4b(colors_value):
    return "You chose: {}".format(colors_value)

@app.callback(Output(component_id='output3c',component_property='src'),
              [Input(component_id='input3',component_property='value'),
               Input(component_id='input3b',component_property='value')])
def callback4c(wheel,color):
    path = 'Images/'
    return encode_image(
        path+file4[(file4['wheels']==wheel)&(file4['color']==color)]['image'].values[0]
        )













#5.Interacting with Viz

#5

@app.callback(
    Output('output5', 'src'),
    [Input('input5', 'hoverData')])
def callback5(hoverData):
    wheel=hoverData['points'][0]['y']
    color=hoverData['points'][0]['x']
    path = 'Images/'
    return encode_image(path+file4[(file4['wheels']==wheel) & \
    (file4['color']==color)]['image'].values[0])


#5B

@app.callback(
    Output('output5B', 'src'),
    [Input('input5B', 'clickData')])
def callback5B(clickData):
    wheel=clickData['points'][0]['y']
    color=clickData['points'][0]['x']
    path = 'Images/'
    return encode_image(path+file4[(file4['wheels']==wheel) & \
    (file4['color']==color)]['image'].values[0])


#5C

@app.callback(
    Output('output5C', 'children'),
    [Input('input5C', 'selectedData')])
def find_density(selectedData):
    pts = len(selectedData['points'])
    rng_or_lp = list(selectedData.keys())
    rng_or_lp.remove('points')
    max_x = max(selectedData[rng_or_lp[0]]['x'])
    min_x = min(selectedData[rng_or_lp[0]]['x'])
    max_y = max(selectedData[rng_or_lp[0]]['y'])
    min_y = min(selectedData[rng_or_lp[0]]['y'])
    area = (max_x-min_x)*(max_y-min_y)
    d = pts/area
    return 'Density = {:.2f}'.format(d)











#6.Live Updating

#6

@app.callback(Output('output6', 'children'),
              [Input('input6', 'n_intervals')])
def update_layout(n):
    return 'Crash free for {} refreshes'.format(n)






if __name__ == '__main__':
    app.run_server()