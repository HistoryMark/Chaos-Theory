## Saveblocker ##
## Once story arc flag 'saveblocker' enabled due to choices, redefines quick menu and navigation menu to block saving and loading of other saves.

## Normal Menu Screens Enabled/Disabled

default persistent.quick_menunormal = True
default persistent.main_menunormal = True

## Saveblock Check ##
    
if persistent.saveblock:
    jump saveblocker
    
else:
    jump saveblockernull
    
## Saveblock Call ##

label saveblocker:
    
## Saveblocker Distorts Game Menus ##
    
    $ persistent.quick_menunormal = False
    $ persistent.main_menunormal = False

## Save-blocked Quick Menu screen ##

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if persistent.quick_menunormal:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Prefs") action ShowMenu('preferences')
            
    if persistent.saveblock:
        
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu()
            textbutton _("Prefs") action ShowMenu('preferences')
        

## Save-blocked Navigation screen ##

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing
            
        if persistent.main_menunormal:

            textbutton _("New Game") action Start()
            
            textbutton _("Continue") action FileLoad("1", page="auto")

        else:
            
            textbutton _("New Game") action ShowMenu()
                        
            textbutton _("Continue") action FileLoad("1", page="auto")

        if persistent.saveblock:
            
            textbutton _("Save") action ShowMenu()

            textbutton _("Load") action ShowMenu()
        
        else:
            
            textbutton _("Save") action ShowMenu('save')
            
            textbutton _("Load") action ShowMenu('load')

            textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()
                        
            textbutton _("History") action ShowMenu("history")

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
        
label saveblockernull:
    pass
