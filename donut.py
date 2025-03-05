import tkinter as tk
import pytz
from datetime import datetime

timezone = pytz.timezone("Asia/Bangkok")

root = tk.Tk()
root.title("Digital Clock (GMT+7)")
root.geometry("600x300")
root.resizable(False, False)

canvas = tk.Canvas(root, width=600, height=300, highlightthickness=0)
canvas.pack(fill="both", expand=True)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

def draw_gradient(canvas, width, height, start_color, end_color):
    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)
    steps = height
    for i in range(steps):
        ratio = i / steps
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * ratio)
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * ratio)
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * ratio)
        color = rgb_to_hex((r, g, b))
        canvas.create_line(0, i, width, i, fill=color)

draw_gradient(canvas, 600, 300, "#2c003e", "#0d1b2a")

shadow_text = canvas.create_text(302, 152, text="", fill="#000000", font=("Courier", 80, "bold"))
clock_text = canvas.create_text(300, 150, text="", fill="white", font=("Courier", 80, "bold"))

def update_time():
    now = datetime.now(timezone)
    time_str = now.strftime("%H:%M:%S")
    canvas.itemconfig(shadow_text, text=time_str)
    canvas.itemconfig(clock_text, text=time_str)
    root.after(1000, update_time)

update_time()
root.mainloop()
