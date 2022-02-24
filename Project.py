class Project:
    def __init__(self, name: str, days: int, score: int, best_before: int, num_roles: int):#skills: dict):
        self.name = name
        self.days = days
        self.score = score
        self.best_before = best_before
        self.num_roles = num_roles
        self.finish_date = None
        # the roles here have the form
        self.skills = dict()
        self.working_on = list() # people working on the project


    def release_workers(self):
        for worker in self.working_on:
            worker.release()

    def get_finish_day(self):
        """returns the day the project was finished"""
        return self.finish_date

    def complete(self, val):
        """Sets the day project is finished"""
        self.finish_date = val


    def add_role(self, skill, value):
        """""This method is just for instantiation
        please do not use :)"""
        self.skills[skill] = int(value) 
# UwU

    def get_roles(self):
        """Get tehe roles required for the project"""
        return self.roles


    def get_score(self):
        """Get the max score you get for completing the project"""
        return self.score

    
    def get_days(self):
        return self.days 


    def get_best_before(self):
        return self.best_before

    def try_team(self, t_skills) -> bool: # team is a "Person" (Person + Person + ... + Person)
        """Take is n a "person" (a sum of people" and returns True if the teams skillset matches"""
        skills = self.skills

        for skill, level in skills.items():
            if not t_skills.get(skill):
                return False 
            else:
                if t_skills.get(skill) < level:
                    return False
        return True



    
    def __repr__(self):
        return f"""{self.name}
        Days: {self.days}
        Points: {self.score}
        Best Before: {self.best_before}
        Roles: {self.skills}"""

    



    
    