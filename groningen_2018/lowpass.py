import nengo

model = nengo.Network()
with model:
    stim = nengo.Node([0])
    a = nengo.Ensemble(n_neurons=100, dimensions=1)
    nengo.Connection(stim, a)
    
    
    b = nengo.Ensemble(n_neurons=100, dimensions=1)
    
    synapse_actual = 0.05
    synapse_desired = 0.005
    
    def recurrent(x):
        return x*(1-synapse_actual / synapse_desired)
        
    def forward(x):
        return (synapse_actual / synapse_desired) * x
        
    nengo.Connection(a, b, function=forward, synapse=synapse_actual)
    nengo.Connection(b, b, function=recurrent, synapse=synapse_actual)