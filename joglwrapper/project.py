import os
import json

class Project:
    '''Project class to get information on project saved by Reader class'''

    def __init__(self, index):

        self.path = f'./joglwrapper/cache/{index}'

        with open(f'{self.path}/info.json', 'r', encoding='utf-8') as f:
            self.raw_dict = json.loads(f.read())['projects'][0]

        self.index = index
        self.id = self.raw_dict['id']
        self.title = self.raw_dict['title']
        self.short_title = self.raw_dict['short_title']
        self.short_description = self.raw_dict['short_description']
        self.status = self.raw_dict['status']
        self.grant_info = self.raw_dict['grant_info']
        self.is_private = self.raw_dict['is_private']
        self.is_reviewed = self.raw_dict['is_reviewed']
        self.follower_count = self.raw_dict['followers_count']
        self.needs_count = self.raw_dict['needs_count']
        self.posts_count = self.raw_dict['posts_count']
        self.reviews_count = self.raw_dict['reviews_count']
        self.members_count = self.raw_dict['members_count']

    def get_members(self):
        '''Get information on all members'''
        
        members = []

        directory = os.fsdecode(f'{self.path}/users/')

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".json"):
                members.append(Member(os.path.join(directory, filename), self.index))

        return members
    
    def get_member(self, id):
        directory = os.fsdecode(f'{self.path}/users/')

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename == f'{id}.json':
                return Member(os.path.join(directory, filename), self.index)

        return None

class Member:

    def __init__(self, json_file, index):
        self.json_file = json_file

        with open(self.json_file) as f:
            self.raw_dict = json.loads(f.read())

        self.index = index
        self.id = self.raw_dict['id']
        self.first_name = self.raw_dict['first_name']
        self.last_name = self.raw_dict['last_name']
        self.nickname = self.raw_dict['nickname']

        self.short_bio = self.raw_dict['short_bio']
        self.affliation = self.raw_dict['affiliation']

        self.followers_count = self.raw_dict['stats']['followers_count']
        self.projects_count = self.raw_dict['stats']['projects_count']
        self.spaces_count = self.raw_dict['stats']['spaces_count']

    def get_skills(self):
        return self.raw_dict['skills']
    
    def get_interests(self):
        skills = {
            1 : "No Poverty",
            2 : "Zero Hunger",
            3 : "Good Health and Well-being",
            4 : "Quality Education",
            5 : "Gender Equality",
            6 : "Clean Water and Sanitation",
            7 : "Affordable and Clean Energy",
            8 : "Decent Work and Economic Growth",
            9 : "Industry, Innovation, and Infrastructure",
            10 : "Reduced Inequalities",
            11 : "Sustainable Cities and Communities",
            12 : "Responsible Consumption and Production",
            13 : "Climate Action",
            14 : "Life Below Water",
            15 : "Life on Land",
            16 : "Peace, Justice, and Strong Institutions",
            17 : "Partnership for the Goals",
        }

        interests = []

        for interest in self.raw_dict['interests']:
            interests.append(skills[interest])
        
        return interests
    
    def get_location(self):
        return f"({self.raw_dict['geoloc']['lat']}, {self.raw_dict['geoloc']['lng']})"
    
    def get_needs(self):
        # Refer to reader.py matching function
        # Write a function here to return a list of Need classes.
        # The Need class is defined at the bottom of this file. 
        # Define the Need class to open up the locally saved JSON in __init__, then have instance variables and/or functions to return info for that specific Need
        # Refer to the JSON to see what data Need actually has

        directory = os.fsdecode(f'./joglwrapper/cache/{self.index}/users/needs/{self.id}/')

        needs_list = []
        for file in os.listdir(directory):
            with open(f'./joglwrapper/cache/{self.index}/users/needs/{self.id}/{file}', 'r', encoding='utf-8') as f:
                needs_list.append(Need(json.loads(f.read())))

        return needs_list
    
    def get_proposals(self):
        # Refer to reader.py matching function
        # Refer to get_needs() for instructions
        return []
    
    def get_peer_reviews(self):
        # Refer to reader.py matching function
        # Refer to get_needs() for instructions
        return []
    
    def get_spaces(self):
        # Refer to reader.py matching function
        # Refer to get_needs() for instructions
        return []
    
    def get_programs(self):
        # Refer to reader.py matching function
        # Refer to get_needs() for instructions
        return []

    def get_challenges(self):
        # Refer to reader.py matching function
        # Refer to get_needs() for instructions
        return []

    def get_projects(self):
        # Refer to reader.py matching function
        # Refer to get_needs() for instructions
        return []

    def __str__(self):
        return f'{self.first_name} {self.last_name} (id: {self.id})'
    
    def __repr__(self):
        return f'user_{self.id}'
    

class Need:

    def __init__(self, json_file):
        self.json_file = json_file

        self.id = json_file['id']
        self.title = json_file['title']
        self.content = json_file['content']
        self.status = json_file['status']
        self.project_status = json_file['project_status']
        
        self.followers = json_file['followers_count']
        self.members = json_file['members_count']
        self.saves = json_file['saves_count']
        self.posts = json_file['posts_count']

        self.is_urgent = True if self.json_file['is_urgent'] == "true" else False
        self.has_followed = True if self.json_file['has_followed'] == "true" else False
        self.has_saved = True if self.json_file['has_saved'] == "true" else False
        self.is_admin = True if self.json_file['is_admin'] == "true" else False
        self.is_member = True if self.json_file['is_member'] == "true" else False
        self.is_owner = True if self.json_file['is_owner'] == "true" else False
    
    def get_skills(self):
        skills = []

        for skill in self.json_file['skills']:
            skills.append(skill)

        return skills
    
    def __str__(self):
        return f'Need: {self.title}'
    
    def __repr__(self):
        return f'need_{self.id}'

    # Write functions or assign self variables to retrieve locally stored data

class Proposal:

    def __init__(self, json_file):
        self.json_file = json_file

    # Write functions or assign self variables to retrieve locally stored data

class PeerReview:

    def __init__(self, json_file):
        self.json_file = json_file

    # Write functions or assign self variables to retrieve locally stored data

class Space:

    def __init__(self, json_file):
        self.json_file = json_file

    # Write functions or assign self variables to retrieve locally stored data

class Program:

    def __init__(self, json_file):
        self.json_file = json_file

    # Write functions or assign self variables to retrieve locally stored data

class Challenges:

    def __init__(self, json_file):
        self.json_file = json_file

    # Write functions or assign self variables to retrieve locally stored data

class Member_Project:

    def __init__(self, json_file):
        self.json_file = json_file

    # Write functions or assign self variables to retrieve locally stored data