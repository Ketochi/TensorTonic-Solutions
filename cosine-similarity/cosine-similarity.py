import numpy as np

def cosine_similarity(a, b):
    a_np = np.array(a)
    b_np = np.array(b)

    a_flat = a_np.flatten()
    b_flat = b_np.flatten()

    dot_prod = np.dot(a_flat,b_flat)

    norm_a = np.linalg.norm(a_flat)
    norm_b = np.linalg.norm(b_flat)

    if norm_a !=0 and norm_b != 0:
        cos = dot_prod/(norm_a*norm_b) 
    else:
        cos = 0
    return cos