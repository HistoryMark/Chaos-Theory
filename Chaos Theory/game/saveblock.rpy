#Quick/Main Menu Access Saveblocker

if saveblock:
    jump saveblocker
    
else:
    jump saveblockernull

label saveblocker:
    pass
        
label saveblockernull:
    pass

#When variable 'saveblock' true when invoked by script (Via story arc flags), create function with conditional statement to rewrite and change quick menu, and main menu with its navigation screen. Block access and functionality to save/load screens during the 'diverged' story arc.