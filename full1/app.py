from joblib import load
from transformation import FeatureAdder

import pandas as pd
from flask import Flask, redirect, url_for, request
app = Flask(__name__)
  
#@app.route('/success/<name>')
#def success(name, churn):
#   return 'welcome %s %i' % name % churn
  

pipe = load('churn.joblib') 


def model_predict(d):
    x = pd.DataFrame([d.values()], columns=d.keys())
    return pipe.predict(x)

@app.route('/predict',methods = ['POST'])
def predict():
   if request.method == 'POST':
      user = request.form.to_dict()
      prediction = model_predict(user)
      return str(prediction) 
#   else:
#      user = request.args.get('nm')
#      return redirect(url_for('success',name = user))
  
if __name__ == '__main__':
   app.run(debug = True)