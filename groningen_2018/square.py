import nengo

model = nengo.Network()
with model:
    a = nengo.Ensemble(n_neurons=1000, dimensions=1)
    
    stim = nengo.Node([0])
    nengo.Connection(stim, a)
    
    b = nengo.Ensemble(n_neurons=200, dimensions=1)
    
    def square(x):
        return 1 if x>0 else -1

    nengo.Connection(a, b, function=square)