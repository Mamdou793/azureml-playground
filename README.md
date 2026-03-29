This project demonstrates a complete, production‑grade machine learning workflow on Azure Machine Learning, starting from training a model and ending with a fully deployed Managed Online Endpoint that serves real‑time predictions.
It’s intentionally simple (Iris dataset + Logistic Regression) so the focus stays on the MLOps pipeline, not the model complexity.


This repository contains everything needed to:
Train a scikit‑learn model
Register it in Azure ML
Package a custom inference environment
Deploy the model to a Managed Online Endpoint
Send real‑time predictions
Version and track the entire workflow in Git



Structure:
azureml-playground/
│
├── train.py                # Model training script
├── score.py                # Inference script for the deployed endpoint
├── environment.yml         # Custom conda environment for deployment
├── deployment.yml          # Managed Online Deployment configuration
├── sample_request.json     # Example payload for testing the endpoint
│
├── outputs/
│   └── iris_logreg.pkl     # Trained model artifact (optional to include)
│
└── README.md               # Project documentation




Training:
The model is trained using a simple Logistic Regression classifier on the Iris dataset.

train.py:

Loads the dataset

Trains the model

Saves the artifact to outputs/iris_logreg.pkl

(Optional) Registers the model in Azure ML

This script can be run locally or as an Azure ML job.




Creating the Deployment Environment:
Azure ML requires a custom environment for inference.
environment.yml defines:
Python version
scikit‑learn
Azure ML inference server
Azure ML SDK packages
This environment is built into a Docker image during deployment.



Deploying to a Managed Online Endpoint
deployment.yml defines:
The endpoint name
The deployment name
The model to load
The scoring script
The environment
The compute SKU

Deployment is done via CLI:
az ml online-deployment create \
  --name iris-deployment \
  --endpoint-name iris-endpoint-26970 \
  --file deployment.yml \
  --all-traffic


Invoking the Endpoint:
A sample request is included:

json
{
  "input_data": [[5.1, 3.5, 1.4, 0.2]]
}

Invoke using:

bash
az ml online-endpoint invoke \
  --name iris-endpoint-26970 \
  --request-file sample_request.json
  
Example output:

Code
"[0]"



Key Learnings"
This project demonstrates:

How to structure ML code for Azure ML
How to build and register models
How to create custom inference environments
How to deploy real-time endpoints
How to debug container startup issues
How to version everything in Git
