import tkinter as tk

def on_button_click():
    label.config(text="按钮被点击了！")

# 创建主窗口
root = tk.Tk()
root.title("简单的图形化界面")
root.geometry("300x200")

# 添加一个标签
label = tk.Label(root, text="欢迎使用图形化界面！", font=("Arial", 12))
label.pack(pady=20)

# 添加一个按钮
button = tk.Button(root, text="点击我", command=on_button_click)
button.pack(pady=10)

# 运行主循环
root.mainloop()

print("图形化界面已关闭。")