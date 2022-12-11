def factorial(n):
    fact = 1
    while(n>1):
        fact = fact * n
        n = n-1
    return fact
def combinations(n, k):
    num = factorial(n)
    den = factorial(k) * factorial(n-k)
    return num / den
def comb_ways(a, total_num, num_choices):
    num = factorial(num_choices) * factorial(total_num - num_choices)
    den = factorial(a) * factorial(num_choices - a) * factorial((total_num - num_choices) - (num_choices - a)) * factorial(num_choices -a)
    return num / den
def one_ticket_probability (total_num, tickets, num_choices, num_joker, match_num, joker_ball = False):
    outcome_numbers = combinations(total_num, num_choices)
    successful_outcome = tickets
    if joker_ball == True:
        outcome_jokerball = num_joker
    else :
        outcome_jokerball = (num_joker) / (num_joker - 1)
    total_outcomes = (outcome_numbers / comb_ways(match_num, total_num, num_choices)) * outcome_jokerball
    probability_winning = (successful_outcome / total_outcomes)
    print("You're chances of winning are: {:.18f}" .format(probability_winning))
    print("You're chances of winning are 1 in {}" .format(
        total_outcomes / successful_outcome))
    return probability_winning, (total_outcomes / successful_outcome)

total_numbers = 50 #Range
number_choices = 6 # Number of choices
total_jokerballs = 5 #Number of joker balls
match_numbers = 6 #Countr of matched numbers
Joker_present = True #Presence of joker ball
tickets = 1 #Total number of tickets bought

for match_numbers in range(match_numbers + 1):
    if (Joker_present):
        print("joker ball matches-", end=" ")
    else:
        print("joker ball does not matches-", end=" ")
    print("count of numbers that matched the winning numbers = {}" .format(match_numbers))
    one_ticket_probability(total_numbers, tickets, number_choices, total_jokerballs, match_numbers, Joker_present)

#First we define a new function that calculates
#the probabilities and also gives results in a message box
import tkinter as tk
from tkinter import messagebox

def calculate(entries):
    cal = one_ticket_probability(int(entries['Total numbers'] .get()),
                                 int(entries['Tickets bought'] .get()),
                                 int(entries['Choices given'] .get()),
                                 int(entries['total_jokerballs'] .get()),
                                 int(entries['Match balls'] .get()), v.get())
    messagebox.showinfo(
        "for the selected choices ",
        "\nYou're chances of winning are {:.18f} \nYou're chances of winning are 1 in {}\n"
        .format(cal[0], cal[1]))
#we use tkinter to make a window object
root = tk.Tk()
#we make a form for user to give his values
def makeform(root, fields):
        entries = {}
        #these are default values for lotto-india
        default_vals = ['50', '6', '5', '6', '1']
        for field in fields:
            print(field)
            row = tk.Frame(root)
            lab = tk.Label(row, width=22, text=field +": ", anchor='w')
            ent = tk.Entry(row)
            ent.insert(0, default_vals[fields.index(field)])
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries[field] = ent
        return entries
fields = [
        'total number', 'choices given', 'total_jokerballs', 'match balls',
        'tickets bought'
]
ents = makeform(root, fields)
v = tk.IntVar()
tk.Label(root,
             text="jokerball matches",
             justify= tk.CENTER,
             padx=20).pack()
tk.Radiobutton(root, text="mathces", padx=20, variable=v,
                   value=True).pack(anchor=tk.CENTER)
tk.Radiobutton(root, text="no mathces", padx=20, variable=v,
                   value=False).pack(anchor=tk.CENTER)
b1 = tk.Button(root, text='calculate odds',
                   command=(lambda e=ents: calculate(e)))
b1.pack(side=tk.LEFT, padx=5, pady=5)
b3 = tk.Button(root, text='quit', command=root.quit)
b3.pack(side=tk.LEFT, padx=5, pady=5)

text2 = tk.Text(root, height=20, width=60)
scroll = tk.Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color', foreground='#476042',
                        font=('Tempus Sans ITC', 12, 'bold'))
text2.insert(tk.END, '\nlottery prediction\n', 'big')
quote =""" 
    total number: total numbers in range from witch numbers are 
    choices given: number of num,bers we can select excluding the
    """
text2.insert(tk.END, quote, 'color')
text2.pack(side=tk.LEFT)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
root.mainloop()



