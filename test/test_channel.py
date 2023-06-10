from src.channel import Channel
import pytest


@pytest.fixture
def channel():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')
def test__init__(channel):
    assert isinstance(channel, Channel)
    assert channel.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'

def test_print_info(channel):
    assert channel.print_info()== None
