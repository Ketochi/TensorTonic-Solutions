import numpy  as np
def minmax_scale(X, axis=0, eps=1e-12):
    X = np.asarray(X)
    min_val = X.min(axis=axis, keepdims=True)
    max_val = X.max(axis=axis, keepdims=True)
    return (X - min_val) / (max_val - min_val + eps)