import sys
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog

np.set_printoptions(threshold=sys.maxsize)

def encode_image():
    src = filedialog.askopenfilename(title="Select Source Image")
    message = e1.get()
    dest = filedialog.asksaveasfilename(title="Select Destination Image", defaultextension=".png")
    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size // n

    message += "$t3g0"
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print("ERROR: Need larger file size")

    else:
        index = 0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1

        array = array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest)
        tk.Label(root, text="Image Encoded Successfully").grid(row=3, column=0, columnspan=2)

def decode_image():
    src = filedialog.askopenfilename(title="Select Source Image")
    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size // n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i + 8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$t3g0" in message:
        tk.Label(root, text="Hidden Message: " + message[:-5]).grid(row=3, column=0, columnspan=2)
    else:
        tk.Label(root, text="No Hidden Message Found").grid(row=3, column=0, columnspan=2)

root = tk.Tk()
root.title("$t3g0")
root.geometry("400x200")

tk.Label(root, text="Enter Message to Hide:").grid(row=0, column=0, pady=10)
e1 = tk.Entry(root)
e1.grid(row=0, column=1, pady=10)

tk.Button(root, text="Encode", command=encode_image).grid(row=1, column=0, padx=10, pady=10)
tk.Button(root, text="Decode", command=decode_image).grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="").grid(row=2, column=0, columnspan=2)

root.mainloop()
