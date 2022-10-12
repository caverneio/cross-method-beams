from lib.classes.section import Section
from lib.classes.beam import Beam
from lib.classes.loads.distributedLoad import DistributedLoad
from lib.classes.loads.centralPointLoad import CentralPointLoad

cool_beam = Beam(
    [
        Section(10, [DistributedLoad(4)], "l"),
        Section(10, [DistributedLoad(4), CentralPointLoad(85)], "r"),
    ]
)

print("Moments:")
print(cool_beam.getMoments())

print("Reactions:")
print(cool_beam.getReactions())
