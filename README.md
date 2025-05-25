# Predicting University tuition throughout the past 7 years 🧑‍🎓

This project is a predictive model project that will be able to predict about how a student had payed or will pay, based on the year, their province, their level of study, their program and their nationality.

Data was taken from Statistics Canada

Canadian Undergards: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3710000301 

Canadian Grads: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3710000401

International undergrads: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3710022401

International grads: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3710022501

## Description of Final Project notebook 🚀
Fixing all null values and merging all 4 csvs into 1 dataframe

EDA and cleaning/dropping redundant columns

Analyzing Data of the year 2024/2025 with seaborn and matplotlib

Preprocessing: encoding and scaling

Data modeling:Linear Regression, ElasticNetCV, RandomforestRegressor and Classifier, Logistic Regression

New Data input

Saving model to then deploy on streamlit


## CSV files 📁

[Canadian Undergrads](c_undegrad.csv)

[Canadian grads](c_grad.csv)

[International Undergrads](i_undergrad.csv)

[International grads](i_grad.csv)

## streamlit py

[app.py](app.py)

[explore_page](explore_page.py)

[predict_page](predict_page.py)
