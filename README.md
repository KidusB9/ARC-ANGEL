# ARC-ANGEL
# ARC-ANGEL API Server

## Overview

ARC-ANGEL is a high-performance, scalable Flask-based API server offering services from object detection to sentiment analysis. The server is designed to be easy to deploy and integrate into any system.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Object Detection
- Sentiment Analysis
- Built with Flask and Python
- Uses TensorFlow, OpenAI, Google Cloud Vision, and Google Cloud Language

## Installation

To get started with ARC-ANGEL, you'll need to install some prerequisites. Use the following commands to install the required Python packages:

```bash
pip install Flask
pip install tensorflow
pip install google-cloud-vision
pip install google-cloud-language

## Or you can install all dependencies at once using the provided requirements.txt:
```bash
pip install -r requirements.txt

## Installation

```bash
git clone https://github.com/yourusername/ARC-ANGEL.git
cd ARC-ANGEL

# Sample Python code to call the Object Detection API
import requests
response = requests.post('http://localhost:5000/api/v1/object-detection', json={"your": "data_here"})


## Important Code Snippets

In addition to the basic setup and API calls, here are some key parts of the code that make ARC-ANGEL work:

### Object Detection Endpoint

The object detection endpoint uses Flask, OpenCV, and Google Vision API. The POST method accepts base64 encoded images, processes them, and returns the detected objects.

```python
@app.route('/object-detection', methods=['POST'])
def object_detection():
    data = request.get_json()
    frame_data = data.get('frameData')
    img_str = frame_data.split(',')[1]
    img_bytes = base64.b64decode(img_str)
    img_arr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image = vision.Image(content=img_bytes)
    response = vision_client.object_localization(image=image)
    objects = response.localized_object_annotations
    return jsonify({'result': [obj.name for obj in objects]})

```python object detection
import cv2

def get_image_from_user():
    video_cap = cv2.VideoCapture(0)
    frames = []
    while True:
        ret, frame = video_cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (300, 300))
        frames.append(frame)
    video_cap.release()

    output = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('output.avi', output, 20.0, (300, 300))
    for frame in frames:
        out.write(frame)
    out.release()

    with open('output.avi', 'rb') as f:
        content = f.read()
    return content

### Speech Transcription and Intent Detection

These two functions are crucial for handling the speech input from the user and detecting the user's intent. They make use of Google's Speech-to-Text API and custom keyword matching to route the request to the appropriate action.

#### Speech Transcription
Here's the function to transcribe speech, either from a microphone or an audio file:

```python
def transcribe_speech(audio_source):
   def transcribe_speech(audio_source):
    if audio_source == 'microphone':
        CHANNELS = 1
        RATE = 16000
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = "audio.wav"

        print("Recording audio...")
        audio_data = sd.rec(int(RATE * RECORD_SECONDS), samplerate=RATE, channels=CHANNELS)
        sd.wait()
        print("Finished recording.")

        with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wavefile:
            wavefile.setnchannels(CHANNELS)
            wavefile.setsampwidth(2)
            wavefile.setframerate(RATE)
            wavefile.writeframes(audio_data.tobytes())

        audio_file_path = WAVE_OUTPUT_FILENAME
    else:
        audio_file_path = audio_source

    with open(audio_file_path, 'rb') as audio_file:
      
        content = audio_file.read()

    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )
    if not transcript:
        return 'Transcription failed.'
    return transcript


Contributing
Contributions are welcome! Please read our contributing guidelines for details.

License
ARC-ANGEL is open-sourced under the MIT License.
