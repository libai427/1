import tkinter as tk

def button_click(text):
    if text == "AC":
        entry.delete(0, tk.END)
    elif text == "=":
        try:
            expression = entry.get()
            # 替换显示符号为Python可识别的运算符
            expression = expression.replace("×", "*").replace("÷", "/")
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "除零错误")
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "输入错误")
    else:
        # 替换显示的运算符为实际计算使用的符号
        if text == "×":
            entry.insert(tk.END, "*")
        elif text == "÷":
            entry.insert(tk.END, "/")
        else:
            entry.insert(tk.END, text)

# 创建主窗口
root = tk.Tk()
root.title("简单计算器")
root.geometry("300x400")

# 显示输入框
entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# 按钮布局（文本 + 点击事件）
buttons = [
    ("AC", 1, 0), ("÷", 1, 1), ("×", 1, 2), ("-", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("+", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), 
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), 
    ("0", 5, 0, 2), (".", 5, 2),  # 0按钮跨两列
    ("=", 3, 3, 2)  # =按钮跨两行
]

for button in buttons:
    text, row, col = button[0], button[1], button[2]
    col_span = button[3] if len(button) > 3 else 1
    row_span = button[4] if len(button) > 4 else 1
    btn = tk.Button(
        root, text=text, font=("Arial", 16),
        command=lambda t=text: button_click(t)
    )
    btn.grid(row=row, column=col, columnspan=col_span, rowspan=row_span, sticky="nsew")

# 让格子自动拉伸
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
