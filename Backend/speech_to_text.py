# import whisper
# model = whisper.load_model("base")
# result = model.transcribe("C:\\Users\\celin\\Downloads\\ea7195ac-828b-429d-8ba5-9bf980e07c32.mp3")
#     # "https://drive.google.com/file/d/1A6d32C0s_oPzZNv2yey1NQRn8I-dc1Yx/view?usp=sharing"
    
# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import os
#audio_file= open("C:\\Users\\celin\\Downloads\\ea7195ac-828b-429d-8ba5-9bf980e07c32.mp3", "rb")
openai.api_key = "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"
audio_file = open("C:\\Users\\celin\\OneDrive\\Documents\\GitHub\\hello\\Backend\\test.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript)


# transcribed_text = result["text"]

# print(transcribed_text)

# with open("transcription.text" "w") as text_file:
#     text_file.write(result["text"])


####################################################################




# from google.cloud import speech

# import os
# from dotenv import load_dotenv

# load_dotenv()

# Google_Key = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# def run_quickstart() -> speech.RecognizeResponse:
#     # Instantiates a client
#     client = speech.SpeechClient()

#     # The name of the audio file to transcribe
#     gcs_uri = "cloud-samples-data/speech/brooklyn_bridge.wav"

#     audio = speech.RecognitionAudio(uri=gcs_uri)

#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=16000,
#         language_code="en-US",
#     )

#     # Detects speech in the audio file
#     response = client.recognize(config=config, audio=audio)

#     for result in response.results:
#         print(f"Transcript: {result.alternatives[0].transcript}")
# run_quickstart()




    
    

# Imports the Google Cloud client library