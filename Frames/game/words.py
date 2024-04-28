import random

class Words:
    def __init__(self):
        self.words = {
           1: {
        "Colors 1": ['red', 'blue', 'green', 'black', 'white', 'pink', 'cyan'],
        "Numbers": ['two', 'one', 'ten', 'nine', 'five', 'six'],
        "Animals 1": ['cat', 'dog', 'bat', 'fox', 'cow', 'owl', 'pig', 'goat', 'rat', 'bird', 'lion']},       
           2: {
        "Animals 2": ['wolf', 'deer', 'lion', 'seal', 'bear', 'worm', 'frog', 'hawk', 'crow', 'duck', 'crab'],
        "Body Parts": ['arm', 'eye', 'head', 'neck', 'jaw', 'ear', 'hand', 'foot', 'hip'],
        "Food": ['pie', 'jam', 'tea', 'egg', 'beef', 'rice', 'jam', 'pork', 'cake']},
            3: {
        "Relatives": ['sister', 'brother', 'father', 'mother', 'aunt', 'uncle'],
        "Colors 2": ['brown', 'magenta', 'indigo', 'yellow', 'maroon', 'purple'],
        "Fruit": ['apple', 'lemon', 'banana', 'mango', 'orange', 'cherry', 'peach', 'guava', 'grapes', 'pear']},
           4: {
        "Country": ['spain', 'france', 'mexico', 'india', 'norway', 'china', 'japan'],
        "Sports": ['soccer', 'boxing', 'hockey', 'skating', 'archery', 'bowling'],
        "Musical Instruments": ['violin', 'guitar', 'piano', 'flute', 'trumpet', 'ukulele', 'triangle']},
           5: {
        "Animals 3": ['sloth', 'skunk', 'otter', 'goose', 'raven', 'moose', 'llama', 'koala', 'hyena', 'bison'],
        "Professions": ['firefighter', 'politician', 'musician', 'journalist', 'surgeon', 'psychiatrist', 'astronomer'],
        "Superheroes": ['flash', 'darna', 'groot', 'rocket', 'batman', 'hawkeye', 'shazam']},
           6: {
        "Fast Food Chains": ['jollibee', 'chowking', 'greenwich', 'kfc', 'subway', 'mcdonald', 'starbucks', 'chipotle', 'popeyes'],
        "Greek Gods 1": ['poseidon', 'hera', 'athena', 'zeus', 'apollo', 'ares', 'aphrodite', 'hades'],
        "Car Brands": ['porsche', 'chevrolet', 'cadillac', 'dodge', 'bugatti', 'volkswagen', 'mclaren', 'maserati']},
           7: {
        "Greek Gods 2": ['demeter', 'dionysus', 'persephone', 'hestia', 'hephaestus', 'artemis', 'cronus', 'prometheus'],
        "Alcohol Brands": ['bacardi', 'hennessy', 'smirnoff', 'baileys', 'emperador', 'ginebra', 'fundador'],
        "Mythology": ['phoenix', 'cerberus', 'werewolf', 'sphinx', 'centaur', 'minotaur', 'chimera', 'unicorn']},
    }
        
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
