import requests
from competitor import Competitor

def get_data(url: str) -> dict:
    '''
    Gets the data from the url and returns the data as a dictionary
    '''
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching data:", str(e))
        data = {}
        return data

def get_live_race(data: dict) -> int:
    '''
    Finds the currenct live race number
    returns:
    race number: int - first is 1
    flight number: int - first is 0
    race number in flight: int - first is 0
    '''
    for flightno, flight in enumerate(data['trackedRacesInfo']):
        for raceno, race in enumerate(flight['fleets']):
            if race['trackedRace']['live']:
                return (flightno+1) * (raceno+1), flightno, raceno

    print("No live races")
    return None    

if __name__ == '__main__':
    url = 'https://danishleague2024.sapsailing.com/sailingserver/api/v2/leaderboards/Danish Sailing League 2024 2. div - Aarhus'
    data = get_data(url)

    live_race, live_flight, live_flight_race = get_live_race(data)
    print(live_race, live_flight, live_flight_race)