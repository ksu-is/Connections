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
