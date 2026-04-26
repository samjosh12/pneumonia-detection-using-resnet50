from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Dummy preprocessing
def preprocess_image(image):
    # simulate preprocessing
    return image / 255.0

@app.route('/')
def home():
    return "AI Pneumonia Detection System"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # simulate image input
        data = request.json
        
        # dummy input array
        img = np.random.rand(64, 64, 3)
        
        # preprocessing
        processed_img = preprocess_image(img)
        
        # dummy model prediction
        prediction = np.random.rand()
        
        if prediction > 0.5:
            result = "PNEUMONIA"
        else:
            result = "NORMAL"
        
        return jsonify({
            "prediction": result,
            "confidence": float(prediction)
        })
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
