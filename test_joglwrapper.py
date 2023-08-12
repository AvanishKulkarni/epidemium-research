from joglwrapper import Reader
from joglwrapper import Project
from pathlib import Path

reader = Reader()
reader.save_project(1)
reader.save_members(1)
reader.save_project(5)
reader.save_members(5)
reader.save_project(3)
reader.save_members(3)
reader.save_member_needs(1)
reader.save_member_needs(5)
reader.save_member_needs(3)

project = Project(1)

RachelA = project.get_member(671)
print(RachelA)
proposals = RachelA.get_proposals(1)
print(proposals[0].title)


needs = RachelA.get_needs()
print(needs[0].get_skills())

