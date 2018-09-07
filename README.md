# ising-on-the-cake
A repository for my numerical Ising simulations. The classes directory contains useful classes for use in data generation.

## The setup

Data generation is performed by datagen. This file depends on a number of class files to setup a bunch of lattices, instantiate configurations, and perform Monte Carlo updating. The output of data generation is a pandas dataframe object which contains useful information about the simulated lattices. Depending on the lattice size that the user selects, a single configuration holds N by N bits which correspond to the spins on the lattice. To reduce the dimensionality, we perform principle component analysis and feed the 2 dominant principle components into the dataframe.

## The R scripts directory

The R scripts directory contains some useful R scripts for performing k-means clustering, plotting, etc. These are data analysis files.

## Future commits

0. Streamline the whole process, from data generation to analysis, so that the output from running main() is the critical temperature interval.

1. More efficient implementations of Monte Carlo updating. Currently data gen takes a long time and hogs a huge amount of memory (as it is storing many, many lattices and updating them simultaneously).

2. A graphical user interface? Possible animations of the updating procedure.
