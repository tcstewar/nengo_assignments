import nengo

model = nengo.Network()
with model:
    stim = nengo.Node([0,0])
    a = nengo.Ensemble(n_neurons=500, dimensions=1)
    nengo.Connection(stim[0], a)
    nengo.Connection(stim[1], a)
    

    c = nengo.Ensemble(n_neurons=500, dimensions=1)
    def f2(x_plus_y):
        return x_plus_y * x_plus_y
    nengo.Connection(a, c, function=f2)
        