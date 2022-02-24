from Project import Project 
from Person import Person
from sys import stdin as inp
import itertools


def sum_people(_people):
    s = _people[0]
    for i in _people[1:]:
        s += i
    return s

if __name__ == '__main__':
    people = list()
    projects = list() 
    working = set() # currently working
    active_projects = list()

    all_roles = set()

    # take the input here 
    num_projects, num_people = list(map(int, inp.readline().strip().split()))

    # adding in the people first ofc ofc 
    for _ in range(num_people):
        # get the name and the number of skills the person has so that we
        # can add each skill to a set

        name, num_skills = inp.readline().strip().split()
        num_skills = int(num_skills)
        # addd skills to this in the next loop
        skills = set()
        for _ in range(num_skills):
            skill = inp.readline().strip()
            skills.add(skill)

        pers = Person(name)
        for skill in skills:
            pers.add_skill(*skill.split())

        people.append(pers)
        print(pers)

    # now get the projects
    for _ in range(num_projects):
        # okay so this is a long list 
        in_ = inp.readline().strip().split()
        name = in_[0]
        days, score, best_before, roles = map(int, in_[1:])
        # fill this with project roles in the next loop
        project_roles = set()
        for _ in range(roles):
            role = inp.readline().strip()
            project_roles.add(role)
        
        prjk = Project(name, days, score, best_before, roles) #, project_roles) # removed this from the constructor
        for role in project_roles:
            prjk.add_role(*role.split())

        projects.append(prjk)
        print(prjk)


    current_day = -1
    projects = list(sorted(projects, key=lambda p: p.best_before))
    # print(projects) # ok så denne printer bare en representasjon men det er n prosjekter her
    
    

    while projects:
        current_day += 1

        for project in active_projects:
            if current_day ==  project.get_finish_day():
                project.release_workers()
            
        if not people :# if is empty
            continue
        
        for project in projects:
            if project.best_before + project.score <= current_day + project.days:
                projects.remove(project)
            else:
                # so we need k people on this project
                k = project.num_roles # num people needed
                a_people = list(filter(lambda p: p.is_availible(), people))
                subsets = itertools.combinations(a_people, k)
                for subset in subsets:
                    team = sum_people(subset)
                    # print('team', team)
                    if project.try_team(team):
                        print(project.name)
                        print(team.name)
                        for person in subset:
                            person.send_to_work() # same
                            project.working_on.append(person) # now this asshole is at work
                        try:
                            # print('removing project', project)
                            active_projects.append(project)
                            projects.remove(project)
                            project.complete(project.get_days()+current_day)
                            break
                        except Exception:
                            print('fog')
                            continue
                        
                        



                # filter(lambda t: set(t) == k) # ideen her er at settet skal være 
                
                # if can fill project with current available staff
                # remove filled staff for number of days required
                # projects.remove(project)
