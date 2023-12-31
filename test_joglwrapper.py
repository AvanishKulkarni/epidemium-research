from joglwrapper import Reader
from joglwrapper import Project
from joglwrapper import Output
from pathlib import Path

reader = Reader()
reader.save_project(1)
reader.save_members(1)
reader.save_project(5)
reader.save_members(5)
reader.save_project(3)
reader.save_members(3)

reader.save_member_proposals(1)
reader.save_member_challenges(1)

project1 = Project(1)

PascalD = project1.get_member(7938)
RachelA = project1.get_member(671)

chal1 = RachelA.get_challenges()
chal_47 = chal1[0]
print(chal_47.description)

#challenges = RachelA.get_challenges()

'''
output = Output()

output.generate_project(1, 'test')

output.generate_all_users(1)

output.generate_user(671, 'test')

project = Project(1)
'''
