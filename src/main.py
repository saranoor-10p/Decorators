from functools import wraps
from flask import Flask
import time
app = Flask(__name__)
# Defining our custom decorator

def timer(function):
    @wraps(function)
    def wrapper():
        #return "<p>Wrapper running!</p>"
        start=time.time()
        res=function()
        end= time.time()
        print("time to execute is", end-start)
        return res
    return wrapper

# Using it to decorate a function
@app.route("/")
@timer
def hi_there(*args, **kwargs):
    return "Hi, there."

if __name__ == '__main__':
   app.run()