import requests
import datetime
import json

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print('failed request', url)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    departements = ["62", "59", "80", "60", "02", "08", "51", "10", "52", "55", "54", "88", "57", "67", "68", "70"]
    # departements = ["55", "54", "88"]

    progress = 0
    for department in departements:
        with open(department + '.json', 'w') as jsonfile:
            communes = get_data(
                "https://geo.api.gouv.fr/departements/" + department + "/communes?geometry=contour&format=geojson&type=commune-actuelle")['features']

            for commune in communes:
                print('progress: ', progress / len(communes) * 100)
                sections = get_data("https://cadastre.data.gouv.fr/bundler/cadastre-etalab/communes/" + commune['properties']['code'] + "/geojson/sections")
                if(sections):
                    for sectie in sections['features']:
                        mutations = get_data("https://app.dvf.etalab.gouv.fr/api/mutations3/" + commune['properties']['code'] + "/" + sectie['id'][5:])
                        if(mutations):
                            for mutation in mutations['mutations']:
                                if mutation['type_local'] == 'Maison' and mutation['nature_mutation'] == "Vente" and datetime.datetime.strptime(mutation['date_mutation'], '%Y-%m-%d') > datetime.datetime.strptime('2020-01-01', '%Y-%m-%d'):
                                    json.dump(mutation, jsonfile)
                                    jsonfile.write('\n')
                    progress += 1