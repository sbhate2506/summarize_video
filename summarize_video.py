from youtube.youtube import (
    validate_youtube_url, 
    get_transcript, 
    get_comments
)
from chain.custom_chains import get_summary_chain
from output_parser import Summary

def summarize_video(url:str):
    video_id, title = validate_youtube_url(url)
    transcript = get_transcript(video_id)
    comments = get_comments(video_id)
    
    summary_chain = get_summary_chain()
    summary_and_sentiments: Summary = summary_chain.invoke(
        input={"transcript": transcript, "comments": comments}
    )
    
    return title, summary_and_sentiments

if __name__=="__main__":
    pass