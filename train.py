import os
import argparse
from datetime import datetime

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--output_dir", type=str, default="outputs")
    args = parser.parse_args()

    run_id = os.environ.get("AZUREML_RUN_ID", "local-run")
    print(f"Run ID: {run_id}")
    print(f"Starting training at {datetime.utcnow().isoformat()} UTC")
    print(f"Training for {args.epochs} epochs (dummy hyperparameter).")

    # Load data
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    # Train model
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Test accuracy: {acc:.4f}")

    # Save model
    os.makedirs(args.output_dir, exist_ok=True)
    model_path = os.path.join(args.output_dir, "iris_logreg.pkl")
    joblib.dump(model, model_path)
    print(f"Model saved to: {model_path}")

    print("Training complete.")


if __name__ == "__main__":
    main()

