class CharacterInfo:
    def __init__(self):

        self.character_names = ["zyrus", "allan", "richard", "france", "renzo"]
        
        self.zyrus = {
            1 : {
            "name" : "Keyboard Rage",
            "description" : "Zyrus's anger issues serve an unexpected purpose: when he vents his frustration on his keyboard, it inadvertently removes five wrong keys. Who knew anger could be so helpful?",
            "cooldown" : "2 rounds"
                },
            2 : {
            "name" : "Pointless Procedure",
            "description" : "Zyrus possesses a forbidden skill born from his laziness: the ability to skip a level but in return he wouldn't earn any points",
            "cooldown" : "1-time use"
            }}
        
        self.france = {
            1 : {
            "name" : "Extra Rice",
            "description" : "France is so hungry that he have to ask Diwata for more extra rice gaining him extra 20 seconds when the timer runs out",
            "cooldown" : "1-time use (Passive Skill)"
                },
            2 : {
            "name" : "Diwata Pares",
            "description" : "France is hungry because he's been hanged for a long time. He craves for pares so he will call Diwata to cook his delicious pares. After eating, you will get unlimited guesses without limit for 3 seconds. (1 use only)",
            "cooldown" : "1-time use"
            }}
        
        self.richard = {
            1 : {
            "name" : "Time Dilation",
            "description" : "Richard perceives time slower than others.",
            "cooldown" : "Passive Skill"
            
                },
            2 : {
            "name" : "Tap! Tap! Tap!",
            "description" : "Richard will release all his pent-up stress to stop the time for 20 seconds. Guess what? the power of time dilation works with the skill active cooldown",
            "cooldown" : "2 rounds"
            }}
        
        self.allan = {
            1 : {
            "name" : "The Last Minute Man",
            "description" : "Allan works best when the due date is near. He will provide assistance and reveal one letter at the time when the player has one last health or 6 mistakes.",
            "cooldown" : "Passive Skill"
                },
            2 : {
            "name" : "Bahala na si Batman!",
            "description" : "Allan just accepts his fate to be hanged. But instead of speeding up the process, him being unaffected by anything that will happen from now causes him to be immune from a mistake. After this skill is activated, a mistake from the player will be ignored and not be counted.",
            "cooldown" : "1 round"
            }}
        
        self.renzo = {
            1 : {
            "name" : "Pwede po parevert?",
            "description" : "This ability grants players the ability to change the word given by Renzo, offering significant assistance when they struggle to guess the original word.",
            "cooldown" : "1 round"
                },
            2 : {
            "name" : "Shinigami Eyes!",
            "description" : "This ability activates Renzo's Eyes (Shinigami Eyes) power. This newfound ability allows them to predict half of the letters needed to complete the level's word in exchange for the half of the points on that round",
            "cooldown" : "3 rounds"
            }}
        
    def skill_info(self, skill_number: int, character: str) -> tuple[str, str, str]:
        if character == "zyrus":
            return (self.zyrus[skill_number]["name"], self.zyrus[skill_number]["description"], self.zyrus[skill_number]["cooldown"])
        if character == "france":
            return (self.france[skill_number]["name"], self.france[skill_number]["description"], self.france[skill_number]["cooldown"])
        if character == "richard":
            return (self.richard[skill_number]["name"], self.richard[skill_number]["description"], self.richard[skill_number]["cooldown"])
        if character == "allan":
            return (self.allan[skill_number]["name"], self.allan[skill_number]["description"], self.allan[skill_number]["cooldown"])
        if character == "renzo":
            return (self.renzo[skill_number]["name"], self.renzo[skill_number]["description"], self.renzo[skill_number]["cooldown"])
        
characters_info = CharacterInfo()
