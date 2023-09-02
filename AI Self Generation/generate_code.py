import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM
from keras.optimizers import RMSprop

# 1. Load the codebase if you dont have a code base go to my web site Www.kidusberhanu.com to get the code base
with open('code.txt', 'r') as f:
    code = f.read()

# 2. Extract and sort unique characters
chars = sorted(list(set(code)))

# 3. Define the length of sequences you want the model to consider
maxlen = 60
step = 3
sentences = []
next_chars = []

for i in range(0, len(code) - maxlen, step):
    sentences.append(code[i: i + maxlen])
    next_chars.append(code[i + maxlen])

# 4. Vectorization
x = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

# 5. Building the LSTM model
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))

optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

# 6. Helper function to sample an index from a probability array
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

# 7. Mapping characters to indices and vice versa
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

# 8. Code generation function
def generate_code(length=400):
    start_index = np.random.randint(0, len(code) - maxlen - 1)
    generated = ''
    sentence = code[start_index: start_index + maxlen]
    generated += sentence

    model.load_weights('weights.best.hdf5')  # Load the best model

    for i in range(length):
        x_pred = np.zeros((1, maxlen, len(chars)))
        for t, char in enumerate(sentence):
            x_pred[0, t, char_indices[char]] = 1.

        preds = model.predict(x_pred, verbose=0)[0]
        next_index = sample(preds, 1.0)
        next_char = indices_char[next_index]

        sentence = sentence[1:] + next_char
        generated += next_char

    return generated

print(generate_code ())
