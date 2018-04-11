import nengo
model = nengo.Network()
with model:
    stim_food = nengo.Node([0,0])
    food = nengo.Ensemble(n_neurons=200, dimensions=2)
    nengo.Connection(stim_food, food)
    
    stim_light = nengo.Node(0)
    light = nengo.Ensemble(n_neurons=100, dimensions=1)
    nengo.Connection(stim_light, light)
    
    motor = nengo.Ensemble(n_neurons=200, dimensions=2)
    
    do_food = nengo.Ensemble(n_neurons=1000, dimensions=3,
                             radius=1.5)
    nengo.Connection(food, do_food[0:2])
    nengo.Connection(light, do_food[2])
    
    def food_func(x):
        food_x, food_y, light = x
        if light < 0.5:
            return food_x, food_y
        else:
            return 0, 0
        
    nengo.Connection(do_food, motor, function=food_func)
    
    
    pos = nengo.Ensemble(n_neurons=500, dimensions=2)
    nengo.Connection(pos, pos, synapse=0.2)
    nengo.Connection(motor, pos, synapse=0.2, transform=0.2)


    do_home = nengo.Ensemble(n_neurons=1000, dimensions=3,
                             radius=1.5)
    nengo.Connection(pos, do_home[0:2])
    nengo.Connection(light, do_home[2])
    
    def home_func(x):
        pos_x, pos_y, light = x
        if light < 0.5:
            return 0, 0
        else:
            return -pos_x, -pos_y 
        
    nengo.Connection(do_home, motor, function=home_func)


