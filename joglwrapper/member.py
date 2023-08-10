import os
import json

from joglwrapper.member_activities import *

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
        self.affiliation = self.raw_dict['affiliation']

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
        try:
            for file in os.listdir(directory):
                with open(f'./joglwrapper/cache/{self.index}/users/needs/{self.id}/{file}', 'r', encoding='utf-8') as f:
                    needs_list.append(Need(json.loads(f.read())))
        finally:
            return needs_list
    
    def get_proposals(self):
        # Refer to reader.py matching function
        # Refer to get_needs() for instructions
        directory = os.fsdecode(f'./joglwrapper/cache/{self.index}/users/proposals/{self.id}/')

        proposals_list = []

        try:
            for file in os.listdir(directory):
                with open(f'./joglwrapper/cache/{self.index}/users/proposals/{self.id}/{file}', 'r', encoding='utf-8') as f:
                    proposals_list.append(Proposal(json.loads(f.read())))
        finally:
            return proposals_list
    
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