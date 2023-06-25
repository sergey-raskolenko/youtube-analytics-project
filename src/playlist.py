import datetime
import isodate
import os
from googleapiclient.discovery import build

class PlayList:
    api_key: str = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, playlist_id):
        """
        Инициализатор объекта класса Playlist
        """
        self.__playlist_id = playlist_id
        self.__title = self.playlist_info().get('items')[0].get('snippet').get('title')
        self.__url = f"https://www.youtube.com/playlist?list={self.__playlist_id}"
        self.__playlist_videos_id = self.playlist_ids()

    @property
    def playlist_id(self):
        """
        Геттер id плэйлиста
        """
        return self.__playlist_id

    @property
    def title(self ):
        """
        Геттер названия плэйлиста
        """
        return self.__title

    @property
    def url(self):
        """
        Геттер адреса плэйлиста
        """
        return self.__url
    def playlist_info(self):
        """
        Возвращает информация о плейлисте
        """
        playlist_object = self.youtube.playlists().list(id=self.playlist_id, part='snippet,contentDetails',
                                                   maxResults=50).execute()
        return playlist_object

    def playlist_ids(self):
        """
        Возвращает список с id всех видео в плейлисте
        """
        pl_vid_info = self.youtube.playlistItems().list(playlistId=self.__playlist_id, part='snippet,contentDetails',
                                               maxResults=50,).execute()
        return [item['contentDetails']['videoId'] for item in pl_vid_info['items']]

    def video_response(self):
        """
        Возвращает информацию о всех видео в плейлисте
        """
        return self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                  id=','.join(self.__playlist_videos_id)
                                                  ).execute()

    def show_best_video(self):
        """
        Возвращает ссылку на видео из плейлиста с наибольшим количеством лайков
        """
        video_response = self.video_response()
        all_likes = [video.get('statistics').get('likeCount') for video in video_response.get('items')]

        index_of_max = all_likes.index(max(all_likes))
        return f'https://youtu.be/{self.__playlist_videos_id[index_of_max]}'

    @property
    def total_duration(self):
        """
        Возвращает суммарную длительность всех видео в плейлисте
        """
        seconds_sum = 0
        for i in self.video_response().get('items'):
            seconds_sum += isodate.parse_duration(i['contentDetails']['duration']).total_seconds()
        return datetime.timedelta(seconds=int(seconds_sum))
