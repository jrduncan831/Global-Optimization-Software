
import tsase
from tsase.optimize.minima_basin2 import Hopping

# Set up atoms object
lj = tsase.calculators.lj(cutoff=35.0)
system = tsase.io.read_con('lj38-cluster.con')
system.set_calculator(lj)

print(Hopping)
# Create Instance of GO Class
opt = Hopping(atoms=system,
              temperature=5000,
              minenergy=-173.918427,
              move_type = True,
              distribution='molecular_dynamics',
              jumpmax=None,
              global_jump=None,
              global_reset=False,
              dimer_a=0.001,
              dimer_d=0.01,
              dimer_steps=20,
              timestep=0.1,
              mdmin=2,
              acceptance_criteria=False,
              minimaHopping_history=True,
              beta1=1.04,
              beta2=1.04,
              beta3=1.0/1.04,
              Ediff0=0.5,
              alpha1=0.98,
              alpha2=1./0.98,
              use_geometry=False,
              keep_minima_arrays=False)

# Run global optimization for 10,000 steps or until minenergy is reached
opt.run(10000, maxtemp=50000)

