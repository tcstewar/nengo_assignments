import nengo

model = nengo.Network()
with model:
    stim = nengo.Node([0])
    a = nengo.Ensemble(n_neurons=500, dimensions=1)
    nengo.Connection(stim, a)
    
    b = nengo.Ensemble(n_neurons=500, dimensions=1)
    
    actual_synapse = 0.005
    desired_effect = 0.005
    
    def forward(x):
        return (actual_synapse / desired_effect) * x
    
    
    nengo.Connection(a, b, function=forward, 
                    synapse=actual_synapse)
    
    def recurrent(x):
        return (1 - actual_synapse / desired_effect) * x
    
    if actual_synapse != desired_effect:
        nengo.Connection(b, b, function=recurrent,
                    synapse=actual_synapse)
    
