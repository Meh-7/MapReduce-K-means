# K-Means MapReduce with Hadoop Streaming

This repository demonstrates a mini project that implements a K-Means clustering algorithm using a simulated Hadoop MapReduce framework with Hadoop Streaming. The project is designed to run on Google Colab and includes notebooks, data files, and Python scripts.

## Project Structure
kmeans-mapreduce/
├── README.md
├── notebooks/
│   ├── kmeans_mapreduce.ipynb    # Main notebook for clustering with Hadoop MapReduce
│   └── drawdist.ipynb            # Notebook to generate, visualize, and export distributions
├── data/
│   ├── data.txt                  # Unlabeled data points (CSV: x,y)
│   └── data_with_labels.txt      # Data points with labels (CSV: x,y,label)
└── scripts/
    ├── mapper.py                 # Mapper script for K-Means clustering
    └── reducer.py                # Reducer script for updating centroids and aggregating WCSS

## Dependencies

- **Python 3.x**
- **NumPy**
- **Matplotlib**
- **Java OpenJDK 8** (required by Hadoop)
- **Hadoop 3.3.5** (for Hadoop Streaming)

## General Process

1. **Data Generation (drawdist.ipynb):**
   - Generates three bivariate normal distributions.
   - Visualizes the distributions.
   - Exports two files:
     - `data.txt`: Contains unlabeled data points (x,y).
     - `data_with_labels.txt`: Contains data points with an added label (1, 2, or 3).

2. **K-Means MapReduce Clustering (kmeans_mapreduce.ipynb):**
   - Installs and configures Hadoop and Java.
   - Uses Hadoop Streaming to run MapReduce jobs with your `mapper.py` and `reducer.py`.
   - Iteratively updates centroids until convergence (based on Within-Cluster Sum of Squares, WCSS) or maximum iterations are reached.
   - Visualizes the final clusters and centroids.

## How to Run

1. **Open the Notebooks:**
   - Open `drawdist.ipynb` in Google Colab to generate and export the data files.
   - Open `kmeans_mapreduce.ipynb` to run the MapReduce k-means clustering process.

2. **Ensure File Placement:**
   - Keep `mapper.py` and `reducer.py` in the same directory as the notebooks (or update paths accordingly).
   - The generated data files (`data.txt` and `data_with_labels.txt`) should reside in the `data/` folder.

3. **Execute Cells Sequentially:**
   - Follow the instructions in the notebooks to install Hadoop, run MapReduce iterations, and visualize results.
  
