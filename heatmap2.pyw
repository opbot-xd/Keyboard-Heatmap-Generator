import tkinter as tk
import tkinter.font as tkf
import os
import keyboardlayout as kl
import keyboardlayout.tkinter as klt
import matplotlib
from matplotlib import cm
from PIL import Image, ImageTk
window = tk.Tk()
window.focus_force()
window.title("GUI heatmap...")
window.geometry("950x500")
window.config(background="#121212")
window.after(1000, window.focus_force)
window.resizable(False,False)
os.system('pyw keylog.pyw')


file = open("./txts/keylog.txt",'r')
data=(file.read()).split('.')
counter = {'BACKQUOTE': 0, 'ASCII_TILDE': 0, 'DIGIT_1': 0, 'EXCLAMATION': 0, 'DIGIT_2': 0, 'AT': 0, 'DIGIT_3': 0, 'NUMBER': 0, 'DIGIT_4': 0, 'DOLLAR': 0, 'DIGIT_5': 0, 'PERCENT': 0, 'DIGIT_6': 0, 'CARET': 0, 'DIGIT_7': 0, 'AMPERSAND': 0, 'DIGIT_8': 0, 'ASTERISK': 0, 'DIGIT_9': 0, 'DIGIT_0': 0, 'MINUS': 0, 'UNDERSCORE': 0, 'EQUALS': 0, 'PLUS': 0, 'BACKSPACE': 0, 'TAB': 0, 'Q': 0, 'W': 0, 'E': 0, 'R': 1, 'T': 0, 'Y': 0, 'U': 0, 'I': 0, 'O': 0, 'P': 0, 'LEFTPAREN': 0, 'RIGHTPAREN': 0, 'LEFTBRACKET': 0, 'RIGHTBRACKET': 0, 'BRACELEFT': 0, 'BRACERIGHT': 0, 'BACKSLASH': 0, 'PIPE': 0, 'CAPSLOCK': 0, 'A': 9, 'S': 9, 'D': 9, 'F': 9, 'G': 0, 'H': 0, 'J': 12, 'K': 13, 'L': 13, 'SEMICOLON': 0, 'COLON': 4, 'DOUBLEQUOTE': 0, 'SINGLEQUOTE': 0, 'RETURN': 0, 'LEFT_SHIFT': 0, 'Z': 0, 'X': 0, 'C': 0, 'V': 0, 'B': 0, 'N': 0, 'M': 0, 'COMMA': 0, 'LESSTHAN': 0, 'PERIOD': 0, 'GREATERTHAN': 0, 'FORWARDSLASH': 0, 'QUESTION': 0, 'RIGHT_SHIFT': 0, 'LEFT_CONTROL': 0, 'LEFT_META': 0, 'LEFT_ALT': 0, 'SPACE': 0, 'RIGHT_ALT': 0, 'RIGHT_META': 0, 'CONTEXT_MENU': 0, 'RIGHT_CONTROL': 0, 'FUNCTION': 0, 'LEFT_ARROW': 0, 'RIGHT_ARROW': 0, 'UP_ARROW': 0, 'DOWN_ARROW': 0, 'TWO_SUPERIOR': 0, 'U_GRAVE': 0, 'E_ACUTE': 0, 'E_GRAVE': 0, 'C_CEDILLE': 0, 'A_GRAVE': 0, 'DEGREE': 0, 'DIACRATICAL': 0, 'CIRCUMFLEX': 0, 'POUND': 0, 'A_CIRCUMFLEX': 0, 'E_CIRCUMFLEX': 0, 'I_CIRCUMFLEX': 0, 'O_CIRCUMFLEX': 0, 'U_CIRCUMFLEX': 0, 'SECTION': 0, 'MU': 0}
iop=0
for keys in counter:
    counter[keys] = int(data[iop])
    iop+=1
norm = matplotlib.colors.Normalize(vmin=min(counter.values()), vmax=max(counter.values()))
mapper = cm.ScalarMappable(norm=norm, cmap=cm.viridis)

key_size = 60


image1 = Image.open("./imgs/colormap.png")
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(image=test)
label1.image = test
# Position image
label1.place(rely=1, relx=0.5,anchor='s')
# common options for keys
key_info_dict = {
    "margin": 5,
    "txt_color": "black",
    "txt_font": tkf.Font(family='Arial'),
    "txt_padding": (key_size//6, key_size//10)
}

keyboard_layout = klt.KeyboardLayout(
    kl.LayoutName.QWERTY,
    kl.KeyboardInfo(position=(0,0), padding=2),
    (key_size, key_size),  # width, height,
    kl.KeyInfo(**key_info_dict, color="grey"),
    master=window
)

# converting rgba to hex string, e.g.: (0, 0, 255, 1) to #0000FF
def rgba_int_to_hex(rgba):
    hex_vals = map(lambda x: hex(int(255*x))[2:].zfill(2), rgba[:-1])
    return "#" + ''.join(hex_vals)

# coloring each key individually
for k, v in counter.items():
    keyboard_layout.update_key(key=getattr(kl.Key, k), 
                            key_info=kl.KeyInfo(**key_info_dict, 
                                            color=rgba_int_to_hex(mapper.to_rgba(v))))
window.mainloop()