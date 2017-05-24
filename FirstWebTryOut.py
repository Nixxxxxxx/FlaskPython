'''
Created on May 18, 2017

@author: zero
'''

from flask import Flask

app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run()