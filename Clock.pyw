import tkinter as tk
from datetime import datetime
import time

root = tk.Tk()

root.title('Clock')

cnvs = tk.Canvas(width = 700, height = 300, background = 'White')

cnvs.pack()

cnvs.create_text(350, 150, text = '', font = ('', 100), fill = 'Green', tags = 'time')

try:

    while True:

        now = datetime.now()

        s = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second)

        cnvs.itemconfig('time', text = s)

        cnvs.update()

        time.sleep(0.1)

except:

    pass