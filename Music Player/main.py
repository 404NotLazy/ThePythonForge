import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil


class MusicPlayer:
    default_music_path = "/home/" + os.getlogin() + "/Music"

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Music Player")
        self.window.geometry("500x500")

        self.listBox = tk.Listbox(background="white", foreground="cyan", selectbackground="blue", height=15, width=30)
        self.listBox.pack()

        for i in os.listdir(self.default_music_path):
            if i.endswith(".mp3"):
                self.listBox.insert(tk.END, i)

        self.frame = tk.Frame(self.window)
        self.frame.pack()

        playButton = tk.Button(self.frame, text="Play", command=self.playMusic)
        playButton.pack(side="left", anchor="center")

        pauseButton = tk.Button(self.frame, text="Pause", command=self.pauseMusic)
        pauseButton.pack(side="left", anchor="center")

        self.window.mainloop()

    def loadMusic(self):
        self.path = filedialog.askdirectory()

    def playMusic(self):
        pass

    def pauseMusic(self):
        pass

    def stopMusic(self):
        pass


def main():
    app = MusicPlayer()


if __name__ == "__main__":
    main()
