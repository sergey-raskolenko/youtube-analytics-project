import json
import os
from googleapiclient.discovery import build
# import isodate

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YOUTUBE_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.title = self.channel_info()["items"][0]["snippet"]["title"]
        self.description = self.channel_info()["items"][0]["snippet"]["description"]
        self.url = f'https://www.youtube.com/channel/{self.channel_id}'
        self.subscriber_count = self.channel_info()["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel_info()["items"][0]["statistics"]["videoCount"]
        self.view_count = self.channel_info()["items"][0]["statistics"]["viewCount"]

    @property
    def channel_id(self):
        return self.__channel_id

    def channel_info(self):
        youtube = build('youtube', 'v3', developerKey=Channel.api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel_info(), indent=2, ensure_ascii=False))
