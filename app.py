from flask import Flask, render_template, request, redirect
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.io import push_notebook, show, output_notebook
from bokeh.layouts import row
from bokeh.plotting import figure
from bokeh.charts import TimeSeries, show, output_file, Line
from bokeh.embed import components 

app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
  return redirect('/index_lulu')

@app.route('/index_lulu',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('userinfo_lulu.html')
    else:
        #app.vars['name'] = request.form['name_lulu']
        
        #api_url = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?date.gte=20150101&date.lt=20160101&ticker=%s&api_key=2XQ6zJNRhsnW213SikQe' % app.vars['name']
        #print api_url
        #r = requests.get(api_url)

        #raw_data = r.json()
        #a = raw_data['datatable']['data']
        #b = raw_data['datatable']['columns']
        #df = pd.DataFrame(a,columns = [b[0]['name'],b[1]['name'],b[2]['name'],b[3]['name'],b[4]['name'],b[5]['name'],b[6]['name'],b[7]['name'],b[8]['name'],b[9]['name'],b[10]['name'],b[11]['name'],b[12]['name'],b[13]['name'],])
        #time = pd.DataFrame(df,columns=[b[2]['name'], b[1]['name'], b[3]['name']])
        
        
        #data = dict(
            #AAPL=df['close'],
            #Date=df['date'],
            #MSFT=df['high'],
            #IBM=df['open'],
        #)
        #tsline = TimeSeries(data,
            #x='Date', y=['IBM', 'MSFT', 'AAPL'],
            #color=['IBM', 'MSFT', 'AAPL'], dash=['IBM', 'MSFT', 'AAPL'],
            #title="Timeseries", ylabel='Stock Prices', legend=True)
        
        #output_file("templates/lines.html", title="line plot example")

        #return redirect('/lines')

    
@app.route('/next_lulu',methods=['POST'])
def next_lulu():
    return redirect('/layout_lulu')

@app.route('/lines',methods=['GET','POST'])
def plot():
    return render_template('lines.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0')
