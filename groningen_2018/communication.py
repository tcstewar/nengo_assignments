import nengo

model = nengo.Network()
with model:
    a = nengo.Ensemble(n_neurons=100, dimensions=1)
    
    stim = nengo.Node([0])
    nengo.Connection(stim, a)
    
    b = nengo.Ensemble(n_neurons=200, dimensions=1)
    
    nengo.Connection(a, b)