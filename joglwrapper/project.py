import os
import json

class Project(object):

    def __init__(self, index):

        with open(f'./joglwrapper/cached_projects/{index}.json', 'r', encoding='utf-8') as f:
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
        members = []

        # TODO return a list of member objects with cached data
    


# - id
# - title, short_title
# - description
# - status
# - is_private
# - is_reviewed
# - follower count
# - needs count
# - posts count
# - users
#   - first name, last name
#   - bio
#   - owner t/f
#   - admin t/f
# - documents
# - challenges
# - geoloc
# - member count
# - skills "keywords"

class Member():
    def __init__(self, id):
        self.id = id

        with open(f'./joglwrapper/cached_users/{self.id}.json', 'r', encoding='utf-8') as f:
            self.raw_dict = json.loads(f.read())

        self.first_name = self.raw_dict['first_name']
        self.last_name = self.raw_dict['last_name']
        self.is_owner = True if self.raw_dict['owner'] == "true" else False
        self.is_admin = True if self.raw_dict['admin'] == "true" else False
        self.is_member = True if self.raw_dict['member'] == "true" else False