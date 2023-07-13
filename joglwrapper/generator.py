import requests
import json

class generator:

    def __init__(self):
        pass
        
    def update_data(self):
        path = f"https://jogl-backend.herokuapp.com/api/programs/11/projects"
        response = requests.get(path)

        if response.status_code == 200:
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(response.json())

            return response.json()
        else:
            return None