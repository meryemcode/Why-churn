from urllib import response
from flask import Flask , request , jsonify , make_response
import models.train_model as train
# import wget
# import os
# import shutil

app = Flask(__name__)


# @app.route('/categorization',methods = ['GET'])
# def get():
#     # posterId = request.args.get("posterId")
#     # poster_url = basePosterURL + posterId
#     # poster_filename = wget.download(poster_url, out=imgFolderCacheName)
#     # res = cnnCateg.evaluatePoster(model,poster_filename)
#     # response =  jsonify({
#     #       'status': 'ok',
#     #       'data': res
#     #     })
#     # response.headers.add('Access-Control-Allow-Origin', '*')
#     # response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
#     return response


@app.route('/')
def hello():
    # response =  jsonify({
          
    #     })
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return "Hello Atfal"



@app.route('/clusterise',methods = ['GET'])
def cluster():
    state = request.args.get("state")
    accLength = request.args.get("accLength")
    IntPlan = request.args.get("IntPlan")
    IntCharges = request.args.get("IntCharges")
    IntMins = request.args.get("IntMins")
    VMplan = request.args.get("VMplan")
    VMmessage = request.args.get("VMmessage")
    DayCallsMins = request.args.get("DayCallsMins")
    EveCallsMins = request.args.get("EveCallsMins")
    NightCallsMins = request.args.get("NightCallsMins")
    ServiceCalls = request.args.get("ServiceCalls")
    DayCharge = request.args.get("DayCharge")
    EveCharge = request.args.get("EveCharge")
    NightCharge = request.args.get("NightCharge")
    # response = jsonify(Tree)
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

if __name__ == "__main__":
    print("\nCluster Model Importation\n")    
    clusterModel = train.getModel()
    print("\nCluster Model Importation Done\n")    

    app.run( debug=True, port=4996)
