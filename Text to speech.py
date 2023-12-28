while True:
    import gtts
    import playsound

    user = input("enter the text: ") # takes the text from the user.
    sound = gtts.gTTS(user, lang="en")

    sound.save("audio.mp3") # Saves the audio in mp3.
    playsound.playsound("audio.mp3") # Plays the audio of the text that was save.