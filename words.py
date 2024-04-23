import random

class Words:
    def __init__(self):
        self.words = {
            1:{
                "Animal": ['cat', 'dog', 'bat', 'fox', 'cow', 'owl', 'pig', 'bee', 'rat', 'ant'],
                "Tool": ['saw', 'axe', 'pen', 'cup', 'jar', 'axe', 'mat', 'jar', 'tap', 'cut'],
                "Body": ['arm', 'eye', 'lip', 'leg', 'toe', 'ear', 'jaw', 'rib', 'hip'],
                "Food": ['pie', 'jam', 'tea', 'egg', 'pea', 'ham', 'jam', 'pie', 'nut', 'pot']}
        }
        
    def lvl_1(self) -> str:
        random_category = random.choice(list(self.words[1].keys()))
        random_index = random.randrange(0, len(random_category))
        
        random_word = self.words[1][random_category][random_index].upper()
        print(random_category, random_word)
        return (random_category, random_word)
    
word_to_guess = Words()


if __name__ == "__main__":
    x = Words()
    print (x.lvl_1())