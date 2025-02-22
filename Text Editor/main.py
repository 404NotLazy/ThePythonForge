from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class TextEditor:
    def __init__(self):
        self.window = Tk()

        self.window.title("Text Editor")
        self.window.geometry("500x500")

        self.menuBar = Menu(self.window)

        self.window.config(menu=self.menuBar)

        self.fileMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)

        self.fileMenu.add_command(label="Open", command=self.openFile)
        self.fileMenu.add_command(label="Save", command=self.saveFile)
        self.fileMenu.add_command(label="New", command=self.newFile)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Close", command=self.closeFile)

        self.editMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Edit", menu=self.editMenu)

        self.textBox = Text(self.window, background="white", foreground="black")
        self.textBox.pack(fill=BOTH, expand=True)

        self.textBox.bind("<Control-s>", lambda event: self.saveFile())
        self.textBox.bind("<Control-o>", lambda event: self.openFile())

        self.window.mainloop()

    def openFile(self):
        try:
            self.filePath = filedialog.askopenfilename(
                defaultextension=".txt",
                filetypes=(
                    ("Text Files", ".txt"),
                    ("Python Files", ".py"),
                    ("All types", "*.*"),
                )
            )
            if self.filePath:
                self.textBox.delete("1.0", END)
                with open(self.filePath, "r") as f:
                    self.lines = f.readlines()
                    for line in self.lines:
                        self.textBox.insert("end", line)
        except Exception as e:
            messagebox.showerror("Error", "Error opening file!")

    def saveFile(self):
        try:
            self.filePath = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=(
                    ("Text Files", ".txt"),
                    ("Python Files", ".py"),
                    ("All types", "*.*"),
                ),
            )
            if self.filePath:
                with open(self.filePath, "w") as f:
                    f.write(self.textBox.get("1.0", END))
        except Exception as e:
            messagebox.showerror("Error", "Error saving file!")

    def newFile(self):
        try:
            self.textBox.delete("1.0", END)
        except Exception as e:
            messagebox.showerror("Error", "Error opening new file!")

    def closeFile(self):
        try:
            self.window.quit()
        except Exception as e:
            messagebox.showerror("Error", "Something gone wrong")

def main():
    app = TextEditor()


if __name__ == "__main__":
    main()
