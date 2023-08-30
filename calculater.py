import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

expression = ""

def press(number):
  global expression
  expression += str(number)
  text_field.insert(tk.END, number)

def clear():
  global expression
  expression = ""
  text_field.delete(0, tk.END)

def evaluate():
  global expression
  try:
    result = eval(expression)
    text_field.insert(tk.END, " = " + str(result))
  except:
    text_field.insert(tk.END, "Invalid expression")

text_field = tk.Entry(root, width=30)
text_field.grid(row=0, column=0, columnspan=4)

button_1 = tk.Button(root, text="1", command=lambda: press(1))
button_1.grid(row=1, column=0)

button_2 = tk.Button(root, text="2", command=lambda: press(2))
button_2.grid(row=1, column=1)

button_3 = tk.Button(root, text="3", command=lambda: press(3))
button_3.grid(row=1, column=2)

button_4 = tk.Button(root, text="4", command=lambda: press(4))
button_4.grid(row=2, column=0)

button_5 = tk.Button(root, text="5", command=lambda: press(5))
button_5.grid(row=2, column=1)

button_6 = tk.Button(root, text="6", command=lambda: press(6))
button_6.grid(row=2, column=2)

button_7 = tk.Button(root, text="7", command=lambda: press(7))
button_7.grid(row=3, column=0)

button_8 = tk.Button(root, text="8", command=lambda: press(8))
button_8.grid(row=3, column=1)

button_9 = tk.Button(root, text="9", command=lambda: press(9))
button_9.grid(row=3, column=2)

button_0 = tk.Button(root, text="0", command=lambda: press(0))
button_0.grid(row=4, column=0)

button_clear = tk.Button(root, text="Clear", command=clear)
button_clear.grid(row=4, column=1)

button_add = tk.Button(root, text="+", command=lambda: press("+"))
button_add.grid(row=4, column=2)

button_subtract = tk.Button(root, text="-", command=lambda: press("-"))
button_subtract.grid(row=5, column=0)

button_multiply = tk.Button(root, text="×", command=lambda: press("*"))
button_multiply.grid(row=5, column=1)

button_divide = tk.Button(root, text="÷", command=lambda: press("/"))
button_divide.grid(row=5, column=2)

button_equal = tk.Button(root, text="=", command=evaluate)
button_equal.grid(row=5, column=3)

root.mainloop()