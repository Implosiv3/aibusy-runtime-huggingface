from aibusy_runtime_huggingface.service.huggingface_client import DefaultHuggingfaceClient
from aibusy.engine.plugin.abstract import Plugin
from aibusy.engine.builder import EngineBuilder
from aibusy.service.huggingface.abstract import HuggingfaceClient


class HuggingfaceRuntimePlugin(
    Plugin
):
    """
    The Hugginface plugin that will register the
    `DefaultHuggingfaceClient` class for the
    `HuggingfaceClient` type.
    """
    
    def register(
        builder: EngineBuilder
    ):
        builder.services.register(
            HuggingfaceClient,
            DefaultHuggingfaceClient()
        )

        