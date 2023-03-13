from datetime import datetime
import os
import requests
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,json

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

# @app.route('/Searchforuser', methods=['POST'])
# def search():

#         searchName = request.form.get('searchName')
#         count = 1
#         countfounded = 1
#         founded = False

 
#         listFordisplayName = []
#         ListParsing = ["mail", "displayName", "userPrincipalName"]
        
#         dicofDics = {}
#         dicofounded = {}
#         url = "https://prod-31.westeurope.logic.azure.com:443/workflows/0b121fa521f04f0aa6185a49dce36fa5/triggers/request/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Frequest%2Frun&sv=1.0&sig=TJ5tk6JKlHQL4rqpaohEWe_zs1MLyL-nlQX7kCLwdQY"

#         payload={}
#         headers = {}

#         response = requests.request("POST", url, headers=headers, data=payload)
#         jsonResponse = response.json()
#         jsonResponse = jsonResponse["value"]


#         for items in jsonResponse:
#            currentElement =  []
#            currentElement.append(items['mail'])
#            currentElement.append(items['displayName'])
#            currentElement.append(items['userPrincipalName'])
#            dicofDics[count] = currentElement
#            count = count +1
#            listFordisplayName.append(currentElement)
       
           
     
#         if(searchName == ''):
#             return render_template('Searchforuser.html', dicofDics = dicofDics)
          
      
#         for item in dicofDics:
#             if(searchName in dicofDics[item][2] or searchName in dicofDics[item][1]):
#                 dicofounded[countfounded] = dicofDics[item]
#                 countfounded = countfounded + 1 
#                 founded = True

          
#         if founded:
#             dicofDics = dicofounded
            
#             return render_template('Searchforuser.html', dicofDics = dicofDics)
#         else:
       
#             return "user not found"

if __name__ == '__main__':
   app.run()