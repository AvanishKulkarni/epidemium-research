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

member = project.get_member(671)
print(member)
