import random
from fastapi import FastAPI
from api_handler import FastAPIHandler

app = FastAPI()
app.handler = FastAPIHandler()

@app.get('/')
def root_dir():
    return({'Hello': 'world'})

@app.post('/api/prediction')
def make_prediction(employer_id: int, item_features: dict):
    prediction = app.handler.predict(item_features)
    return ({
             'salary': prediction,
             'employee_id': employer_id
            })

'''
"work_year": 2024,
"experience_level": "SE",
"employment_type": "FT",
"job_title": "Data Scientist",
"employee_residence": "US",
"remote_ratio": 50,
"company_location": "US",
"company_size": "L"
'''