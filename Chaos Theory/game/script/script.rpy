#Project Chaos Theory
#Rewritten [Title Pending], A Visual Novel by Mark Perez

#Opening Cover Summary: Follow the story of Alex, the usual loner who enjoys anime and manga, but mostly an ordinary highschool student, except who has the extraordinary psychic power of being able to read and change her own and others' memories. From a boring and usual high school life, she uses her power to try to get friends and change their lives and her own forever. Meet your newest friend, Sam, the good-natured and slightly childish (and foolish) freshman with a knack of getting into trouble. Ari, the enigmatic prodigy with a shy, reserved, and quiet manner whose intelligence attracts those around him. Bella, Sam's childhood friend, who's a peppy, enthusiastic, and charming optimist while always wears a smile. Cynthia, the queen of the class, who commands the attention of everyone in the room by her presence, beauty, and boldness to be controversial. Watch her story unfold as an awakened psychic power changing Alex's normal high school life being rewritten into one with action, comedy, drama, romance, and suspense. 

# Main Characters

define x = Character("Alex")

define s = Character("Sam", image="Sam")

define a = Character("Ari", image="Ari")

define c = Character("Cynthia", image="Cynthia")

define b = Character("Bella", image="Bella")

# Family and Friends

#Sam's Family

define mom = Character("Mrs.Moore")

define seb = Character("Sebastian")

define dia = Character("Diana")

#Ari's Guardian

define kgw = Character("Aunt Yui")

#Bella's Family

define bmom = Character("Mrs. Garcia")

define bbro = Character("Vincent")

#Cynthia's Friends

define fd = Character("Ferdinand")

define jen = Character("Jenny")

define cel = Character("Celica")

define ser = Character("Sarah")

# Unknown/Other Characters

define sfsa = Character("Female Student A")

define sfsb = Character("Female Student B")

define sfsc = Character("Female Student C")

define sfsd = Character("Female Student D")

define smsa = Character("Male Student A")

define smsb = Character("Male Student B")

define smsc = Character("Male Student C")

define smsd = Character("Male Student D")

define tcha = Character("Teacher A")

define tchb = Character("Teacher B")

define doc = Character("Doctor")

define stm = Character("Strange Man")

define stf = Character("Strange Woman")

define gng = Character("Gangster Leader")

define gnga = Character("Gangster A")

define gngb = Character("Gangster B")

define gngc = Character("Gangster C")

define pol = Character("Police Officer")

# Character Sprites (48)

#Sam's sprites

image Sam neutral = "images/sprites/Sam_neutral.png"
    
image Sam happy = "images/sprites/Sam_happy.png"
    
image Sam sad = "images/sprites/Sam_sad.png"
    
image Sam embarrassed = "images/sprites/Sam_embarrassed.png"
    
image Sam talking = "images/sprites/Sam_talking.png"
    
image Sam crying = "images/sprites/Sam_crying.png"

image Sam angry = "images/sprites/Sam_angry.png"

image Sam blushing = "images/sprites/Sam_blushing.png"

image Sam hurt = "images/sprites/Sam_hurt.png"

image Sam surprised = "images/sprites/Sam_surprised.png"

image Sam closed = "images/sprites/Sam_closed.png"

image Sam insane = "images/sprites/Sam_insane.png"
    
#Bella's sprites
    
image Bella neutral = "images/sprites/Bella_neutral.png"
        
image Bella happy = "images/sprites/Bella_happy.png"
    
image Bella sad = "images/sprites/Bella_sad.png"
        
image Bella embarrassed = "images/sprites/Bella_embarrassed.png"
    
image Bella talking = "images/sprites/Bella_talking.png"
    
image Bella crying = "images/sprites/Bella_crying.png"

image Bella angry = "images/sprites/Bella_angry.png"

image Bella blushing = "images/sprites/Bella_blushing.png"

image Bella hurt = "images/sprites/Bella_hurt.png"

image Bella surprised = "images/sprites/Bella_surprised.png"

image Bella closed = "images/sprites/Bella_closed.png"

image Bella insane = "images/sprites/Bella_insane.png"
    
#Ari's sprites

image Ari neutral = "images/sprites/Ari_neutral.png"
    
image Ari happy = "images/sprites/Ari_happy.png"   
    
image Ari sad = "images/sprites/Ari_sad.png"
    
image Ari embarrassed = "images/sprites/Ari_embarrassed.png"
    
image Ari talking = "images/sprites/Ari_talking.png"
    
image Ari crying = "images/sprites/Ari_crying.png"

image Ari angry = "images/sprites/Ari_angry.png"

image Ari blushing = "images/sprites/Ari_blushing.png"

image Ari hurt = "images/sprites/Ari_hurt.png"

image Ari surprised = "images/sprites/Ari_surprised.png"

image Ari closed = "images/sprites/Ari_closed.png"

image Ari insane = "images/sprites/Ari_insane.png"

#Cynthia's sprites
    
image Cynthia neutral = "images/sprites/Cynthia_neutral.png"
    
image Cynthia happy = "images/sprites/Cynthia_happy.png"
    
image Cynthia sad = "images/sprites/Cynthia_sad.png"

image Cynthia embarrassed = "images/sprites/Cynthia_embarrassed.png"
    
image Cynthia talking = "images/sprites/Cynthia_talking.png"
    
image Cynthia crying = "images/sprites/Cynthia_crying.png"

image Cynthia angry = "images/sprites/Cynthia_angry.png"

image Cynthia blushing = "images/sprites/Cynthia_blushing.png"

