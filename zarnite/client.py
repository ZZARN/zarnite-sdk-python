import json
from typing import Optional, Any
from zarnite.configuration import Configuration
from zarnite.api_client import ApiClient
from zarnite.exceptions import ApiException

# Import generated APIs
from zarnite.api.agents_api import AgentsApi
from zarnite.api.behaviors_api import BehaviorsApi
from zarnite.api.learners_api import LearnersApi
from zarnite.api.knowledge_api import KnowledgeApi
from zarnite.api.memory_api import MemoryApi
from zarnite.api.usage_billing_api import UsageBillingApi
from zarnite.api.api_keys_api import APIKeysApi
from zarnite.api.deployments_api import DeploymentsApi
from zarnite.api.playground_api import PlaygroundApi
from zarnite.api.analytics_api import AnalyticsApi
from zarnite.api.dashboard_api import DashboardApi
from zarnite.api.routing_api import RoutingApi
from zarnite.api.voice_runtime_api import VoiceRuntimeApi

class ZarniteError(Exception):
    """Custom Exception raised by the Zarnite Client."""
    def __init__(self, message: str, status: Optional[int] = None, code: Optional[str] = None, data: Optional[Any] = None) -> None:
        super().__init__(message)
        self.message = message
        self.status = status
        self.code = code
        self.data = data

def _wrap_api_call(api_method):
    """Decorator to catch internal ApiExceptions and raise clean ZarniteError exception (Task 3.2)."""
    def wrapper(*args, **kwargs):
        try:
            return api_method(*args, **kwargs)
        except ApiException as exc:
            status = exc.status
            message = exc.reason or "Zarnite API request failed."
            code = "API_ERROR"
            data = None
            
            # Attempt to parse detailed JSON validation error message
            if exc.body:
                try:
                    data = json.loads(exc.body)
                    if isinstance(data, dict):
                        if "message" in data:
                            message = data["message"]
                        elif "detail" in data:
                            detail = data["detail"]
                            message = detail if isinstance(detail, str) else json.dumps(detail)
                        if "code" in data:
                            code = data["code"]
                except Exception:
                    pass
            raise ZarniteError(message, status, code, data) from exc
    return wrapper

class ZarniteApiWrapper:
    """Proxy class to dynamically wrap all API calls with the clean error handler."""
    def __init__(self, api_instance: Any) -> None:
        self._api_instance = api_instance

    def __getattr__(self, name: str) -> Any:
        attr = getattr(self._api_instance, name)
        if callable(attr) and not name.startswith("_"):
            return _wrap_api_call(attr)
        return attr

class Zarnite:
    """High-level premium Python client SDK wrapper for the Zarnite Platform APIs (Task 3.1)."""
    def __init__(self, api_key: str, base_path: Optional[str] = None) -> None:
        if not api_key:
            raise ZarniteError("API Key is required to initialize the Zarnite Client.")

        self.configuration = Configuration()
        self.configuration.access_token = api_key
        
        if base_path:
            self.configuration.host = base_path
        else:
            self.configuration.host = "https://api.zarnite.com"

        self.api_client = ApiClient(configuration=self.configuration)

        # Initialize and wrap generated sub-service APIs with clean error interception (Task 3.1, 3.2)
        self.agents = ZarniteApiWrapper(AgentsApi(self.api_client))
        self.behaviors = ZarniteApiWrapper(BehaviorsApi(self.api_client))
        self.learners = ZarniteApiWrapper(LearnersApi(self.api_client))
        self.knowledge = ZarniteApiWrapper(KnowledgeApi(self.api_client))
        self.memory = ZarniteApiWrapper(MemoryApi(self.api_client))
        self.usage = ZarniteApiWrapper(UsageBillingApi(self.api_client))
        self.api_keys = ZarniteApiWrapper(APIKeysApi(self.api_client))
        self.deployments = ZarniteApiWrapper(DeploymentsApi(self.api_client))
        self.playground = ZarniteApiWrapper(PlaygroundApi(self.api_client))
        self.analytics = ZarniteApiWrapper(AnalyticsApi(self.api_client))
        self.dashboard = ZarniteApiWrapper(DashboardApi(self.api_client))
        self.routing = ZarniteApiWrapper(RoutingApi(self.api_client))
        self.voice_runtime = ZarniteApiWrapper(VoiceRuntimeApi(self.api_client))
