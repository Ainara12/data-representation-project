
'''
DATA REPRESENTATION FINAL PROJECT
STUDENT NAME: Ainara Ruiz Castillo
STUDENT ID: G00387880




'''

from flask import Flask, jsonify, request, abort
from subscriberDAO import subscriberDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

#app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello, World!"

#curl "http://127.0.0.1:5000/subscribers"
@app.route('/subscribers')
def getAll():
    #print("in getall")
    results = subscriberDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/subscribers/2"
@app.route('/subscribers/<int:id>')
def findById(id):
    foundSub = subscriberDAO.findByID(id)

    return jsonify(foundSub)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Name\":\"Esther\",\"Paid\":300,\"Membership\":123}" http://127.0.0.1:5000/subscribers
@app.route('/subscribers', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    subscriber = {
        "id": request.json['id'],
        "Name": request.json['Name'],
        "Paid": request.json['Paid'],
    }
    values =(subscriber['id'],subscriber['Name'],subscriber['Paid'])
    newId = subscriberDAO.create(values)
    subscriber['id'] = newId
    return jsonify(subscriber)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Name\":\"Esther\",\"Paid\":300,\"Membership\":123}" http://127.0.0.1:5000/subscribers/345
@app.route('/subscribers', methods=['POST'])
@app.route('/subscribers/<int:id>', methods=['PUT'])
def update(id):
    foundSub = subscriberDAO.findByID(id)
    if not foundSub:
        abort(404)
       
    
    if not request.json:
        abort(400)
        

    reqJson = request.json
    if 'Paid' in reqJson and type(reqJson['Paid']) is not int:
        abort(400)

    if 'Title' in reqJson:
        foundSub['id'] = reqJson['id']
    if 'Name' in reqJson:
        foundSub['Name'] = reqJson['Name']
    values = (foundSub['id'],foundSub['Name'],foundSub['Paid'])
    subscriberDAO.update(values)
    return jsonify(foundSub)
        

    

@app.route('/subscribers/<int:id>' , methods=['DELETE'])
def delete(id):
    subscriberDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)
