import tkinter as tk
import tkinter.messagebox as mb
import math
import numpy as np


def task_a():
    return 'Result: log2(15)= ' + str(math.log2(15))


def task_b():
    str1 = 'First number ' + str(np.random.uniform(0, 1)) + '\n'
    str2 = 'Second number ' + str(np.random.uniform(0, 1)) + '\n'
    str3 = 'Third number ' + str(np.random.uniform(0, 1)) + '\n'
    str4 = 'Fourth number ' + str(np.random.uniform(0, 1)) + '\n'
    return str1 + str2 + str3 + str4


def task_c():
    return str(dir())


class Dialog(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lab 3.3, task d")
        self.geometry('350x200')
        btn_task_a = tk.Button(self, text="task a",
                               command=self.show_task_a)
        btn_task_b = tk.Button(self, text="task b",
                               command=self.show_task_b)
        btn_task_c = tk.Button(self, text="task c",
                               command=self.show_task_c)

        opts = {'padx': 40, 'pady': 5, 'expand': True, 'fill': tk.BOTH}
        btn_task_a.pack(**opts)
        btn_task_b.pack(**opts)
        btn_task_c.pack(**opts)

    def show_task_a(self):
        msg = task_a()
        mb.showinfo("task_a", msg)

    def show_task_b(self):
        msg = task_b()
        mb.showinfo("task_b", msg)

    def show_task_c(self):
        msg = task_c()
        mb.showinfo("task_c", msg)


# if __name__ == "__main__":
#     app = Dialog()
#     app.mainloop()
# app = Dialog()
# app.mainloop()
