import os
from dotenv import load_dotenv
from pytube import YouTube, extract
from pytube.exceptions import VideoUnavailable, RegexMatchError
from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build

load_dotenv()

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
    # Disable OAuthlib's HTTPS verification when running locally.
    # DO NOT leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv("YOUTUBE_API_KEY")
    
    yt = build(api_service_name, api_version, developerKey = DEVELOPER_KEY)
    
    video_response = yt.commentThreads().list(
        part = 'snippet,replies',
        videoId = video_id
    ).execute()
    
    comments = []
    while video_response:
        for item in video_response["items"]:
            comments.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])
            
        if 'nextPageToken' in video_response:
            video_response = yt.commentThreads().list(
                part = 'snippet,replies',
                videoId = video_id,
                pageToken = video_response['nextPageToken']            
            ).execute()
        else:
            break
            
    return comments
    


if __name__ == "__main__":
    pass
    #video_id = validate_youtube_url("https://www.youtube.com/watch?v=kBNPVcRYTyw")
    #print(f'transcript : {get_transcript(video_id)}')
    #print(f'comments : {get_comments(video_id)}')