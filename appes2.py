from flask import Flask, render_template, request
app = Flask(__name__)
import pandas as pd 



df = pd.read_csv('squads_database.csv')

@app.route('/', methods=['GET'])
def index():
    

    return render_template('indexs.html')

@app.route('/risp', methods=['GET'])
def risp():
    nome = request.args['sqname']
    date = request.args['sqdate']
    city = request.args['sqcity']
    

    return render_template('indexs1.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)