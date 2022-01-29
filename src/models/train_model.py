import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
import pickle
import os
from datetime import date
from utils.transformers import CallsTransformer,ChargeTransformer,MinsTransformer,ChurnEs

df = pd.read_csv('https://raw.githubusercontent.com/donnemartin/data-science-ipython-notebooks/master/data/churn.csv')
FilePath = 'models/'
Filename = 'churn.data'

final_pipeline = Pipeline(steps=[
                                ('calls transformer',CallsTransformer()),
                                ('charge transformer',ChargeTransformer()),
                                ('Mins transformer',MinsTransformer()),
                                ('minMax',MinMaxScaler()),
                                ('pca',PCA(n_components=7)),
                                ('KMeans cluster',ChurnEs(df,3)),
                        ], memory='ClusterCash')






def getModel():
    if ( not os.path.exists(FilePath + Filename)) :
        model = final_pipeline.fit(df)
        SerializedDataModelFile = open(FilePath + Filename,"wb")
        dictInfoData ={
                        'projectName':'Churn',
                        'author':'Hamza CHAFKAN',
                        'date':date.today(),
                        'version':'1.0.0',
                        'model':model,
                        'Session_info':{
                            'OS':{
                                'core': os.name
                            }
                        }
        }

        beautyPrint(dictInfoData)
        pickle.dump(dictInfoData,SerializedDataModelFile)
        SerializedDataModelFile.close()
        return model
    else :
        SerializedDataModelFile = open(FilePath + Filename, 'rb')
        Serdata = pickle.load(SerializedDataModelFile)
        SerializedDataModelFile.close()
        beautyPrint(Serdata)
        return Serdata['model']

def beautyPrint(Dict):
    for key, value in Dict.items():
        if key != 'model': 
            print(key, ' : ', value)



# model.score(X_test,Y_test)


# resCluster = model.fit_transform(df)
# resCluster.head(n=3)