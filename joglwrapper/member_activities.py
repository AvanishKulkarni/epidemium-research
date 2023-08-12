import os
import json

class Activity:
    
    def __init__(self, json_file):
        self.json_file = json_file
        
        self.type = "Unknown Activity"
        self.id = json_file['id']
        self.title = json_file['title']

        self.summary = ""

class Proposal(Activity):

    def __init__(self, json_file):
        Activity.__init__()

        self.summary = json_file['summary'] 
        
        self.funding = json_file['funding']
        self.project_id = json_file['project_id']
        self.peer_review_id = json_file['peer_review_id']
        self.score = json_file['score']

        self.is_validated = True if self.json_file['is_validated'] == "true" else False

    def get_skills(self) -> list[str]:
        skills = []
        for skill in self.json_file['skills']:
            skills.append(skill)

        return skills
    
    def __str__(self):
        return f'Proposal: {self.title}'
    
    def __repr__(self):
        return f'proposal_{self.id}'

    # Write functions or assign self variables to retrieve locally stored data

class Need(Activity):

    def __init__(self, json_file):
        Activity.__init__(self, json_file)

        self.type = "Need"

        self.summary = json_file['content']
        self.status = json_file['status']
        self.project_status = json_file['project_status']
        
        self.followers = json_file['followers_count']
        self.members = json_file['members_count']
        self.saves = json_file['saves_count']
        self.posts = json_file['posts_count']

        self.is_urgent = True if json_file['is_urgent'] == "true" else False
        self.has_followed = True if json_file['has_followed'] == "true" else False
        self.has_saved = True if json_file['has_saved'] == "true" else False
        self.is_admin = True if json_file['is_admin'] == "true" else False
        self.is_member = True if json_file['is_member'] == "true" else False
        self.is_owner = True if json_file['is_owner'] == "true" else False
    
    def get_skills(self) -> list[str]:
        skills = []

        for skill in self.json_file['skills']:
            skills.append(skill)

        return skills

    # Write functions or assign self variables to retrieve locally stored data

class Space(Activity):

    def __init__(self, json_file):
        Activity.__init__(self, json_file)
        self.type = "Space"

    # Write functions or assign self variables to retrieve locally stored data

class Program(Activity):

    def __init__(self, json_file):
        Activity.__init__(self, json_file)
        self.type = "Program"

    # Write functions or assign self variables to retrieve locally stored data

class Peer_Review(Activity):

    def __init__(self, json_file):
        Activity.__init__(self, json_file)
        self.type = "Peer Review"

    # Write functions or assign self variables to retrieve locally stored data

class Member_Project(Activity):

    def __init__(self, json_file):
        Activity.__init__(self, json_file)
        self.type = "Project"
        
        self.summary = json_file['short_description']
        self.short_title = json_file['short_title']

        self.status = json_file['status'] 

        self.followers_count = json_file['followers_count']
        self.is_private = json_file['is_private']
        self.is_reviewed = json_file['is_reviewed']

        self.members_count = json_file['members_count']
        self.needs_count = json_file['needs_count']
        self.posts_count = json_file['posts_count']
        self.reviews_count = json_file['reviews_count']
        self.saves = json_file['saves_count']

        self.creator = f"{json_file['creator']['first_name']} {json_file['creator']['last_name']} (id: {json_file['creator']['id']})"
   
        self.has_valid_proposal = True if self.json_file['has_valid_proposal'] == "true" else False


    def get_location(self) -> dict:
        return f"({self.raw_dict['geoloc']['lat']}, {self.raw_dict['geoloc']['lng']})"
 
    def get_skills(self) -> list[str]:
        skills = []

        for skill in self.json_file['skills']:
            skills.append(skill)
        return skills

    def __str__(self):
        return f'Project: {self.title}'
    
    def __repr__(self):
        return f'project_{self.id}'

class Challenge(Activity):

    def __init__(self, json_file):
        Activity.__init__(self, json_file)
        self.type = "Challenge"

    # Write functions or assign self variables to retrieve locally stored data
