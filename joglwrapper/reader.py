import os
import json
from pathlib import Path
from . import session

class Reader(object):
    '''Reader class to generate and save information from JOGL'''
    
    def __init__(self):
        pass
        
    def save_project(self, index):
        '''Generates and saves information on the project at index'''

        if os.path.exists(f'./joglwrapper/cache/{index}/info.json'):
            pass
        else:
            print("no cache, regenerating")
            project_info_path = f'https://jogl-backend.herokuapp.com/api/programs/11/projects?items=1&page={index}'
            project_info_response = session.get(project_info_path)

            if project_info_response.status_code != 200 or (len(project_info_response.json()["projects"]) == 0):
                print("no project data found in API")
                return None
            else:
                Path(f'./joglwrapper/cache/{index}/users/').mkdir(parents=True, exist_ok=True)
                with open(f'./joglwrapper/cache/{index}/info.json', 'w', encoding='utf-8') as f:
                    json.dump(project_info_response.json(), f)

    def save_members(self, index):
        '''Generates and saves information on the members in project at index'''
        
        is_empty = not any(Path(f'./joglwrapper/cache/{index}/users/').iterdir())

        with open(f'./joglwrapper/cache/{index}/info.json', 'r', encoding='utf-8') as f:
            id_list = []
            
            for member in json.loads(f.read())['projects'][0]['users_sm']:
                id_list.append(member['id'])

        if (is_empty):

            for member in id_list:
                path = f'https://jogl-backend.herokuapp.com/api/users/{member}/'
                response = session.get(path)

                Path(f'./joglwrapper/cache/{index}/users/').mkdir(parents=True, exist_ok=True)
                member_json = response.json()

                with open(f'./joglwrapper/cache/{index}/users/{member}.json', 'w', encoding='utf-8') as f:
                    json.dump(member_json, f)

    # Completed
    def save_member_needs(self, index):
        '''Generates and saves information on all needs under a user's profile'''
        
        # Needs can be found at the URL below, stored as a JSON file.
        # https://jogl-backend.herokuapp.com/api/users/{member_id}/objects/needs
        # Use the above functions as a guide if you aren't sure how to do it. 
        # Get the needs for *all* members in a project, you should be able to read the IDs of every member from the project info.json
        # Basically save everything locally as a JSON, named like {id}_needs in the member folder ./cache/{id}/users/
        # Then write a matching function in ./joglwrapper/project.py to read it
        # Test in test_joglwrapper.py

        # Creates initial needs folder
        Path(f'./joglwrapper/cache/{index}/users/needs').mkdir(parents=True, exist_ok=True)
        is_empty = not any(Path(f'./joglwrapper/cache/{index}/users/needs/').iterdir())
        if not is_empty: 
            return None

        for member in os.listdir(f'./joglwrapper/cache/{index}/users/'):
            member = member[:-5]

            needs_path = f"https://jogl-backend.herokuapp.com/api/users/{member}/objects/needs"
            needs_response = session.get(needs_path)

            if needs_response.status_code == 200:
                needs_json = needs_response.json()

                if len(needs_json) > 0:
                    
                    for need in needs_json:
                        Path(f'./joglwrapper/cache/{index}/users/needs/{member}/').mkdir(parents=True, exist_ok=True)
                        with open(f'./joglwrapper/cache/{index}/users/needs/{member}/{need["id"]}.json', 'w', encoding='utf-8') as f:
                            json.dump(need, f)     
    
    # Completed
        pass
            
    def save_member_proposals(self, index):
        # Proposals can be found at: https://jogl-backend.herokuapp.com/api/users/101/objects/proposals
        # Has a tendency to be empty, but havent checked everything so make sure to check for that
        # Refer to save_member_needs() function for instructions

        pass
        
    def same_member_peer_reviews(self, index):
        # Peer Reviews can be found at: https://jogl-backend.herokuapp.com/api/users/101/objects/peer_reviews
        # Refer to save_member_needs() function for instructions
        pass

    def save_member_spaces(self, index):
        # Spaces can be found at: https://jogl-backend.herokuapp.com/api/users/101/objects/spaces
        # Refer to save_member_needs() function for instructions
        pass

    def save_member_programs(self, index):
        # Programs can be found at: https://jogl-backend.herokuapp.com/api/users/101/objects/programs
        # Refer to save_member_needs() function for instructions
        pass

    def save_member_challenges(self, index):
        # Challenges can be found at: https://jogl-backend.herokuapp.com/api/users/101/objects/challenges
        # Refer to save_member_needs() function for instructions
        pass

    def save_member_projects(self, index):
        # Projects can be found at: https://jogl-backend.herokuapp.com/api/users/101/objects/projects
        # Refer to save_member_needs() function for instructions
        
        for member in os.listdir(f'./joglwrapper/cache/{index}/users/'):
            member = member[:-5]

            projects_path = f"https://jogl-backend.herokuapp.com/api/users/{member}/objects/projects"
            projects_response = session.get(projects_path)

            if projects_response.status_code == 200:
                projects_json = projects_response.json()

                if len(projects_json) > 0:
                    
                    for project in projects_json:
                        Path(f'./joglwrapper/cache/{index}/users/projects/{member}/').mkdir(parents=True, exist_ok=True)
                        with open(f'./joglwrapper/cache/{index}/users/projects/{member}/{project["id"]}.json', 'w', encoding='utf-8') as f:
                            json.dump(project, f) 

    def save_all(self):

        for index in range(1, 7):
            self.save_project(index)
            self.save_members(index)
            self.save_member_needs(index)
            self.save_member_proposals(index)
            self.save_member_spaces(index)
            self.save_member_programs(index)
            self.save_member_challenges(index)
            self.save_member_projects(index)
        Path(f'./joglwrapper/cache/{index}/users/projects').mkdir(parents=True, exist_ok=True)
        is_empty = not any(Path(f'./joglwrapper/cache/{index}/users/projects/').iterdir())
        if not is_empty: 
            return None


