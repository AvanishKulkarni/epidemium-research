from joglwrapper import Reader
from joglwrapper import Project
from joglwrapper import Output
from pathlib import Path

from pyvis.network import Network

net = Network(height='1000px', width='100%', bgcolor='darkgrey')
net.barnes_hut(spring_length=1, spring_strength=0.1, damping=0.5, central_gravity=0.7)

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

    net.add_node(n_id=index, 
                 label=f'Project {index}',
                 color='aqua',
                 mass=4,
                 shape='database',
                 title=f"<p>{project.title} (id: {project.id})<br>{project.short_description}</p>",
                 value=500
                 )

    for member in project.get_members():
        net.add_node(n_id=member.id, 
                     label=f'{str(member)}',
                     color='grey',
                     shape='diamond',
                     title=f'<p><b>{str(member)}</b></p><p>Affiliation: {member.affiliation}</p><p>Bio: {member.short_bio}</p>'
                     )
        net.add_edge(member.id, index)

        for activity in member.get_activities():

            net.add_node(n_id=activity.id,
                         label=activity.type, 
                         title=f"<p><b>{activity.type}: {activity.title}:</b></p><p>{activity.summary}</p>",
                         shape="circle",
                         color="green")
            net.add_edge(member.id, activity.id)

net.show('test.html', notebook=False)