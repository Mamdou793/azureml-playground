This project demonstrates a complete, production‑grade machine learning workflow on Azure Machine Learning, starting from training a model and ending with a fully deployed Managed Online Endpoint that serves real‑time predictions.
It’s intentionally simple (Iris dataset + Logistic Regression) so the focus stays on the MLOps pipeline, not the model complexity.


This repository contains everything needed to train a scikit‑learn model, register it in Azure ML, package a custom inference environment, deploy the model to a Managed Online Endpoint, send real‑time predictions, version and track the entire workflow in Git


The model is trained using a simple Logistic Regression classifier on the Iris dataset.

train.py:

Loads the dataset, trains the model, saves the artifact to outputs/iris_logreg.pkl, (Optional) Registers the model in Azure ML. This script can be run locally or as an Azure ML job.


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



This project demonstrates:

How to structure ML code for Azure ML, how to build and register models, how to create custom inference environments, how to deploy real-time endpoints, how to debug container startup issues, and how to version everything in Git
