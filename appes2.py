from flask import Flask, render_template, request
app = Flask(__name__)
import pandas as pd 



df = pd.read_csv('squads_database.csv')
df1 = []

@app.route('/', methods=['GET'])
def index():
    

    return render_template('indexs.html')

@app.route('/risp', methods=['GET'])
def risp():
    nome = request.args['sqname']
    date = request.args['sqdate']
    city = request.args['sqcity']
    d = {'nome_squadra': [nome], 'data_fondazione': [date], 'città': [city]}
    df = pd.DataFrame(data=d, index=[1])
    print(df)
    df.to_csv('squads_database.csv')

    return render_template('indexs1.html')


@app.route('/risp1', methods=['GET'])
def risp1():
    nome = request.args['sqname']
    date = request.args['sqdate']
    city = request.args['sqcity']
    for i in df:
        df[df['nome_squadra'].str.contains(nome)]
        #da completare


    return render_template('indexs1.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)