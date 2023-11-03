# dask-data-analysis
Data analysis in the ligate project using dask

## Introduction
Recommended youtube: Matthew Rocklin https://www.youtube.com/watch?v=FXsgmwpRExM

Open source framework of Matthew Rocklin for parallelization of python code and data structures. 


### Features
- Dask makes it easy to scale Python libraries like NumPy, pandas, and scikit-learnDask can also parallelize any Python code (not described here)
- For arrays, dataframes, and other high-level collections, Dask achieves the parallelization by dividing the objects into chunks or partitions, which can be distributed over multiple CPUs or GPUs.
- The collections are then used to create a task graph which can be executed by schedulers on a single machine or a cluster
- Easy integration with HPC (e.g. via SLURM batch schedulers) and GPU-optimised libraries such as Nvidia Rapids.

