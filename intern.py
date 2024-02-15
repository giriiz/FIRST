pip install librosa
import librosa

audio_file_path = 'your_audio_file.wav'

audio_data, sampling_rate = librosa.load(audio_file_path, sr=None)

print(f"The sampling rate of the audio file is: {sampling_rate} Hz")

