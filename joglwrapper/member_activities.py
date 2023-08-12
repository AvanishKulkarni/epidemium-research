import os
import json

class Proposal:

    def __init__(self, json_file):
        self.json_file = json_file

        self.id = json_file['id']
        self.title = json_file['title']
        self.summary = json_file['summary'] 
        
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
    
    def __str__(self):
        return f'Proposal: {self.title}'
    
    def __repr__(self):
        return f'proposal_{self.id}'

    # Write functions or assign self variables to retrieve locally stored data

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

class Space:

    def __init__(self, json_file):
        self.json_file = json_file

    # Write functions or assign self variables to retrieve locally stored data

class Program:

    def __init__(self, json_file):
        self.json_file = json_file

    # Write functions or assign self variables to retrieve locally stored data

class Peer_Review:

    def __init__(self, json_file):
        self.json_file = json_file

    # Write functions or assign self variables to retrieve locally stored data

class Member_Project:

    def __init__(self, json_file):
        self.json_file = json_file

    # Write functions or assign self variables to retrieve locally stored data

        self.id = json_file['id']
        self.title = json_file['title'] 
        
        self.short_description = json_file['short_description']
        self.short_title = json_file['short_title']

        self.project_status = json_file['project_status']
        self.status = json_file['status'] 

        #self.city = json_file['city']
        #self.country = json_file['country']
        #self.created_at = json_file['created_at']

        # creator
        self.first_name = json_file['first_name']
        self.last_name = json_file['last_name']
        self.short_bio = json_file['short_bio']
        self.followers_count = json_file['followers_count']

        
        
        #self.is_looking_for_collaborators = True if self.json_file['is_looking_for_collaborators'] == "true" else False
        self.is_private = json_file['is_private']
        self.is_reviewed = json_file['is_reviewed']

        #self.maturity = json_file['maturity']
        self.members_count = json_file['members_count']
        self.needs_count = json_file['needs_count']
        self.posts_count = json_file['posts_count']
        self.reviews_count = json_file['reviews_count']
        self.saves = json_file['saves_count']

        #self.updated_at = json_file['updated_at']
   
        # users
        self.has_followed = True if self.json_file['has_followed'] == "true" else False
        self.has_saved = True if self.json_file['has_saved'] == "true" else False
        self.is_admin = True if self.json_file['is_admin'] == "true" else False
        self.is_member = True if self.json_file['is_member'] == "true" else False
        self.is_owner = True if self.json_file['is_owner'] == "true" else False
        #self.is_pending = True if self.json_file['is_pending'] == "true" else False
        #self.is_reviewer = True if self.json_file['is_reviewer'] == "true" else False
        #self.has_valid_proposal = True if self.json_file['has_valid_proposal'] == "true" else False --> is_validated?


    # geoloc
    def get_location(self):
        return f"({self.raw_dict['geoloc']['lat']}, {self.raw_dict['geoloc']['lng']})"
 
    def get_skills(self):
        skills = []

        for skill in self.json_file['skills']:
            skills.append(skill)
        return skills

    def __str__(self):
        return f'Need: {self.title}'
    
    def __repr__(self):
        return f'need_{self.id}'
    

    


class Challenge:

    def __init__(self, json_file):
        self.json_file = json_file

    # Write functions or assign self variables to retrieve locally stored data
