
Pneumonia Detection using ResNet50

Overview
This project focuses on detecting pneumonia from chest X-ray images using a deep learning-based approach. It demonstrates how AI can be applied in healthcare for early disease detection. The system is designed as a web application where users can upload images and receive predictions in real time.

Features
Image preprocessing and normalization
AI-based prediction (Pneumonia / Normal)
Confidence score output
Flask-based backend for deployment

Approach
Used deep learning concepts for image classification
Applied preprocessing techniques such as normalization
Simulated model inference pipeline
Structured the project to reflect real-world AI deployment workflow

Tech Stack
Python
Flask
NumPy
TensorFlow / Keras (conceptual use)

Workflow
User sends an image request
Image is preprocessed (normalized)
Data is passed to the model
Model generates prediction
Result is returned as JSON response
Project Structure

pneumonia-detection-using-resnet50/
│
├── app.py
├── util.py
├── requirements.txt
├── README.md

Output Example
{
"prediction": "PNEUMONIA",
"confidence": 0.78
}

Future Improvements
Integrate real trained ResNet50 model
Improve accuracy using larger datasets
Add frontend UI
Deploy on cloud platforms (AWS/GCP)

Note
This project demonstrates the deployment and inference pipeline. The model training phase is not included and is represented in a simplified manner.

Conclusion
This project highlights how deep learning can be applied in healthcare for early disease detection and decision support.
