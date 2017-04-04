import nengo

model = nengo.Network()
with model:
    stim = nengo.Node([0,0])
    a = nengo.Ensemble(n_neurons=500, dimensions=2, radius=5)
    nengo.Connection(stim, a)
    

    c = nengo.Ensemble(n_neurons=500, dimensions=1)
    def f2(xy):
        x, y = xy
        return x*x + 2*x*y + y*y
        
    nengo.Connection(a, c, function=f2)
        