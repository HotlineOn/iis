import random
from fastapi import FastAPI
from api_handler import FastAPIHandler
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram, Gauge, Counter, Summary


app = FastAPI()
app.handler = FastAPIHandler()

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

prediction_metric = Histogram(
    'prediction_metric_histogram',
    'histogram of predicted salaries',
    buckets=(100000, 1000000, 3000000, 5000000, 15000000, 50000000, 100000000)
)

@app.get('/')
def root_dir():
    return({'Hello': 'world'})

@app.post('/api/prediction')
def make_prediction(employee_id: int, item_features: dict):
    prediction = app.handler.predict(item_features)
    return ({
             'salary': prediction,
             'employee_id': employee_id
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