from joglwrapper import Project

project_instance = Project(3)
response = project_instance.info()
print(type(response))