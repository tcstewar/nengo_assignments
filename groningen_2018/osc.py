import nengo
model = nengo.Network()
with model:
    
    a = nengo.Ensemble(n_neurons=100, dimensions=2)
    
    synapse = 0.1
    def oscillator(x):
        r = 1
        s = 3
        return [synapse * (-x[1] * s + x[0] * (r - x[0]**2 - x[1]**2)) + x[0],
                synapse * ( x[0] * s + x[1] * (r - x[0]**2 - x[1]**2)) + x[1]]

    nengo.Connection(a, a, synapse=synapse, function=oscillator)
    
    
    b = nengo.Ensemble(n_neurons=100, dimensions=2)
    nengo.Connection(b, b, synapse=synapse, function=oscillator)
    
    nengo.Connection(a, b, transform=0.1, synapse=0.3)
    nengo.Connection(b, a, transform=0.1, synapse=0.01)
    