import json
import os
from googleapiclient.discovery import build

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
        """Геттер параметра channel_id для объекта Channel"""
        return self.__channel_id


    def channel_info(self):
        """Возвращает список словарей с информацией о канале"""
        youtube = Channel.get_service()
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel_info(), indent=2, ensure_ascii=False))

    def to_json(self, filename):
        """Записывает параметры объекта класса в json файл """
        with open(filename, 'w', encoding='utf-8') as f:
            data = [self.channel_id, self.title, self.description, self.url, self.subscriber_count,
                    self.video_count, self.view_count]
            json.dump(data, f)


    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=Channel.api_key)
