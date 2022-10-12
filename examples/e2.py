import sys

sys.path.insert(0, "./")

from lib.classes.section import Section
from lib.classes.beam import Beam
from lib.classes.loads.distributedLoad import DistributedLoad
from lib.classes.loads.centralPointLoad import CentralPointLoad

# Source: https://youtu.be/B1k4E12Vn6I?t=1538

cool_beam = Beam(
    [
        Section(6.5, [DistributedLoad(4.5)], "l"),
        Section(6, [DistributedLoad(4.5), CentralPointLoad(7.5)]),
        Section(7, [DistributedLoad(4.5)], "r"),
    ]
)

moments = cool_beam.getMoments()
print(moments)

reactions = cool_beam.getReactions()
print(reactions)
