import nengo

model = nengo.Network()
with model:
    stim = nengo.Node([0])
    a = nengo.Ensemble(n_neurons=100, dimensions=1)
    nengo.Connection(stim, a)
    
    
    b = nengo.Ensemble(n_neurons=100, dimensions=1)
    nengo.Connection(a, b, synapse=0.005)
    
    
    def recurrent(x):
        return x**2
    nengo.Connection(b, b, function=recurrent, synapse=0.1)