image Cynthia hurt = "images/sprites/Cynthia_hurt.png"

image Cynthia surprised = "images/sprites/Cynthia_surprised.png"

image Cynthia closed = "images/sprites/Cynthia_closed.png"

image Cynthia insane = "images/sprites/Cynthia_insane.png"
    
#Background Scenes

image bg schoolcafe = "images/backgrounds/schoolcafe.jpg"

image bg schoolyard = "images/backgrounds/schoolyard.jpg"

image bg sidewalk = "images/backgrounds/sidewalk.jpg"

image bg sidewalknight = "images/backgrounds/sidewalknight.jpg"

image bg hospital = "images/backgrounds/hospital.jpg"
    
image bg classroom = "images/backgrounds/classroom.jpg"
    
image bg hallway = "images/backgrounds/hallway.jpg"
    
image bg clubroom = "images/backgrounds/clubroom.jpg"
    
image bg home = "images/backgrounds/home.jpeg"
    
image bg schoolfield = "images/backgrounds/schoolfield.jpg"
    
image bg mall = "images/backgrounds/mall.jpg"
    
image bg conferencecenter = "images/backgrounds/conferencecenter.jpg"

image bg shadybuilding = "images/backgrounds/shadybuilding.jpg"
    
image bg boardwalk = "images/backgrounds/boardwalk.jpg"
    
image bg park = "images/backgrounds/park.jpg"
    
image bg busyroad = "images/backgrounds/busyroad.jpg"

image bg void = "images/backgrounds/void.jpg"
    
#Character Graphics (16)

#Ch1 CGs

    #image bg cgsketching101 = "images/cg/sketching101.jpg"
    
    #image bg cghardwork = "images/cg/hardwork.jpg"
    
    #image bg cgpresidentcynthia = "images/cg/presidentcynthia.jpg"
    
    #image bg cgdonnamoore = "images/cg/donnamoore.jpg"

#Ch2 CGs
    
    #image bg cgnaturalteacher = "images/cg/naturalteacher.jpg"
    
    #image bg cgheavylifting = "images/cg/heavylifting.jpg"

    #image bg cgpagebypage = "images/cg/pagebypage.jpg"
    
    #image bg cgwritingtogether = "images/cg/writingtogether.jpg"

#Ch3 CGs

    #image bg cgheatedsituation = "images/cg/heatedsituation.jpg"
    
    #image bg cgaccident = "images/cg/accident.jpg"
    
    #image bg cgtaken = "images/cg/taken.jpg"
    
    #image bg cgmother = "images/cg/mother.jpg"
    
#Ch4 CGs

    #image bg notalone = "images/cg/notalone.jpg"

    #image bg unspokenfeelings = "images/cg/unspokenfeelings.jpg"
    
    #image bg afriend = "images/cg/afriend.jpg"
    
    #image bg courage = "images/cg/courage.jpg"
    
#Ending Images (7)
    
    #image bg samsnote = "images/endings/Sam_ending.jpg"
    
    #image bg arisletter = "images/endings/Ari_ending.jpg"
    
    #image bg bellaspoem = "images/endings/Bella_ending.jpg"
    
    #image bg cynthiasdiary = "images/endings/Cynthia_ending.jpg"
    
    #image bg samsaddress1 = "images/endings/Boring_ending.jpg"
    
    #image bg samsaddress2 = "images/endings/Diverged_ending.jpg"
    
    #image bg myletter = "images/endings/True_ending.jpg"
    
#Background Music (5)

define audio.maintheme = "music/maintheme.mp3"

define audio.regularday = "music/regularday.mp3"

define audio.sweetly = "music/Sweetly_Said.mp3"

define audio.playful = "music/playful.mp3"

define audio.emotion = "music/emotion.mp3"

define audio.sadness = "music/sadness.mp3"

label start:


    #Story Arc Flags
    
    default Ch1S_active = False
    default Ch1A_active = False
    default Ch1B_active = False
    default Ch1C_active = False
    
    default Ch2S_active = False
    default Ch2A_active = False
    default Ch2B_active = False
    default Ch2C_active = False

    default Ch3S_active = False
    default Ch3A_active = False
    default Ch3B_active = False
    default Ch3C_active = False
    
    #Persistent Data (CGs Unlocked)
    
    default persistent.Ch1SCG_unlocked = False
    default persistent.Ch1ACG_unlocked = False
    default persistent.Ch1BCG_unlocked = False
    default persistent.Ch1CCG_unlocked = False

    default persistent.Ch2SCG_unlocked = False
    default persistent.Ch2ACG_unlocked = False
    default persistent.Ch2BCG_unlocked = False
    default persistent.Ch2CCG_unlocked = False

    default persistent.Ch3SCG_unlocked = False
    default persistent.Ch3ACG_unlocked = False
    default persistent.Ch3BCG_unlocked = False
    default persistent.Ch3CCG_unlocked = False
    
    default persistent.Ch4SCG_unlocked = False
    default persistent.Ch4ACG_unlocked = False
    default persistent.Ch4BCG_unlocked = False
    default persistent.Ch4CCG_unlocked = False
    default persistent.saveblock = False

    #Paths in the Game

    #Sam's Ending - Appeal to Sam, resolve his story

    #Ari's Ending = Appeal to Ari, resolve his story
    
    #Bella's Ending - Appeal to Bella, resolve her story

    #Cynthia's Ending = Appeal to Cynthia, resolve her story

    #True Ending = Appeal to everyone and resolve all stories, for the true story
    
#Game Start
    jump Ch0