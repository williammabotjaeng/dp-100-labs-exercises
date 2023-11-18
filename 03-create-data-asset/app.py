from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential

my_path = './test.csv'

my_data = Data(
    path=my_path,
    type=AssetTypes.URI_FILE,
    description="test csv file",
    name="test",
    version="1.0.0"
)

try:
    credential = DefaultAzureCredential()
    # Check if given credential can get token successfully.
    credential.get_token("https://management.azure.com/.default")
except Exception as ex:
    # Fall back to InteractiveBrowserCredential in case DefaultAzureCredential not work
    credential = InteractiveBrowserCredential()

ml_client = MLClient.from_config(credential=credential)

ml_client.data.create_or_update(my_data)