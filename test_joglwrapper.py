from joglwrapper import Reader
from joglwrapper import Project


reader = Reader()
reader.get(1)
reader.get(5)
reader.get(3)

project = Project(1)
print(project.id)

test_list = project.get_members()
member = test_list[0]
print(str(test_list))
print(member)
print(member.is_owner)
print(member.id)
