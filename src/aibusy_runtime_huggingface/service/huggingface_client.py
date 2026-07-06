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
        revision: Union[str, None],
        local_dir: str,
        allow_patterns: Union[list[str], None] = None,
        ignore_patterns: Union[list[str], None] = None,
    ) -> Path:
        path = snapshot_download(
            repo_id = repository,
            revision = revision,
            local_dir = local_dir,
            allow_patterns = allow_patterns,
            ignore_patterns = ignore_patterns
        )

        return Path(path)