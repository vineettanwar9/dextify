from flask import Flask, render_template, request
from distutils.log import debug
from fileinput import filename
import os
import cv2
from json import load



app = Flask(__name__)   


@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/process', methods=['POST', 'GET'])
def process():
    if request.method == 'POST':
        f = request.files['file']
        f.save('page.jpg')
        img = cv2.imread('page.jpg')
        cv2.imwrite("static/image/page.jpg", img)
        os.system('python checkout.py')
        os.system('python tester.py')
        file = open('items.txt','r')
        ans = file.read()
        file.close()

    return render_template("result.html", ans=ans)

if __name__=='__main__':
   app.run(debug = True)
