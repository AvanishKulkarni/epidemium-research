import os
import json

class Project(object):

    def __init__(self, index):

        with open(f'./joglwrapper/cached_results/{index}.json', 'r') as f:
            print(f"opened project at index {index}")

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
        self.follower_count = self.raw_dict['follower_count']
        self.needs_count = self.raw_dict['needs_count']
        self.posts_count = self.raw_dict['posts_count']
        self.reviews_count = self.raw_dict['reviews_count']
        self.members_count = self.raw_dict['members_count']
    


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