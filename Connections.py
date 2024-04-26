import random
import tkinter as tk
from tkinter import messagebox

class ConnectionsGame:#created a word list with 16 words and assigned them a difficulty level.
    def __init__(self, word_list):
        self.list=word_list
        self.categories={
            "Embodiment":{"words":["Ideal","Example","Model","Symbol"],"difficulty":1},
            "Related to Trains":{"words":["Car","Conductor","Station","Track"],"difficulty":2},
            "Starting with the same sound":{"words":["Cymbal","Scimitar","Simmer","Symphony"],"difficulty":3},
            "Ear...":{"words":["Drum","Mark","Wax","Wig"],"difficulty":4}
        }
        #Assigning each difficulty with a certain color
        self.difficulty={
            1:"yellow",
            2:"green",
            3:"blue",
            4:"purple"
        }
        #Creates the tinker window connections and creates a window that someone can interact with until they close the UI.
        #Also establishes alot of things the game needs such as lives, round count, selected words etc. 
        self.lives=3
        self.round=0
        self.selected_words=[]
        self.root=tk.Tk()
        self.root.title("Connections Game") #Add Title Connections to the Top
        self.instructions=tk.Label(self.root,text="",wraplength=400,justify=tk.LEFT) 
        self.instructions.grid(row=0,columnspan=4,padx=10,pady=10)
        self.word_buttons=[]
        #Creates A Submit button at a specific location.
        self.submit_button=tk.Button(self.root,text="Submit",command=self.submit_words,state=tk.DISABLED)
        self.submit_button.grid(row=6,columnspan=4,pady=10)
        self.lives_label=tk.Label(self.root,text=f"Lives: {self.lives}")
        self.lives_label.grid(row=7,columnspan=4)
        #Creates A start button at a specific location.
        self.start_button=tk.Button(self.root,text="Start",command=self.start_round)
        self.start_button.grid(row=8,columnspan=4,pady=10)
        self.root.mainloop()

    #Starts the game
    def start_round(self):
        self.round+=1
        random.shuffle(self.list)
        self.start_button.config(state=tk.DISABLED)
        self.populate_grid()
        self.submit_button.config(state=tk.NORMAL)


    def start_round(self):
        self.round += 1
        random.shuffle(self.list)
        self.start_button.config(state=tk.DISABLED)
        self.populate_grid()
        self.submit_button.config(state=tk.NORMAL)
        # Adds instructions on how to play the game. 
        self.instructions.config(text="""
Find groups of four items that share something in common.

Select up to four items by clicking on them, then tap 'Submit' to check if your guess is correct.
Find the groups without making 3 mistakes!

Category Examples:
FISH: Bass, Flounder, Salmon, Trout
FIRE ___: Ant, Drill, Island, Opal

Categories will always be more specific than "5-LETTER-WORDS," "NAMES" or "VERBS."

Each puzzle has exactly one solution. Watch out for words that seem to belong to multiple categories!

Each group is assigned a color, which will be revealed as you solve:
Easy: Yellow
Moderate: Green
Hard: Blue
Difficult: Purple
""")

    #Creates the 4x4 grid. Makes it so buttons can be selected and deselected. 
    def populate_grid(self):
        words=self.get_words_for_round()
        for i in range(4):
            for j in range(4):
                index=i*4+j
                if index<len(words):
                    word=words[index]
                    button=tk.Button(self.root,text=word,width=15,height=2,command=lambda word=word:self.toggle_word(word))
                    button.grid(row=i+1,column=j,padx=5,pady=5)
                    self.word_buttons.append(button)

    #Looks at the round count and determines how many words need to be returned. 
    def get_words_for_round(self):
        if self.round==1:
            return self.list
        guessed_categories=[category for category,data in self.categories.items() if not set(data["words"]).isdisjoint(self.list)]
        remaining_categories=[category for category in self.categories.keys() if category not in guessed_categories]
        remaining_words=[word for category in remaining_categories for word in self.categories[category]["words"]]
        return remaining_words

    #Further enhances the toggle feature by making the word background red. Also doesn't let the user select more than 4 words. 
    def toggle_word(self,word):
        if word in self.selected_words:
            self.selected_words.remove(word)
            self.update_word_button_color(word,"SystemButtonFace")
        else:
            if len(self.selected_words)<4:
                self.selected_words.append(word)
                self.update_word_button_color(word,"red")
            else:
                messagebox.showwarning("Warning","You can only select up to 4 words.")


    def update_word_button_color(self,word,color):
        for button in self.word_buttons:
            if button["text"]==word:
                button.config(bg=color)

    #Let's the user know they must select 4 words. 
    def submit_words(self):
        if len(self.selected_words)!=4:
            messagebox.showerror("Error","Please select exactly 4 words.")
            return

        for category,data in self.categories.items():
            if set(self.selected_words)==set(data["words"]):
                messagebox.showinfo("Correct",f"Category '{category}' was the category")
                self.remove_guessed_words(data["words"])
                self.update_category_colors(category,data["difficulty"])
                self.round+=1
                self.populate_grid()
                return
        #Gives an error message if the user guesses incorrectly and removes 1 life from their life bank. When the user gets to 0 lives, they lose. 
        messagebox.showerror("Incorrect","Try again.")
        self.deselect_words()
        self.lives-=1
        self.lives_label.config(text=f"Lives: {self.lives}")
        if self.lives==0:
            messagebox.showinfo("Game Over","Better Luck Next Time!")
            self.root.destroy()
    #Removes the words that were guessed from the list
    def remove_guessed_words(self,words_to_remove):
        for word in words_to_remove:
            for category,data in self.categories.items():
                if word in data["words"]:
                    data["words"].remove(word)
        self.selected_words.clear()

    def deselect_words(self):
        for word in self.selected_words:
            self.update_word_button_color(word,"SystemButtonFace")
        self.selected_words.clear()
    #Updates the words that were guessed correctly with the correct background color
    def update_category_colors(self,category,difficulty):
        color=self.difficulty[difficulty]
        for button in self.word_buttons:
            if button["text"] in self.categories[category]["words"]:
                button.config(bg=color)

def main(): #Creates the game with the words 
    words=["Ideal","Example","Model","Symbol","Car","Conductor","Station","Track","Cymbal","Scimitar","Simmer","Symphony","Drum","Mark","Wax","Wig"]
    
    game=ConnectionsGame(words)

if __name__=="__main__":
    main()
