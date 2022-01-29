from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin
class FeatureAdder(BaseEstimator, TransformerMixin):
  def __init__(self):
    pass
  def fit(self, X, y=None):
    return self
  def transform(self, X, y= None):
    X['Total Calls'] = X['Day Calls'] + X['Eve Calls'] + X['Night Calls']
    X['percent_day_calls'] = X['Day Calls'] / X['Total Calls']
    X['percent_eve_calls'] = X['Eve Calls'] / X['Total Calls']
    for param in ['Day', 'Eve', 'Night', 'Intl']:
      X[param+ '_unit_cost'] = X[param+ ' Charge'] / X[param+ ' Mins']
    X['total_charge'] = X['Day Charge']+X['Eve Charge']+X['Night Charge']+X['Intl Charge']
    X['calls_nb'] = X['Total Calls'] / X['Account Length']
    X['service_calls_nb'] = X['CustServ Calls'] / X['calls_nb']
    X['both_plans'] = X['Intl Plan'] + '_' + X['VMail Plan']
    X['charge_per_month'] = X['total_charge'] / X['Account Length']
    X['log_charger_per_month'] = np.log(1 + X['charge_per_month'])
    X['total_calls'] = X['Day Calls']+X['Eve Calls']+X['Night Calls']+X['Intl Calls']
    X['total_mins'] = X['Day Mins']+X['Eve Mins']+X['Night Mins']+X['Intl Mins']
    X['mins_per_call'] = X['total_mins'] / X['total_calls']
    X['log_calls_nb'] = np.log(1 + X['calls_nb'])
    X.loc[X['log_calls_nb'] >= 1.959200, 'freq_calls'] = 'high_calls'
    X.loc[X['log_calls_nb'] < 1.959200, 'freq_calls'] = 'med_calls'
    X.loc[X['log_calls_nb'] < 1.383042, 'freq_calls'] = 'low_calls'
    X.loc[X['mins_per_call'] >= 2.195963, 'freq_min_per_call'] = 'super_high_calls'
    X.loc[X['mins_per_call'] < 2.195963, 'freq_min_per_call'] = 'high_calls'
    X.loc[X['mins_per_call'] < 1.939936, 'freq_min_per_call'] = 'med_calls'
    X.loc[X['mins_per_call'] < 1.705187, 'freq_min_per_call'] = 'low_calls'
    X['minmax_Account Length'] = (X['Account Length'] - X['Account Length'].min())/ (X['Account Length'].max() - X['Account Length'].min())
    predictors = ['Account Length', 'Intl Plan', 'VMail Plan', 'VMail Message', 'percent_day_calls', 
              'percent_eve_calls', 'service_calls_nb', 'both_plans', 'log_charger_per_month',
              'mins_per_call', 'log_calls_nb', 'freq_calls', 'freq_min_per_call']
    final = pd.get_dummies(X[predictors])
    return final