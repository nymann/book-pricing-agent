from book_pricing_agent.api import Api
from book_pricing_agent.core.config import Config
from book_pricing_agent.core.service_container import ServiceContainer

config = Config()
service_container = ServiceContainer(config=config)
api = Api(config=config, service_container=service_container).api
