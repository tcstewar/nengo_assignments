import nengo

model = nengo.Network()
with model:
    a = nengo.Ensemble(n_neurons=100, dimensions=1)
    stim_a = nengo.Node([0])
    nengo.Connection(stim_a, a)

    b = nengo.Ensemble(n_neurons=100, dimensions=1)
    stim_b = nengo.Node([0])
    nengo.Connection(stim_b, b)


    c = nengo.Ensemble(n_neurons=500, dimensions=2,
                        radius=1.4)
    
    nengo.Connection(a, c[0])
    nengo.Connection(b, c[1])
    
    d = nengo.Ensemble(n_neurons=100, dimensions=1)
    
    def product(x):
        return x[0]*x[1]
    nengo.Connection(c, d, function=product)
    
    