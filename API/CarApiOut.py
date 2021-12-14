import requests
import json


def checkModel(mark, usermodel):
    mark = mark.replace(" ", "")
    usermodel = usermodel.replace(" ", "")
    base_url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{}?format=json".format(mark.lower())
    response = requests.get(base_url)
    data_cars = response.text
    data = json.loads(data_cars)
    for model in data['Results']:
        model = model["Model_Name"].replace(" ", "")
        if model.lower() == usermodel.lower():
            return 1

