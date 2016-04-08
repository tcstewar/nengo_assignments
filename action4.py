import nengo
import numpy as np
import nengo.spa as spa

vocab = spa.Vocabulary(32)

model = nengo.Network()
with model:
    state = spa.State(32, vocab=vocab)
    bg = nengo.networks.actionselection.BasalGanglia(4)
    nengo.Connection(state.output, bg.input, 
                     transform=[vocab.parse('DOG').v,
                                vocab.parse('CAT').v,
                                vocab.parse('RAT').v,
                                vocab.parse('COW').v,
                                ])    
    
