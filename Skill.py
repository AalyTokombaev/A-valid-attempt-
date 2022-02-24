class Skill:
    # I don't know if we're gonna use this one
    # cool to have for abstraction's sake
    def __init__(self, name: str, level: int):
        self.name = name 
        self.level = level
    
    def level_up(self):
        self.level += 1
        