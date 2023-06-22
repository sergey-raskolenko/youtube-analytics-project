from src.video import Video
import pytest

@pytest.fixture
def video():
    return Video('AWX4JnAnjBE')

def test__init__(video):
    assert isinstance(video, Video)
    assert video.video_id == 'AWX4JnAnjBE'
    assert video.video_title == 'GIL в Python: зачем он нужен и как с этим жить'
    assert video.video_url == 'https://www.youtube.com/watch?v=AWX4JnAnjBE'
    assert video.video_view_count >= 51227
    assert video.video_like_count >= 2176
    assert repr(video) == "Video('AWX4JnAnjBE')"
    assert str(video) == 'GIL в Python: зачем он нужен и как с этим жить'

