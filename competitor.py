class Competitor:
    def __init__(self, name: str, id: str, race: list, boat: list) -> None:
        '''
        Initializes the competitor object
        name: str -> the name of the competitor
        id: str -> the id of the competitor
        race: list -> List of race number in each flight
        boat: list -> List of boat number in each race
        '''
        self.name = name
        self.id = id
        self.race = race
        self.boat = boat
    
    def leaderboard_rank(self, rank: int) -> None:
        '''
        Defines the leaderboards rank of the competitor
        '''
        self.l_rank = rank
    
    def race_rank(self, rank: int) -> None:
        '''
        Defines the race rank of the competitor
        '''
        self.r_rank = rank

    def distance_to_leader(self, distance: float) -> None:
        '''
        Defines the distance to the leader of the competitor
        '''
        self.dtl = distance


if __name__ == '__main__':
    competitor1 = Competitor('Hellerup sejlklub', 'HSII', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(competitor1.name)
    print(competitor1.id)
    print(competitor1.race)