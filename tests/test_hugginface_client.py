"""
A simple test to verify that pytes is working and
the tests are being detected.
"""
import pytest


@pytest.mark.mandatory
@pytest.mark.asyncio
async def test_download_repo():
    from aibusy_runtime_huggingface.service.huggingface_client import DefaultHuggingfaceClient
    from pathlib import Path
    import shutil

    hugginface_client = DefaultHuggingfaceClient()

    assert hugginface_client is not None

    local_dir = 'test_files/test-repo'

    await hugginface_client.download_snapshot(
        repository = 'huggingface/test-model-repo',
        revision = 'main',
        local_dir = local_dir
    )

    assert Path(local_dir).exists()
    shutil.rmtree(local_dir)
    assert not Path(local_dir).exists()