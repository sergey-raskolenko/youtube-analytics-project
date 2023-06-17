import json
import os
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YOUTUBE_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__title = self.title
        self.__description = self.description
        self.__url = self.url
        self.__subscriber_count = self.subscriber_count
        self.__video_count = self.video_count
        self.__view_count = self.view_count



    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    @property
    def channel_id(self):
        """Геттер параметра channel_id для объекта Channel"""
        return self.__channel_id

     @property
    def title(self) -> str:
         """Возвращает название канала"""
         return self.channel_info().get("items")[0].get("snippet").get("title")

    @property
    def description(self) -> str:
        """Возвращает описание канала"""
        return self.channel_info().get("items")[0].get("snippet").get("description")

    @property
    def url(self) -> str:
        """Возвращает ссылку на канал"""
        return f'https://www.youtube.com/channel/{self.channel_id}'

    @property
    def subscriber_count(self) -> int:
        """Возвращает количество подписчиков"""
        return int(self.channel_info().get("items")[0].get("statistics").get("subscriberCount"))

    @property
    def video_count(self) -> int:
        """Возвращает количество видео"""
        return int(self.channel_info().get("items")[0].get("statistics").get("videoCount"))

    @property
    def view_count(self) -> int:
        """Возвращает количество просмотров"""
        return int(self.channel_info().get("items")[0].get("statistics").get("viewCount"))

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
            data = {
                'channel_id': self.channel_id,
                'title': self.title,
                'description': self.description,
                'url': self.url,
                'subscriber_count': self.subscriber_count,
                'video_count': self.video_count,
                'view_count': self.view_count
            }
            json.dump(data, f)

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=Channel.api_key)
