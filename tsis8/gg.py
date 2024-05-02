import keyboard

def pause_game():
    print("Game Pause")
keyboard.add_hotkey('p')  

def power_up_activates():
    print('Power is Activated')
keyboard.add_hotkey('CTRL + ALT + a')

def undo_act():
    print("Undo the last action")
keyboard.add_hotkey('CTRL + Z')

cheat_code_sequence = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'b', 'a']
cheat_index = 0

def check_cheat_code(key_event):
    global cheat_index
    if key_event.name == cheat_code_sequence[cheat_index]:
        cheat_index += 1
        if cheat_index == len(cheat_code_sequence):
            print("Cheat code entered. Unlocking special abilities...")
            cheat_index = 0
    else:
        cheat_index = 0

keyboard.on_press(callback=check_cheat_code)


keyboard.wait()