import json

from src.channel import Channel
import pytest
import os


@pytest.fixture
def channel():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')
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
