import random

class Words:
    def __init__(self):
        self.words = {
            1:{
                "Animal": ['cat', 'dog', 'bat', 'fox', 'cow', 'owl', 'pig', 'lion', 'rat', 'bird', 'goat'],
                "Body": ['arm', 'eye', 'head', 'leg', 'neck', 'ear', 'jaw', 'hand', 'hip', 'foot'],
                "Food": ['pie', 'jam', 'tea', 'egg', 'pea', 'beef', 'tuna', 'mint', 'cake']},
            2:{
                "Country" : ['spain', 'france', 'mexico', 'india', 'norway'],
                "Sports" : ['soccer', 'boxing', 'skating', 'hockey']
        }}
        
    def random_word(self, level: int) -> tuple[str, str]:
        try:
            random_category = random.choice(list(self.words[level].keys()))
            random_index = random.randrange(0, len(self.words[level][random_category]))
            random_word = self.words[level][random_category][random_index].upper()
            print(random_category, random_word)
            return (random_category, random_word)
        except:
            print ("level exceed")
    
words = Words()
