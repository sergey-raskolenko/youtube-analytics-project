import json
import os
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YOUTUBE_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__title = self.channel_info().get("items")[0].get("snippet").get("title")
        self.__description = self.channel_info().get("items")[0].get("snippet").get("description")
        self.__url = f'https://www.youtube.com/channel/{self.channel_id}'
        self.__subscriber_count = int(self.channel_info().get("items")[0].get("statistics").get("subscriberCount"))
        self.__video_count = int(self.channel_info().get("items")[0].get("statistics").get("videoCount"))
        self.__view_count = int(self.channel_info().get("items")[0].get("statistics").get("viewCount"))
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.channel_id}')"

    def __str__(self) -> str:
        return f'{self.title} ({self.url})'

    def __add__(self, other) -> int:
        """Складывает два операнда"""
        if isinstance(other, Channel) is False:
            raise TypeError("second operand must be a Channel")
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other) -> int:
        """Вычитает из первого второй операнд"""
        if isinstance(other, Channel) is False:
            raise TypeError("second operand must be a Channel")
        return self.subscriber_count - other.subscriber_count

    def __lt__(self, other) -> bool:
        """Первый меньше второго операнда"""
        if isinstance(other, Channel) is False:
            raise TypeError("second operand must be a Channel")
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other) -> bool:
        """Первый меньше либо равен второму операнду"""
        if isinstance(other, Channel) is False:
            raise TypeError("second operand must be a Channel")
        return self.subscriber_count <= other.subscriber_count

    def __gt__(self, other) -> bool:
        """Первый больше второго операнда"""
        if isinstance(other, Channel) is False:
            raise TypeError("second operand must be a Channel")
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other) -> bool:
        """Первый больше либо равен второму операнду"""
        if isinstance(other, Channel) is False:
            raise TypeError("second operand must be a Channel")
        return self.subscriber_count >= other.subscriber_count

    def __eq__(self, other) -> bool:
        """Первый больше либо равен второму операнду"""
        if isinstance(other, Channel) is False:
            raise TypeError("second operand must be a Channel")
        return self.subscriber_count == other.subscriber_count

    @property
    def channel_id(self) -> str:
        """Геттер параметра channel_id для объекта Channel"""
        return self.__channel_id

    @property
    def title(self) -> str:
         """Возвращает название канала"""
         return self.__title

    @property
    def description(self) -> str:
        """Возвращает описание канала"""
        return self.__description

    @property
    def url(self) -> str:
        """Возвращает ссылку на канал"""
        return self.__url

    @property
    def subscriber_count(self) -> int:
        """Возвращает количество подписчиков"""
        return self.__subscriber_count

    @property
    def video_count(self) -> int:
        """Возвращает количество видео"""
        return self.__video_count

    @property
    def view_count(self) -> int:
        """Возвращает количество просмотров"""
        return self.__view_count

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
