from joglwrapper import Reader
from joglwrapper import Project
from joglwrapper import Output
from pathlib import Path

from pyvis.network import Network

net = Network(height='1000px', width='1000px')
net.barnes_hut(spring_length=1)

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

    net.add_node(index, 
                 label='Project 1',
                 color='#5d97f5',
                 mass=4,
                 shape='box',
                 value=100
                 )

    for member in project.get_members():
        net.add_node(n_id=member.id, 
                     label=f'{str(member)}',
                     color='#FFFFFF',
                     shape='diamond'
                     )
        net.add_edge(member.id, index)


net.show_buttons()
net.show('test.html', notebook=False)