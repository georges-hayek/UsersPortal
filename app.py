from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,json
import requests
import os
import webbrowser


app = Flask(__name__)



@app.route('/',methods = ['POST', 'GET'])
def re():
   # email = request.form.get('email')
   print('Request for index page received')
   return render_template('admin.html')



@app.route("/logout")
def logout():
   return redirect("https://portal.azure.com/")




@app.route('/',methods = ['POST', 'GET'])
def index():
   email = request.form.get('email')
   print('Request for index page received')
   return render_template('index.html', email = email)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'cropped-fav-32x32.png')

@app.route('/runworkflow', methods=['POST'])
def hello():
   



   name = request.form.get('name')
   time = request.form.get('time')
   selectedElement = request.form.get('selectedElement')

   url = "https://prod-116.westeurope.logic.azure.com:443/workflows/b5ec6624f9134978ac2a6674f7250589/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=It5HnPQGqTARWURkkRlJGQGwCOy98VxeUYcShEXXc9k"

   payload = json.dumps({
   "name": name,
   "time": time,
   "selectedElement": selectedElement,
 
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



@app.route('/runworkflowuser', methods=['POST'])
def hellouser():



   name = request.form.get('name')
   time = request.form.get('time')
   selectedElement = request.form.get('selectedElement')
   reason = request.form.get('reason')
   url = "https://prod-116.westeurope.logic.azure.com:443/workflows/b5ec6624f9134978ac2a6674f7250589/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=It5HnPQGqTARWURkkRlJGQGwCOy98VxeUYcShEXXc9k"

   payload = json.dumps({
   "name": name,
   "time": time,
   "selectedElement": selectedElement,
   "reason": reason
   })
   headers = {
   'Content-Type': 'application/json'
   }

   response = requests.request("POST", url, headers=headers, data=payload)

   print(response.text)




   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('runworkflowuser.html', name = name, time = time,selectedElement=selectedElement)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))





@app.route('/admin', methods=['GET','POST'])
def admin():
   emailRequest = request.form.get('emailRequest')
   print(emailRequest)
   return render_template('admin.html',emailRequest = emailRequest)



@app.route('/users', methods=['GET','POST'])
def usersss():

   return render_template('users.html')

@app.route('/table', methods=['GET'])
def table():
   print('Request for admin page received')
   return render_template('table.html')


@app.route('/login', methods=['GET'])
def login():
   return render_template('login.html')


@app.route('/TrackUsers', methods=['GET'])
def TrackUsers():
   url = "https://prod-138.westeurope.logic.azure.com:443/workflows/64cd242a3de74203b257a4ba5d25cb10/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=SY27BzE8Rnrpu0Fc1iKdskfBB3VzO3DkUrpHVrbQ3JY"

   payload = {}
   headers = {}

   response = requests.request("POST", url, headers=headers, data=payload)
   print( response.json())
   response = response.json()
 



   return render_template('trackUser.html', response = response)   


if __name__ == '__main__':
   app.run()







