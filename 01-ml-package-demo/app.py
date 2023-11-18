import os
from dotenv import load_dotenv
from azure.ai.ml import MLClient
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