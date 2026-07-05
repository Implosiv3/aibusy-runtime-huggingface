"""
A simple test to verify that pytes is working and
the tests are being detected.
"""
import pytest


@pytest.mark.mandatory
def test_instances():
    from aibusy_runtime_huggingface.service.huggingface_client import DefaultHuggingfaceClient

    assert DefaultHuggingfaceClient() is not None
