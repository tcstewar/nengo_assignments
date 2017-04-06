import nengo
import numpy as np
import nengo.spa as spa

vocab = spa.Vocabulary(32)

model = nengo.Network()
with model:
    state = spa.State(32, vocab=vocab)
    q = nengo.networks.EnsembleArray(n_neurons=50, n_ensembles=4)
    for ens in q.ensembles:
        ens.intercepts = nengo.dists.Uniform(0, 1)
        ens.encoders = nengo.dists.Choice([[1]])
        
    nengo.Connection(state.output, q.input, 
                     transform=[vocab.parse('DOG').v,
                                vocab.parse('CAT').v,
                                vocab.parse('RAT').v,
                                vocab.parse('COW').v,
                                ])    

    def positive(x):
        return max(x, 0)
    q.add_output('positive', positive)
    
    e = 1
    i = -0.3

    transform = [[e, i, i, i], [i, e, i, i], [i, i, e, i], [i, i, i, e]]
    nengo.Connection(q.positive, q.input, transform=transform)
    