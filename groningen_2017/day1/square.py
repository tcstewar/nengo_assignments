import nengo

model = nengo.Network()
with model:
    a = nengo.Ensemble(n_neurons=1000, dimensions=1,
                       radius=1)
    
    stim = nengo.Node([0])
    
    nengo.Connection(stim, a)

    b = nengo.Ensemble(n_neurons=500, dimensions=1)
    
    def square(x):
        return x*x
    

    nengo.Connection(a, b, function=square)

