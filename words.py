import random

class Words:
    def __init__(self):
        self.words = {
            1:{
                "Animal": ['cat', 'dog', 'bat', 'fox', 'cow', 'owl', 'pig', 'bee', 'rat', 'ant'],
                "Object": ['saw', 'axe', 'pen', 'cup', 'jar', 'axe', 'mat', 'jar', 'tap', 'cut'],
                "Body": ['arm', 'eye', 'lip', 'leg', 'toe', 'ear', 'jaw', 'rib', 'hip'],
                "Food": ['pie', 'jam', 'tea', 'egg', 'pea', 'ham', 'jam', 'pie', 'nut', 'pot']},
            2:{
                "Animal": ['eel', 'hen', 'elk', 'ape', 'yak', 'boa', 'fly', 'koi', 'ram', 'doe'],
                "Object": ['pan', 'bag', 'key', 'rug', 'bow', 'hat', 'car', 'net'],
                "Body": ['gum', 'head', 'nose', 'chin', 'hair', 'neck', 'knee', 'hand', 'foot'],
                "Food": ['cake', 'corn', 'loaf', 'oats', 'pork', 'tofu', 'rice', 'beef']},
            3:{
                "Animal": ['bear', 'wolf', 'crab', 'deer', 'dove', 'duck', 'frog', 'goat', 'lion', 'mule'],
                "Object": ['book', 'sofa', 'fork', 'door', 'shoe', 'tent', 'bell', 'cape'],
                "Body": ['heel', 'calf', 'palm', 'face', 'shin', 'nail', 'anus', 'skin', 'sole'],
                "Food": ['soup', 'stew', 'taco', 'peas', 'tart', 'date', 'pear', 'lime']},
            4:{
                "Animal": ['snake', 'mouse', 'sheep', 'tiger', 'shark', 'panda', 'eagle', 'whale', 'zebra', 'horse'],
                "Object": ['phone', 'paper', 'wheel', 'table', 'train', 'watch', 'truck', 'clock'],
                "Body": ['heart', 'brain', 'ankle', 'elbow', 'wrist', 'mouth', 'liver', 'chest', 'skull'],
                "Food": ['ramen', 'gravy', 'bacon', 'honey', 'steak', 'sushi', 'bread', 'mochi']},
            5:{
                "Animal": ['sloth', 'skunk', 'otter', 'goose', 'raven', 'moose', 'llama', 'koala', 'hyena', 'bison'],
                "Object": ['chain', 'flute', 'house', 'pearl', 'pedal', 'knife', 'arrow', 'flint'],
                "Body": ['teeth', 'thumb', 'navel', 'thigh', 'spine', 'waist', 'femur', 'ovary', 'penis'],
                "Food": ['crepe', 'salad', 'prune', 'pizza', 'donut', 'dairy', 'nacho', 'kebab']},
    
            6:{
                "Animal": ['jackal', 'wombat', 'ferret', 'hornet', 'bobcat', 'baboon', 'badger', 'dugong', 'ocelot', 'weasel'],
                "Object": ['book', 'sofa', 'fork', 'door', 'shoe', 'tent', 'tire', 'cape'],
                "Body": ['thorax', 'spleen', 'navel', 'pelvis', 'tonsil', 'muscle', 'eyelid', 'tendon', 'larynx'],
                "Food": ['squash', 'radish', 'walnut', 'celery', 'lychee', 'parsley', 'cashew', 'turnip']},
            
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
