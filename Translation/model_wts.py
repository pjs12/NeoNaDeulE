import numpy as np
import json
from tensorflow import keras


def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def predict_mo(lst):
    model = keras.models.load_model("Translation/file//wts_model2.h5")
    char_indices = json.load(open("Translation/file//ci_dic.json", "r"))
    indices_char = json.load(open("Translation/file//ic_dic.json", "r"))

    result = ''

    for i in lst:

        if char_indices.get(i) is None:
            result += i + ' '
            continue

        if i[-1] == '요' or i[-1] == '다':
            result += i + ' '
            continue

        if i[-1] == '끝':
            if result[-2] == '다':
                result = result[:-2]
                result += '었다 '
            continue

        x = np.zeros((1, 20, len(char_indices)))
        x[0, len(i), char_indices[i]] = 1.

        preds = model.predict(x, verbose=0)[0]
        next_index = sample(preds)
        next_char = indices_char[str(next_index)]

        if next_char == '.':
            result += i + ' '
            continue

        result += (i + next_char + ' ')

    return result


def new_text(text):
    try:
        text.remove('')
        while '?' in text:
            text.remove('?')
    except Exception:
        return text
    return text
