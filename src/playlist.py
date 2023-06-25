from src.video import Video, PLVideo
import os
from googleapiclient.discovery import build

class PlayList:
    api_key: str = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.__title = self.playlist_info().get('items')[0].get('snippet').get('title')
        self.__url = f"https://www.youtube.com/playlist?list={self.__playlist_id}"
        self.__playlist_videos_id = self.playlist_ids()

    @property
    def playlist_id(self):
        return self.__playlist_id

    @property
    def title(self ):
        return self.__title

    @property
    def url(self):
        return self.__url
    def playlist_info(self):
        playlist_object = self.youtube.playlists().list(id=self.playlist_id, part='snippet,contentDetails',
                                                   maxResults=50).execute()
        return playlist_object

    def playlist_ids(self):
        pl_vid_info = self.youtube.playlistItems().list(playlistId=self.__playlist_id, part='snippet,contentDetails',
                                               maxResults=50,).execute()
        return [item['contentDetails']['videoId'] for item in pl_vid_info['items']]

    def show_best_video(self):
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                  id=','.join(self.__playlist_videos_id)
                                                  ).execute()
        all_likes = [video.get('statistics').get('likeCount') for video in video_response.get('items')]

        index_of_max = all_likes.index(max(all_likes))
        return f'https://youtu.be/{self.__playlist_videos_id[index_of_max]}'






