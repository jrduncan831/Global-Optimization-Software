# Global-Optimization-Software
This repo includes instructions for how to use global optimization software created by my undergraduate research group which combines basin hopping and minima hopping methods and allows users to mix and match features of both methods.  This repo also includes results from this project as well as a demo for how to use the software.

## Installation 

In order to to use run this global optimization software you will need to install TSASE.  TSASE depends on Atomic Simulation Environment (ASE). 

### ASE

You can find installation instructions for ASE at the following webpage: 

https://wiki.fysik.dtu.dk/ase/install.html

### TSASE 

You can find installation instructions for TSASE at the following webpage:

http://theory.cm.utexas.edu/tsase/download.html

### Software documentation

You can find documentation of how to use the global optimzation sofware in TSASE here:

http://theory.cm.utexas.edu/tsase/global_optimizer.html


## Demo  

The script demo_bgsd.py is a short demo of how you can find a saddle point for an Aluminum Adatom on a (100) Surface with BGSD.  The low energy saddle points found and probabilities of finding various saddle points for this system can be found in Figures 6 and 8 of the BGSD publication. 

## Results

All results for this project can be found on our research group interactive webpage: 

http://fri.oden.utexas.edu/~fri/fridb_GO/server.py

First select the material of interest (38, 55, 75 or 102 Lennard Jones Clusters).  Results will be displayed in a table.  You can sort the results by various metrics by clicking on the column header.
