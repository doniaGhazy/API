import numpy as np
import requests
import json


# Load data
X_test= #getting the result.

# Serialize the data into json and send the request to the model
payload = {'data': json.dumps(X_test.tolist())}
y_predict = requests.post('http://127.0.0.1:5000/predict', data=payload).json()


writeFile =open('result.json', 'w')
    writeFile.write(y_predict)
    writeFile.close()
