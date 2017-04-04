import nengo

model = nengo.Network()
with model:
    stim = nengo.Node([0,0])
    a = nengo.Ensemble(n_neurons=500, dimensions=2)
    nengo.Connection(stim, a)
    
    b = nengo.Ensemble(n_neurons=500, dimensions=3)
    def f1(xy):
        x, y = xy
        return x*x, x*y, y*y
    nengo.Connection(a, b, function=f1)
    
    c = nengo.Ensemble(n_neurons=500, dimensions=1)
    def f2(combined):
        xx, xy, yy = combined
        return xx + 2*xy + yy
    nengo.Connection(b, c, function=f2)
        