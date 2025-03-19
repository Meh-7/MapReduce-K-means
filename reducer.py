#!/usr/bin/env python
import sys

def main():
    current_centroid = None
    sum_vector = None
    count_total = 0
    total_wcss = 0.0

    # Process each mapper output line from standard input.
    # Each line is expected to be of the form: 
    # <centroid_index><tab><x1,x2,...,xN><tab>1<tab><squared_distance>
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split("\t")
        if len(parts) != 4:
            continue
        try:
            centroid_index = int(parts[0])
            point_str = parts[1]
            count_val = int(parts[2])
            point = [float(x) for x in point_str.split(",")]
            wcss_contrib = float(parts[3])
        except Exception as e:
            continue

        # If we're still aggregating for the same centroid
        if current_centroid == centroid_index:
            # Sum up the vectors element-wise
            sum_vector = [s + p for s, p in zip(sum_vector, point)]
            count_total += count_val
            total_wcss += wcss_contrib
        else:
            # For a new centroid, output the aggregate for the previous one (if it exists)
            if current_centroid is not None:
                # Compute new centroid by averaging the summed vector
                new_centroid = [s / count_total for s in sum_vector]
                new_centroid_str = ",".join(map(str, new_centroid))
                # Emit centroid index, new centroid, and aggregated WCSS for that cluster
                print(f"{current_centroid}\t{new_centroid_str}\t{total_wcss}")
            # Initialize aggregation for the new centroid
            current_centroid = centroid_index
            sum_vector = point
            count_total = count_val
            total_wcss = wcss_contrib

    # Output the final centroid's aggregate after processing all input
    if current_centroid is not None:
        new_centroid = [s / count_total for s in sum_vector]
        new_centroid_str = ",".join(map(str, new_centroid))
        print(f"{current_centroid}\t{new_centroid_str}\t{total_wcss}")

if __name__ == "__main__":
    main()
