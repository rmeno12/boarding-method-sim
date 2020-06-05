Airplane Boarding Method Simulations
====================================
  
A project to investigate the effectiveness of different boarding methods inspired by [this](https://www.youtube.com/watch?v=oAHbLRjF0vo) CGP Grey video and using ideas from "Optimal boarding method for airline passengers" by Jason H. Steffen, which can be found [here](https://arxiv.org/abs/0802.0733).

## How to use
### Environment setup
To setup the environment (recommended to be in a venv):
```
$ pip install -r requirements.txt -y
```

### Using the Simulation
To run the sorting method defined by `method.py` on a plane with a given `width` and number of `rows`:
```
$ python3 method.py rows width
```
Optionally, you can choose to run the method with increased verbosity to show each step taken when performing the calculations:
```
$ python3 method.py rows width --verbose
```

For more information on command line arguments of `method.py` run 
```
$ python3 method.py --help
```
Note: `calculation.py` only contains the time calculation function and cannot function on its own
