from joglwrapper import Reader
from joglwrapper import Project

reader = Reader()
reader.get(1)
reader.get(5)


project = Project(1)
print(project.id)