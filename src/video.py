import json
import os
from googleapiclient.discovery import build
class Video:
    api_key: str = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, id_video):
        self.__video_id = id_video
        self.__video_title = self.video_info().get('items')[0].get('snippet').get('title')
        self.__video_url =f'https://www.youtube.com/watch?v={self.video_id}'
        self.__video_view_count = int(self.video_info().get('items')[0].get('statistics').get('viewCount'))
        self.__video_like_count = int(self.video_info().get('items')[0].get('statistics').get('likeCount'))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.video_id}')"

    def __str__(self) -> str:
        return f'{self.video_title}'

    @property
    def video_id(self):
        return self.__video_id
    @property
    def video_title(self):
        return self.__video_title
    @property
    def video_url(self):
        return self.__video_url
    @property
    def video_view_count(self):
        return self.__video_view_count
    @property
    def video_like_count(self):
        return self.__video_like_count

    def video_info(self):
        """Возвращает список словарей с информацией о видео"""
        video_object = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                  id=self.video_id).execute()
        return video_object

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.video_info(), indent=2, ensure_ascii=False))

class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.__playlist_id = playlist_id

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.video_id}', '{self.playlist_id}')"

    def __str__(self) -> str:
        return f'{self.video_title}'

    def playlist_video_info(self):
        """Возвращает список словарей с информацией о плэйлисте"""
        playlist_object = self.youtube.playlistItems().list(part="snippet",
                                                       playlistId=self.playlist_id, videoId=self.video_id
                                                       ).execute()
        return playlist_object

    @property
    def playlist_id(self):
        return self.__playlist_id
