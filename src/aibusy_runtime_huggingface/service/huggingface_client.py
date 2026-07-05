# TODO: Should this be in 'aibusy' (?)
from aibusy.service.huggingface.abstract import HuggingfaceClient
from huggingface_hub import snapshot_download
from pathlib import Path
from typing import Union


class DefaultHuggingfaceClient(
    HuggingfaceClient
):
    
    async def download_snapshot(
        self,
        *,
        repository: str,
        revision: Union[str, None] = None,
        local_dir: Union[str, None] = None
    ) -> Path:
        path = snapshot_download(
            repo_id = repository,
            revision = revision,
            local_dir = local_dir
        )

        return Path(path)