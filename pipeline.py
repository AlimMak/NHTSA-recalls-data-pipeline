import requests, csv

def extract_recalls(make, model, year):
    url = f"https://api.nhtsa.gov/recalls/recallsByVehicle?make={make}&model={model}&modelYear={year}"
    response = requests.get(url)

    if response.status_code == 200:
        RecallData = response.json()
        print(f"Success! Found {RecallData['Count']} Recalls")
        return RecallData
    else:
        print(f"Error: {response.status_code}")
        print(response.text)




#use RecallData('results')
def transform_recalls(results):
    dictList = []
    for recall in results:
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
# csv_path = "data/test.csv"
def load_to_csv(data, filename):
    with open(f"data/{filename}.csv", 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)













brand = "Honda"
carModel = "accord"
productionYear = "2020"
dataFile = "testData"
data = extract_recalls(brand, carModel, productionYear)
transformedData = transform_recalls(data['results'])
load_to_csv(transformedData, dataFile)