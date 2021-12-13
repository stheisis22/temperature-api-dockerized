from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/temps/api', methods=['GET', 'POST'])
def convert_temp():
    source = request.args.get('source')
    temp = float(request.args.get('temp'))
    to = request.args.get('to')
    res = 0    
    
    if source+to == 'cf':
        res = (temp * 1.8) + 32
        to = "Fahrenheit"

    elif source+to == 'ck':
        res = (temp + 273.15)
        to = "Kelvin"

    elif source+to == 'fc':
        res = (temp - 32)/1.8
        to = "Celsius"

    elif source+to == 'fk':
        res = ((temp - 32)/1.8) + 273.15
        to = "Kelvin"

    elif source+to == 'kc':
        res = (temp - 273.15)
        to = "Celsius"

    elif source+to == 'kf':
        res = ((temp - 273.15) * 1.8) + 32
        to = "Fahrenheit" 

    else: 
        res = "Magnitud no soportada, ingrese: celsius, fahrenheit o kelvin "

    return { to:res }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')