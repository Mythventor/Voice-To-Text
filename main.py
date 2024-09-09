import speech_recognition as sr
from pydub import AudioSegment
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# Function to perform the conversion and recognition
def process_audio(file_path, language_code):
    try:
        # Convert audio to WAV if it is not already in WAV format
        if not file_path.endswith('.wav'):
            wav_path = 'converted_voice.wav'
            audio = AudioSegment.from_file(file_path)
            audio.export(wav_path, format='wav')
        else:
            wav_path = file_path

        # Initialize recognizer
        recognizer = sr.Recognizer()

        # Load the converted WAV file into the recognizer
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)

        # Attempt to recognize speech in the audio file
        try:
            text_output = recognizer.recognize_google(audio_data, language=language_code)
        except sr.UnknownValueError:
            text_output = "I'm sorry, but I couldn't understand the audio."
        except sr.RequestError:
            text_output = "I'm sorry, there was an issue with the recognition service."

        # Display the recognized text in the text box
        result_text.delete(1.0, tk.END)  # Clear previous text
        result_text.insert(tk.END, text_output)  # Insert new text
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to handle the file selection and language choice
def start_recognition():
    file_path = filedialog.askopenfilename(
        title="Select an audio file",
        filetypes=[("Audio Files", "*.m4a *.wav *.aiff *.flac *.mp3")]
    )

    if file_path:
        language = language_var.get()
        language_code = languages.get(language)
        if language_code:
            process_audio(file_path, language_code)
        else:
            messagebox.showerror("Error", "Invalid language selection")
    else:
        messagebox.showwarning("Warning", "No file selected")

# Supported languages
languages = {
    "English (US)": "en-US",
    "English (UK)": "en-GB",
    "Cantonese (Traditional)": "yue-Hant",
    "Mandarin (Simplified)": "zh-CN",
    "Vietnamese": "vi-VN",
    "Spanish": "es-ES",
    "French": "fr-FR",
    "German": "de-DE",
    "Japanese": "ja-JP",
    "Korean": "ko-KR",
    
}

# Create the root window
root = tk.Tk()
root.title("Speech Recognition")

# Create and place widgets
tk.Label(root, text="Language:").grid(row=0, column=0, padx=10, pady=10)

language_var = tk.StringVar(value="English (US)")
language_menu = tk.OptionMenu(root, language_var, *languages.keys())
language_menu.grid(row=0, column=1, padx=10, pady=10)

select_button = tk.Button(root, text="Select Audio File", command=start_recognition)
select_button.grid(row=1, columnspan=2, pady=20)

# Create a scrolled text box to display recognized text
result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
result_text.grid(row=2, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()