import os
from dotenv import load_dotenv
from azure.ai.ml import MLClient, command
from azure.identity import DefaultAzureCredential

# Load environment variables from .env file
load_dotenv()

# Retrieve the credentials from environment variables
subscription_id = os.getenv("SUBSCRIPTION_ID")
workspace_name = os.getenv("WORKSPACE_NAME")
resource_group = os.getenv("RESOURCE_GROUP")

# Create the MLClient instance with the credentials
ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace_name
)

# configure job
job = command(
    code="./src",
    command="python train.py",
    environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu@latest",
    compute="aml-cluster",
    experiment_name="train-model"
)

print("ML Job", job)

# connect to workspace and submit job
returned_job = ml_client.create_or_update(job)

print("Returned Job", returned_job)

