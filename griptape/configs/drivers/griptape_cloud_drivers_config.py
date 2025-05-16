import os
import uuid
from typing import Optional

from attrs import define, field
from attrs import Factory

from griptape.configs.drivers import DriversConfig
from griptape.drivers.prompt.griptape_cloud import GriptapeCloudPromptDriver
from griptape.drivers.image_generation.griptape_cloud import GriptapeCloudImageGenerationDriver
from griptape.drivers.memory.conversation.griptape_cloud import GriptapeCloudConversationMemoryDriver
from griptape.drivers.vector.griptape_cloud import GriptapeCloudVectorStoreDriver
from griptape.drivers.structure_run.griptape_cloud import GriptapeCloudStructureRunDriver
from griptape.drivers.ruleset.griptape_cloud import GriptapeCloudRulesetDriver
from griptape.drivers.file_manager.griptape_cloud import GriptapeCloudFileManagerDriver
from griptape.drivers.event_listener.griptape_cloud import GriptapeCloudEventListenerDriver
from griptape.drivers.observability.griptape_cloud import GriptapeCloudObservabilityDriver
from griptape.utils.decorators import lazy_property


@define
class GriptapeCloudDriversConfig(DriversConfig):
    _structure_run_driver: Optional[GriptapeCloudStructureRunDriver] = field(
        default=None, kw_only=True, metadata={"serializable": True}, alias="structure_run_driver"
    )
    _file_manager_driver: Optional[GriptapeCloudFileManagerDriver] = field(
        default=None, kw_only=True, metadata={"serializable": True}, alias="file_manager_driver"
    )
    _event_listener_driver: Optional[GriptapeCloudEventListenerDriver] = field(
        default=None, kw_only=True, metadata={"serializable": True}, alias="event_listener_driver"
    )
    _observability_driver: Optional[GriptapeCloudObservabilityDriver] = field(
        default=None, kw_only=True, metadata={"serializable": True}, alias="observability_driver"
    )
    
    # Default API key for all drivers
    api_key: str = field(
        default=Factory(lambda: os.environ.get("GT_CLOUD_API_KEY", "dummy_key_for_tests")),
        kw_only=True
    )
    
    # Default base URL for all drivers
    base_url: str = field(
        default=Factory(lambda: os.getenv("GT_CLOUD_BASE_URL", "https://cloud.griptape.ai")),
        kw_only=True
    )
    
    # Default structure ID for structure-related drivers
    structure_id: str = field(
        default=Factory(lambda: os.environ.get("GT_CLOUD_STRUCTURE_ID", f"test-structure-{uuid.uuid4()}")),
        kw_only=True
    )
    
    # Default structure run ID for run-related drivers
    structure_run_id: str = field(
        default=Factory(lambda: os.environ.get("GT_CLOUD_STRUCTURE_RUN_ID", f"test-run-{uuid.uuid4()}")),
        kw_only=True
    )
    
    # Default bucket ID for file manager driver
    bucket_id: str = field(
        default=Factory(lambda: os.environ.get("GT_CLOUD_BUCKET_ID", "test-bucket")),
        kw_only=True
    )
    
    # Default knowledge base ID for vector store driver
    knowledge_base_id: str = field(
        default=Factory(lambda: os.environ.get("GT_CLOUD_KNOWLEDGE_BASE_ID", "test-kb")),
        kw_only=True
    )

    @lazy_property()
    def prompt_driver(self) -> GriptapeCloudPromptDriver:
        return GriptapeCloudPromptDriver(api_key=self.api_key, base_url=self.base_url)

    @lazy_property()
    def image_generation_driver(self) -> GriptapeCloudImageGenerationDriver:
        return GriptapeCloudImageGenerationDriver(api_key=self.api_key, base_url=self.base_url)

    @lazy_property()
    def conversation_memory_driver(self) -> GriptapeCloudConversationMemoryDriver:
        return GriptapeCloudConversationMemoryDriver(api_key=self.api_key, base_url=self.base_url)

    @lazy_property()
    def vector_store_driver(self) -> GriptapeCloudVectorStoreDriver:
        return GriptapeCloudVectorStoreDriver(
            api_key=self.api_key, 
            base_url=self.base_url,
            knowledge_base_id=self.knowledge_base_id
        )

    @lazy_property()
    def structure_run_driver(self) -> GriptapeCloudStructureRunDriver:
        return GriptapeCloudStructureRunDriver(
            api_key=self.api_key, 
            base_url=self.base_url,
            structure_id=self.structure_id
        )

    @lazy_property()
    def ruleset_driver(self) -> GriptapeCloudRulesetDriver:
        return GriptapeCloudRulesetDriver(api_key=self.api_key, base_url=self.base_url)

    @lazy_property()
    def file_manager_driver(self) -> GriptapeCloudFileManagerDriver:
        return GriptapeCloudFileManagerDriver(
            api_key=self.api_key, 
            base_url=self.base_url,
            bucket_id=self.bucket_id
        )

    @lazy_property()
    def event_listener_driver(self) -> GriptapeCloudEventListenerDriver:
        return GriptapeCloudEventListenerDriver(
            api_key=self.api_key, 
            base_url=self.base_url,
            structure_run_id=self.structure_run_id
        )

    @lazy_property()
    def observability_driver(self) -> GriptapeCloudObservabilityDriver:
        return GriptapeCloudObservabilityDriver(
            api_key=self.api_key, 
            base_url=self.base_url,
            structure_run_id=self.structure_run_id
        )