
class PlayerStats:
    def __init__(self,reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self,nationality):
        players = self.reader.get_players()
        filtered_and_sorted_players = sorted(list(filter(lambda x: (x.nationality == nationality), players)),key=lambda x: x.points,reverse=True)
        return filtered_and_sorted_players