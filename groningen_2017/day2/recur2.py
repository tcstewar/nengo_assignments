import nengo

model = nengo.Network()
with model:
    stim = nengo.Node([0])
    
    a = nengo.Ensemble(n_neurons=100, dimensions=1)
    
    actual_synapse = 0.1
    desired_filter = 0.005
    
    def forward(x):
        return (actual_synapse/desired_filter) * x
    
    nengo.Connection(stim, a, function=forward,
                     synapse=actual_synapse)
    
    def recurrent(x):
        return (1-actual_synapse/desired_filter)*x
    nengo.Connection(a, a, function=recurrent,
                        synapse=actual_synapse)
