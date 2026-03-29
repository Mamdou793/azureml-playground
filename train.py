import os
import argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=5)
    args = parser.parse_args()

    run_id = os.environ.get("AZUREML_RUN_ID", "local-run")
    print(f"Run ID: {run_id}")
    print(f"Starting training at {datetime.utcnow().isoformat()} UTC")
    print(f"Training for {args.epochs} epochs...")

    for epoch in range(1, args.epochs + 1):
        print(f"Epoch {epoch}/{args.epochs} - dummy loss: {1.0 / epoch}")

    print("Training complete.")

if __name__ == "__main__":
    main()
