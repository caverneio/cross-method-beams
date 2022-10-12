import sys

sys.path.insert(0, "./")

from lib.classes.section import Section
from lib.classes.beam import Beam
from lib.classes.loads.distributedLoad import DistributedLoad
from lib.classes.loads.centralPointLoad import CentralPointLoad

# Source: https://youtu.be/UxilXVnXBsQ?t=313

cool_beam = Beam(
    [
        Section(4, [DistributedLoad(0.42)], "l"),
        Section(5, [DistributedLoad(0.29)], "r"),
    ]
)


moments = cool_beam.getMoments()
print(moments)

reactions = cool_beam.getReactions()
print(reactions)
