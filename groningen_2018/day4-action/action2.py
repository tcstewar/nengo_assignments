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
                                
    q_all = nengo.Ensemble(n_neurons=1000, dimensions=4, radius=2)
    nengo.Connection(q.output, q_all)
    r = nengo.networks.EnsembleArray(n_neurons=50, n_ensembles=4)
    def q_max(x):
        result = [0, 0, 0, 0]
        result[np.argmax(x)] = 1
        return result
    nengo.Connection(q_all, r.input, function=q_max)
