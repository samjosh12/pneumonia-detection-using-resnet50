import numpy as np

def preprocess_image(img):
    """
    Simple preprocessing function
    - Normalize pixel values
    - Ensure correct format
    """
    img = np.array(img)
    img = img / 255.0  # normalize
    return img
