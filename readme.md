# Beam calculator

This project is a simple beam calculator. You can calculate the bending moments at the supports of a beam. This is done using the Hardy Cross method.

## Considerations

- Beams are assumed to have E.I = 1 along its length.
- Fixed supports are assumed to be only at the beginning and the end of the beam.
- Only central point loads and distributed loads can be used.

## Usage

Download, clone or fork this project and edit the `main.py` file

Create your beam with the following format:

```python
cool_beam = Beam(
    [
        Section(6.5, [DistributedLoad(4.5)], "l"),
        Section(6, [DistributedLoad(4.5), CentralPointLoad(7.5)]),
        Section(7, [DistributedLoad(4.5)], "r"),
    ]
)
```

A beam is composed of sections, which may have loads. The first section is the leftmost one, and the last one is the rightmost one. You can indicate if the sections in the left or right side of the beam are fixed by adding the string "l" or "r" as the third argument of the Section constructor.

Then, you can calculate the bending moments with the following commands:

```python
moments = cool_beam.getMoments()
print(moments)

# Output:
[-14.945, 17.642, 19.171, 17.977]
```

You can pass the number of iterations for the Cross method as the first argument of the `getMoments` method. The default value is 100.

The first value is the bending moment at the leftmost support of the beam, and the last value is the bending moment at the rightmost one.

You can also get the cross method table with the following command:

```python
cross_table = cool_beam.runCrossMethod(3)
print(cross_table)

# Output:
           0          1          2          3          4          5
0 -15.843750  15.843750 -19.125000  19.125000 -18.375000  18.375000
1   0.000000   1.575000   1.706250  -0.403846  -0.346154  -0.000000
2   0.787500   0.000000  -0.201923   0.853125  -0.000000  -0.173077
3  -0.000000   0.096923   0.105000  -0.459375  -0.393750   0.000000
4   0.048462  -0.000000  -0.229687   0.052500   0.000000  -0.196875
5  -0.000000   0.110250   0.119437  -0.028269  -0.024231   0.000000
6   0.055125  -0.000000  -0.014135   0.059719   0.000000  -0.012115
```

You should pass the number of iterations as the first argument of the `runCrossMethod` method. The default value is 10.

The output is a Pandas DataFrame, so you can use all the methods of this library to manipulate it.

## TODO:

- [x] Calculate bending moments at the supports.
- [ ] Calculate reactions at the supports
- [ ] Print results in a nice way
- [ ] Support for more types of loads: point loads, moments, etc.

Author: _@cuevatnt_
