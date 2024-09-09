# Speech Recognition App

## Description
This is a speech recognition application using Python. It allows users to select an audio file, choose a language for speech recognition, and displays the recognized text in a user-friendly interface.

## Features
- Supports multiple audio file formats (`.m4a`, `.wav`, `.aiff`, `.flac`, `.mp3`).
- Recognizes speech in various languages including English, Mandarin, Spanish, French, German, Japanese, Korean, and Vietnamese.
- Displays the recognized text within a GUI interface.

## Requirements
- Python 3.10 or higher
- `ffmpeg` for audio format conversion (ONLY if you would want to use additional audio format other than '.wav')

## Installation

### 1. Clone the Repository
```
git clone https://github.com/Mythventor/Voice-To-Text.git
cd Voice-To-Text
```
### 2. Install Dependencies
Use pip to install the required libraries:
```
pip install SpeechRecognition pydub
```

### 3. Install ffmpeg (OPTIONAL)
If you would want to support other audio format other than '.wav'
Make sure `ffmpeg` is installed and accessible in your system's PATH. You can download `ffmpeg` from [ffmpeg.org]

### 4. Run the Application
```
python main.py
```




