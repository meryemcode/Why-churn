# Why Churn ?

## Project Name

Why Churn ? (Churn Prediction using Machine Learning)

## Objective

A general-purpose application for solving problems with machine learning applied to predicting customer churn

## Details about the data

It consists of 3333 entries and 21 columns. Independent informations about customers.

| Columns| Description |
|----------------|---------------|
| State| string. 2-letter code of the US state of customer residence  |
| Account Length |  numerical. Number of months the customer has been with the current telco provider    |
| Area Code  |   string="area_code_AAA" where AAA = 3 digit area code.   |
| Phone |      |
| Intl Plan   |  (yes/no). The customer has international plan.    |
| VMail Plan  |    (yes/no). The customer has voice mail plan.  |
| VMail Message  |   numerical. Number of voice-mail messages.   |
| Day Mins |    numerical. Total minutes of day calls.   |
| Day Calls|numerical. Total minutes of day calls.|
| Day Charge|numerical. Total charge of day calls.|
| Eve Mins|numerical. Total minutes of evening calls.|
| Eve Calls|numerical. Total number of evening calls.|
| Eve Charge|numerical. Total charge of evening calls.|
| Night Mins|numerical. Total minutes of night calls.|
| Night Calls|numerical. Total number of night calls.|
| Night Charge|numerical. Total charge of night calls.|
| Intl Mins|numerical. Total minutes of international calls.|
| Intl Calls|numerical. Total number of international calls.|
| Intl Charge|numerical. Total charge of international calls|
| CustServ Calls|numerical. Number of calls to customer service|
| Churn|(yes/no). Customer churn - target variable.|

## Results

## Contributors

## Credits

Orange Digital Center Rabat

## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


<a href = "https://github.com/Tanu-N-Prabhu/Python/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo = meryemcode/Why-churn"/>
</a>