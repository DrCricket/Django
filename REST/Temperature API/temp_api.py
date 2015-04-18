import sqlite3
import csv
from flask import Flask, jsonify, abort

data = []


def create_data():
    f = open("Mean_Temperatures_India1901-2012.csv",'rU')

    reader  = csv.reader(f,delimiter=',')
    raw_data = []
    n = -1
    
    for i in reader:
        raw_data.append(i)
        n = n+1

    label = raw_data[0] ## Keys - Year, Annual, Jan-Mar, Apr-Jun, Jul-Sept, Oct-Dec
    raw_data.pop(0)
    
    for i in raw_data:
        data.append({
            label[0].lower():int(i[0]),
            label[1].lower():float(i[1]),
            label[2].lower():float(i[2]),
            label[3].lower():float(i[3]),
            label[4].lower():float(i[4]),
            label[5].lower():float(i[5])
         })
    f.close()



app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'temp':data})

@app.route('/temperature/api/v1.0/<int:year>', methods=['GET'])
def get_by_year(year):

    if isinstance(year,int) == False:
        abort(400)
    
    result = [d for d in data if d['year'] == year]
    
    if len(result) == 0:
        abort(404)
    return jsonify({'temp':result})


@app.route('/temperature/api/v1.0/<int:year>/<string:period>')
def get_year_specific(year,period):
    if isinstance(year,int) == False:
        abort(400)
    
    result = [d for d in data if d['year'] == year]
    result_final = result[0]

    if len(result) == 0:
        abort(404)
    
    if period.lower() == 'jan-feb':
        result_final = result[0]['jan-feb']
    elif period.lower() == 'mar-may':
        result_final = result[0]['mar-may']
    elif period.lower() == 'jun-sep':
        result_final = result[0]['jun-sep']
    elif period.lower() == 'oct-dec':
        result_final = result[0]['oct-dec']
    elif period.lower() == 'annual':
        result_final = result[0]['annual']
    else:
        abort(400)
    result = [{period:result_final}]
    return jsonify({'temp':result})        
        
    

if __name__ == "__main__":
    create_data()
    app.run()

    
    





