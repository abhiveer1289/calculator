import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.create_ui()

    def create_ui(self):
        self.display = tk.Entry(self.root, width=20, font=("Arial", 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        button_labels = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'AC'
        ]

        row_count, col_count = 1, 0

        for label in button_labels:
            tk.Button(
                self.root,
                text=label,
                padx=20,
                pady=10,
                font=("Arial", 16),
                command=lambda lbl=label: self.on_button_click(lbl)
            ).grid(row=row_count, column=col_count, padx=5, pady=5)

            col_count += 1
            if col_count > 3:
                col_count = 0
                row_count += 1

    def on_button_click(self, label):
        if label == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif label == 'C':
            self.display.delete(len(self.display.get()) - 1, tk.END)
        elif label == 'AC':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, label)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
