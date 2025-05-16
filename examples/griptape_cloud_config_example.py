"""
Example showing how to use the GriptapeCloudDriversConfig.

To run this example, you need to set the GT_CLOUD_API_KEY environment variable:
export GT_CLOUD_API_KEY=your_api_key

You can also set other environment variables for specific drivers:
export GT_CLOUD_BASE_URL=https://your-custom-endpoint.com
export GT_CLOUD_STRUCTURE_ID=your-structure-id
export GT_CLOUD_STRUCTURE_RUN_ID=your-run-id
export GT_CLOUD_BUCKET_ID=your-bucket-id
export GT_CLOUD_KNOWLEDGE_BASE_ID=your-kb-id
"""

import os
from griptape.configs.drivers import GriptapeCloudDriversConfig
from griptape.structures import Agent

# Check if the API key is set
if "GT_CLOUD_API_KEY" not in os.environ:
    print("Warning: GT_CLOUD_API_KEY environment variable not set. Using dummy key for demonstration.")
    # For real usage, uncomment the following line:
    # raise ValueError("Please set the GT_CLOUD_API_KEY environment variable")

# Create a new agent with the GriptapeCloudDriversConfig
# You can provide configuration parameters directly or use environment variables
with GriptapeCloudDriversConfig(
    # Optional: Override default values
    # api_key="your-api-key-here",
    # base_url="https://cloud.griptape.ai",
    # structure_id="your-structure-id",
    # structure_run_id="your-run-id",
    # bucket_id="your-bucket-id",
    # knowledge_base_id="your-kb-id"
):
    # This agent will use Griptape Cloud for all operations
    agent = Agent()
    
    # Run a simple task
    response = agent.run("What is the capital of France?")
    print(response)

# You can also create a config instance and use it later
cloud_config = GriptapeCloudDriversConfig()

# Access individual drivers if needed
prompt_driver = cloud_config.prompt_driver
vector_store_driver = cloud_config.vector_store_driver

# Use the config with another agent
with cloud_config:
    another_agent = Agent()
    response = another_agent.run("Tell me about Paris.")
    print(response)