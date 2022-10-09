from section import Section
from beam import Beam
from distributedLoad import DistributedLoad
from centralPointLoad import CentralPointLoad


# TEST 1: https://youtu.be/B1k4E12Vn6I?t=1538

cool_beam = Beam(
    [
        Section(6.5, [DistributedLoad(4.5)], "l"),
        Section(6, [DistributedLoad(4.5), CentralPointLoad(7.5)]),
        Section(7, [DistributedLoad(4.5)], "r"),
    ]
)

cross_table = cool_beam.runCrossMethod(3)
moments = cool_beam.getMoments()
print(cross_table)
print(moments)


# TEST 2: https://youtu.be/UxilXVnXBsQ?t=313

cool_beam = Beam(
    [
        Section(4, [DistributedLoad(0.42)], "l"),
        Section(5, [DistributedLoad(0.29)], "r"),
    ]
)

cross_table = cool_beam.runCrossMethod(3)
moments = cool_beam.getMoments()
print(cross_table)
print(moments)


# TEST 3: https://youtu.be/JtCmXzA4oEg?t=1049

cool_beam = Beam(
    [
        Section(3, [DistributedLoad(6)]),
        Section(4, [DistributedLoad(6)]),
    ]
)

cross_table = cool_beam.runCrossMethod(3)
moments = cool_beam.getMoments()
print(cross_table)
print(moments)
