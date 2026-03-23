from flask import Flask 
from flask import render_template as ren_templ # with as we can reduce 

app = Flask (__name__)

#functions for navigating through site pages    
@app.route ('/') #in (/name of site page) 
def home():
    return ren_templ('index.html') # here in () we indicate the path to the file of the desired page {with }
