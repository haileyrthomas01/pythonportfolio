import PySimpleGUI as sg
import mysql.connector
import pandas as pd
import os

# define the gui window
sg.theme('SandyBeach')
layout = [ 
    [sq.Text('Please enter SQL')],
    [sq.MultiLine(size = (50, 5), key = 'textbox')],
    [sq.Submit(), sg.Cancel()]
]

window = sg.Window('Report Generator', layout)
event, values = window.read()
query = values['textbox']

# sql connection/query
cnx = mysql.connector.connect(user = user1, password = password1,
                              host = host1, database = database1)

# create and open report
df = pd.read_sql(query, cnx)
df.to_excel('report.xlsx', index=False)
os.startfile('report.xlsx')