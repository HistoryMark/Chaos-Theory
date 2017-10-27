# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Main Characters

define s = Character("Sam")

define a = Character("Ari")

define c = Character("Cynthia")

define b = Character("Bella")

# Supporting Characters

define MJ = Character("Mr.Jager")

define MC = Character("Mrs.Cole")

define MM = Character("Mr.Moore")

define MD = Character("Diana")

define MV = Character("Violet")

# Stock Characters

define St = Character ("A Teacher")

define Sms1 = Character ("A Male Student")

define Sms2 = Character ("Another Male Student")

define Sfs1 = Character ("A Female Student")

define Sfs2 = Character ("Another Female Student")

define Yw = Character ("Young Woman")

define Ym = Character ("Young man")

define Ow = Character ("Old woman")

define Om = Character ("Old man")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #image bg schoolyard = "schoolyard.png"
    scene bg schoolyard

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    St "Everyone here alright? Okay, good. Now roll call!"
    
    Sms1 "Is there an actual fire this time? The sprinklers went off."
    
    St "No, the fire alarm malfunctioned and turned on the sprinklers."
    
    Sms2 "I heard someone broke an alarm and set it off."
    
    Sfs1 "Well thanks to that idiot, we're all soaked and have to sit out here."
    
    Sfs2 "There's no class for a while, why are you mad?"
    
    Sfs1 "Because I want to leave this stupid place already, but i'm held up here by having the fire department look at a broken fire alarm set off by one of the many idiots in this school."
    
    St "We have to follow fire emergency procedures and make sure everyone is safe first, okay? Sorry for holding you up for your last class, but I still have to follow safety rules to keep my job."

    image Sam neutral = "Sam_neutral.png"
    show Sam neutral
    
    s "I'm wondering how I got myself in a mess like this..."

    s "All I'll say is that it was just another of my dumb ideas."
    
    hide Sam neutral
    with dissolve
    with fade
    
    #image bg principals-office = "principalsoffice.png"
    scene bg principals-office
    
    #image MrJager angry = "MrJager_angry.png"
    show MrJager angry at right
    
    MJ "Breaking a fire alarm and setting a false alarm off, on your first day? You're already making trouble!"
    
    #image Sam surprised = "Sam_surprised.png"
    show Sam surprised at left
    
    s "Mr.Jager! What are you doing here?!"
    
    MJ "I'm a transfered here to look after punks from junior high moving here like you! I got a promotion here."
    
    #image Sam angry = "Sam_angry.png"
    show Sam angry
    
    s "Tch...I'm telling you it was an accident that I broke it!"
    
    #image MrsCole talking = "MrsCole_talking.png"
    show MrsCole talking
    
    MC "Regardless of whether it was an accident or not, you still broke a fire alarm and you must understand there are consequences for your actions Mr.Moore."
    
    show Sam neutral
    
    s "Yeah, yeah, so what? Detention? Suspension? What do I have to sit through?"
    
    MC "Tampering with emergency equipment and creating a false alarm is a serious offense against the school and the fire department. You could also be charged with a misdemeanor, but you're still a minor."
    
    MC "For now, I will document it as an accident to get you away from that okay? I have contacted your parents to speak with us and take you home."
    
    MC "Hopefully you will stay out of trouble. The Semester doesn't start until two weeks from now, but you're still required to be here and discipline yourself."
    
    hide Sam neutral
    hide MrsCole talking
    hide MrJager angry
    with dissolve
    with fade
    
    #image bg Sams-house = "samshouse.png"
    scene bg Sams-house
    
    #image MrMoore neutral = "MrMoore_neutral.png"
    show MrMoore neutral
    
    MM "..."
    
    show Sam angry at right
    
    s "..."
    
    MM "Why did you do it?"
    
    menu:
        
        "It was an accident!":
            jump lie
            
        "It was just a dumb idea that didn't work.":
            jump truth
    
    default trueSam1 = False
    
    label lie:
    
    $ trueSam1 = False
    
    MM "Couldn't you have avoided the accident completely? Mr.Jager told me you were messing around in the halls and broke the alarm playing around."
    
    s "..."
    
    jump trouble
    
    label truth:
        
    $ trueSam1 = True
    
    MM "What were you trying to do?"
    
    s "Only you came so it didn't work."
    
    MM "..."
    
    jump trouble
   
    label trouble:
    
    MM "Let me rephrase the question, I know you're smart enough to stay out of trouble, but why do you make trouble anyway?"
    
    s "..."
    
    if trueSam1:
        
        s "Why didn't Mom come with you?"
        
        MM "You know she's always busy at work, i'm lucky enough to be able to pick you up myself since I have the day off today. She's working abroad right now and won't be back for a couple months."
        
        s "A couple months? When is she actually coming home?"
        
        MM "I think she might be home by Halloween, but I'm always around since I work in town."
        
        s "I had to wait 3 whole months of my summer for her to come back only to tell me, on my birthday, she couldn't make it by her secretary? I haven't seen her since your wedding and now you're telling me I have to wait another 3 months or so for her?"
        
        MM "Why are you so worried? I'm here for you."
        
        s "I'll be honest, Dad, I'm trying to get close to you, but you're still a stranger to me. Albert is the only person other than Mom in the house I actually know, and even he doesn't show up most of the time."
        
        MM "What are you saying?"
        
        s "I feel alone and empty in that house! I hate it there! I miss Mom, okay? I do stupid shit in school because that place sucks and just as boring as hell without doing any of it!"
        
        MM "...I'm sorry. I know I just came into your life and I don't know much about your problems, but I'll try to make it up to you okay?"
        
        s "Apologizing for nothing is the only thing you can do? I guess i'll say i'm sorry for cursing at you, but I just needed to vent."
        
        MM "..."
        
        jump home
        
    else:
        
        MM "I guess you just like messing around...Here we are, back to the house."
        
        jump home
        
    label home:
        show MrMoore neutral
        show Sam angry
        with dissolve
        with fade
    
        #image Diana neutral = "Diana_neutral.png"
        show MrMoore neutral at left
        show Sam neutral at right
        show Diana neutral
        
        Yw "Welcome home, Master Moore and Young Master."
        
        "She bows to express courtesy..."
        
        MM "Sam, I know from Albert you have a knack to kick our maids out of insanity, but please be kind to our new maid, Diana. She's 21 and she's studying as an undergrad in Hospitality and Management in college outside of working as a maid."
        
        MD "Pleased to meet you, Young Master Sam."
        
        #image Sam blushing = "Sam_blushing.png"
        show Sam blushing at right
        
        s "Uhh..Same, I guess.."
        
        s "(Since when did Mom hire such a cute maid?!?)"
        
        MM "I met her at a networking convention for my company and decided to hire her myself, even though your Mother wanted to hire one herself. Now please be nice with her, Sam, she's got school work aside with her housekeeping, so don't cause trouble, okay? I'm begging you."
        
        s "....Okay.."
        
        #image Diana happy = "Diana_happy.png"
        show Diana happy
        
        MD "I hope we get along together!"
        
        "She smiles sweetly at me, i'm confused by her beauty to keep my cool."
        
        s "Uhh..Yeah, okay. (I say with a half smile)"
        
        MD "You're blushing, young master."
        
        "She lets out a small chuckle"
        
        s "Ahh! Okay, that's enough, just stay out of my way and i'll stay out of yours! You know how to flirt and kiss up to your boss, i'll give you that!"
        
        MD "As you wish, young master. I just want to address you in a respectable manner."
        
        "She bows and smiles sweetly at me again."
        
        s "R-right."
        
    hide Sam blushing at right
    hide MrMoore neutral at left
    hide Diana happy
    with dissolve
    with fade
    
    #image bg Sams-house-inside = "samshouseinside.png"
    scene bg Sams-house-inside
        
    # This ends the game.

    return
