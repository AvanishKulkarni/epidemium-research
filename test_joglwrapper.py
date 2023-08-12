from joglwrapper import Reader
from joglwrapper import Project
from joglwrapper import Output
from pathlib import Path

from pyvis.network import Network

net = Network(height='1000px', width='1000px')
net.barnes_hut()

# reader = Reader()
# reader.save_all()

output = Output()

output.generate_meta()

# net.add_nodes([1, 2, 3])
# net.add_edge(1,2)
# net.add_edge(3,2)

net.show('test.html', notebook=False)