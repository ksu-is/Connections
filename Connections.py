import random
import tkinter as tk
from tkinter import messagebox

class ConnectionsGame:#created a word list with 16 words and assigned them a difficulty level.
    def __init__(self):
        self.categories={
            "Embodiment":{"words":["Ideal","Example","Model","Symbol"],"difficulty":1},
            "Related to Trains":{"words":["Car","Conductor","Station","Track"],"difficulty":2},
            "Starting with the same sound":{"words":["Cymbal","Scimitar","Simmer","Symphony"],"difficulty":3},
            "Ear...":{"words":["Drum","Mark","Wax","Wig"],"difficulty":4}
        }
        #Assigning each difficulty with a certain color
        self.difficulty_colors={
            1:"yellow",
            2:"green",
            3:"blue",
            4:"purple"
        }
        #Creates the tinker window connections and creates a window that someone can interact with until they close the UI. 
        self.root=tk.Tk()
        self.root.title("Connections")#Add Title Connections to the Top

        #Makes the game not auto start.
        self.game_started=False
        self.selected_buttons=[]
        self.correct_categories=set()
        self.create_start_button()
        self.game_interface=None
        self.root.mainloop()

    #Creates a start button and a restart button
    def create_start_button(self):
        if not self.game_started:
            start_button=tk.Button(self.root,text="Start",command=self.start_game)
            start_button.pack()
        else:
            restart_button=tk.Button(self.root,text="Restart",command=self.restart_game)
            restart_button.pack()

    # Adds instructions on how to play the game. 
    def create_instructions_label(self):
        instructions=(
            "Find groups of four items that share something in common.\n\n"
            "Select up to four items by clicking on them, then tap 'Submit' to check if your guess is correct.\n"
            "Find the groups without making 4 mistakes!\n\n"
            "Category Examples:\n"
            "FISH: Bass, Flounder, Salmon, Trout\n"
            "FIRE ___: Ant, Drill, Island, Opal\n\n"
            "Categories will always be more specific than '5-LETTER-WORDS,' 'NAMES' or 'VERBS.'\n"
            "Each puzzle has exactly one solution. Watch out for words that seem to belong to multiple categories!\n\n"
            "Each group is assigned a color, which will be revealed as you solve:\n"
            "Easy: Yellow\n"
            "Moderate: Green\n"
            "Hard: Blue\n"
            "Difficult: Purple"
        )
        instructions_label=tk.Label(self.game_interface,text=instructions,wraplength=400,justify=tk.LEFT)
        instructions_label.pack()

    #Creates a submit button
    def create_submit_button(self):
        submit_button=tk.Button(self.game_interface,text="Submit",command=self.submit_guess)
        submit_button.pack(side=tk.LEFT,padx=5,pady=5)
        
        restart_button=tk.Button(self.game_interface,text="Restart",command=self.restart_game)
        restart_button.pack(side=tk.LEFT,padx=5,pady=5)

    #Creates a lives counter and tracks them
    def create_lives_display(self):
        self.lives=3
        self.lives_label=tk.Label(self.game_interface,text=f"Lives: {self.lives}")
        self.lives_label.pack()

    #Defines all parts of the game when you start it. 
    def start_game(self):
        if not self.game_started:
            self.game_started=True
            self.game_interface=tk.Toplevel(self.root)
            self.game_interface.title("Connections Game")
            self.create_instructions_label()
            self.create_buttons()
            self.create_submit_button()
            self.create_lives_display()
            self.root.focus()

    def restart_game(self):
        if self.game_interface and self.game_interface.winfo_exists():
            self.game_interface.destroy()
        self.game_started=False
        self.create_start_button()

    def submit_guess(self):
        # Check if all selected buttons belong to the same category
        categories=[self.get_category(button) for button in self.selected_buttons]
        if len(set(categories))==1:
            category=categories[0]
            self.correct_categories.add(category)
            self.disable_category_buttons(category)
            messagebox.showinfo("Correct!")
        else:
            messagebox.showinfo("Incorrect, guess again.")
            #Removes a life everytime the player guesses a wrong grouping
            self.lives-=1
            self.lives_label.config(text=f"Lives: {self.lives}")
            if self.lives==0:
                messagebox.showinfo("Game over.")
                self.restart_game()
        self.clear_selection()

    #Creates buttons and creates space between them. Pack will allow me to create the grid.
    def create_buttons(self):
        frame=tk.Frame(self.game_interface)
        frame.pack()

        all_words=[word for data in self.categories.values() for word in data["words"]]
        button_dict={}

        for i,word in enumerate(all_words):
            category=list(self.categories.keys())[i//4]
            data=self.categories[category]
            difficulty=data["difficulty"]
            color=self.difficulty_colors.get(difficulty,"white")

            button=tk.Button(frame,text=word,bg="white")
            button.grid(row=i//4,column=i%4,padx=5,pady=5)
            button.bind("<Button-1>",lambda event,word=word,button=button:self.toggle_button(event,word,button))
            button_dict[button]=category
        
        self.game_interface.buttons=button_dict

    #Makes the button you toggle red and if you uncheck it white. 
    def toggle_button(self,event,word,button):
        if button not in self.selected_buttons:
            if len(self.selected_buttons)<4:
                self.selected_buttons.append(button)
                button.config(bg="red")
        else:
            self.selected_buttons.remove(button)
            button.config(bg="white")

    def get_category(self,button):
        return self.game_interface.buttons[button]

    def clear_selection(self):
        for button in self.selected_buttons:
            button.config(bg="white")
        self.selected_buttons.clear()

    def disable_category_buttons(self,category):
        for button,cat in self.game_interface.buttons.items():
            if cat==category:
                button.config(state="disabled")

game=ConnectionsGame()
