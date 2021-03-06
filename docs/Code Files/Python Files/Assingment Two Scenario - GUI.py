import tkinter

def evaluate():
    A = str(entry_1.get())
    B = str(entry_2.get())
    C = str(entry_3.get())
    D = str(entry_4.get())
    E = int(entry_5.get())
    question = 0
    score = 0


    if A == "D" or A == "d":
        score += 1
        question += 1
        entry_1.configure()
    elif A != "D" or A != "d":
        score += 0
        question += 1
        entry_1.configure(bg="red")
    if B == "G" or B == "g":
        score += 1
        question += 1
        entry_2.configure()
    elif B != "G" or B != "g":
        score += 0
        question += 1
        entry_2.configure(bg="red")
    if C == "F" or B == "f":
        score += 1
        question += 1
        entry_3.configure()
    elif C != "F" or B != "f":
        score += 0
        question += 1
        entry_3.configure(bg="red")
    if D == "E" or D == "e":
        score += 1
        question += 1
        entry_4.configure()
    elif D != "E" or D != "e":
        score += 0
        question += 1
        entry_4.configure(bg="red")
    if E == 3:
        score += 1
        question += 1
        entry_5.configure()
    elif E != 3:
        score += 0
        question += 1
        entry_5.configure(bg="red")

    evaluate1.configure(text=f"You scored {score} out of {question} questions.")


window = tkinter.Tk()

window.title("Assignment Two Scenario - GUI")
window.geometry("450x200")
window.resizable(0, 0)


label_0 = tkinter.Label(window, text="Welcome")
label_1 = tkinter.Label(window, text="Who lives in the second corner?")
label_2 = tkinter.Label(window, text="Who lives in the middle?")
label_3 = tkinter.Label(window, text="Who lives between B and G?")
label_4 = tkinter.Label(window, text="Who is the neighbor of A?")
label_5 = tkinter.Label(window, text="How many houses are there between B and E?")

label_0.grid(column=0, row=0)
label_1.grid(column=0, row=1)
label_2.grid(column=0, row=2)
label_3.grid(column=0, row=3)
label_4.grid(column=0, row=4)
label_5.grid(column=0, row=5)

entry_1 = tkinter.Entry(window, text="")
entry_2 = tkinter.Entry(window, text="")
entry_3 = tkinter.Entry(window, text="")
entry_4 = tkinter.Entry(window, text="")
entry_5 = tkinter.Entry(window, text="")

entry_1.grid(column=1, row=1)
entry_2.grid(column=1, row=2)
entry_3.grid(column=1, row=3)
entry_4.grid(column=1, row=4)
entry_5.grid(column=1, row=5)

button_1 = tkinter.Button(window, text="Evaluate", fg="black", bg="white", command=evaluate)
button_1.grid(column=1, row=6)

evaluate1 = tkinter.Label(window)
evaluate1.grid(column=0, row=7)

window.mainloop()
