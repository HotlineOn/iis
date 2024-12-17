import requests
import time
import random

for i in range(50):
    params = {'employee_id': i}
    data = {
        "work_year": 2024,
        "experience_level": "SE",
        "employment_type": "FT",
        "job_title": "Data Scientist",
        "employee_residence": "US",
        "remote_ratio": 50,
        "company_location": "US",
        "company_size": "L"
    }
    response = requests.post('http://salary-predict:8000/api/prediction', params=params, json=data)
    time.sleep(random.randint(1,5))
    print(response.json())