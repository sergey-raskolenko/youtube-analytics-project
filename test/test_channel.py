import json

from src.channel import Channel
import pytest
import os


@pytest.fixture
def channel():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')

@pytest.fixture
def channel2():
    return Channel('UCwHL6WHUarjGfUM_586me8w')

def test__init__(channel):
    assert isinstance(channel, Channel)
    assert channel.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'
    assert channel.title == 'MoscowPython'
    assert channel.description == 'Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\n\
Присоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)'
    assert channel.url == 'https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A'
    assert int(channel.subscriber_count) >= 26100
    assert int(channel.video_count) >= 687
    assert int(channel.view_count) >= 2323778

def test__repr__(channel):
    assert channel.__repr__() == "Channel('UC-OVMPlMA3-YCIeg4z5z23A')"

def test__str__(channel):
    assert channel.__str__() == f'{channel.title} ({channel.url})'

def test_set_channel_id(channel):
    with pytest.raises(AttributeError):
        channel.channel_id = 'Новое название'

def test_print_info(channel):
    assert channel.print_info() is None

def test_to_json(channel):
    filename = 'moscowpython.json'
    channel.to_json(filename)
    path = os.path.join(filename)
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert len(data) == 7

def test_arithmetic_functions(channel, channel2):
    with pytest.raises(TypeError):
        channel + 1
    with pytest.raises(TypeError):
        channel - 1
    with pytest.raises(TypeError):
        channel > 1
    with pytest.raises(TypeError):
        channel >= 1
    with pytest.raises(TypeError):
        channel < 1
    with pytest.raises(TypeError):
        channel <= 1
    with pytest.raises(TypeError):
        channel == 1
    assert channel + channel2 == 101000
    assert channel - channel2 == -48800
    assert channel2 - channel == 48800
    assert channel < channel2
    assert channel <= channel2
    assert channel2 > channel
    assert channel2 >= channel
    assert (channel == channel2) is False

