import nengo
import numpy as np
import nengo.spa as spa

vocab = spa.Vocabulary(32)
vocab2 = spa.Vocabulary(32)

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

    
    thal = nengo.networks.actionselection.Thalamus(4)
    nengo.Connection(bg.output, thal.input)
    
    
    motor = spa.State(32, vocab=vocab2)
    nengo.Connection(thal.output, motor.input, 
                     transform=np.array([vocab2.parse('BARK').v,
                                vocab2.parse('MEOW').v,
                                vocab2.parse('SQUEAK').v,
                                vocab2.parse('MOO').v,
                                ]).T)    

    
