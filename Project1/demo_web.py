from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
import os
import sys
import smog_index
import flesch
import gunning
import dale_chall
from textstat.textstat import textstat

def Ans (a, s) :
    if a == 1:
        return flesch.flesch_reading_ease(s)
    elif a == 2:
        return smog_index.smog_index(s)
    elif a == 3:
        return gunning.gunning_fog(s)
    elif a == 4 :
        return dale_chall.dale_chall_readability_score(s) 

UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)
UPLOAD_FOLDER = ''
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/display', methods = ['POST'])
def File():
    file = request.files['fil']
    a = request.form['chooseindex']
    filename = secure_filename(file.filename)
    filepath = os.path.dirname(os.path.realpath(__file__))+"\\"+filename
    InputFile = open(filepath, encoding="utf-8")
    val = Ans(int(a), InputFile.read())
    return str(val)

if __name__ == '__main__':
    app.run(debug=True)