import whisper

# Load the Whisper model
model = whisper.load_model("base")  # You can use "tiny", "small", "medium", or "large" models

# Transcribe an audio file
audio_path = "/home/bs-00594/Downloads/audio.wav"  # Replace with your actual audio file
result = model.transcribe(audio_path)

# Print the transcribed text
print("Transcription:\n", result["text"])
