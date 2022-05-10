from covid import Covid
import COVID19Py
import requests
import json

covid = Covid()

case_id = input("შეიყვანეთ ქვეყნის ID: ")
italy_cases_id = covid.get_status_by_country_id(case_id) # ეძებს კოვიდ სტატისტიკა ქვეყნის ID_ით
country_name = input("შეიყვანეთ ქვეყნა: ")
italy_cases_name = covid.get_status_by_country_name(country_name)  # ეძებს კოვიდ სტატისტიკა ქვეყნის დასახელებით
print(json.dumps(covid.get_total_confirmed_cases(), indent=4))  # მიიღებ მხოლოდ კოვიდის დადასტურებულ შემთხვევებს
print(json.dumps(covid.get_total_deaths(), indent=4))  # მიიღებ კოვიდით გარდაცვილი ადამიანების რაოდენობას
print(json.dumps(covid.get_data(), indent=4))  # მიიღებ ინფორმაციას ყველა ქვეყანაზე
print(json.dumps(italy_cases_name, indent=4))


# მეორე API რადგან პირველს არ ქონდა HTTPS
countryName = input('შეიყვანეთ ქვეყნის დასახელება: ')
url = f'https://coronavirus-tracker-api.herokuapp.com/v2/locations?source=jhu&country={countryName}&timelines=false'
r = requests.get(url)
d_resp = json.loads(r.text)
print(d_resp)
print(json.dumps(d_resp, indent=4))
