from collections import defaultdict



class Person:
    def __init__(self, name: str): #skillset: dict):
        self.name = name
        self.skillset = dict()
        self.availible = True
    
    def is_availible(self):
        """Check if the team member is availible for work"""
        return self.availible

    def send_to_work(self):
        """Send a team member to work"""
        self.availible = False

    def release(self):
        """release the team member from work"""
        self.availible = True


    def get_name(self):
        """Returns the name of the person."""
        return self.name

    def get_skills(self):
        """Returns the skills the person has."""
        return self.skillset

    def add_skill(self, name, level):
        self.skillset[name] = int(level)

    
    def __repr__(self):
        return f"{self.name}: {self.skillset}"

    def __add__(self, other):
        self_skills = self.get_skills()
        other_skills = other.get_skills()
        
        combined_skills = self_skills

        for skill in list(other_skills.keys()) + list(self_skills.keys()):
            combined_skills[skill]= max(self_skills.get(skill,0), other_skills.get(skill,0))
        # print(f'Creating a person from {self} and {other}')

        return combined_skills

        
        

