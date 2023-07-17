from joglwrapper import Reader
from joglwrapper import Project

reader = Reader()
reader.get(1)
reader.get(5)
reader.get(3)

project = Project(1)

member = project.get_member(562)
print(type(member))
print(member)
