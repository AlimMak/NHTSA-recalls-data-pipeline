import requests
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

brand = "Honda"
carModel = "accord"
productionYear = "2020"

extract_recalls(brand, carModel, productionYear)