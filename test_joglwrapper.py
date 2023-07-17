from joglwrapper import Reader
from joglwrapper import Project
from pathlib import Path

reader = Reader()
reader.get_project(1)
reader.get_members(1)
reader.get_project(5)
reader.get_members(5)
reader.get_project(3)
reader.get_members(3)

project = Project(1)

RachelA = project.get_member(671)
print(RachelA)
print(RachelA.get_skills())
print(RachelA.get_interests())

Burgundxyz = project.get_member(896)
print(Burgundxyz.get_location())
print(Burgundxyz.get_interests())