import random
import tkinter as tk

WORD_LIST = ["python", "tkinter", "hangman", "gui"]

class Hangman:
    def __init__(self):
        self.word = random.choice(WORD_LIST)
        self.missed_letters = []
        self.correct_letters = []
        
        self.window = tk.Tk()
        self.window.title("Hangman")
        
        self.canvas = tk.Canvas(self.window, width=400, height=400)
        self.canvas.pack()
        
        self.label = tk.Label(self.window, text="Guess the word!")
        self.label.pack()
        
        self.entry = tk.Entry(self.window)
        self.entry.pack()
        self.entry.bind("<Return>", self.guess_letter)
        
        self.draw_frame()
        
    def draw_frame(self):
        self.canvas.delete("all")
        self.canvas.create_text(200, 150, text=self.get_display_word(), font=("Helvetica", 30))
        
        if len(self.missed_letters) > 0:
            self.canvas.create_text(150, 50, text="Misses: " + " ".join(self.missed_letters))
            
        self.window.after(1000, self.draw_frame)
        
    def get_display_word(self):
        display = []
        for letter in self.word:
            if letter in self.correct_letters:
                display.append(letter)
            else:
                display.append("_")
        return " ".join(display)
    
    def guess_letter(self, event):
        guess = event.widget.get()
        if guess in self.missed_letters or guess in self.correct_letters:
            return
        
        if guess in self.word:
            self.correct_letters.append(guess)
        else:
            self.missed_letters.append(guess)
            
        event.widget.delete(0, tk.END)
        
game = Hangman()
game.window.mainloop()