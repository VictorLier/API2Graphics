import requests
import time

class Data:
    def __init__(self, url: str) -> None:
        '''
        Initializes the data object
        url: str -> the url of the data
        '''
        self.url = url
        self.data = self.get_data()
        self.live_race = None

    def get_data(self) -> dict:
        '''
        Gets the data from the url and returns the data as a dictionary
        '''
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print("Error occurred while fetching data:", str(e))
            data = {}
            return data

    def get_live_race(self) -> None:
        '''
        Finds the currenct live race number:
        self.live_race: int - first is 1
        self.live_flight: int - first is 0
        self.live_flight_race in flight: int - first is 0
        '''
        for flightno, flight in enumerate(self.data['trackedRacesInfo']):
            for raceno, race in enumerate(flight['fleets']):
                if race['trackedRace']['live']:
                    self.live_race = flightno * 3 + (raceno+1)
                    self.live_flight = flightno
                    self.live_flight_race = raceno

        if self.live_race == None:
            print("No live race is found")

    def get_next_starttime(self) -> int:
        '''
        Returns the time to start of the next race
        '''
        for flightno, flight in reversed(list(enumerate(self.data['trackedRacesInfo']))):
            for raceno, race in reversed(list(enumerate(flight['fleets']))):
                if not race['trackedRace']['startTimeMillis']==None:
                    self.start_time=race['trackedRace']['startTimeMillis']
                    break
            else:
                continue
            break

    def get_time_to_start(self) -> int:
        '''
        Returns the time to start of the next race
        '''
        current_time = int(time.time()*1000)
        self.time_to_start = (self.start_time - current_time) / 1000
    

# If no race is live. Abandoned/postponed


if __name__ == '__main__':
    data = Data('https://danishleague2024.sapsailing.com/sailingserver/api/v2/leaderboards/Danish Sailing League 2024 1. div - Aarhus')

    data.get_live_race()
    print(data.live_race)
    data.get_next_starttime()
    data.get_time_to_start()
    print(data.time_to_start)