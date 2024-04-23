import random
import tkinter as tk
from tkinter import messagebox

class ConnectionsGame: #created a word list with 16 words and assigned them a difficulty level. 
    def __init__(self, word_list):
        self.list=word_list
        self.categories={
            "Embodiment":{"words":["Ideal", "Example", "Model", "Symbol"], "difficulty":1},
            "Related to Trains":{"words":["Car", "Conductor", "Station", "Track"], "difficulty":2},
            "Starting with the same sound":{"words":["Cymbal", "Scimitar", "Simmer", "Symphony"], "difficulty":3},
            "Ear...":{"words":["Drum", "Mark", "Wax", "Wig"], "difficulty":4}
        }
        #Assigning each difficulty with a certain color
        self.difficulty_colors = {
            1: "yellow",
            2: "green",
            3: "blue",
            4: "purple"
        }
        #Creates the tinker window connections and creates a window that someone can interact with until they close the UI. 
        self.root = tk.Tk()
        self.root.title("Connections")
        self.create_buttons()
        self.root.mainloop()
