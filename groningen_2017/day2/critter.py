import nengo

model = nengo.Network()
with model:
    
    desired_direction_stim = nengo.Node([0,0])
    
    desired_direction = nengo.Ensemble(n_neurons=200, dimensions=2)
    nengo.Connection(desired_direction_stim, desired_direction)
    
    motor = nengo.Ensemble(n_neurons=200, dimensions=2)
    
    #nengo.Connection(desired_direction, motor)
    
    position = nengo.Ensemble(n_neurons=200, dimensions=2)
    nengo.Connection(motor, position, transform=0.05)
    nengo.Connection(position, position, synapse=0.1)
    
    scared_stim = nengo.Node([0])
    scared = nengo.Ensemble(n_neurons=100, dimensions=1)
    nengo.Connection(scared_stim, scared)
    
    do_desired = nengo.Ensemble(n_neurons=500, dimensions=3)
    nengo.Connection(desired_direction, do_desired[:2])
    nengo.Connection(scared, do_desired[2])
    
    def do_desired_func(x):
        desired_x, desired_y, scared = x
        if scared < 0.5:
            return desired_x, desired_y
        else:
            return 0, 0
    nengo.Connection(do_desired, motor, function=do_desired_func)
        
    do_home = nengo.Ensemble(n_neurons=500, dimensions=3)
    nengo.Connection(position, do_home[:2])
    nengo.Connection(scared, do_home[2])
    
    def do_home_func(x):
        pos_x, pos_y, scared = x
        if scared > 0.5:
            return -5*pos_x, -5*pos_y
        else:
            return 0, 0
    nengo.Connection(do_home, motor, function=do_home_func)
    