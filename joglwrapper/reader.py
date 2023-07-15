import os
import json
from . import session

class Reader(object):
    
    def __init__(self):
        pass
        

    def info(self, index):

        if os.path.exists(f'./joglwrapper/cached_results/{index}.json'):
            print("cached result exists")
        else:
            print("no cache, regenerating")
            path = f'https://jogl-backend.herokuapp.com/api/programs/11/projects?items=1&page={index}'
            response = session.get(path)

            if response.status_code != 200 or (len(response.json()["projects"]) == 0):
                print("no data found in API")
                return None
            else:
                with open(f'./joglwrapper/cached_results/{index}.json', 'w', encoding='utf-8') as f:
                    json.dump(response.json(), f)
                    return response.json()
            