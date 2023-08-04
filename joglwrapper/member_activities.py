import os
import json


class Activity:
    
    def __init__(self, json_file):
        self.json_file = json_file
        
        self.type = "Unknown Activity"
        self.id = json_file['id']
        self.title = json_file['title']

        self.description = ""

    def __str__(self):
        return f'Proposal: {self.title}'
    
    def __repr__(self):
        return f'proposal_{self.id}'

class Proposal(Activity):

    def __init__(self, json_file):
        self.type = "Proposal"
        self.description = json_file['summary']
        
        self.funding = json_file['funding']
        self.project_id = json_file['project_id']
        self.peer_review_id = json_file['peer_review_id']
        self.score = json_file['score']

        self.is_validated = True if self.json_file['is_validated'] == "true" else False

    def get_skills(self):
        skills = []
        for skill in self.json_file['skills']:
            skills.append(skill)

        return skills

    # Write functions or assign self variables to retrieve locally stored data

class Need(Activity):

    def __init__(self, json_file):
        self.type = "Need"

        self.description = json_file['content']
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

    # Write functions or assign self variables to retrieve locally stored data

class Space(Activity):

    def __init__(self, json_file):
        self.type = "Space"

    # Write functions or assign self variables to retrieve locally stored data

class Program(Activity):

    def __init__(self, json_file):
        self.type = "Program"

    # Write functions or assign self variables to retrieve locally stored data

class Peer_Review(Activity):

    def __init__(self, json_file):
        self.type = "Peer Review"

    # Write functions or assign self variables to retrieve locally stored data

class Member_Project(Activity):

    def __init__(self, json_file):
        self.type = "Project"

    # Write functions or assign self variables to retrieve locally stored data

class Challenge(Activity):

    def __init__(self, json_file):
        self.type = "Challenge"

    # Write functions or assign self variables to retrieve locally stored data