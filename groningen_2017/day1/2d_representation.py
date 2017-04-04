import nengo

model = nengo.Network()
with model:
    a = nengo.Ensemble(n_neurons=1000, dimensions=2,
                       radius=1)
    
    stim = nengo.Node([0,0])
    
    nengo.Connection(stim, a)



