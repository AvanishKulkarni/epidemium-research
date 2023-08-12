import os
import json

from joglwrapper.member_activities import *
from joglwrapper.member import Member

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

    def get_members(self) -> list[Member]:
        '''Get information on all members'''
        
        members = []

        directory = os.fsdecode(f'{self.path}/users/')

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".json"):
                members.append(Member(os.path.join(directory, filename), self.index))

        return members
    
    def get_member(self, id) -> Member:
        directory = os.fsdecode(f'{self.path}/users/')

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename == f'{id}.json':
                return Member(os.path.join(directory, filename), self.index)

        return None
    


