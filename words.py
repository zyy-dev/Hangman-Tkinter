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
        return self.words[1]["Animal"][random.randrange(1, len(self.words[1]["Animal"]))]
    
    
if __name__ == "__main__":
    x = Words()
    print (x.lvl_1())