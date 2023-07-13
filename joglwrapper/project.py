import os
import json
from . import session

class Project(object):
    
    def __init__(self, index):
        self.index = index
        

    def info(self):

        if os.path.exists(f'./joglwrapper/cached_results/{self.index}.json'):
            print("cached result exists")
        else:
            print("no cache")
            path = f'https://jogl-backend.herokuapp.com/api/programs/11/projects?items=1&page={self.index}'
            response = session.get(path)
            if response.status_code != 200:
                return ConnectionError
            else:
                with open(f'./joglwrapper/cached_results/{self.index}.json', 'w', encoding='utf-8') as f:
                    json.dump(response.json(), f)

        with open(f'./joglwrapper/cached_results/{self.index}.json', 'r', encoding='utf-8') as f:
            return json.loads(f.read())