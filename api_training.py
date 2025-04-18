import requests

API_KEY = "2573|C5XQ7AOqy3dFPubkjfC30tLTAPOEmOQb77igS54R"

def get_country(country_name):
    URL = f"https://restfulcountries.com/api/v1/countries/{country_name}"

    req_headers = {
        "Accept":"application/json",
        "Authorization":f"Bearer {API_KEY}"
    }
    
    try:

        response = requests.get(url=URL, headers=req_headers)
        data = response.json()
        name = data["data"]["name"] #nigeria
        covid = data["data"]["covid19"]["total_case"] #67,557
        full_name = data["data"]["full_name"] # 1. Oficjalna nazwa kraju
        #president_name = data["data"]["current_president"]["name"] # 2. Imię i nazwisko prezydenta
        #president_picture = data["data"]["current_president"]["href"]["picture"] # 3. Zdjęcie prezydenta
        country_description = data["data"]["description"] # 4. Opis kraju
        flag_picture = data["data"]["href"]["flag"] # 5. Flaga kraju
        
        print(covid)
        
    except KeyError as er:
        print("Nie znaleziono klucza", er)
        print(er)
    except Exception as er:
        print("Wystapil blad", er)

country = input("Podaj nazwe kraju: ")
if len(country) > 1:
    get_country(country)
