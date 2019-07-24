# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:55:02 2019

@author: xiang
"""

# in this file, we will use the flask to handle the POST requests that we will get from the request.py
# importing the mothods and libraries 
# numpy to create the array of requested data, 
# pickle to load our trained model to predit

from flask import Flask, request
from flask import render_template, redirect

# create the instance of the flask()and load the model into model. 
app = Flask(__name__)
@app.route("/")
def home():

   return render_template("index.html")

@app.route("/get_post_json", methods = ['GET', 'POST'])
def get_post():   
   if request.method == 'POST':

      #print(request.__dict__)  

      # A = request.form["inputValue1"]
      # print(A) 
      inputValue1 = request.form["inputValue1"]
      inputValue2 = request.form["inputValue2"]
      inputValue3 = request.form["inputValue3"]
      inputValue4 = request.form["inputValue4"]

      from pandas import DataFrame
      df = DataFrame({'poverty' : inputValue1, 'grade_level' : inputValue2, 
      'total_price_excluding_optional_support': inputValue3, 'total_price_including_optional_support' : inputValue4}, index = [0])   
      
      from sklearn.externals import joblib
      knn = joblib.load('static/knn.pk1')
      result = knn.predict(df)
      
      # if result == 1:
      #    return redirect('/positiveresults')
      # else:
      #    return redirect('/negativeresults')
   
      return str(result)
@app.route("/positiveresults")
def positiveresults():

     return render_template("positiveresults.html")


@app.route("/negativeresults")
def negativeresults ():

     return render_template("negativeresults.html")

@app.route("/team")
def team ():

     return render_template("team.html")


@app.route("/process")
def process ():

    return render_template("process.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    