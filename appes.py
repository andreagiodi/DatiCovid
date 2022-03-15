from flask import Flask, render_template, request
app = Flask(__name__)
import pandas as pd 


df = pd.read_csv("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea-dose-addizionale-booster.csv")


@app.route('/', methods=['GET'])
def index():
    reg = df['nome_area'].drop_duplicates().to_list()

    return render_template('index.html', reg=reg)


@app.route('/risp', methods=['GET'])
def risp():
    regione = request.args['vaccini']
    df3 = df[df['nome_area']== regione]
    
    return render_template('index1.html', tables=[df3.to_html()], titles=[''])




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)