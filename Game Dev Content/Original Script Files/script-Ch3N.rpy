#Alternate/Diverged Story Arc Episode 3: Chapters 3BE & 3D
#Chapter 3N: Friends?
label Ch3No:

if Ch1BE_active:
    jump Pass3BE
    
elif Ch2BE_active:
    jump Pass3BE
    
else:
    
    "..."

label redo_Ch3BE:

menu:
    
    "Friends?"
    
    "Yes":
        jump Ch3BE
        
    "No":
        "Are you sure?"
menu:
    
    "Yes":
        jump Ch3D
        
    "No":
        jump redo_Ch3BE

#Chapter 3BE: Awkward Love
label Ch3BE:

label Pass3BE:
    
    #Chapter 3 Boring Ending

#Chapter 3D: Falling Out
label Ch3D:
    
    #Chapter 3 Diverged Ending
    
#At end of Chapter 3, depending on branch taken, goes straight to separate endings in Chapter 4
#Redemption Story Flag: Saveblocker disabled and Normal Menus enabled once reaching Ch.4A, 4B, 4C, 4S, or 4BE. Unlocked and completed after player reaches Ch4D, diverged story arc, then promptly restarts game and avoids diverged story arc.