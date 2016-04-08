import nengo
import numpy as np
import nengo.spa as spa

vocab = spa.Vocabulary(32)

model = nengo.Network()
with model:
    state = spa.State(32, vocab=vocab)
    q = nengo.networks.EnsembleArray(n_neurons=50, n_ensembles=4)
    nengo.Connection(state.output, q.input, 
                     transform=[vocab.parse('DOG').v,
                                vocab.parse('CAT').v,
                                vocab.parse('RAT').v,
                                vocab.parse('COW').v,
                                ])    
    
    e = 1
    i = -0.3

    transform = [[e, i, i, i], [i, e, i, i], [i, i, e, i], [i, i, i, e]]
    nengo.Connection(q.output, q.input, transform=transform)
    