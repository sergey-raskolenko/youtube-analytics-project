import json
import os
from googleapiclient.discovery import build
class Video:
    api_key: str = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, id_video):
        """
        Инициализатор объекта класса Video с информацией о видео
        """
        self.__id = id_video
        self.__title = None
        self.__url = None
        self.__view_count = None
        self.__like_count = None
        try:
            video_info = self.video_info().get('items')[0]
            self.__title = video_info.get('snippet').get('title')
            self.__url = f'https://www.youtube.com/watch?v={self.id}'
            self.__view_count = int(video_info.get('statistics').get('viewCount'))
            self.__like_count = int(video_info.get('statistics').get('likeCount'))
        except Exception:
            print(f"Exception: Wrong ID of video")



    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.id}')"

    def __str__(self) -> str:
        return f'{self.title}'

    @property
    def id(self):
        return self.__id
    @property
    def title(self):
        return self.__title
    @property
    def url(self):
        return self.__url
    @property
    def view_count(self):
        return self.__view_count
    @property
    def like_count(self):
        return self.__like_count

    def video_info(self):
        """Возвращает список словарей с информацией о видео"""
        video_object = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                  id=self.id).execute()
        return video_object

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.video_info(), indent=2, ensure_ascii=False))

class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.__playlist_id = playlist_id

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.id}', '{self.playlist_id}')"

    def __str__(self) -> str:
        return f'{self.title}'

    def playlist_video_info(self):
        """Возвращает список словарей с информацией о плэйлисте"""
        playlist_object = self.youtube.playlistItems().list(part="snippet",
                                                       playlistId=self.playlist_id, videoId=self.id
                                                       ).execute()
        return playlist_object

    @property
    def playlist_id(self):
        return self.__playlist_id
