from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,json
import requests
import os

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/runworkflow', methods=['POST'])
def hello():



   name = request.form.get('name')
   time = request.form.get('time')
   selectedElement = request.form.get('selectedElement')
   url = "https://prod-208.westeurope.logic.azure.com:443/workflows/9cb9b9b69dad46f692b7804c3d546bc1/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=jGeQ-GVf2nZ2p99KNJpGmVt-61T3IzimUduOdEizTCM"

   payload = json.dumps({
   "name": name,
   "time": time,
   "selectedElement": selectedElement
   })
   headers = {
   'Content-Type': 'application/json'
   }

   response = requests.request("POST", url, headers=headers, data=payload)

   print(response.text)




   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('runworkflow.html', name = name, time = time,selectedElement=selectedElement)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


@app.route('/admin', methods=['GET'])
def admin():
   print('Request for admin page received')
   return render_template('admin.html')

if __name__ == '__main__':
   app.run()







