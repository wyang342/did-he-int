import tkinter as tk
import graph

def run():
	global entry
	ign = entry.get()
	graph.main(ign)

root = tk.Tk()
root.title('Favorite League Champions')
root.geometry("250x150")

text = tk.Text(root, height=2, width=30)
text.pack()
text.insert(tk.END, "Enter the summoner name:")

entry = tk.Entry(root)
entry.pack()
entry.focus_set()

button = tk.Button(root, text="show graph", command=run)
button.pack()
root.mainloop()

if __name__ == '__main__':
    run()