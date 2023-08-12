from joglwrapper import Reader
from joglwrapper import Project
from joglwrapper import Output
from pathlib import Path

from pyvis.network import Network

net = Network(height='500px', width='500px')
net.barnes_hut()

# reader = Reader()
# reader.save_all()

# output = Output()
# output.generate_meta()



# NOTE you can add infinite edges and it only adds one - makes it very easy

# TODO 
# get list of all users
# get list of all connections between users (shared activities)
# generate graph from it to see how it looks


for index in range(1, 7):
    project = Project(index)

    net.add_node(index, label='Project 1')

    for member in project.get_members():
        net.add_node(member.id, label=f'{str(member)}')
        net.add_edge(member.id, index)

net.show('test.html', notebook=False)