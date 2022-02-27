# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
from subprocess import Popen
  
# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/')
def home():  
        data = "API to download P.P. Prabodh Swamiji Live Pooja"
        return data;
  
# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/download/<url>', methods = ['GET'])
def disp(url):
    if("www" in url or "youtube" in url):
        return "only include youtube VIDEO_ID, don't include complete url, https://www.youtube.com/watch?v=VIDEO_ID"
    p = Popen(['python3', 'livestream_saver.py', 'download', '-q', '360', 'https://www.youtube.com/watch?v='+url]) 
    return "Download triggered, DO NOT HIT THIS ENDPOINT AGAIN!"
  
  
# driver function
if __name__ == '__main__':
    app.run(debug = True)