import nengo

model = nengo.Network()
with model:
    stim_food = nengo.Node([0,0])
    
    food = nengo.Ensemble(n_neurons=200, dimensions=2)
    nengo.Connection(stim_food, food)
    
    motor = nengo.Ensemble(n_neurons=200, dimensions=2)
    
    #nengo.Connection(food, motor)
    
    position = nengo.Ensemble(n_neurons=500, 
                dimensions=2, radius=10)
    nengo.Connection(position, position, 
                    synapse=0.1)
    
    nengo.Connection(motor, position)
    
    stim_scared = nengo.Node([0])
    
    scared = nengo.Ensemble(n_neurons=100, 
                dimensions=1)
    nengo.Connection(stim_scared, scared)
    
    decide_scared = nengo.Ensemble(500, dimensions=3)
    nengo.Connection(scared, decide_scared[0])
    nengo.Connection(position, decide_scared[[1,2]],
                        transform=0.1)
    
    def scared_func(x):
        scared, pos_x, pos_y = x
        if scared > 0.5:
            return -pos_x, -pos_y
        else:
            return 0, 0
    nengo.Connection(decide_scared, motor,
                function=scared_func)
            
    decide_food = nengo.Ensemble(1000, 
            dimensions=3)
    nengo.Connection(scared, decide_food[0])
    nengo.Connection(food, decide_food[[1,2]])
    
    def food_func(x):
        scared, food_x, food_y = x
        if scared < 0.5:
            return food_x, food_y
        else:
            return 0, 0
    nengo.Connection(decide_food, motor,
                function=food_func)
            
            
    
    
    