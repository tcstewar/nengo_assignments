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
    
    
    act = spa.State(32, vocab=vocab2)
    channel = spa.State(32, vocab=vocab2)
    motor = spa.State(32, vocab=vocab2)
    nengo.Connection(act.output, channel.input)
    nengo.Connection(channel.output, motor.input)
    
    nengo.Connection(thal.output, motor.input, 
                     transform=np.array([vocab2.parse('0').v,
                                vocab2.parse('MEOW').v,
                                vocab2.parse('SQUEAK').v,
                                vocab2.parse('MOO').v,
                                ]).T)    
                                
    for ens in channel.all_ensembles:
        nengo.Connection(bg.output[0], ens.neurons, transform=np.ones((ens.n_neurons, 1)))

    
