import youtube_transcript_api

from transformers import pipeline
summarization = pipeline('summarization')


def get_video_transcript(video_id):
    transcript = youtube_transcript_api.YouTubeTranscriptApi.get_transcript(video_id)
    text = ' '.join([t['text'] for t in transcript])
    return text


def summarize_youtube_video(youtube_link):
    video_id = youtube_link.split("v=")[1]

    try:
        full_transcript = get_video_transcript(video_id)

        num_iters = int(len(full_transcript) / 1000)
        summarized_text = []
        for i in range(0, num_iters + 1):
            start = 0
            start = i * 1000
            end = (i + 1) * 1000
            # print("input text \n" + full_transcript[start:end])
            out = summarization(full_transcript[start:end], min_length=5, max_length=20)
            out = out[0]
            out = out['summary_text']
            # print("Summarized text\n"+out)
            summarized_text.append(out)

        # Adjust the number of sentences for the summary as needed
        return summarized_text

    except :
        return "Error: Failed to summarize the YouTube video."



