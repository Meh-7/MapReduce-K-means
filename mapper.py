#!/usr/bin/env python
import sys
import math

def load_centroids(filename="centroids.txt"):
    """
    Load centroids from a file.
    Each line in the file should be of the form:
    <centroid_index><tab><x1,x2,x3,...,xN>
    """
    centroids = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("\t")
                if len(parts) != 2:
                    continue
                index = int(parts[0])
                vector = [float(x) for x in parts[1].split(",")]
                centroids[index] = vector
    except Exception as e:
        sys.stderr.write("Error loading centroids: " + str(e) + "\n")
    return centroids

def squared_distance(point, centroid):
    """Compute squared Euclidean distance between two vectors."""
    return sum((p - c) ** 2 for p, c in zip(point, centroid))

def main():
    # Load current centroids from a file
    centroids = load_centroids()
    if not centroids:
        sys.stderr.write("No centroids loaded. Exiting.\n")
        return

    # Process each data point from standard input
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            # Assume input point is a comma-separated list of numbers
            point = [float(x) for x in line.split(",")]
        except Exception as e:
            sys.stderr.write("Error parsing data point: " + str(e) + "\n")
            continue

        # Find the nearest centroid
        min_distance = None
        nearest_index = None
        for idx, centroid in centroids.items():
            dist = squared_distance(point, centroid)
            if min_distance is None or dist < min_distance:
                min_distance = dist
                nearest_index = idx

        # Emit key-value pair: <centroid_index> <tab> <point_vector> <tab> 1 <tab> <squared_distance>
        point_str = ",".join(map(str, point))
        print(f"{nearest_index}\t{point_str}\t1\t{min_distance}")

if __name__ == "__main__":
    main()
