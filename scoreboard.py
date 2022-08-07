from turtle import Turtle
ALIGN = 'center'
FONT = ('Arial', 22, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open('score_record.txt') as f:
            self.high_score = int(f.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score_board()


    def update_score_board(self):
        self.clear()
        self.write(f'SCORE: {self.score}  High Score: {self.high_score}', move=False, align=ALIGN, font=FONT)


    def refresh_score(self):
        self.score += 1
        self.update_score_board()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('score_record.txt', 'w') as f:
                f.write(f'{self.high_score}')
        self.score = 0
        self.update_score_board()

    def contunue_or_not(self, res):
            if res.lower() == 'yes':
                return True
            elif res.lower() == 'no':
                return False



    # def game_over(self):
    #     self.goto(0, 0)
    #     global FONT
    #     FONT = ('Arial', 40, 'normal')
    #     self.clear()
    #     self.write('Game Over', move=False, align=ALIGN, font=FONT)
    #     self.goto(0, -50)
    #     FONT = ('Arial', 30, 'normal')
    #     self.update_score_board()
