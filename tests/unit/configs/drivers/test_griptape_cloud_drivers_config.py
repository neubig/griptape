import os
import pytest
import requests
from unittest.mock import patch, MagicMock

from griptape.configs.drivers import GriptapeCloudDriversConfig
from griptape.drivers.prompt.griptape_cloud import GriptapeCloudPromptDriver
from griptape.drivers.image_generation.griptape_cloud import GriptapeCloudImageGenerationDriver
from griptape.drivers.memory.conversation.griptape_cloud import GriptapeCloudConversationMemoryDriver
from griptape.drivers.vector.griptape_cloud import GriptapeCloudVectorStoreDriver
from griptape.drivers.structure_run.griptape_cloud import GriptapeCloudStructureRunDriver
from griptape.drivers.ruleset.griptape_cloud import GriptapeCloudRulesetDriver
from griptape.drivers.file_manager.griptape_cloud import GriptapeCloudFileManagerDriver
from griptape.drivers.event_listener.griptape_cloud import GriptapeCloudEventListenerDriver
from griptape.drivers.observability.griptape_cloud import GriptapeCloudObservabilityDriver


class TestGriptapeCloudDriversConfig:
    @pytest.fixture(autouse=True)
    def setup_env_vars(self):
        # Set dummy environment variables for testing
        with patch.dict(os.environ, {
            "GT_CLOUD_API_KEY": "test_api_key",
            "GT_CLOUD_STRUCTURE_ID": "test-structure-id",
            "GT_CLOUD_STRUCTURE_RUN_ID": "test-run-id",
            "GT_CLOUD_BUCKET_ID": "test-bucket-id",
            "GT_CLOUD_KNOWLEDGE_BASE_ID": "test-kb-id"
        }):
            yield
    
    @pytest.fixture(autouse=True)
    def mock_requests(self):
        # Create a mock response for API calls
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "test-bucket-id", "name": "Test Bucket"}
        mock_response.raise_for_status.return_value = None
        
        # Patch the requests.request method to return our mock response
        with patch("requests.request", return_value=mock_response):
            yield

    def test_prompt_driver(self):
        config = GriptapeCloudDriversConfig()
        assert isinstance(config.prompt_driver, GriptapeCloudPromptDriver)
        assert config.prompt_driver.api_key == "test_api_key"

    def test_image_generation_driver(self):
        config = GriptapeCloudDriversConfig()
        assert isinstance(config.image_generation_driver, GriptapeCloudImageGenerationDriver)
        assert config.image_generation_driver.api_key == "test_api_key"

    def test_conversation_memory_driver(self):
        config = GriptapeCloudDriversConfig()
        assert isinstance(config.conversation_memory_driver, GriptapeCloudConversationMemoryDriver)
        assert config.conversation_memory_driver.api_key == "test_api_key"

    def test_vector_store_driver(self):
        config = GriptapeCloudDriversConfig()
        assert isinstance(config.vector_store_driver, GriptapeCloudVectorStoreDriver)
        assert config.vector_store_driver.api_key == "test_api_key"
        assert config.vector_store_driver.knowledge_base_id == "test-kb-id"

    def test_structure_run_driver(self):
        config = GriptapeCloudDriversConfig()
        assert isinstance(config.structure_run_driver, GriptapeCloudStructureRunDriver)
        assert config.structure_run_driver.api_key == "test_api_key"
        assert config.structure_run_driver.structure_id == "test-structure-id"

    def test_ruleset_driver(self):
        config = GriptapeCloudDriversConfig()
        assert isinstance(config.ruleset_driver, GriptapeCloudRulesetDriver)
        assert config.ruleset_driver.api_key == "test_api_key"

    def test_file_manager_driver(self):
        config = GriptapeCloudDriversConfig()
        assert isinstance(config.file_manager_driver, GriptapeCloudFileManagerDriver)
        assert config.file_manager_driver.api_key == "test_api_key"
        assert config.file_manager_driver.bucket_id == "test-bucket-id"

    def test_event_listener_driver(self):
        config = GriptapeCloudDriversConfig()
        assert isinstance(config.event_listener_driver, GriptapeCloudEventListenerDriver)
        assert config.event_listener_driver.api_key == "test_api_key"
        assert config.event_listener_driver.structure_run_id == "test-run-id"

    def test_observability_driver(self):
        config = GriptapeCloudDriversConfig()
        assert isinstance(config.observability_driver, GriptapeCloudObservabilityDriver)
        assert config.observability_driver.api_key == "test_api_key"
        assert config.observability_driver.structure_run_id == "test-run-id"