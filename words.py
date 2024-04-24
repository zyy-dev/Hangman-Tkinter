import random

class Words:
    def __init__(self):
        self.words = {
           1: {
        "Animals 1": ['cat', 'dog', 'bat', 'fox', 'cow', 'owl', 'pig', 'goat', 'rat', 'bird', 'lion'],
        "Body Parts": ['arm', 'eye', 'head', 'neck', 'jaw', 'ear', 'hand', 'foot', 'hip'],
        "Food": ['pie', 'jam', 'tea', 'egg', 'beef', 'rice', 'jam', 'pie', 'pork', 'cake']},
           2: {
        "Country": ['spain', 'france', 'mexico', 'india', 'norway', 'china', 'japan'],
        "Sports": ['soccer', 'boxing', 'hockey', 'skating', 'archery', 'bowling'],
        "Musical Instruments": ['violin', 'guitar', 'piano', 'flute', 'trumpet', 'ukulele', 'triangle']},
           3: {
        "Animals 2": ['sloth', 'skunk', 'otter', 'goose', 'raven', 'moose', 'llama', 'koala', 'hyena', 'bison'],
        "Professions": ['firefighter', 'politician', 'musician', 'journalist', 'surgeon', 'psychiatrist', 'astronomer'],
        "Superheroes": ['flash', 'darna', 'groot', 'rocket', 'batman', 'hawkeye', 'shazam']},
           4: {
        "Fast Food Chains": ['jollibee', 'chowking', 'greenwich', 'kfc', 'subway', 'mcdonald', 'starbucks', 'chipotle', 'popeyes'],
        "Greek Gods 1": ['poseidon', 'hera', 'athena', 'zeus', 'apollo', 'ares', 'aphrodite', 'hades'],
        "Car Brands": ['porsche', 'chevrolet', 'cadillac', 'dodge', 'bugatti', 'volkswagen', 'mclaren', 'maserati']},
           5: {
        "Greek Gods 2": ['demeter', 'dionysus', 'persephone', 'hestia', 'hephaestus', 'artemis', 'cronus', 'prometheus'],
        "Alcohol Brands": ['bacardi', 'hennessy', 'smirnoff', 'baileys', 'emperador', 'ginebra', 'fundador'],
        "Mythology": ['phoenix', 'cerberus', 'werewolf', 'sphinx', 'centaur', 'minotaur', 'chimera', 'unicorn']},
    }
        
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
