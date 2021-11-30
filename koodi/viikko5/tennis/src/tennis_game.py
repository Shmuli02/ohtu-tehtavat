class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score_text = {
            '00':'Love-All',
            '11':'Fifteen-All',
            '22':'Thirty-All',
            '33':'Forty-All',
            '0':'Love',
            '1':'Fifteen',
            '2':'Thirty',
            '3':'Forty',
            'D':'Deuce',
            'A1':f"Advantage {self.player1_name}",
            'A2':f"Advantage {self.player2_name}",
            'W1':f"Win for {self.player1_name}",
            'W2':f"Win for {self.player2_name}"
        }

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            if self.player2_score <= 3:
                score = self.score_text[str(self.player1_score)+str(self.player2_score)]
            else:
                score = self.score_text['D']

        elif self.player1_score >= 4 or self.player2_score >= 4:
            point_diff = self.player1_score - self.player2_score

            if point_diff == 1:
                score = self.score_text['A1']
            elif point_diff == -1:
                score = self.score_text['A2']
            elif point_diff >= 2:
                score = self.score_text['W1']
            else:
                score = self.score_text['W2']
        else:
            return f"{self.score_text[str(self.player1_score)]}-{self.score_text[str(self.player2_score)]}"

        return score
