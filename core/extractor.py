import json

from core.contents.chatgpt import completion

response_obj='''[
  {
    "start_time": 97.19, 
    "end_time": 127.43,
    "description": "Put here a simple description of the context in max 10 words"
    "duration":36 #Length in seconds
  },
]'''

def analyze_transcript(transcript: str):
    transcript: list = transcript.split("\n")
    chunks = []
    contents = []

    print(f"\nChunking the transcript...")

    # chunk the transcript in multiple parts of a max of 3000 characters
    content = ""
    while len(transcript) > 0:
        while len(content) < 3000:
            content += transcript.pop(0)
        chunks.append((content, completion(content)))

    print(chunks)

    for (transcript_data, interesting_segment) in chunks:
        try:
            contents_chunk = json.loads(interesting_segment["content"])
            contents += contents_chunk
        except Exception as e:
            print(f"Exception: {e}")
            continue

    return contents