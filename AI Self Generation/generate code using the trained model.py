import numpy as np

i have defiend this in my AWS code i suggest you do the same to run the model
# chars, code, maxlen, model, sample, char_indices, indices_char

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

try:
    while True:
        print(generate_code())
except KeyboardInterrupt:
    print("Code generation stopped.")
