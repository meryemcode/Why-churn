import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.cluster import KMeans


class CallsTransformer(BaseEstimator,TransformerMixin):
    def __init__(self):
        pass

    def transform(self, dataframe, **transform_params):
        (dataframe['Day Calls'] == dataframe['Eve Calls'] + dataframe['Night Calls']).astype(int).mean()
        dataframe['Total Calls'] = dataframe['Day Calls'] + dataframe['Eve Calls'] + dataframe['Night Calls']
        dataframe['percent_day_calls'] = dataframe['Day Calls'] / dataframe['Total Calls']
        dataframe['percent_eve_calls'] = dataframe['Eve Calls'] / dataframe['Total Calls']
        dataframe['calls_nb'] = dataframe['Total Calls'] / dataframe['Account Length']
        dataframe['service_calls_nb'] = dataframe['CustServ Calls'] / dataframe['calls_nb']
        dataframe['log_calls_nb'] = np.log(1 + dataframe['calls_nb'])
        dataframe.loc[dataframe['log_calls_nb'] >= 1.959200, 'freq_calls'] = 'high_calls'
        dataframe.loc[dataframe['log_calls_nb'] < 1.959200, 'freq_calls'] = 'med_calls'
        dataframe.loc[dataframe['log_calls_nb'] < 1.383042, 'freq_calls'] = 'low_calls'
        dataframe.groupby('freq_calls').agg({'log_calls_nb' : ['min', 'median', 'max']})

        dataframe['total_calls'] = dataframe['Day Calls']+dataframe['Eve Calls']+dataframe['Night Calls']+dataframe['Intl Calls']
        return dataframe

    def fit(self, X, y=None, **fit_params):
        return self
        
class ChargeTransformer(BaseEstimator,TransformerMixin):
    def __init__(self):
        pass

    def transform(self, dataframe, **transform_params):

        dataframe['total_charge'] = dataframe['Day Charge']+dataframe['Eve Charge']+dataframe['Night Charge']+dataframe['Intl Charge']
        dataframe['both_plans'] = dataframe['Int\'l Plan'] + '_' + dataframe['VMail Plan']
        dataframe['charge_per_month'] = dataframe['total_charge'] / dataframe['Account Length']
        dataframe['log_charger_per_month'] = np.log(1 + dataframe['charge_per_month'])

        return dataframe

    def fit(self, X, y=None, **fit_params):
        return self

class MinsTransformer(BaseEstimator,TransformerMixin):
    def __init__(self):
        pass

    def transform(self, dataframe, **transform_params):
        dataframe['total_mins'] = dataframe['Day Mins']+dataframe['Eve Mins']+dataframe['Night Mins']+dataframe['Intl Mins']
        dataframe['mins_per_call'] = dataframe['total_mins'] / dataframe['total_calls']
        dataframe.loc[dataframe['mins_per_call'] >= 2.195963, 'freq_min_per_call'] = 'super_high_calls'
        dataframe.loc[dataframe['mins_per_call'] < 2.195963, 'freq_min_per_call'] = 'high_calls'
        dataframe.loc[dataframe['mins_per_call'] < 1.939936, 'freq_min_per_call'] = 'med_calls'
        dataframe.loc[dataframe['mins_per_call'] < 1.705187, 'freq_min_per_call'] = 'low_calls'
        predictors = ['Account Length', 'Int\'l Plan', 'VMail Plan', 'VMail Message', 'percent_day_calls', 
                'percent_eve_calls', 'service_calls_nb', 'both_plans', 'log_charger_per_month',
                'mins_per_call', 'log_calls_nb', 'freq_calls', 'freq_min_per_call']
        return pd.get_dummies(dataframe[predictors])

    def fit(self, X, y=None, **fit_params):
        return self


class ChurnEs(BaseEstimator,TransformerMixin):
    def __init__(self,finalDf , clusters = 10):
        self.clusters = clusters
        self.finalDf = finalDf

    def fit(self, dataframe, y=None, **fit_params):
        self.dataframe=dataframe
        self.model = KMeans(n_clusters = self.clusters)
        self.model.fit(self.dataframe)
        return self

    def transform(self, dataframe, **transform_params):
        self.dataframe=dataframe
        data_= self.finalDf
        data_['cluster'] = self.model.predict(dataframe)
        return data_