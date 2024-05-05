from pygame import mixer

class Audio:
    def __init__ (self):
        mixer.init()
        
    def correct(self):
        mixer.music.load("./assets/audios/audios_correct.mp3")  # Load the audio file
        mixer.music.play()  # Play the audio
        
    def wrong(self):
        mixer.music.load("./assets/audios/audios_wrong.mp3")  # Load the audio file
        mixer.music.play()  # Play the audio
        
    def win(self):
        mixer.music.load("./assets/audios/audios_win.mp3")  # Load the audio file
        mixer.music.play()  # Play the audio

    def lose(self):
        mixer.music.load("./assets/audios/audios_lose.mp3")  # Load the audio file
        mixer.music.play()  # Play the audio
        
    def click(self):
        mixer.music.load("./assets/audios/button_click.mp3")  # Load the audio file
        mixer.music.play()  # Play the audio
        
    def skill(self, character: str, skill_number: str):
        mixer.music.load(f"./assets/audios/{character}_skill_{skill_number}_audio.mp3")  # Load the audio file
        mixer.music.play()  # Play the audio
        
play_audio = Audio()