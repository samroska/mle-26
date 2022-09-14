
import pandas as pd
import joblib
import logging
from data.objects import DataObject

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
#TODO look at how 
model = joblib.load('./data/sementation.pkl')

def format_input(dataframe):

    dataframe['x12'] = dataframe['x12'].str.replace('$','')
    dataframe['x12'] = dataframe['x12'].str.replace(',','')
    dataframe['x12'] = dataframe['x12'].str.replace(')','')
    dataframe['x12'] = dataframe['x12'].str.replace('(','-')
    dataframe['x12'] = dataframe['x12'].astype(float)

    dataframe['x63'] = dataframe['x63'].str.replace('%','')
    dataframe['x63'] = dataframe['x63'].astype(float)

    return dataframe

def format_output(dataframe):
    dataframe.rename(columns={0:"phat"}, inplace=True)
    filtered_df = dataframe['business_result'] = dataframe[dataframe['phat'] > .758]
    return filtered_df

def get_prediction(input: DataObject):
    
    logging.info('Procession DataObject size:{}'.format(len(input.data)))

    dataframe = pd.DataFrame(input.data,index=[0])
    formatted_df = format_input(dataframe)
    #TODO theres something with statsmodels that I am missing. 
    predict = pd.DataFrame(model.predict(formatted_df))
    final = format_output(predict)
    return final