import json
import random

class SixtyJiazi:
    def __init__(self, poem_path):
        with open(poem_path, 'r', encoding='UTF-8') as fin:
            self.poems = json.load(fin)
    
    def pick(self):
        r = random.randint(0, 59)
        return self.poems[r]

if __name__ == "__main__":
    sj = SixtyJiazi('./sixty_jiazi.json')
    print(sj.pick())