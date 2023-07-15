from joglwrapper import Reader
from joglwrapper import Project

reader = Reader()
response = reader.info(1)

project = Project(1)
print(project.id)