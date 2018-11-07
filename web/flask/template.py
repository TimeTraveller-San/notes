from flask import Flask,jsonify,request,send_file
from flask_api import status
from flask_cors import CORS
import os
import requests
app = Flask(__name__)
CORS(app) #not adding this little shit causes CORS fuck ups. I will someday
            #read in depth about CORS ffs until then, fuck it, i am fine with
            #(kinda ashamed) of my ignorance


@app.route("/",methods=['GET'])
def index():
    id=request.args.get('id')
    #get args from the url like that^

# This is to recieve file
@app.route('/uploader', methods = ['POST'])
def upload_file():
    print("HERE!")
    if request.method == 'POST':
      f = request.files['file']
      print(type(f))
      print(f)
      # f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

if __name__ == '__main__':
    #remove debug=True before actual deployment smh
   app.run(debug = True)

