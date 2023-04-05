from flask import request
from flask import Flask
import os
from app import app
from flask import Flask, render_template
# importing Flask and other modules
from flask import Flask, request, render_template
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('main.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   print("jai hind")
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)

# if __name__ == '__main__':
#    app.run(debug = True)