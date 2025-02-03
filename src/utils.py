#all common things are done here 

import os
import sys
import numpy as np
import pandas as pd
import dill

from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X_train,y_train,X_test,y_test,models,params):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]

            para = params[list(models.keys())[i]]

            grid = GridSearchCV(model,para,cv=3,n_jobs=-1)

            #fit the model
            grid.fit(X_train,y_train)
            print(model)

            model.set_params(**grid.best_params_)
            model.fit(X_train,y_train) 

            #predict both train and test 
            y_pred_train = model.predict(X_train)
            y_pred_test = model.predict(X_test)

            #check performace metrix 
            train_model_score = r2_score(y_train,y_pred_train)
            test_model_score = r2_score(y_test,y_pred_test)

            report[list(models.keys())[i]] = test_model_score
        
        return report
    
    except Exception as e:
        raise CustomException(e,sys)
    

def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)
