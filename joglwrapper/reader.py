import os
import json
from pathlib import Path
from . import session

class Reader(object):
    '''Reader class to generate and save information from JOGL'''
    
    def __init__(self):
        pass
        

    def get_project(self, index):
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

    def get_members(self, index):
        '''Generates and saves information on the members in project at index'''
        
        is_empty = not any(Path(f'./joglwrapper/cache/{index}/users/').iterdir())

        with open(f'./joglwrapper/cache/{index}/info.json', 'r', encoding='utf-8') as f:
            id = json.loads(f.read())['projects'][0]['id']

        if (is_empty):
            member_path = f'https://jogl-backend.herokuapp.com/api/projects/{id}/members'
            member_response = session.get(member_path)

            if member_response.status_code == 200:
                Path(f'./joglwrapper/cache/{index}/users/').mkdir(parents=True, exist_ok=True)
                member_json = member_response.json()

                for member in member_json['members']:
                    with open(f'./joglwrapper/cache/{index}/users/{member["id"]}.json', 'w', encoding='utf-8') as f:
                        json.dump(member, f)

                    print(member['id'])
                
            else:
                print('no member data found in API')
                return None               

            