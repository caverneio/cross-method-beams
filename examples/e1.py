import sys

sys.path.insert(0, "./")

from lib.classes.section import Section
from lib.classes.beam import Beam
from lib.classes.loads.distributedLoad import DistributedLoad
from lib.classes.loads.centralPointLoad import CentralPointLoad


cool_beam = Beam(
    [
        Section(2, [DistributedLoad(5), CentralPointLoad(10)], "l"),
        Section(2, [DistributedLoad(5)]),
        Section(2, [DistributedLoad(5)], "r"),
    ]
)

moments = cool_beam.getMoments()
print(moments)

reactions = cool_beam.getReactions()
print(reactions)
