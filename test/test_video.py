from src.video import Video, PLVideo
import pytest

@pytest.fixture
def video():
    return Video('AWX4JnAnjBE')

@pytest.fixture
def pl_video():
    return PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')

def test__init__for_video(video):
    assert isinstance(video, Video)
    assert video.id == 'AWX4JnAnjBE'
    assert video.title == 'GIL в Python: зачем он нужен и как с этим жить'
    assert video.url == 'https://www.youtube.com/watch?v=AWX4JnAnjBE'
    assert video.view_count >= 51227
    assert video.like_count >= 2176
    assert repr(video) == "Video('AWX4JnAnjBE')"
    assert str(video) == 'GIL в Python: зачем он нужен и как с этим жить'

def test__init_for_pl_video(pl_video):
    assert isinstance(pl_video, PLVideo)
    assert pl_video.id == '4fObz_qw9u4'
    assert pl_video.title == 'MoscowPython Meetup 78 - вступление'
    assert pl_video.url == 'https://www.youtube.com/watch?v=4fObz_qw9u4'
    assert pl_video.view_count >= 582
    assert pl_video.like_count >= 9
    assert pl_video.playlist_id == 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC'
    assert repr(pl_video) == "PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')"
    assert str(pl_video) == 'MoscowPython Meetup 78 - вступление'



