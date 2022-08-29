from flask import Flask, render_template, request, redirect,url_for, flash, jsonify, send_file
import pandas as pd
import os
app = Flask(__name__)

#setting path variable for current working directory
PATH = os.getcwd()

# reading the data in the csv file
FILE_NAME = 'data1.csv'
df = pd.read_csv(FILE_NAME)
colNames = df.columns.tolist()

#Homepage Route
@app.route('/')
def home():
    return render_template('display_data.html', tables=[df.to_html(classes=["table", "table-striped", "table-sm", "border"])], titles=[''])

#Add new page Route
@app.route('/addrecord', methods=['POST', 'GET'])
def addRecord():
    if request.method=="POST":
        data= request.form #retriveing data from form
        data= dict(data) 
        global df
        try:
            df = df.append(data, ignore_index=True)
            df.to_csv(FILE_NAME, index=False)
            flash('Record has been added!')
        except:
            flash('Something went wrong!')
        
    return render_template('add_data.html', colNames=colNames)

@app.route('/delete_record', methods=['POST', 'GET'])
def deleteRecord():
    if request.method=="POST":
        data= request.json
        del_row=(data[0]) #fetching idex of the row
        del_row= int(del_row)
        global df
        try:
            df= df.drop(del_row,axis=0)
            df.to_csv(FILE_NAME, index=False)
        except:
            print('Something went wrong!')

    return render_template('display_data.html')

@app.route('/download_file', methods=['GET'])
def download_file():
    return send_file(PATH+"/"+FILE_NAME, mimetype='text/csv')

if __name__ == '__main__':
    app.secret_key='wh_csv_app'
    app.run(debug=True)