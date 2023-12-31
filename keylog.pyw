from pynput.keyboard import Key
from pynput.keyboard import Listener
the_keys = []
shift_pressed=False
def functionPerKey(key):  
    the_keys.append(key)
    global shift_pressed
    if key == Key.shift:
        shift_pressed = True
    storeKeysToFile(the_keys)






def storeKeysToFile(keys):
    global key_count
    key_count={'BACKQUOTE': 0, 'ASCII_TILDE': 0, 'DIGIT_1': 0, 'EXCLAMATION': 0, 'DIGIT_2': 0, 'AT': 0, 'DIGIT_3': 0, 'NUMBER': 0, 'DIGIT_4': 0, 'DOLLAR': 0, 'DIGIT_5': 0, 'PERCENT': 0, 'DIGIT_6': 0, 'CARET': 0, 'DIGIT_7': 0, 'AMPERSAND': 0, 'DIGIT_8': 0, 'ASTERISK': 0, 'DIGIT_9': 0, 'DIGIT_0': 0, 'MINUS': 0, 'UNDERSCORE': 0, 'EQUALS': 0, 'PLUS': 0, 'BACKSPACE': 0, 'TAB': 0, 'Q': 0, 'W': 0, 'E': 0, 'R': 0, 'T': 0, 'Y': 0, 'U': 0, 'I': 0, 'O': 0, 'P': 0, 'LEFTPAREN': 0, 'RIGHTPAREN': 0, 'LEFTBRACKET': 0, 'RIGHTBRACKET': 0, 'BRACELEFT': 0, 'BRACERIGHT': 0, 'BACKSLASH':0 , 'PIPE': 0, 'CAPSLOCK': 0, 'A': 0, 'S': 0, 'D': 0, 'F': 0, 'G': 0, 'H': 0, 'J': 0, 'K': 0, 'L': 0, 'SEMICOLON': 0, 'COLON': 0, 'DOUBLEQUOTE': 0, 'SINGLEQUOTE': 0, 'RETURN': 0, 'LEFT_SHIFT': 0, 'Z': 0, 'X': 0, 'C': 0, 'V': 0, 'B': 0, 'N': 0, 'M': 0, 'COMMA': 0, 'LESSTHAN': 0, 'PERIOD': 0, 'GREATERTHAN': 0, 'FORWARDSLASH': 0, 'QUESTION': 0, 'RIGHT_SHIFT': 0, 'LEFT_CONTROL': 0, 'LEFT_META': 0, 'LEFT_ALT': 0, 'SPACE': 0, 'RIGHT_ALT': 0, 'RIGHT_META': 0, 'CONTEXT_MENU': 0, 'RIGHT_CONTROL': 0, 'FUNCTION': 0, 'LEFT_ARROW': 0, 'RIGHT_ARROW': 0, 'UP_ARROW': 0, 'DOWN_ARROW': 0, 'TWO_SUPERIOR': 0, 'U_GRAVE': 0, 'E_ACUTE': 0, 'E_GRAVE': 0, 'C_CEDILLE': 0, 'A_GRAVE': 0, 'DEGREE': 0, 'DIACRATICAL': 0, 'CIRCUMFLEX': 0, 'POUND': 0, 'A_CIRCUMFLEX': 0, 'E_CIRCUMFLEX': 0, 'I_CIRCUMFLEX': 0, 'O_CIRCUMFLEX': 0, 'U_CIRCUMFLEX': 0, 'SECTION': 0, 'MU': 0}
    
    for _ in keys:
        
        if _ in ["|","'\\'"]:
            key_count['PIPE']+=1
        i=(str(_)).replace("'","")
        print(i=="Key.backspace")
        if i=='`' or i=="~":
            key_count['ASCII_TILDE']+=1
        if i=="-" or i=='_':
            key_count['UNDERSCORE']+=1
        if i=="=" or i=="+":
            key_count['PLUS']+=1
        if i=='Key.backspace':
            key_count['BACKSPACE']+=1
        if str(i)=='Key.tab':
            key_count['TAB']+=1
        if i.upper() in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            key_count[i.upper()]+=1
        if i=='1' or i=="!":
            key_count['EXCLAMATION']+=1
        if i=='2' or i=="@":
            key_count['AT']+=1
        if i=='3' or i=="#":
            key_count['NUMBER']+=1
        if i=='4' or i=="$":
            key_count['DOLLAR']+=1
        if i=='5' or i=="%":
            key_count['PERCENT']+=1
        if i=='6' or i=="^":
            key_count['CARET']+=1
        if i=='7' or i=="&":
            key_count['AMPERSAND']+=1
        if i=='8' or i=="*":
            key_count['ASTERISK']+=1
        if i=='9' or i=="()":
            key_count['LEFTPAREN']+=1
        if i=='0' or i==")":
            key_count['RIGHTPAREN']+=1
        if i in ["[","{"]:
            key_count['BRACELEFT']+=1
        if i in ["]","}"]:
            key_count['BRACERIGHT']+=1
        if i in ["|","\\"]:
            key_count['PIPE']+=1    
        if i == 'Key.caps_lock':
            key_count['CAPSLOCK']+=1
        if i in [':',';']:
            key_count["COLON"]+=1
        if i in ['"',"'"]:
            key_count["DOUBLEQUOTE"]+=1
        if i=='Key.enter':
            key_count['RETURN']+=1
        if i=='Key.shift':
            key_count['LEFT_SHIFT']+=1
        if i==',' or i=='<':
            key_count['LESSTHAN']+=1
        if i=='.' or i=='>':
            key_count['GREATERTHAN']+=1
        if i=='/' or i=='?':
            key_count['QUESTION']+=1
        if i=='Key.shift_r':
            key_count['RIGHT_SHIFT']+=1
        if i=='Key.ctrl_l':
            key_count['LEFT_CONTROL']+=1
        if i=='Key.cmd':
            key_count['LEFT_META']+=1
        if i=='Key.alt_l':
            key_count['LEFT_ALT']+=1
        if i=='Key.space':
            key_count['SPACE']+=1
        if i=='Key.alt_gr':
            key_count['RIGHT_ALT']+=1
        if i=='Key.ctrl_r':
            key_count['RIGHT_CONTROL']+=1

        
    with open('./txts/keylog.txt', 'w') as log:
        for _ in key_count:
            i=str(key_count[_])
            log.write(i+'.')
def onEachKeyRelease(key):
    global shift_pressed

    if key == Key.esc and shift_pressed:
        print(key_count['BACKSPACE'])
        return False

    if key == Key.shift:
        shift_pressed = False


with Listener(
    on_press = functionPerKey,
    on_release = onEachKeyRelease
) as the_listener:
    the_listener.join()