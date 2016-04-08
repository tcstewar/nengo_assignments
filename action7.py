import nengo
import numpy as np
import nengo.spa as spa

vocab = spa.Vocabulary(32)
vocab2 = spa.Vocabulary(32)

model = spa.SPA()
with model:
    model.state = spa.State(32, vocab=vocab)
    model.act = spa.State(32, vocab=vocab2)
    model.motor = spa.State(32, vocab=vocab2)
    
    model.bg = spa.BasalGanglia(
        spa.Actions(
            'dot(state, DOG) --> motor=act',
            'dot(state, CAT) --> motor=MEOW',
            'dot(state, RAT) --> motor=SQUEAK',
            'dot(state, COW) --> motor=MOO',
        ))            
    
    model.thal = spa.Thalamus(model.bg)
