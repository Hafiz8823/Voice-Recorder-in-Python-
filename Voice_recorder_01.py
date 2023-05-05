# First of all install following pip's in you computer if those are not install already
# pip install scipy
# pip install sounddevice

# Import required modules
import sounddevice
from scipy.io.wavfile import write
# Sample_rate
fs=44100

# Ask the user to enter the recording time:

second=int (input("Enter the Recording time in seconds: "))
print("Recording....\n")
record_voice=sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
sounddevice.wait()
write("MyRecording.wav",fs,record_voice)
print("Recording is done please check the folder to listen the recording")  




