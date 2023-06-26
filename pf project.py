import tkinter as tk
from tkinter import ttk
import os
import openai

def file(language, difficulty,feature):
    # Save the output to a file
    file_var =open(language+difficulty+feature, "w")
    file_var.write(result.get("1.0", tk.END))

def generate():
    # create a prompt by getting the values entered by user
    try:
        language = language_dropdown.get()

        if not language or language not in ["Python", "Java", "C++", "Javascript", "Golang", "Php.net", "C#"]:
            result.delete("1.0", tk.END)
            result.insert(tk.END, "Invalid input. Please select a valid programming language.")
            raise ValueError("Please select a valid programming language")



        prompt = "Please generate 10 ideas for a coding project. The programming language is " + language + ". "
        difficulty = difficulty_value.get()
        prompt += "The difficulty is " + difficulty + ". "

        if(checkbox_var1.get() and checkbox_var2.get()):
            feature="Database and API"
        elif(checkbox_var2.get()):
            feature="API"
        elif(checkbox_var1.get()):
            feature="Database"
        else:
            feature=""

        if checkbox_var1.get():
            prompt += "The project should include a Database. "
        if checkbox_var2.get():
            prompt += "The project should include an API. "

        result.delete("1.0", tk.END)
        result.insert(tk.END, prompt)

        # Your OpenAI code here
        openai.api_key = "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"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content
        print(answer)
        name="LANGUAGE:",language,"\tDIFFICULTY:",difficulty
        result.insert("0.0","\n")
        result.insert("0.0",answer)
        result.insert("0.0","\n")
        result.insert("0.0",name)
        result.insert("0.0","\n")
    
    except ValueError:
        result.delete("1.0", tk.END)
        result.insert(tk.END, "Invalid input. Please select a programming language.")
    except Exception as e:
        result.delete("1.0", tk.END)
        result.insert(tk.END, "An error occurred: " + str(e))
    file(language, difficulty, feature)


#create a GUI window 
window=tk.Tk()
window.geometry("750x630")
window.configure(bg="black")
window.title("ChatGPT Project Idea Generaotor")
window.resizable(0,0)

#declare the specifications of different fontstyles
font_style1=("Times New Roman",30,"bold")
font_style2=("Times New Roman",15,"bold")
font_style3=("Times New Roman",15)

#add the main title of the window
title_label=tk.Label(window, text="Project Idea Generator", font=font_style1,
                     background="black", foreground="white")
title_label.pack(padx=10, pady=(40,20))

frame=tk.Frame(window, background="black")
frame.pack(fill="x", padx=100)

#craete a frame for the user to choose a programming language
language_frame=tk.Frame(frame, background="#36454F", highlightbackground="#36454F",
                        highlightthickness=5)
language_frame.pack(padx=100, pady=(25,5), fill="x")

language_label=tk.Label(language_frame, text="Programming Language",
                        font=font_style2, background="#36454F",
                          foreground="white")
language_label.pack()

language_dropdown=ttk.Combobox(language_frame, values=["Python","Java","C++","Javascript",
                                                       "Golang","Php.net","C#"])
language_dropdown.pack(pady=10)

#create a frame for the user to choose difficulty level
difficulty_frame=tk.Frame(frame, background="#36454F", highlightbackground="#36454F",
                          highlightthickness=5)
difficulty_frame.pack(padx=100, pady=5, fill="both")

difficulty_label=tk.Label(difficulty_frame, text="Project Difficulty", font=font_style2,
                          background="#36454F",
                          foreground="white")
difficulty_label.pack()

difficulty_value=tk.StringVar()

radio_button1=tk.Radiobutton(difficulty_frame, text="Easy", variable=difficulty_value,
                             value="Easy", font=font_style3, background="#36454F",
                          foreground="white")
radio_button1['selectcolor'] = 'black'
radio_button1.pack(side="left", padx=(20,10), pady=10, fill="both")

radio_button2=tk.Radiobutton(difficulty_frame, text="Medium", variable=difficulty_value,
                             value="Medium", font=font_style3, background="#36454F",
                          foreground="white")
radio_button2['selectcolor'] = 'black'
radio_button2.pack(side="left", padx=10, pady=10, fill="both")

radio_button3=tk.Radiobutton(difficulty_frame, text="Hard", variable=difficulty_value,
                             value="Hard", font=font_style3, background="#36454F",
                          foreground="white")
radio_button3['selectcolor'] = 'black'
radio_button3.pack(side="left", padx=10, pady=10, fill="both")

#create a frame for the user to choose features
features_frame=tk.Frame(frame, background="#36454F", highlightbackground="#36454F",
                        highlightthickness=5)
features_frame.pack(padx=100, pady=5, fill="both")

difficulty_label=tk.Label(features_frame, text="Features", font=font_style2, background="#36454F",
                          foreground="white")
difficulty_label.pack()


checkbox_var1 = tk.IntVar()
checkbox_var2 = tk.IntVar()

checkbox1 = tk.Checkbutton(features_frame, text="Database", variable=checkbox_var1,
                           font=font_style3, background="#36454F",
                          foreground="white")
checkbox1['selectcolor'] = 'black'
checkbox1.pack(side="left", padx=50, pady=10)

checkbox2 = tk.Checkbutton(features_frame, text="API", variable=checkbox_var2,
                           font=font_style3, background="#36454F",
                          foreground="white")
checkbox2['selectcolor'] = 'black'
checkbox2.pack(side="left", padx=30, pady=10)

#create a button that on clicking run the generate function
button=tk.Button(frame, text="Generate Ideas", background="lightblue" , command=generate)
button.pack(padx=100, fill="x", pady=(5,20))

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#create a textbox to show the result
result = tk.Text(window, yscrollcommand=scrollbar.set, font=font_style3,
                 height=10, background="#36454F",
                          foreground="white") 
result.pack(padx=100, fill="x", pady=10, side=tk.LEFT)

scrollbar.config(command=result.yview)


window.mainloop()

#new line



