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
        
    def lvl_1(self) -> tuple[str, str]:
        random_category = random.choice(list(self.words[1].keys()))
        random_index = random.randrange(0, len(random_category))
        
        random_word = self.words[1][random_category][random_index].upper()
        print(random_category, random_word)
        return (random_category, random_word)
    
word_to_guess = Words()


if __name__ == "__main__":
    x = Words()
    print (x.lvl_1())
