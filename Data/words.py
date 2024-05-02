import random

class Words:
    def __init__(self):
        self.words = {
           1: {
        "Colors": ['red', 'blue', 'green', 'black', 'white', 'pink', 'cyan'],
        "Numbers": ['two', 'one', 'ten', 'nine', 'five', 'six'],
        "Animals": ['cat', 'dog', 'bat', 'fox', 'cow', 'owl', 'pig', 'goat', 'rat', 'bird', 'lion']},       
           2: {
        "Animals": ['wolf', 'deer', 'lion', 'seal', 'bear', 'worm', 'frog', 'hawk', 'crow', 'duck', 'crab'],
        "Body Parts": ['arm', 'eye', 'head', 'neck', 'jaw', 'ear', 'hand', 'foot', 'hip'],
        "Food": ['pie', 'jam', 'tea', 'egg', 'beef', 'rice', 'jam', 'pork', 'cake']},
           3: {
        "Relatives": ['sister', 'brother', 'father', 'mother', 'aunt', 'uncle'],
        "Colors": ['brown', 'magenta', 'indigo', 'yellow', 'maroon', 'purple'],
        "Fruit": ['apple', 'lemon', 'banana', 'mango', 'orange', 'cherry', 'peach', 'guava', 'grapes', 'pear']},
           4: {
        "Country": ['spain', 'france', 'mexico', 'india', 'norway', 'china', 'japan'],
        "Sports": ['basketball', 'volleyball', 'tennis', 'baseball', 'golf', 'football'],
        "Musical Instruments 1": ['violin', 'guitar', 'piano', 'flute', 'trumpet', 'ukulele', 'triangle']},
           5: {
        "Professions 1": ['doctor', 'police', 'dentist', 'teacher', 'lawyer', 'chef', 'artist', 'barber', 'baker', 'tailor'],
        "Sports": ['soccer', 'boxing', 'hockey', 'skating', 'archery', 'bowling'],
        "Marvel Characters": ['vision', 'punisher', 'wolverine', 'deadpool', 'hulk', 'daredevil', 'hawkeye']},
           6: {
        "Animals": ['sloth', 'skunk', 'otter', 'goose', 'raven', 'moose', 'llama', 'koala', 'hyena', 'bison'],
        "Professions": ['firefighter', 'politician', 'musician', 'journalist', 'surgeon', 'psychiatrist', 'astronomer'],
        "DC Characters": ['flash', 'cyborg', 'darkseid', 'deadshot', 'doomsday', 'deathstroke', 'shazam']},
           7: {
        "Fast Food Chains": ['jollibee', 'chowking', 'greenwich', 'kfc', 'subway', 'mcdonald', 'starbucks', 'chipotle', 'popeyes'],
        "Greek Gods": ['poseidon', 'hera', 'athena', 'zeus', 'apollo', 'ares', 'aphrodite', 'hades'],
        "Car Brands": ['porsche', 'chevrolet', 'cadillac', 'dodge', 'bugatti', 'volkswagen', 'mclaren', 'maserati']},
           8: {
        "Greek Gods": ['demeter', 'dionysus', 'persephone', 'hestia', 'hephaestus', 'artemis', 'cronus', 'prometheus'],
        "Alcohol Brands": ['bacardi', 'hennessy', 'smirnoff', 'baileys', 'emperador', 'ginebra', 'fundador'],
        "Mythology": ['phoenix', 'cerberus', 'werewolf', 'sphinx', 'centaur', 'minotaur', 'chimera', 'unicorn']},
           9: {
        "Dog Breeds": ['dalmatian', 'poodle', 'beagle', 'chihuahua', 'rottweiler', 'pomeranian', 'corgi', 'dobermann'],
        "Cat Breeds": ['siamese', 'burmese', 'persian', 'sphynx', 'siberian', 'balinese'],
        "Programming Languages": ['python', 'javascript', 'rust', 'swift', 'go', 'sql', 'assembly', 'php']},
          10: {
        "Movies": ['titanic', 'twilight', 'alladin', 'jumanji', 'ghostbusters', 'saw', 'godzilla', 'transformers']},
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
