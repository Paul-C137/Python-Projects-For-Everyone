from pydub import AudioSegment
from pydub.playback import play

# Replace 'sound_file.mp3' with the path to your sound file
sound_file = 'sound_file.mp3'

# Load the sound file
sound = AudioSegment.from_file(sound_file)

# Play the sound
play(sound)
