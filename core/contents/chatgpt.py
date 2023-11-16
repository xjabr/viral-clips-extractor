from openai import OpenAI

from core.config import OPENAI_TOKEN

client = OpenAI(api_key=OPENAI_TOKEN)

response_obj='''[
  {
    "start_time": 97.19, 
    "end_time": 127.43,
    "description": "Put here a simple description of the context in max 10 words"
    "duration":36 #Length in seconds
  },
]'''

def completion(transcript):
    prompt = f"This is a transcript of a video. Please identify the most interesing sections from the whole, make sure that the duration is more than 2 minutes (it MUST to be more than 120 seconds), Make Sure you provide extremely accurate timestamps and respond only in this JSON format {response_obj}  \n Here is the Transcription:\n{transcript}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "system", "content": "Viral Context Extractor bot is a Video Maker with a lot of experience in this sector and help you by a transcript of a video return a JSON Array object with the informations of the most important parts, funniest and viral for social."},
          {"role": "user", "content": "Transcript of the video..."},
          {"role": "assistant", "content": response_obj},
          {"role": "user", "content": prompt}
        ],
        n=1,
        stop=None
    )

    print(response)
    print(response.choices)
    print(response.choices[0])

    return response.choices[0].message.content