import nengo

model = nengo.Network()
with model:
    a = nengo.Ensemble(n_neurons=100, dimensions=1)
    stim_a = nengo.Node([0])
    nengo.Connection(stim_a, a)

    b = nengo.Ensemble(n_neurons=100, dimensions=1)
    stim_b = nengo.Node([0])
    nengo.Connection(stim_b, b)


    c = nengo.Ensemble(n_neurons=100, dimensions=1,
                        radius=1)
    
    nengo.Connection(a, c)
    nengo.Connection(b, c)
    
    