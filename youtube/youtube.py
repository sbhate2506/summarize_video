from pytube import YouTube, extract
from pytube.exceptions import VideoUnavailable, RegexMatchError
from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build

def validate_youtube_url(url):
    try:
        yt = YouTube(url)
    except VideoUnavailable:
        print('video unavailable')
    except RegexMatchError:
        print('invalid url')
    else:
        video_id=extract.video_id(url)
        return video_id

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    
    output = ''
    for x in transcript:
        sentence = x['text']
        output += f' {sentence} '
    
    return output
    
def get_comments(video_id):
    
    


if __name__ == "__main__"
    pass