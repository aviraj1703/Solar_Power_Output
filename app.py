from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':

        solar_watts = float(request.form['watt'])
        hours = float(request.form['hour'])
        eff = float(request.form['efficiency'])
        daily_hr = float(solar_watts*hours*eff)
        total_unit = float(daily_hr/100000.0000)
        unit_saved = float(total_unit*3.5)

        return render_template('result.html',daily_unit = total_unit*30, money_saved=unit_saved*30)

if __name__ == '__main__':
    app.run(debug=True)