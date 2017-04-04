import nengo

model = nengo.Network()
with model:
    a = nengo.Ensemble(n_neurons=100, dimensions=1,
                       radius=2)
    
    stim = nengo.Node(0)
    
    nengo.Connection(stim, a)



