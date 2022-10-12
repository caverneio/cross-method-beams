import sys

sys.path.insert(0, "./")

from lib.classes.section import Section
from lib.classes.beam import Beam
from lib.classes.loads.distributedLoad import DistributedLoad
from lib.classes.loads.centralPointLoad import CentralPointLoad

# Source: https://youtu.be/JtCmXzA4oEg?t=1049

cool_beam = Beam(
    [
        Section(3, [DistributedLoad(6)]),
        Section(4, [DistributedLoad(6)]),
    ]
)

moments = cool_beam.getMoments()
print(moments)

reactions = cool_beam.getReactions()
print(reactions)
