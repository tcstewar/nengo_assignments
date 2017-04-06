import nengo
import nengo.spa as spa

D = 32  # the dimensionality of the vectors

vocab = spa.Vocabulary(D)
for i in range(100):
    vocab.parse('W{}'.format(i))

model = spa.SPA()
with model:
    model.vision = spa.State(D, vocab=vocab)

    model.memory = spa.State(D, vocab=vocab, feedback=1)

    nengo.Connection(model.vision.output, model.memory.input,
                     transform=0.1)
