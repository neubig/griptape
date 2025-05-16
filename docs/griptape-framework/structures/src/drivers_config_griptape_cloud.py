from griptape.configs.drivers import GriptapeCloudDriversConfig
from griptape.structures import Agent

# Create a new agent with the GriptapeCloudDriversConfig
with GriptapeCloudDriversConfig():
    # This agent will use Griptape Cloud for all operations
    agent = Agent()
    
    # Run a simple task
    response = agent.run("What is the capital of France?")