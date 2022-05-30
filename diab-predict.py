#!/usr/bin/env python
# coding: utf-8


endpoint = 'http://8af37ccc-d552-4236-bfcf-e99521622cff.centralindia.azurecontainer.io/score' 
key = 'lwECsgZfE5axaektCfVVyyiPnExb2aMv'

import urllib.request
import json
import os

data = {
    "Inputs": {
        "WebServiceInput0":
        [
            {
                    'Pregnancies': 4,
                    'Glucose': 158,
                    'BloodPressure': 140,
                    'SkinThickness': 37,
                    'Insulin': 135,
                    'BMI': 24.7,
                    'DiabetesPedigreeFunction': 0.72,
                    'Age': 48
            },
        ],
    },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ key)}

req = urllib.request.Request(endpoint, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    json_result = json.loads(result)
    output = json_result["Results"]["WebServiceOutput0"][0]
    predicted_answer = output["Scored Labels"]
    if(predicted_answer >= 0.5):
        print('Prediction: YES, This patient is likely to have diabetes')
    else:
        print('Prediction: NO, This patient is likely not to have diabetes')
    print('Probability of having Diabetes: ',predicted_answer)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))