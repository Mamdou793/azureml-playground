import os
import joblib
import json
import numpy as np

def init():
    global model
    # Use the Azure environment variable to find the model folder
    model_root = os.getenv("AZUREML_MODEL_DIR")
    
    # Path includes 'outputs' because that's how the model was registered
    model_path = os.path.join(model_root, "outputs", "iris_logreg.pkl")
    
    print(f"Loading model from: {model_path}")
    model = joblib.load(model_path)
    print("Model loaded successfully!")

def run(raw_data):
    try:
        # Standard Azure ML data format is usually a dictionary
        data = json.loads(raw_data)
        
        # Check if the key exists to prevent crashing
        if "input_data" not in data:
            return {"error": "Missing 'input_data' key in request body"}
            
        inputs = np.array(data["input_data"])
        preds = model.predict(inputs)
        
        return preds.tolist()
    except Exception as e:
        return {"error": str(e)}