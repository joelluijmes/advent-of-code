import os
from math import sqrt
from itertools import permutations

type coord = tuple[int, int, int]


def read_junction_box_coordinates() -> list[coord]:
    """Reads and parses the input.txt. List of junction boxes in 3D space as tuples."""

    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(f"{current_dir}/input.txt", "r") as fp:
        lines = [x.strip() for x in fp.readlines()]

    return [tuple(int(x) for x in row.split(",")) for row in lines]


def calculate_distance(coord1: coord, coord2: coord):
    """Calculates the Euclidean distance."""

    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2 + (coord1[2] - coord2[2]) ** 2)


def connect_circuits(junction_boxes: list[coord], k=1000):
    """Connects the circuits based on connecting closest junction boxes."""

    # permutations returns all possible linkage options. However, that also contains the reverse link.
    # In the case of this puzzle, the reverse orientation is considered a duplicate e.g. A-B == B-A
    # so we filter those out. Keeping only the unique links between boxes.
    all_combinations = list(permutations(junction_boxes, 2))
    all_combinations = [x for x in all_combinations if x <= x[::-1]]

    # Pre-compute all the distances between the possible combinations
    ordered_junctions = sorted(
        (((box1, box2), calculate_distance(box1, box2)) for (box1, box2) in all_combinations),
        key=lambda x: x[1],
    )

    # List of junction boxes that form a circuit together
    junction_to_circuit: dict[coord, list[coord]] = {}

    # we only consider k closest combinations per instruction
    for (coord1, coord2), _ in ordered_junctions[:k]:
        # If both junction boxes are already connected
        if coord1 in junction_to_circuit and coord2 in junction_to_circuit:

            # Link up their circuits if they are not in the same one
            if junction_to_circuit[coord1] != junction_to_circuit[coord2]:
                merged_circuit = junction_to_circuit[coord1] + junction_to_circuit[coord2]
                for x in merged_circuit:
                    junction_to_circuit[x] = merged_circuit

        # If both junction boxes are not in the circuit, create a new one
        elif coord1 not in junction_to_circuit and coord2 not in junction_to_circuit:
            circuit = [coord1, coord2]
            junction_to_circuit[coord1] = circuit
            junction_to_circuit[coord2] = circuit

        # If one is in the circuit, append it
        elif coord1 in junction_to_circuit:
            circuit = junction_to_circuit[coord1]
            circuit.append(coord2)
            junction_to_circuit[coord2] = circuit

        elif coord2 in junction_to_circuit:
            circuit = junction_to_circuit[coord2]
            circuit.append(coord1)
            junction_to_circuit[coord1] = circuit

    unique_circuits = list(set(tuple(x) for x in junction_to_circuit.values()))
    return unique_circuits


def main():
    junction_boxes = read_junction_box_coordinates()
    circuits = connect_circuits(junction_boxes)

    # The answer is the product of the three largest circuits, bit weird but ok.
    a, b, c = sorted((len(x) for x in circuits), reverse=True)[:3]
    result = a * b * c

    print("Total: ", result)


if __name__ == "__main__":
    main()
