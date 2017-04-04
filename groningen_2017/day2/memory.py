import nengo

model = nengo.Network()
with model:
    stim = nengo.Node([0,0])
    
    a = nengo.Ensemble(n_neurons=200, dimensions=2)
    
    actual_synapse=0.1
    
    def forward(x):
        return actual_synapse * x
    
    nengo.Connection(stim, a, function=forward,
                     synapse=actual_synapse)
    
    def recurrent(x):
        return x
    nengo.Connection(a, a, function=recurrent,
                        synapse=actual_synapse)
