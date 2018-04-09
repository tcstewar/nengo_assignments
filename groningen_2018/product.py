import nengo

model = nengo.Network()
with model:
    a = nengo.Ensemble(n_neurons=100, dimensions=1)
    
    stim_a = nengo.Node([0])
    nengo.Connection(stim_a, a)
    
    b = nengo.Ensemble(n_neurons=100, dimensions=1)
    
    stim_b = nengo.Node([0])
    nengo.Connection(stim_b, b)
    
    
    c = nengo.Ensemble(n_neurons=100, dimensions=2)
    #def func1(x):
    #    return x, 0
    #def func2(x):
    #    return 0, x
    #nengo.Connection(a, c, function=func1)
    #nengo.Connection(b, c, function=func2)
    
    
    nengo.Connection(a, c[0])
    nengo.Connection(b, c[1])
    
