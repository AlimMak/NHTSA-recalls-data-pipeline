import requests, csv

def extract_recalls(data):

    RecallData = []
    for car in data:
        url = f"https://api.nhtsa.gov/recalls/recallsByVehicle?make={car['make']}&model={car['model']}&modelYear={car['year']}"
        response = requests.get(url)

        if response.status_code == 200:
            RecallData.append(response.json())
            currCar = response.json()
            print(f"Success! Found {currCar['Count']} Recalls")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    return RecallData



#use RecallData('results')
def transform_recalls(recallInfo):
    dictList = []
    for response in recallInfo:  # each API response
        for recall in response['results']:  # each recall inside that response
            simplified = {"campaign_number": recall["NHTSACampaignNumber"], 
                          "make": recall["Make"].title(),
                          "model": recall["Model"].title(),
                          "year": recall["ModelYear"],
                          "component": recall["Component"],
                          "summary": recall["Summary"] 
                          }
            dictList.append(simplified)
    return dictList



#usedictList here
fieldnames = ["campaign_number", "make", "model", "year", "component", "summary"]

def load_to_csv(data, filename):
    with open(f"data/{filename}.csv", 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)










brand = "Honda"
carModel = "Accord"
productionYear = "2020"
dataFile = "testData"

cars = [{"make": "Honda", "model": "Accord", "year": "2020"}, 
        {"make": "Ford","model": "F-150", "year": "2018"}, 
        {"make": "Ford", "model": "Mustang", "year": "2018"}]


data = extract_recalls(cars)
transformedData = transform_recalls(data)
load_to_csv(transformedData, dataFile)