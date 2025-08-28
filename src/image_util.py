import numpy as np

# TODO: decompose greyscale and expand

def rgb_to_greyscale(img, flatten=False):
    flat = np.mean(img, axis=-1, keepdims=True)
    if flatten:
        return flat
    return np.repeat(flat, repeats=3, axis=-1).astype(int)

def reduce_values(img, thresh=0.5):
    return np.repeat(
        np.where(np.mean(img, axis=-1, keepdims=True) < thresh*255, 0, 255)
        , repeats=3, axis=-1).astype(int)
