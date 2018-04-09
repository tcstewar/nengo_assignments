import nengo

model = nengo.Network()
with model:
    a = nengo.Ensemble(n_neurons=100, dimensions=2)
    
    stim = nengo.Node([0,0])
    nengo.Connection(stim, a)