from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,json
import requests
import os

app = Flask(__name__)



@app.route('/',methods = ['POST', 'GET'])
def index():
   # email = request.form.get('email')
   print('Request for index page received')
   return render_template('index.html')






@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/',methods = ['POST', 'GET'])
def index():
   email = request.form.get('email')
   print('Request for index page received')
   return render_template('index.html', email = email)



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

@app.route('/Searchforuser', methods=['POST'])
def search():

        searchName = request.form.get('searchName')
        count = 1
        countfounded = 1
        founded = False

 
        listFordisplayName = []
        ListParsing = ["mail", "displayName", "userPrincipalName"]
        
        dicofDics = {}
        dicofounded = {}
        url = "https://prod-31.westeurope.logic.azure.com:443/workflows/0b121fa521f04f0aa6185a49dce36fa5/triggers/request/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Frequest%2Frun&sv=1.0&sig=TJ5tk6JKlHQL4rqpaohEWe_zs1MLyL-nlQX7kCLwdQY"

        payload={}
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload)
        jsonResponse = response.json()
        jsonResponse = jsonResponse["value"]


        for items in jsonResponse:
           currentElement =  []
           currentElement.append(items['mail'])
           currentElement.append(items['displayName'])
           currentElement.append(items['userPrincipalName'])
           dicofDics[count] = currentElement
           count = count +1
           listFordisplayName.append(currentElement)
       
           
     
        if(searchName == ''):
            return render_template('Searchforuser.html', dicofDics = dicofDics)
          
      
        for item in dicofDics:
            if(searchName in dicofDics[item][2] or searchName in dicofDics[item][1]):
                dicofounded[countfounded] = dicofDics[item]
                countfounded = countfounded + 1 
                founded = True

          
        if founded:
            dicofDics = dicofounded
            
            return render_template('Searchforuser.html', dicofDics = dicofDics)
        else:
       
            return "user not found"









@app.route('/admin', methods=['GET','POST'])
def admin():
   emailRequest = request.form.get('emailRequest')
   print(emailRequest)
   return render_template('admin.html',emailRequest = emailRequest)


@app.route('/table', methods=['GET'])
def table():
   print('Request for admin page received')
   return render_template('table.html')


@app.route('/login', methods=['GET'])
def login():
   return render_template('login.html')


   


if __name__ == '__main__':
   app.run()







