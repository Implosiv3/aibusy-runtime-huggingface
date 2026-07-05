# TODO: Should this be in 'aibusy' (?)
from aibusy.service.huggingface.abstract import HuggingfaceClient
from huggingface_hub import snapshot_download
from typing import Union


class DefaultHuggingfaceClient(
    HuggingfaceClient
):
    
    async def download_snapshot(
        self,
        *,
        repository: str,
        revision: Union[str, None] = None,
    ) -> str:

        return snapshot_download(
            repo_id = repository,
            revision = revision,
        )