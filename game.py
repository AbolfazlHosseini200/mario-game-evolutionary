class Game:
    def __init__(self, levels):
        # Get a list of strings as levels
        # Store level length to determine if a sequence of action passes all the steps

        self.levels = levels
        self.current_level_index = -1
        self.current_level_len = 0

    def load_next_level(self):
        self.current_level_index += 1
        self.current_level_len = len(self.levels[self.current_level_index])

    def get_score(self, actions):
        # Get an action sequence and determine the steps taken/score
        # Return a tuple, the first one indicates if these actions result in victory
        # and the second one shows the steps taken

        current_level = self.levels[self.current_level_index]
        steps = 0
        game_environment = 0
        for i in range(self.current_level_len - 1):
            current_step = current_level[i]
            if current_step == '_':
                if not actions[i - 1] == '0':
                    game_environment -= 0.5
                    # pass
                steps += 1
            elif current_step == 'M' and (actions[i - 1] == '0' or actions[i - 1] == '2'):
                steps += 1
                game_environment += 2
            elif current_step == 'G':
                if actions[i - 1] == '1':
                    steps += 1
                if actions[i - 2] == '1':
                    game_environment += 2.5
            elif current_step == 'L' and actions[i - 1] == '2':
                steps += 1
            else:
                break
        return steps == self.current_level_len - 1, steps, game_environment


g = Game(["____G__L__", "___G_M___L_"])
g.load_next_level()
# g.load_next_level()
# This outputs (False, 4)
# print(g.get_score("0010000000"))
