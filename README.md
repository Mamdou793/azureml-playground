A lightweight, cross‑platform desktop application built with Avalonia UI and .NET 8, performing real‑time Iris flower classification using a trained machine learning model.
This project demonstrates end‑to‑end engineering: model integration, UI design, packaging, and native macOS app distribution.


<img width="414" height="441" alt="Screenshot 2026-03-30 at 8 13 14 PM" src="https://github.com/user-attachments/assets/fb1c9442-b608-4f8a-a681-dd63d893bf36" />

<img width="414" height="441" alt="Screenshot 2026-03-30 at 8 14 02 PM" src="https://github.com/user-attachments/assets/d48b8654-a19b-4cf0-87ff-945f12ce42e9" />


✨ Features

Native macOS .app bundle with a custom icon

Self‑contained — no .NET installation required

Clean Avalonia UI with responsive layout

Local ML inference (no cloud dependency)

Cross‑platform codebase (macOS, Windows, Linux)

Simple, intuitive workflow for entering iris measurements

Instant prediction output with confidence values



✨ How to Run (macOS)

Download the latest release ZIP from the Releases page.

Extract the ZIP — you’ll get IrisClassifier.app.

On first launch, macOS may warn about an unverified developer.

Right‑click the app → Open

Confirm you want to run it

The app will open normally from then on.


✨ How It Works

The app uses a trained ML model to classify iris flowers into:

Setosa

Versicolor

Virginica

The model takes four numeric inputs:

Sepal Length

Sepal Width

Petal Length

Petal Width

The UI collects these values, sends them to the model, and displays the predicted class.


✨ Tech Stack

<img width="365" height="129" alt="Screenshot 2026-03-30 at 8 26 48 PM" src="https://github.com/user-attachments/assets/ccc34c6a-0a7a-438e-a7be-911396ad97f9" />




Cloud Version (Azure ML Experiment)

Before building the desktop version, this project included a cloud‑hosted ML workflow deployed to Azure Machine Learning using:

Managed Online Endpoints

YAML deployment files

az ml online-deployment create

Traffic routing and versioning

REST‑based inference


This experiment demonstrated:

packaging a model for cloud inference

deploying and managing endpoints via CLI

testing predictions through HTTP requests

understanding serverless ML hosting

The current version of the app uses local ML inference only, but the Azure ML workflow is included here.
