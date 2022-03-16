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
    df.to_csv('squads_database.csv')

    return render_template('indexs1.html')


@app.route('/risp2', methods=['GET'])
def risp2():
    nome = request.args['sqname']
    date = request.args['sqdate']
    city = request.args['sqcity']
    df = pd.read_csv('squads_database.csv')
    if nome == '':
        if date == '':
          
          df1 = df[df['città'].str.contains(city)]
        else:
            df1 = df[df['data_fondazione'].str.contains(date)]
    if nome != '':
        df1 = df[df['nome_squadra'].str.contains(nome)]
    print(df1)

    return render_template('indexs2.html')



@app.route('/risp1', methods=['GET'])
def risp1():
    nome = request.args['sqname']
    date = request.args['sqdate']
    city = request.args['sqcity']
    df = pd.read_csv('squads_database.csv')
    if nome == '':
        if date == '':
          
          df1 = df[df['città'].str.contains(city)]
        else:
            df1 = df[df['data_fondazione'].str.contains(date)]
    if nome != '':
        df1 = df[df['nome_squadra'].str.contains(nome)]
    print(df1)


    return render_template('indexs1.html', tables=[df1.to_html()], titles=[''])





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)