import random
import tkinter as tk
from PIL import Image, ImageTk  

user_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissors"]

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_text.set("Your Score: 0  |  Computer Score: 0")
    result_text.set("")
    congrats_text.set("")
    retry_button.pack_forget() 

def update_image(choice, label):
    try:
        img = Image.open(f"{choice.lower()}.png") 
        img = img.resize((100, 100))  
        img = ImageTk.PhotoImage(img)  
        label.config(image=img)  
        label.image = img  
    except Exception as e:
        print("Error loading image:", e) 

def play(choice):
    global user_score, computer_score

    if user_score == 10 or computer_score == 10:
        return  

    user_choice = choice
    computer_choice = random.choice(choices)

    result_text.set(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result_text.set(result_text.get() + "\nIt's a Tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_text.set(result_text.get() + "\nYou Win!")
        user_score += 1
    else:
        result_text.set(result_text.get() + "\nComputer Wins!")
        computer_score += 1

    update_score()
    update_image(user_choice, user_label)  
    update_image(computer_choice, computer_label)  

def update_score():
    score_text.set(f"Your Score: {user_score}  |  Computer Score: {computer_score}")

    if user_score == 10:
        congrats_text.set("🎉 Congratulations! You Won! 🎉")
        retry_button.pack(pady=20)  
    elif computer_score == 10:
        congrats_text.set("💀 Computer Wins! Try Again! 💀")
        retry_button.pack(pady=20)  

def exit_fullscreen(event):
    root.attributes('-fullscreen', False)  

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.attributes('-fullscreen', True)  
root.config(bg="#222831")

root.bind("<Escape>", exit_fullscreen)

tk.Label(root, text="Rock Paper Scissors", font=("Arial", 30, "bold"), fg="white", bg="#222831").pack(pady=20)

score_text = tk.StringVar()
score_text.set("Your Score: 0  |  Computer Score: 0")
tk.Label(root, textvariable=score_text, font=("Arial", 20), fg="yellow", bg="#222831").pack()


result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Arial", 18), fg="white", bg="#222831").pack(pady=20)

image_frame = tk.Frame(root, bg="#222831")
image_frame.pack()

user_label = tk.Label(image_frame, bg="#222831")
user_label.grid(row=0, column=0, padx=50)

computer_label = tk.Label(image_frame, bg="#222831")
computer_label.grid(row=0, column=1, padx=50)

button_frame = tk.Frame(root, bg="#222831")
button_frame.pack(pady=30)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 18), bg="#ff8c00", fg="white", width=15, height=2, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=20)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 18), bg="#1e90ff", fg="white", width=15, height=2, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=20)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 18), bg="#ff1493", fg="white", width=15, height=2, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=20)

congrats_text = tk.StringVar()
congrats_label = tk.Label(root, textvariable=congrats_text, font=("Arial", 24, "bold"), fg="lightgreen", bg="#222831")
congrats_label.pack(pady=20)

retry_button = tk.Button(root, text="Retry", font=("Arial", 20, "bold"), bg="red", fg="white", command=reset_game)

root.mainloop()