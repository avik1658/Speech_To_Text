import whisper
from transformers import pipeline
import math

# Load the Whisper model
model = whisper.load_model("base.en")  # Use "tiny", "small", "medium", or "large"

# Transcribe an audio file
audio_path = "/home/bs-00594/Downloads/videoTest3.mp4"  # Replace with your actual media file
result = model.transcribe(audio_path)

# Get the transcription text
transcription_text = result["text"]
print("Transcription:\n", transcription_text)

# Initialize the summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to split text into chunks that fit the model's token limit
def split_text(text, max_tokens=500):
    words = text.split(" ")
    chunks = []
    current_chunk = ""

    for word in words:
        # Add the word to the chunk if it doesn't exceed max_tokens
        if len(current_chunk.split(" ")) + len(word.split(" ")) < max_tokens:
            current_chunk += word + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = word + " "

    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

# Split the transcription into manageable chunks
text_chunks = split_text(transcription_text) 

# Summarize each chunk individually
summaries = []
for chunk in text_chunks:
    summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]["summary_text"]
    summaries.append(summary)

# Combine the summaries into one final summary
final_summary = " ".join(summaries)
print("\nFinal Summary:\n", final_summary)

# Load the question generation model
question_generator = pipeline("text2text-generation", model="google/flan-t5-large")
number_of_questions = 10  # Desired number of questions

def split_text(text, max_length=500):
    sentences = text.split(". ")  # Split by sentences
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_length:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

# Split transcription into smaller parts
text_chunks = split_text(transcription_text)

# Determine the number of questions per chunk
questions_per_chunk = math.ceil(number_of_questions / len(text_chunks))

questions = []
for chunk in text_chunks:
    for i in range(questions_per_chunk):
        if len(questions) < number_of_questions:  # Stop when we have enough questions
            prompt = f"Generate a question {i+1} from: {chunk}"
            q = question_generator(prompt, max_length=100, do_sample=True)[0]["generated_text"]
            questions.append(q)

print("\nGenerated Questions:\n","\n".join(questions))
