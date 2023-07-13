import requests
import json

api_url_base = "https://jogl-backend.herokuapp.com/api/programs/11/projects"
headers = {'Content-Type': 'application/json'}



def get_project_list():
    
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


project_list = get_project_list()

if project_list is not None:
    print("Project List:")
    for item in project_list['projects']:
        print(item['title'] + " by: " + item['creator']['first_name'] + " " + item['creator']['last_name'])