#Chaos Theory: A Visual Novel by Mark Perez

#Opening Cover Summary: Follow the story of these four close friends as they go through the treacherous years of high school. As they struggle with conflicts in the life of high schoolers between family, work, friends, and life itself. Will the story be just another drop in the ocean, or will it be something unexpected? Based on experiences from American high school, dive back to high school as what we expected it to be or just relive on how boring it actually was.

# Main Characters

define s = Character("Sam")

define a = Character("Ari")

define c = Character("Cynthia")

define b = Character("Bella")

# Unknown Characters

define sfs = Character("A Female Student")

define sms = Character("A Male Student")

# Character Sprites (24)

    #image Sam = Placeholder("boy")
    
image Sam neutral = "images/Sam_neutral.png"
    
    #image Sam happy = "images/Sam_happy.png"
    
    #image Sam sad = "images/Sam_sad.png"
    
    #image Sam embarrassed = "images/Sam_embarrassed.png"
    
    #image Sam talking = "images/Sam_embarrassed.png"
    
    #image Sam crying = "images/Sam_crying.png"
    
    
    
image Bella neutral = "images/Bella_neutral.png"
        
    #image Bella happy = "images/Bella_happy.png"
    
    #image Bella sad = "images/Bella_sad.png"
        
    #image Bella embarrassed = "images/Bella_embarrassed.png"
    
    #image Bella talking = "images/Bella_talking.png"
    
    #image Bella crying = "images/Bella_crying.png"
    
    
        
    #image Ari = Placeholder("boy")

image Ari neutral = "images/Ari_neutral.png"
    
    #image Ari happy = "images/Ari_happy.png"   
    
    #image Ari sad = "images/Ari_sad.png"
    
    #image Ari embarrassed = "images/Ari_embarrassed.png"
    
    #image Ari talking = "images/Ari_talking.png"
    
    #image Ari crying = "images/Ari_crying.png"


    
image Cynthia neutral = "images/Cynthia_neutral.png"
    
    #image Cynthia happy = "images/Cynthia_happy.png"
    
    #image Cynthia sad = "images/Cynthia_sad.png"

    #image Cynthia embarrassed = "images/Cynthia_embarrassed.png"
    
    #image Cynthia talking = "images/Cynthia_talking.png"
    
    #image Cynthia crying = "images/Cynthia_crying.png"
    
#Background Scenes (12)

    #image bg schoolyard = "images/schoolyard.jpg"

image bg sidewalk = "images/sidewalk.jpg"
    
    #image bg classroom = "images/clasroom.jpg"
    
    #image bg hallway = "images/hallway.jpg"
    
    #image bg clubroom = "images/clubroom.jpg"
    
    #image bg schoolfield = "images/schoolfield.jpg"
    
    #image bg closet = "images/closet.jpg"
    
    #image bg lounge = "images/lounge.jpg"
    
    #image bg mall = "images/mall.jpg"
    
    #image bg conferencecenter = "images/conferencecenter.jpg"
    
    #image bg park = "images/park.jpg"
    
    #image bg tower = "images/tower.jpg"
    
#Character Graphics (9)

    #image bg cghardwork = "images/hardwork.jpg"
    
    #image bg cgfrisbeefun = "images/frisbeefun.jpg"
    
    #image bg cgdonnamoore = "images/donnamoore.jpg"
    
    #image bg cgpresidentcynthia = "images/presidentcynthia.jpg"
    
    #image bg cgwritingtogether = "images/writingtogether.jpg"
    
    #image bg cgheavylifting = "images/heavylifting.jpg"
    
    #image bg cgnaturalteacher = "images/naturalteacher.jpg"
    
    #image bg cgpagebypage = "images/pagebypage.jpg"
    
    #image bg cgunspokenfeelings = "images/unspokenfeelings.jpg"
    
    #image bg cgmother = "images/mother.jpg"
    
    #image bg cgheatedsituation = "images/heatedsituation.jpg"
    
    #image bg cgaccident = "images/accident.jpg"
    
#Ending Images (7)
    
    #image bg samsnote = "images/Sam_ending.jpg"
    
    #image bg arisletter = "images/Ari_ending.jpg"
    
    #image bg bellaspoem = "images/Bella_ending.jpg"
    
    #image bg cynthiasdiary = "images/Cynthia_ending.jpg"
    
    #image bg samsaddress1 = "images/Boring_ending.jpg"
    
    #image bg samsaddress2 = "images/Diverged_ending.jpg"
    
    #image bg myletter = "images/True_ending.jpg"
    
#Background Music (9)

#Music Theme (for Game): EDM/Instrument/Classic (If not composing) or Instrumental (Composed by team artist)
#If not being composed by an artist in the team, refer to the notes below for song suggestions
#Note: Also adjust volume of music in game, so it's not too distracting

define audio.maintheme = "music/maintheme.mp3"
#Main Theme: Snail's House - Pixel Dream

define audio.regularday = "music/regularday.mp3"
#Regular Day Theme: Laxo - Popsicles With Friends

define audio.sweetly = "music/Sweetly_Said.mp3"
#Sweetly Said by Mark Perez
#Sweetly Theme: Snail's House - Love Story

define audio.playful = "music/playful.mp3"
#Playful Theme: WRLD & Richard Caddock - See You

define audio.bitterness = "music/bitterness.mp3"
#Bitterness Theme: Cole Sipe ft.Sophia Odiorne - Innocent

define audio.emotion = "music/Scarred_HeartofLove.mp3"
#Scarred Heart (of Love) by Mark Perez

define audio.sadness = "music/Scarred_HeartofStrength.mp3"
#Scarred Heart (of Strength) by Mark Perez

define audio.heartache = "music/heartache.mp3"
#Cynthia's Endgame Theme

define audio.insanity = "music/WhoAreYou.mp3"
#Who Are You by Mark Perez

label start:

    #Story Arc Flags
    
    default Ch1A_active = False
    default Ch1B_active = False
    default Ch1C_active = False
    default Ch1S_active = False
    default Ch1D_active = False
    
    default Ch2A_active = False
    default Ch2B_active = False
    default Ch2C_active = False
    default Ch2S_active = False
    default Ch2D_active = False
    
    default Ch3A_active = False
    default Ch3B_active = False
    default Ch3C_active = False
    default Ch3S_active = False
    default Ch3D_active = False
    
    default Ch4A_active = False
    default Ch4B_active = False
    default Ch4C_active = False
    default Ch4S_active = False
    default Ch4D_active = False
    
    #Persistent Data
    
    default persistent.Ch1ACG_unlocked = False
    default persistent.Ch1BCG_unlocked = False
    default persistent.Ch1CCG_unlocked = False
    default persistent.Ch1SCG_unlocked = False

    default persistent.Ch2ACG_unlocked = False
    default persistent.Ch2BCG_unlocked = False
    default persistent.Ch2CCG_unlocked = False
    default persistent.Ch2SCG_unlocked = False

    default persistent.Ch3ACG_unlocked = False
    default persistent.Ch3BCG_unlocked = False
    default persistent.Ch3CCG_unlocked = False
    default persistent.Ch3SCG_unlocked = False


#Prologue: An Ordinary Day

    scene bg sidewalk
    #play music regularday loop
    
    "It was an ordinary day, in this ordinarily boring life as a high school student..."
    
    show Bella neutral
    
    sfs "Come on, Sam! We'll be late for school!"
    
    show Sam neutral at right
    
    s "Well, we're already going to be late with that train coming by, so why bother rushing?"
    
    sfs "What train?"
    
    "The lights flash and the gates lower on the railroad crossing as the horn of the train can be heard."
    
    b "Oh, really? Just our luck!"
    
    s "You seem really out of it today, Bella. Are you getting enough sleep?"
    
    b "Er..Okay, so I only slept 4 hours last night."
                                                     
    s "Why did you stay up so late for?"

    show Bella embarrassed
                             
    b "I was binge watching the entire night and lost track of time!"
                                             
    s "Well don't bother rushing anyway, because you'll just end up sleeping in class anyway."
                                                     
    b "I don't sleep in class! I just put my head down from time to time!"
                                                                          
    s "Sure, might as well bring a pillow for those small moments."
                                                                   
    "This silly exchange is how every morning goes by."
    
    "This is the life of this ordinary kid, Sam Moore. I'm 15, a freshman in high school, to which i'm not as excited as my friend is."                                                                                                                 
    
    b "Hmm, I should bring a blanket too...Ack! Oh shut up, Sam! Don't even talk, you don't even pay attention in class and you're wide awake!"                                                                                                 
    
    "This scatter-brained girl is my childhood friend, Bella. She's the same age as I am."
                                                                  
    "We've lived in the same neighborhood since we were in elementary school and have been inseparable ever since."
    
    "Despite how clumsy and bad at time-management she is, she makes up for it in resilience."
        
    "She works overly hard in school, as well has juggling a job and club activities."
        
    "In many ways, she's very much a workaholic and is always excited for school. I still have yet to understand why..."
    
    show Bella neutral
    
    b "Anyway, you're not excited for our first year of high school at all, Sam?"
                                                                         
    s "Why should I? We're forced to attend school by law, and I don't feel motivated to work with a bunch of idiots in a 'class' that need to be babysat."

    show Bella talking
    
    b "Don't say it like that! Yeah, some people don't care about school, but I think you guys just don't understand."

    show Sam sad at right
    
    s "Understand what? That school is just a glorified teenager day care?"
    
    b "It's a place of learning and growth! There's so much you can learn in school other than testing the teachers' patience!"
    
    s "Really?"
    
    b "It's a place where you learn about yourself and grow as a person, a place to learn skills for a bright future!"
    
    "Bella' voice grows louder as she continues of her speech about school.f"
    
    b "It's a place to celebrate and live life while we're young!"
    
    show Sam neutral at right
    
    s "Well, that was an overly dramatic way to put it."
    
    show Bella neutral
    
    b "It's true though. We only experience these 4 years once!"
    
    s "No, it's what we see in another 4 years in college and then for 50 years in a job."
    
    s "Just sitting, 'working', and being told to not break anything."
    
    b "There's more to school than just that! Also, it's just what you make of it, Sam. Speaking of which, are you joining any clubs this year?"
    
    s "No, and I'd like to keep it that way. I'll just spend my 8 hours in the prison called 'school' and take my leave."
    
    b "Oh come on! That's no fun at all! You used to love to play and do all sorts of things in junior high!"
    
    s "Yeah, but it was only to get into trouble. I'd rather just keep to myself rather than have some people yell at me now."
    
    b "I won't take 'no' for an answer! Come with me after school, i'll take you to go see some clubs."

    show Bella happy
    
    b "Well, we're here at the schoolyard! I'm bummed we don't have any classes together, but I still want to see you afterschool, okay? I'll see you then!"
    
    hide Bella happy
    
    "Before I can protest, she runs off to her classes."
    
    s "Ack...Okay, whatever..."

    s "Time for another day of school..."

    hide Sam neutral
    with dissolve
    with fade
    
    scene bg classroom
    
    show Sam neutral
    
    "With that, the another school day ended with seemingly endless classes."
    
    "As I was about to leave the classroom to go meet with Bella, I catch the glare of a student with a pained look on his face right at the doorway."
    
    #stop music fadeout 1.0
    show Ari sad at right
    
    sms "..."
    
    s "Umm...Are you okay?."
    
    sms "...Uhh...No, i'm fine. Please excuse me..."
    
    hide Ari sad 
    
    "He leaves the room in a quiet fashion."
    
    s "...Okay, then..."
    
    "I know most times people just keep to themselves, but somehow I found myself approaching someone to try to help..."

    "If I remember correctly, that was the new transfer student that just got here a couple days ago. Maybe he's having a hard time getting used to things, but I don't think I should worry..."

    s "Whatever, I shouldn't let it bother me, what should bother me is that Bella is dragging me around for clubs."

    hide Sam neutral
    with dissolve
    with fade

    scene bg hallway
    show Sam neutral
    show Bella happy at left
    #play music playful loop
    
    "I meet up with Bella in the hallway to see her waiting for me outside my classroom."
    
    s "You're really serious with forcing me to join a club aren't you?"
    
    b "Come on, you've got the time and energy! Let's get you doing something!"
    
    "Bella takes my hand to go look at the various clubs in school."   
       
    with dissolve

    b "How about the science club? You get to do cool experiments and show off your research!"
                                                                                              
    s "I would have to do research for a project of my choice about 'principles that broadens the horizons', huh?"
       
    "I try to read the club poster with enthusiasm, but it only came out sarcastically."
                                                                                        
    b "Yeah, you get to explore scientific concepts ranging from ecology, like studying the environment, to inorganic chemistry, like learning about metals!"
                                                                                                            
    s "Yeah, no, i've already had my fair share of lab accidents.."

    b "Err...Don't worry, there's other clubs that might interest you."

    with dissolve

    b "How about the fencing club? You learn how to fence and use a sword for sport and defense!"
                                                                                                            
    s "Of course, you definitely want to see me with a sword..."
    
    with dissolve

    b "How about the literature club? You get to read, write, and analyze varying works of literature from manga to modern novels!"
    
    s "I'm not exactly keen with a pen...I'm sure i'll end up writing chicken scratch the whole time."
    
    with dissolve

    show Bella talking at left
    #stop music fadeout 1.0
    
    b "There's gotta be a club you're somewhat interested in, Sam! Please at least try one out before saying no!"
    
    s "I'd rather be at home playing videogames than messing around in school."
    
    show Bella happy at left
    
    b "Come on, Sam! For me? Please?"
    
    s "..."
    
    b "Would you join if it was just me and a small group of friends?"
    
    s "...."
    
    b "Hmm...I've got an idea, wait here. I'm gonna ask a teacher something about the clubs."
    
    "Bella rushes over to the teachers' office with a smile."
    
    with dissolve
    
    #play music maintheme loop
    
    s "So, what happened?"
    
    b "I was asking if we could start a club with just us, but we need at least 4 people in the club for it to be recognized by the school."
    
    b "You would be fine doing something with me and 2 other friends? Please, Sam?"
    
    "Bella stares at me, begging me to give in."
    
    show Sam neutral
    
    s "...Fine, i'll play along with your idea."
    
    s "You have anyone in mind to join us?"
    
    b "I have one other person that my teacher recommended, can you do me a favor and find us a fourth?"
    
    s "Er...Fine, i'll see what I can do. "
    
    b "Thanks, buddy!"
    
    hide Bella happy at left
    
    "Bella happily skips away."
    
    "With that settled, I head home pondering about recruiting another student for our group."
    
    #stop music fadeout 1.0
    hide Sam neutral
    
    scene bg sidewalk
    
    show Sam neutral
    
    "Here I was on my way home just casually walking home from school, then I saw another student from my class walking home from school."
    
    s "Hmm..he looks familiar..."
    
    show Ari sad at right
    
    sms "...."
    
    "He's carrying a bunch of books while blankly staring at the ground..."
    
    s "Why's he carrying all those books home? There can't be that much work in class already! Must be really a nerd."
    
    "As he was standing there stone-faced, a bunch of kids run past him and knock his books out of his arms and landing on the ground, but he didn't even react."
    
    "The kids run off not even knowing of their small accident, but he doesn't even raise a single complaint. Just another pained look."
    
    "Gathering courage, I walk over to him and start gathering his things for him."
    
    #play music bitterness loop
    
    s "Are you okay? Those kids didn't even realize they knocked you over."
    
    "He first stares at me with a bewildered look."
    
    sms "...I could handle this by myself..."
    
    show Sam talking
    
    s "You don't look like you can even handle yourself let alone these books."
    
    sms "..."
    
    s "You look down in the dumps, man. Here let me help you, charity case."
    
    sms "Just leave me be, i'm fine, really..."
    
    show Sam neutral
    
    s "Just let me help you, okay? I can tell with that face, you feel really down today, and you could use some help."
    
    "At times like these, I feel like I can get a good read on how people are feeling and something tells me he could definitely use some help."
    
    s "Here, i'll carry some of these books for you and just give me a smile, okay? I don't like seeing sad people."
    
    "I fall over trying to lift the books, misjudging their weight."
    
    s "Hehehe...Sorry, these books are heavier than I expected! I bet you've got quite some strength to be able to carry these by yourself, or that i'm just pathetically weak. Probably the latter."

    show Ari neutral at right
    
    "His sad stare livens up to a half-smile..."
    
    sms "T-thank you...Here, I will help you in assisting me."
    
    #stop music fadeout 1.0
    
    "He takes half of the books and carries them entrusting me with the other half."
    
    s "Anyway, I saw you earlier, you're from the same class from me, Ari, wasn't it?"
    
    #play music regularday loop
    
    a "Yeah...I'm sorry, I didn't catch yours."
    
    s "Well, my name's Sam. I'm 15 and a freshman at our school, you're a transfer student right?"
    
    "He nods in confirmation."
    
    s "You're also a junior, right? I can tell you're stuck in that class with me because you need that to graduate right?"
    
    a " Indeed."
    
    s "Why are you carrying all these books anyway? It's only the beginning of the first half of the school year! These books are really frickin' heavy!"
    
    a "Those books are my college textbooks for my dual-credit classes, I was taking initiative to read ahead for class."

    s "You're quite an honors student, huh? Sorry, i'm not too impressive as a student myself."

    s "Here, i'll carry these for you anyway. How far do you live from here?"
    
    a "Just three blocks from here. Thank you again for helping me. I apologize that my words do not express all of my gratitude. Here, I will offer you some monetary reward for your deeds."
    
    s "No, it's alright. I wanted to help a fellow today. Seeing you cheer up a bit is enough. It feels good to help! Hehehe!"
    
    "I walk with Ari to his house and find that he only lives a couple blocks away from my house."
    
    s "Do you seriously carry around these books and a backpack to and from school everyday?"
    
    a "It is not an issue for me, it is my daily routine."

    show Sam happy
    
    s "Jeez, I guess you're really getting some serious exercise everyday. I still have trouble lifting half of these huge books!"

    show Ari happy at right
    
    "I let out a short chuckle, Ari's starts to chuckle too."

    show Ari neutral at right
    show Sam neutral

    "We casually get to know each other on the way home talking about school, the weather, and other small talk."

    s "So, how are you liking the city? It's really crowded, but it has its charms I would say."
    
    a "I would agree with you with the fact that it is charming, but it feels lonesome sometimes."

    s "What would make you say that?"

    a "I reside in the city with my aunt, but she's occupied with work frequently. I am studying here and the rest of my family is still back home in Japan."

    s "Oh...I live with my family here, but I never see my parents much because they're working, so I guess we kinda have that in common. Also, you speak English way too well to be Japanese."

    a "My mother is American, so I learned it from her."
    
    s "Oh, cool!"

    s "You said you were in dual-enrollment classes, you really take school very seriously, huh? I admire that, but I don't see myself doing that."

    a "Why not?"

    s "You plan to be a lawyer, engineer, or doctor?"

    a "I aspire to be a surgeon as my family hopes me to be."

    s "It's hard for me to find motivation to even get up for school. I'll probably just end up working at a bar, or shop, but I don't see that much as a problem." 
    
    s "I just don't see myself having much potential and i'm mediocre at best with everything in school."

    a " There is probably something you are proficient and passionate about, you just have to find it and work hard. Everyone has limitless potential and anything can change."

    a "I want to be able to help people. It is not about the skills or the work that matters, rather it is the drive to achieve a goal and fulfill your life with a purpose."

    "I could only stand mute, without a response."

    a "Sorry, I know it sounds rather cliche, but I think it is the truth." 
    
    a "I know it would be dreadful working over 50 years with an occupation you despise, and I would like to live through those 50 years of work on my terms, doing what I love doing."

    s "No, man it's fine. In fact, it's cool you see things that way."

    a "You humble me with your praise..."

    s "Man, I don't even know what to say, or even do with my life. You have a clearer idea of your life."

    a "You will have a bright future ahead of you. You were brave enough to help me, who was just a stranger to you not long ago. You could do even more."

    s "Heh, thanks, man. I appreciate the encouragement at least."

    a "Oh, here we are. This is my house. Thanks for helping me carry my books...You helped me in more ways than one."

    s "No problem, I didn't have anything better to do and I don't think I did that much. Hehehe..."

    "I was preoccupied with helping Ari, I almost forgot about finding someone for Bella's club."

    s "Hey, Ari, are you in any clubs or do you know anyone who's free for one? I need another person for my friends' club."

    a "No, I do not know anyone in school, but you. What is it that your organization plans to accomplish?"

    s "Umm...I don't know, my friend wants to start a club with me and one other person, and we just need a fourth. I'm guessing we just hang out with the four of us then figure what we want to do."

    show Ari embarrassed at right

    a "Hmmm...Okay, I might just drop in. It would be nice having something to do in my spare time at school with someone familiar. If that is okay with you..."

    #stop music fadeout 1.0
    show Sam happy
    #play music maintheme loop

    s "Yeah, friend! I would be happy if you came!"

    show Ari happy at right

    a "Friend?"

    s "I know we just met, but yeah, friend! You seem like a cool person, and it would help you to know someone in school, so yeah friend! How about it?"

    "He stares at me with sheer joy."

    a "Yeah, friend. I will converse with you later."

    hide Ari happy at right
    #stop music fadeout 1.0

    "Ari waves as we exchange goodbyes for the day. I head home with newfound happiness."
    
    s " He talks quite oddly and overly formal, but he's a cool guy. It ought to be interesting with him around."

    with dissolve
    show Sam neutral at left

    "I head home and see Bella and an unfamiliar face waiting for me at the gate."

    #play music regularday loop
    show Cynthia neutral at right
    show Bella neutral

    b "Hey, Sam! Did you find another person to join our group?"

    s "Yeah, his name's Ari. He's a junior in one of my classes and he lives a couple blocks from here. Anyway, who's your partner there?"

    c "Hello, my name's Cynthia and i'm a junior just like your gentleman friend. How are you?~"

    "She introduces herself with a sultry voice."

    show Sam embarrassed at left

    s "Uhh...G-good.."

    "I stammer as i'm frozen by her voice."

    c "I had a falling out with my club, so my teacher pointed me to Bella who was starting a new club with 2 others. I hope we get along together!~"

    b "Yeah! Me too, i'd like to meet Ari too! He lives nearby doesn't he?"

    "I nod."

    b "We could all walk to school together tomorrow since we all live fairly close! That way, we can get to know each other better! How does that sound?"

    show Sam neutral at left

    s "Sounds like a great idea, but we still need to find out what to do for activities for our club."

    show Bella happy

    b "Don't worry, whatever it is, we'll have fun together!"

    show Sam happy at left

    "There it is again, her gleaming smile. It's hard to resist smiling."

    b "Well then, i'll see you guys tomorrow morning!"

    c "I'll look forward to it!~"

    hide Bella happy
    hide Cynthia neutral at right

    "Bella and Cynthia part their separate ways for now."
    
    show Sam neutral at left

    s "Alright! See ya!"

    "I wave after them."

    hide Sam neutral at left
    #stop music fadeout 1.0
    #play music maintheme loop

    "What a change to my life. Somehow, I got wrapped into a small club by Bella and met two new interesting people. I guess I have something to look forward to now at school to maybe make it a little more interesting."

    "This must be what Bella means by it's what you make of it..."

    show Bella neutral at left

    "Bella..."

    show Ari neutral

    "Ari..."

    show Cynthia neutral at right

    "Cynthia..."

    "These are three people I know best right now at my first year of high school. In a way, it's kinda pathetic I don't know many people in school, but I have hope that it'll be a good first year."

    "I'm pretty close to Bella already, but I have chances to get closer to Ari and Cynthia, to be close friends."
    
    hide Bella neutral at left
    hide Ari neutral
    hide Cynthia neutral at right

    "The feeling of hope and determination is warm, but then the thought of reality stings of how boring and dissappointing everything could be."

    "No, I should make the best of my time here and make my story more than just an ordinary life as a high school student."

    "Who knows, maybe something incredible might happen. Emphasis on 'might'."
    
    #stop music fadeout 1.0

    with dissolve
    with fade

    #End of Prologue
    
    #Paths in the Game

    #Boring Ending - Don't appeal to any friends

    #Sam's Ending - Appeal to Sam, resolve his story

    #Bella's Ending - Appeal to Bella, resolve her story

    #Ari's Ending = Appeal to Ari, resolve his story

    #Cynthia's Ending = Appeal to Cynthia, resolve her story

    #True Ending = Appeal to everyone and resolve all stories, for the true story

    #Diverged Ending = Send Sam to insanity, for the forbidden story

#Chapter 1: Expanding Universe

    scene bg sidewalk
    #play music maintheme loop
    
    " I never thought that I would say that I'm looking forward to school since kindergarten, but here I am actually going to school early. I wonder how today will go?"
    
    " As usual morning routine, I get ready for school and walk to school, meeting up with Bella along the way."
    
    show Sam neutral
    
    s "Mornin', Bella! How's it goin?"
    
    show Bella happy at left
    
    b "Fantastic! I actually got some sleep last night!"
    
    s "You got a good night's rest for once?"
    
    b "Hehe...I just couldn't wait for today to happen!"
    
    s "Let's go meet Ari at his house, follow me it's only a couple blocks from here."
    
    b "Let's also go to Cynthia's house along the way, so we can all walk to school together!"
    
    s "The more the merrier!"
    
    "We head out to go meet Ari at his house."
    
    with dissolve
    
    show Bella neutral at left
    
    show Ari neutral at right
    
    s "Mornin'!"
    
    a "Ah...yes, good morning Sam, and good morning to your partner as well. May I ask your name?"
    
    b "The name's Bella! You're Ari, right? Nice to meet you, Sam says you're the cool guy joining our club?"
    
    a "Well yes, but I was going to ask what we do in the club. I am happy to join the club to get to know others, but I would like to be informed of our duties."
    
    b "Don't know yet, we're just hanging out I suppose!"
    
    a "Hanging out?"
    
    s "Yeah, we'll decide when we get there!"
    
    a "Alright. Whatever it may be, I am at your service."
    
    "Ari takes a small bow."
    
    s "You don't need to be so formal all the time, Ari. It's gonna be as carefree as it gets."
    
    show Bella embarrassed at left
    
    b "Hehehe...He's quite a gentleman."
    
    s "Anyway! Let's go meet Cynthia, we ought to introduce everyone seeing as we'll be together for a while."
    
    hide Bella embarrassed at left
    
    "After meeting up with Ari, we travel further down the road to meet Cynthia at her house."
    
    "Cynthia answers the door."
    
    show Cynthia neutral
    
    c "Morning everyone, i'm still getting ready so bear with me. I always get to school fashionably late.~"
    
    b "Ari, this is Cynthia, she's another junior in your class and she's also joining us in our club."
    
    c "Hi!~"
    
    a "Ah...Yes, salutations."
    
    c "I'll see you guys in a bit, give me 5 minutes to get ready.~"
    
    hide Ari neutral at right
    hide Sam neutral
    
    "With that, she hastily closes the door to prepare and we wait outside her house for her."
    
    with dissolve
    
    "We speak to her parents for a brief moment as her classmates, but about 15 minutes had passed until Cynthia came out ready to join us."
    
    show Cynthia neutral
    show Sam neutral at left
    show Ari neutral at right
    
    c "Ok, ready! I didn't make you guys wait too long did I?"
    
    "She gives a slight chuckle."
    
    s "Errr, noo..."
    
    "My impatience tells me otherwise."
    
    a "No, not at all. Your parents also gave us wonderful company."
    
    s "Yeah, you've got a big family, Cynthia! Your mom told us you have 5 other siblings, how do you get by with them?"
    
    c "Stuff just happens."
    
    s "Seriously? Everyone just goes crazy?"
    
    c "We already trust ourselves to take care of each other. It's what you learn when you're with everyone all the time."

    a "I assume you are the only child in your family, Sam?"
    
    s "Yeah, I kinda envy you guys."
    
    hide Ari neutral at right
    show Bella neutral at right
    
    b "C'mon guys, let's get going or we'll be late!"
    
    hide Sam neutral at left
    hide Cynthia neutral
    
    "We head to school with the whole club gathered and casually make more small talk."
    
    #stop music fadeout 1.0
    with dissolve
    with fade
    
    scene bg schoolyard
    #play music regularday loop
    
    show Bella neutral at left
    show Sam neutral
    show Cynthia neutral at right
    
    b "Well, here we are! I had fun talking to you guys, but I gotta get to class, I have Biology lab first! Sorry I have to go so soon!"
    
    s "See ya, I guess you'll meet us at the clubroom right?"
    
    b "Yeah, bye guys!"
       
    hide Bella neutral at left
    
    "She waves as she's sprinting to get to class."
    
    show Ari neutral at left
    
    a "..."
    
    c "You've been awfully quiet this whole walk to school, Ari. Are you a little shy?~"
    
    a "I suppose, or rather I just find it hard to talk much."
    
    s "Yeah I gotcha."
    
    c " Well hopefully, we can change that and get you to come out of that shell.~"
    
    s " Anyways, I also gotta get to class early, i'll see you guys in the clubroom as well."
    
    c "See you around.."
    
    hide Ari neutral at left
    hide Cynthia neutral at right
    hide Sam neutral
    
    "We all part ways to our classes and go on with our schoolday."
    
    with dissolve
    with fade
    
    scene bg hallway
    
    "Another schoolday ends, passing the same boring way as usual."
    
    "As usual, Bella's outside my classroom waiting for me. Her presence always brings light to the room."
    
    show Bella neutral at left
    
    b "Hey Sam! Ready for your first day of our club?"
    
    show Sam happy
    
    s "Seeing as you dragged me into it, yeah. Always up to the crazy stuff we do."
    
    show Bella happy at left
    
    b "That's the spirit!"
    
    hide Sam happy
    hide Bella happy at left
    
    "We walk down to the clubroom and meet up with Ari and Cynthia already in the clubroom."
    
    with dissolve
    with fade
    
    scene bg clubroom
    #stop music fadeout 1.0
    #play music maintheme loop
    
    "Ari is at one corner of the room reading a bunch of large textbooks and Cynthia is painting her nails at another corner of the room."
    
    show Bella happy
    
    b "Alright, that's everyone here! Let's get started with our club meeting!"
    
    show Sam talking at right
    
    s "What do we do for our club activities anyway?"
    
    show Cynthia neutral at left
    
    c "If it gives me a place to just hang out, i'm cool with whatever."
    
    hide Sam talking at right
    show Ari neutral at right
    
    a "..."
    
    hide Ari neutral at right
    hide Cynthia neutral at left
    
    b "I gave it some thought and think that for our club, we should make it an upperclassman and underslassman peer club!"
    
    show Sam neutral at right
    
    s "What does that mean?"
    
    b "Our club is a place where freshmen/sophomores meet with juniors/seniors to help each other out with school whether it's getting used to things around here or just academic help!"
    
    s "That's actually cool, you made up something to hide the fact we're just slacking and hanging out here."
    
    b "Interesting you see it that way, but our club should be a club where we can just chill and enjoy being at school."
    
    b "I know you didn't want to try anything too crazy and I want you to like being in school, Sam. So, i've made this club just that."
    
    show Sam embarrassed at right
    
    s "Bella..."
    
    show Bella embarrassed
    
    b "You can leave if you don't want to be here, Sam. I understand that, but I just want to make friends and be here with you, Sam. I just wanted to do something all of us might enjoy together."
    
    s "Bella, thanks so much for that, but i'm not leaving."
    
    s "I actually kinda looked forward to being here and meeting Cynthia and Ari here, and of course, being here with you."
    
    s "Now come on, it's getting awkward now. Let's go do something else now."
    
    hide Bella embarrassed at right
    hide Sam embarrassed
    
    show Ari talking at right
    
    a "I am a new student here, so I wonder if I will be able to offer assistance, but I will relay any information that could be of use to everyone."
    
    show Cynthia happy at left
    
    c "That's a cool idea to make a place to hang out for us with this club. Don't worry, i'll tell you all about what's going on around here!~"
    
    hide Ari talking at right
    hide Cynthia happy at left
    
    show Bella neutral
    
    b "Alright, for our first peer club meeting, our activity is to just introduce ourselves to each other and get to know each other better! Feel free to open up a little, whatever is said here, stays here."
    
    hide Bella neutral
    
    "Our club activity is to hold meetings between juniors and freshmen to help each other out in school and hang out. It couldn't be any better than just simply hanging out!"
    
    show Cynthia neutral
    
    c "Don't be scared to come at meet me, darling!~"
    
    c "I would be happy to talk about anything with you."
    
    hide Cynthia neutral
    
    "Cynthia gives me smile before heading back to her seat to painting her nails waitng for me to accept her invitation."
    
    "I do want to hang out with everyone here, but I can only spend so much time with everone at a time a day, but i'll have plenty of time to enjoy my time here, I guess."
    
    with dissolve
    with fade
    #stop music fadeout 1.0
    #play music playful loop
    
menu:
    
    "Who should I go hang out with?"
    
    "Ari!":
        jump Ch1A
    
    "Bella!":
        jump Ch1B
        
    "Cynthia!":
        jump TrueFork1

#Chapter 1A: Sam and Ari

label Ch1A:
    
    with dissolve
    with fade
    show Sam neutral at right
    
    s "Hey, Ari! We already kinda know each other, so for now let's just hang out. What's going on?"
    
    show Ari neutral
        
    a "Just reading some material for my classes. Would you be interested in reading about thermodynamics?"
    
    s "Thermo-what now?"
    
    a "Thermodynamics, studying the transfer of energy through systems."
    
    s "In simple terms that would be..."
    
    a "Looking at how objects heat up and cool down."
    
    s "Oh, cool. For what class is this for?"
    
    a "It could be applicable to many different fields of sciences, but I am reading this for Biology, Chemistry, and Physics."
    
    s "I never saw any of this complicated stuff in Chemistry, is this for your college classes?"
    
    a "Indeed, that would explain the complexity of the material."
    
    s "Is it easy for you? I really didn't like Chemistry..."
    
    a "Relatively speaking with my experience and my aptitude for higher level sciences, yes I find it fairly simple to understand fundamental physics at a collegiate level."
    
    s "You're just extremely smart, aren't you?"
    
    a "There's always someone smarter than you. I am just another student like many others."
    
    s "If you say so, but you're definitely not like a lot of us here."
    
    show Ari sad
    
    a "..."
    
    "Suddenly his mood changes as he shows a downcast stare at his books."
    
    "I only meant what I said as a compliment, but it seems to have an opposite effect on him. Did I touch on something sensitive to him?"
    
    hide Sam neutral at right
    
menu:

    "Should I help Ari?"
    
    "Yes":
        jump Ch1AY
        
    "No":
        jump Ch1No

#Ch1A Accepted
label Ch1AY:

    $ Ch1A_active = True
    $ persistent.Ch1ACG_unlocked = True

    show Sam talking at right
    
    s "Oh, sorry did I say something wrong?"
    
    show Ari neutral
    
    a "No, Sam. You are fine. It's just I have been feeling a little down lately. I find myself so unable to focus in my studies. It is quite hard for me to even read my class material."
    
    s "Are you doing alright in class?"
    
    show Ari sad
    
    a "Yes, but that is not the issue. Or is it? I really do not know."
    
    a "I am fairly content as it is. No worries of food, shelter, or other necessities. Good grades, no troubles with my environment, but I still find myself feeling down."
    
    "He stares at the ground with a blank stare similarly to how I first met him."
    
    show Ari neutral
    
    a "Sorry to make you have to listen to my ramble. Please do not worry about me. Perhaps I just need some time alone."
    
    s "Err..."
    
    "It feels extremely wrong to just leave him like this, but I am unsure what to do."
    
    "Until it hit me. Literally, I was messing around with a frisbee I found in the room as Ari was talking and it bounced off the wall and hit me square in the head."
    
    show Sam embarrassed at right
    
    s "Ouch! That's on me."
    
    s "Wait...That's it!"
    
    a "Come again?"
    
    s "You know what you need? Some time to unwind and relax. I'll let you know what I do when I feel down like this!"
    
    a "What would that be?"
    
    show Sam happy at right
    
    s "Playing games! Whether it's videogames or just sports, I always feel better playing. So why don't we play in the field?"
    
    a "I am not against this idea. What do you suppose we do?"
    
    s "Hmmm, let's see..."
    
    s "Have you ever played ultimate frisbee?"
    
    a "No, but I do at least have heard of it."
    
    s "Come on, i'll show you and the girls how to play."
    
    show Bella neutral at left
    
    b "Hey, Sam! What's up?"
    
    s "Is it okay if we go out to the field today and play ultimate frisbee?"
    
    hide Sam neutral at right
    show Cynthia neutral at right
    
    c "That sounds like fun, sure why not?"
    
    b "Seems like everyone is up for it. I'll just ask my teacher if it's okay."
    
    hide Bella neutral at left
    show Sam neutral at left
    
    a "Might as well start gathering our belongings to move to the field."
    
    s "Right."
    
    hide Sam neutral at left
    hide Ari neutral
    hide Cynthia neutral at right
    
    "And so, we got the okay from Bella's teacher and got together to play some frisbee at the field."
    
    with dissolve
    with fade
    
    scene bg schoolfield
    
    show Bella neutral at right
    
    b "This part of the field isn't used by anyone because the football team isn't meeting today, so lucky for us."
    
    show Sam neutral
    
    s "I know, what timing right?"
    
    show Cynthia neutral at left
    
    c "So, teach us how to play frisbee Sam."
    
    hide Cynthia neutral at left
    hide Bella neutral
    
    show Sam talking
    
    s "Alright, so the rules are simple."
    
    "I quickly explain the simple rules of the game to everyone. In a way, it's kinda like football with a frisbee."
    
    s "For our little game, it's a best of 3 goals."
    
    s "It seems a lot of rules, but you'll get the hang of it."
    
    show Sam neutral
    
    s "So what should the teams be?"
    
    show Bella neutral at left
    
    b "How about you and I make a team, and Ari and Cynthia are the other team?"
    
    show Cynthia neutral at right
    
    c "Seems fine with me."
    
    hide Bella neutral at left
    show Ari neutral at left
    
    a "Likewise."
    
    s "Ok, that's it I guess. Now let's start!"
    
    hide Ari neutral at left
    hide Sam neutral
    hide Cynthia neutral at right
    
    with dissolve
    with fade
    
    scene bg cgfrisbeefun
    
    s "Come on, Bella, let's show em what we've got!"
    
    c "Alright Ari, show them we're no slouches either."
    
    a "I will do my best."
    
    b "Alright we've got the frisbee first!"
    
    "The game starts off without a hitch, Bella gets a good pass to me and we pass to each other to make it to the half way point of the field."
    
    a "We have a slight beginner's disadvantage here, but that will not deter us!"
    
    c "Yeah! Let's do this!"
    
    "Cynthia tries to block my pass to Bella, but I still got to throw the frisbee."
    
    b "I got it!"
    
    "With blinding speed, Ari intercepts the frisbee swiftly."
    
    a "Now, it's my turn!"
    
    "Ari nods and makes hand signals to Cynthia motioning her to move for a pass."
    
    s "Like I don't know what you're doing!"
    
    "I sprint to try to intercept Ari's throw with Bella trying to block it, his feint catches both Bella and I off guard."
    
    "Ari quickly passes the frisbee at a low angle and Cynthia catches the frisbee in response."
    
    "Ari doesn't waste time to reposition himself for another pass."
    
    "Cynthia tries to quickly pass to Ari, but fumbles with her throw."
    
    c "Whoops!"
    
    "The frisbee flies at a crescent towards the ground, but Ari sprints to catch it just in time."
    
    s "Not, bad! We've got to be in our A game with this!"
    
    "The volley starts to go back and forth with the frisbee switching sides very frequently."
    
    "Cynthia isn't very accurate with throwing the frisbee nor is she good at catching, but does make up for it with being able to communicate well with Ari." 
    
    "Ari really doesn't talk much, but does communicate through hand signals."
    
    "Bella is quick to move around the field a lot and I am very precise at throwing and catching the frisbee, only to have Ari with his sneaky moves to intercept it."
    
    "We take a timeout to talk with our teammates as no one has scored yet and need a small break."
    
    s "Haahhh...Haahhh. Ari isn't making it easy at all! He's really good at intercepting our passes!"
    
    b "..Haahhh... Yeah, even I have a hard time keeping up with him. Cynthia does a good job to keep up with him."
    
    s "We gotta step it up a notch! They aren't making it easy, even though they're new to this."
    
    "We continue onto the field to continue the match. Cynthia compliments us for our good play, Ari is still silent, but with a smirk on his face."
    
    "Second half of the game, Ari has completely shut down our blocking strategy! Within 5 passes, Ari scores the first goal."
    
    c "Woohoo! Nice one!"
    
    "Ari smiles and goes over to pass the frisbee to me."
    
    s "Well i'll be, you're pretty crafty with maneuvers."
    
    "It becomes another back and forth volley, but eventually after 4 different turns with the frisbee, Bella and I score our first goal."
    
    b "Alright!"
    
    s "One more decides it!"
    
    "We really get into our little game of ultimate frisbee until suddenly I mess up my throw because of the wind."
    
    s "Whoa, I messed that up."
    
    "I throw the frisbee really hard and accidently throw it at an open window and a loud crash is heard from the window."
    
    s "Oh, man. That's on me for sure."
    
    with dissolve
    with fade
    
    scene bg hallway
    #stop music fadeout 1.0
    #play music regularday loop
    
    show Bella embarrassed
    
    b "Luckily no one got hurt and no one was in the room where the frisbee flew through. Apparently the frisbee knocked off a small bunch of beakers in the lab."
    
    show Sam embarrassed at right
    
    s "Well good that no one got hurt."
    
    b "It was an accident so we don't have to serve detention, but we still have to pay for the broken equipment."
    
    s "Oh crap. I got it, although my parents won't be too happy with that."
    
    show Sam neutral at right
    
    s "It's okay, i'll try not to be so accident prone next time. Did you guys at least have fun with frisbee, although we won't be doing it for a long while?"
    
    hide Bella embarrassed
    show Cynthia neutral
    
    c "Yeah, it was fun until you broke some stuff."
    
    show Ari neutral at left
    
    a "It was quite exhilirating."
    
    s "You're not only really athletic, you're really sneaky."
    
    show Ari embarrassed at left
    
    a "Really? I just went out there and lost myself in the game. Thank you for that fun game."
    
    "His demeanor completely changed after the game. I guess it worked in cheering him up."
    
    show Sam happy at right
    
    s "Hehehe..."
    
    a "Come on, let's go help clean up the mess we made now."
    
    show Sam neutral at right
    
    s "Right."
    
    hide Sam neutral at right
    hide Cynthia neutral
    hide Ari embarrassed at left
    
    "And so, we spent the rest of the afternoon cleaning up the broken glass and apologized to the science teacher in that classroom."
    
    show Sam embarrassed
    
    s "Sorry, it got messy because of my clumsiness, Ari."
    
    show Ari neutral at right
    
    a "Think nothing of it. Everything was resolved and no harm done. Also, thanks for teaching me to play that game."
    
    a "Thanks for showing me something new to try, really encourages and inspires me to try something like that another time."
    
    show Sam neutral
    
    s "No problem! Anyway, it was my pleasure to teach ya! Holler at me if you wanna go try something else the next time we meet. I know you'll be awesome at anything I try to teach you."
    
    a "Why do you say that?"
    
    s "You're a quick learner, you've got potential to be awesome at a lot of things. I just know it."
    
    show Ari happy at right
    
    a "Thanks, I really appreciate your encouragement."
    
    s "Same time at the club Thursday?"
    
    show Ari neutral at right
    
    a "We still will probably see each other to school, but when do we meet here again?"

    s "Bella wants us to meet at Tuesdays and Thursdays, she's got work and club stuff from other clubs on the other days and Cynthia requested to meet only at those days. Does it work for you?"
    
    a "Of course, I am flexible."
    
    s "Ok, cool! See ya then!"
    
    hide Ari neutral at right
    hide Sam neutral
    
    "We all went home together that day and every time after our club meetings really enjoying our time together. I really am enjoying myself in the club."
    
    "As I spend more time with Ari, he starts to speak up a little more and has become less shy with us. Hopefully I get to know more about him.."
    
    #stop music fadeout 1.0

#End of Chapter 1A
     
    jump Ch2

#Chapter 1B: School and Work

label Ch1B:

    with dissolve
    with fade
    show Bella neutral
    
    b "You wanna hang out with me today?"
    
    show Sam neutral at right
    
    s "Yeah, I just felt like starting with you first. I know you the best after all..."
    
    show Bella sad
    
    b "Don't you want to go meet with Cynthia or Ari? They're probably much more interesting than me."
    
    s "Don't say that, you're interesting."
    
    b "Yeah? In what way?"
    
    s "Err...You can drink milk through your nose!"
    
    show Bella embarrassed
    
    b "Hey! That was one time and it was an accident!"
    
    show Sam happy at right
    
    s "Hehehe..."
    
    show Bella happy
    
    b "Hehe...Okay i'll take it."
    
    show Bella embarrassed
    
    b "I don't even know where to start. Ummm..."
    
    hide Sam happy at right
    
    "Bella seems to be tongue-tied with her words. Usually she's very talkative and this is one of the rare moments where she becomes mute."
    
menu:
    
    "Should I help Bella?"
    
    "Yes":
        jump Ch1BY
        
    "No":
        jump Ch1No
        
#Chapter 1B Accepted
label Ch1BY:

    $ Ch1B_active = True
    $ persistent.Ch1BCG_unlocked = True
    
    show Sam neutral at right

    s "How about we start with something simple to talk about?"
    
    show Bella neutral
    
    b "What should we talk about then?"
    
    s " How about we just talk about how school is going?"
    
    show Bella embarrassed
    
    b "Okay..."
    
    show Bella neutral
    
    s "Here i'll go first."
    
    s "Umm...School is alright, I guess..."
    
    "I try to be indifferent about it, but I know what I said is definitely not how I feel about school."
        
    show Sam sad at right
    
    s "Honestly, school has been very dull for the most part."
    
    s "Every class is boring, it feels really insulting and stupid to be in stupidly easy classes with all the other freshmen in our class."
    
    s "I just really hate how we're forced to take most of the same classes as freshmen."
    
    b "Really? I've been struggling through these classes? How is it stupidly easy for you?"
    
    s "I learned the stuff ahead of time already, my parents forced me to take summer school. It's just the same shit anyway."
    
    b "Is that why you don't even pay attention in class?"
    
    s "I don't need to! I'd rather not sit and be tortured by people who can't even read short lines of the textbook for an answer."
    
    b "I shouldn't talk anyway, I sleep through class."
    
    show Sam talking at right
    
    s "Do you even get enough sleep?"
    
    b "Aside from club activities in this club, student council, and the literature club, i've got a job to keep outside of school, I have to babysit my siblings, and I do all the chores in my house."
    
    s "That's right, you're the oldest in your family. You also work an afternoon shift at that cafe downtown."
    
    b "I don't get a lot of time to study or sleep. By the time I get home, I have to prepare dinner, clean up the house, and take my siblings to sleep." 
    
    b "By the time I get time to myself, it's already 10 PM, and I use about 2-4 hours trying to get homework done."
    
    s "Geez, I didn't know it's gotten that rough for you."
    
    b "Well, the main reason I got that job was to start saving up for college, because my parents have no money for it."
    
    s "How are you gonna get to college if you can't even get through high school with your sanity?"
    
    show Bella sad
    
    b "Don't worry about it, i'll be able to handle all of this."
    
    s "If you say so, i'm just worried for you."
    
    show Sam neutral at right
    
    s "Anyway, you got anything else to do today aside from homework and this club?"
    
    show Bella neutral
    
    b "Yea, i'm going to run for student body president, so I gotta set up for my campaign."
    
    s "Cool, I guess. It's just probably another popularity contest though."
    
    b "No, it's not! Student body president is a very important position!"
    
    s "What do you exactly do as student body president?"
    
    b "As president, you preside over student council meetings, coordinate and plan student events and pep rallies, and much more!"
    
    s "Sounds way too much hoopla over deciding whether to have confetti or strobe lights in the assembly."
    
    b "Oh, don't say it like that!"
    
    s "I just don't see the hype over planning events where we're forced by the school to attend."
    
    b "We're trying to make them fun for us."
    
    s "In the end, it's still the teachers who have final say in things."
    
    b "We work to negotiate with the teachers to make the events that both the students will like, but also within reason."
    
    s "Alright, then."
    
    b "Speaking of which, I need to go make those posters for the campaign, can you stay here and hold the meeting?"
    
    s "No, i'll go help you out with those."
    
    show Cynthia talking at left
    
    c "I don't have anything to do right now, so i'll go too."
    
    hide Sam neutral at right
    show Cynthia neutral at left
    show Ari talking at right
    
    a "I shall provide aid for your task."
    
    show Ari neutral at right
    
    b "Thanks, everyone! Are you guys sure you want to help me with this instead of our club stuff right now?"
    
    c "This could be considered club activity, we're helping you with academic help and I could show you where the around the school."
    
    b "Okay, then! Seems that it's good with you guys, so let's get to it!"
    
    hide Cynthia neutral at left
    hide Bella neutral
    hide Ari neutral at right
    
    with dissolve
    with fade
    
    scene bg cghardwork
    
    b "Ari, go pick up some copic markers, pens, and other coloring stuff in the closet of the art club."
    
    a "Right."
    
    c "The room should be down the stairwell down the hall."
    
    "Ari and Cynthia take off to go pick up some supplies."
    
    b " Sam, stay here and help me design my posters here."
    
    s "You're asking me to design the poster? I'm not very creative and the most creative thing i've made is the 'S' sign from 6 straight lines."
    
    b "Don't worry, i'm sure we'll come up with something good together. It's better to have two heads than one."
    
    s "If you say so."
    
    "We spend about 10 minutes coming up with a basic idea for a slogan, but we come up with nothing that is worth of a small consideration."
    
    b "We gotta come up with something already!"
    
    s "I think you're trying too hard with coming up with a slogan. It has to be something simple."
    
    b "I don't know."
    
    "Ari and Cynthia return with huge boxes filled with paper, markers, and other art supplies."
    
    a "I hope this will suffice."
    
    c "It's quite a lot, but we definitely have all that we need to make our poster stand out!"
    
    s "Hey, you're back! Anyway, we're trying to come up with a campaign slogan to put on the poster."
    
    a "It seems that you have drawn what appears to be the mythical unicorn on the poster."
    
    c "A unicorn with its own clouds and rainbows, how cute! A little too cute..."
    
    s "Still need something to go with it..."
    
    a "How about something simple to accompany it? Let me ask, what do unicorns remind you of?"
    
    b " Something that comes only in dreams. Something magical."
    
    c "Where can we go with that?"
    
    a "How about something simple, yet common like this: 'Teamwork makes the dream work!' "
    
    b "Ari, that's brilliant!"
    
    a "Really? I do not see its merit as that groundbreaking."
    
    s "Hey, that's pretty good!"
    
    c "I swear i've heard that line from somewhere."
    
    s "Well now, we've got something! Put it on the poster with bold letters!"
    
    c "Lots of glitter!"
    
    a "Please do not add so much glitter that it makes one blind."
    
    "Equipped with an idea, copic markers, glue, and glitter, we get to work on our poster. It turns out to be quite 'something'."
    
    b "I love it!"
    
    s "Err...It's...How can I say this..."
    
    a "Cute."
    
    s "It's really girly!"
    
    c " Is that a bad thing?"
    
    s "It stands out for sure."
    
    a "Then, we've reached our objective."
    
    b " It turned out great guys! Let's get this copied and posted!"
    
    s "Well, she's happy with them, so it's all good."
    
    "We get the posters copied, laminated, and approved to be posted. It took quite a while to get all of this done that it was already 7PM when we got done."
    
    s "We sure did a number on the color printer and the glitter."
    
    c "Heh, I got a little carried away with the glitter."
    
    b " They all look great with glitter!"
    
    a "It does serve as good eye candy."
    
    s "It definitely took a while, but we got it done!"
    
    b "Teamwork truly does make the dream work!"
    
    s "Hehe, you're really embracing that slogan."
    
    b "Thank you everyone, for helping me out with this! I hope there's some way I can pay you for your work."
    
    b "No, you don't have to pay a single dime! It was fun to help out!"
    
    a "I agree, it was entertaining."
    
    s "Yea, don't worry about it. It was part of the club work."
    
    b "Hehe...Thanks guys."
    
    with dissolve
    with fade
    
    scene bg sidewalk
    #stop music fadeout 1.0
    #play music regularday loop
    
    "We shortly all head home together after a long day of work."
    
    "We all casually talk about what's going on in school the next day and plans for tomorrow. We see Cynthia and Ari off, leaving me alone with Bella."
    
    show Bella neutral
    show Sam neutral at left
    
    b "Today, was fun! We got to work together as a team."
    
    s "You definitely needed a team to help with that much work! Don't tell me you planned on doing that all by yourself?"
    
    b "Sorry, I didn't want to bother anyone with it."
    
    s "Dude, i'm your best friend! If you need a shoulder, i've got one for you to lean on. Don't think it's a bother, because your bothers are mine as well, okay?" 
    
    s "You're seriously going to hurt yourself from doing too much work."
    
    s "I know you're a little of a workaholic, but there's such as thing as too much work, even if you're willing to do a lot of work. You can only do so much at a time!"
    
    show Bella happy
    
    b "Thanks, Sam. It means a lot."
    
    "She gives me a bright smile and again it gives we a warm feeling, but this time it feels warmer than before."
    
    b "You're like a big brother to me, always looking after me."
    
    show Sam embarrassed at left
    
    s "Uhh...Yeah, that's cool."
    
    show Bella embarrassed
    
    b "Umm...I didn't mean anything like that! Oh..."
    
    "The warm situation quickly spun into awkwardness."
    
    s "(Ouch, just got friendzoned! Wait, why am I even thinking about this?)"
    
    show Bella neutral
    
    b "Anyways, thanks so much for helping me out all this time!  Sorry I haven't been able to do as much on my end other than put more work to do."
    
    show Sam neutral at left
    
    s "No, it's not like that, it's just we're kinda stuck with each other, being neighbohrs and all. Still, always happy to help."
    
    show Bella happy
    
    b "Hehe. You're too nice to me!"
    
    "We arrive at Bella's house at the end of the exchange."
    
    show Bella neutral
    
    b "I'll see you tommorrow! I'll try to wake up early again!"
    
    s "Yeah's that not likely, I already know you're staying up late again."
    
    show Bella embarrassed
    
    b "Hehe...You know me too well. Anyways, see ya!"
    
    hide Bella embarrassed
    hide Sam neutral at left
    
    "We exchange goodbyes for the day and I promptly head home."
    
    "It felt like it was just natural for me to help Bella, but it felt even better today for some reason. I feel as if i'm getting even close than I ever have with Bella."
    
    "Still, I got friendzoned? Or maybe she doesn't know what she really wanted to say."
    
    "Anyways, I got closer to her in some way. It was also nice for Ari and Cynthia to help as well. I probably should also try to help them out. Seeing as they helped me help Bella."
    
    "We'll see what happens and what new thing will happen..."
    
    #stop music fadeout 1.0
    
#End of Chapter 1B

    jump Ch2
    

label TrueFork1:

    show Cynthia happy
    show Sam neutral at right
    
    c "Hey, Sam! You're hanging out with me today?"
    
    s "Yeah, I haven't spent too much time with you yet and only met you when Bella introduced me to you."
    
    c "Alright, so what do you wanna talk about today?"
    
menu:
    
    "What should I go with as an icebreaker?"
    
    "You":
        jump Ch1C
    
    "Family":
        jump Ch1S

#Chapter 1C: President Cynthia
label Ch1C:

    with dissolve
    with fade
    
    show Cynthia embarrassed
    
    c "Oh? You want to talk about me?~"
    
    s "Uh...Yeah, I guess. I tried to keep it simple."
    
    show Cynthia neutral
    
    c "Uh huh."
    
    show Sam embarrassed at right
    
    "Cynthia stares at me for a moment, and our eyes meet. I try to get my eyes to wander somewhere else to avoid the awkwardness."
    
    c "No, keep your eyes on me. It's a little test."
    
    s "Uh...Okay."
    
    "I try to concentrate on just staring at Cynthia's eyes as she said, but found it extremely awkward."
    
    s "Urk...This is extremely awkward."
    
    c "Well, they say you find someone more attractive or likeable when you stare into their eyes quite a while."
    
    s "You are playing mind games with me that I wonder if they're even mind games at all."
    
    c "Hm..."
    
    "She chuckles a little deviously."
    
    show Sam neutral at right
    
    s "Anyway, about you, I heard you had a falling out with your last club. What happened with your club?"
    
    c "Oh, you're curious about that?"
    
    s "It gave me something to talk about with you I guess."
    
    c "I don't want to talk about it. It wasn't fun. Let's talk about something else."
    
    s "Hmmm..."
    
menu:
    
    "Should I help Cynthia?"
    
    "Yes":
        jump Ch1CY
        
    "No":
        jump Ch1No

#Ch1C Accepted
label Ch1CY:

    $ Ch1C_active = True
    $ persistent.Ch1CCG_unlocked = True
    
    show Sam talking at right
    
    s "No, really. Let's talk about it."
    
    show Cynthia sad
    
    c "Err..."
    
    s "It couldn't have been that bad. Come on."
    
    c "..."
    
    s "It would make you feel better if you would talk to someone about it, even if they don't understand."
    
    c "..."
    
    s "Come on...It's alright."
    
    show Cynthia neutral
    
    c "You're fairly persistent. Fine i'll talk about it."
    
    s "Seriously, what happened?"
    
    hide Sam talking at right
    hide Cynthia sad
    
    with dissolve
    with fade
    #stop music fadeout 1.0
    #play music regularday loop
    
    scene bg cgpresidentcynthia
    
    c "I was the president of the fashion club here and it was just a small club with 4 of my other friends."
    
    s "Fashion club? What do you guys do?"
    
    c "Design clothing, homemade jewelry, upcycling, making costumes, doing makeup tutorials, etc."
    
    s "That sounds cool!"
    
    c "Yeah, it's great, through fundraisers and the other school clubs sponsoring our commisions, we could make any clothing we want and what the other clubs may need for whatever they need it for."
    
    c "The five of worked like crazy, but really well on every aspect of making fashion. Design, material, measuring, styling, planning. Each of us had our own respective roles and we're really great at what we do."
    
    c "Not only that, we really knew each other. Jenny and Celica, the designer and stylist are in the tennis club, Ferdinand, Sarah, and I go to the same classes together. We're all good friends."
    
    s "Then what happened to split you guys up?"
    
    c "Do you know what's the major reason really famous bands break up?"
    
    s "Why?"
    
    c "Money."
    
    s "Your club gets paid by the school, commissions from other clubs, and fundraisers. Money shouldn't be a problem."
    
    c "Exactly. We get funding for our work, but the thing is it isn't equally shared as some members need more money to do their work."
    
    c " I always get the largest portion as president running things and advertising our works." 
    
    c "Ferdinand who's in charge of materials and inventory always go the second largest portion of the funding so he can buy the club whatever we needed to make our clothes."
    
    c "Jenny gets the third larger portion of the cut as the designer, Celica gets the fourth portion as a stylist, and Sarah the smalles cut for measuring."
    
    s "Ok."
    
    c "We all get paid by the remaining budget we have from funding after the project is complete, and I have to distribute our earnings."
    
    c "Sarah wanted a larger portion for her pay, but she her job is mostly simple labor. Ferdinand had used a large portion of the funding from our project as the materials were a little more expensive than usual."
    
    c "Celica argued that everyone should get a raise too if Sarah was asking for one as well, but we didn't have much money left from the completion of the project."
    
    s "Oh."
    
    c "The project was a bust, we didn't sell as much as we had hoped and it was an expensive project. They started to blame each other."
    
    c "We had a huge argument that last for I don't even remember how long, then they had a fight."
    
    s "A fight happened?"
    
    c "We all got sent to detention for that and the club was disbanded after that."
    
    with dissolve
    with fade
    #stop music fadeout 1.0
    #play music playful loop
    
    scene bg clubroom
    
    show Cynthia talking
    show Sam neutral at right
    
    c "I kept wondering what I did wrong as president, but I see that everybody gets a little greedy around money."
    
    c "I really wasn't in it for the money. I just had to find ways to get it to be able to make something. It should be driven by the want to make something, not just to make money."
    
    show Cynthia neutral
    
    c "Anyways, that's my story of the fashion club in a nutshell."
    
    c "I know you guys are different, right? You guys have this club to just hang out, and so i'll do the same."
    
    s "Kinda hard to believe that happened to your little club."
    
    c "I didn't think it would happen as well, but as soon as we just got paid in a daily basis, everyone just expected to get paid. So when we didn't get paid as much, you see what happened with that."
    
    show Bella talking at left
    
    b "That really sucks. You started the club right? That's how you were president?"
    
    show Bella neutral at left
    
    c "Mhm...I had to look hard for 3 other people to join me, but I found 4 other talented people up to the task."
    
    hide Sam neutral at right
    show Ari talking at right
    
    a "Truly you were driven by passion?"
    
    show Ari neutral at right
    
    c "You kinda have to be. I started the club, and even if I wasn't president, I would have worked even without getting paid to do it. It was just a really fun thing to do."
    
    hide Ari neutral at right
    show Sam neutral at right
    
    s "I know we might not have much, but i'll find some ways we can do some of the same stuff here in our club if you would find that really cool."
    
    c "Thanks, Sam, but just hanging out with you guys for the sake of hanging out is cool as it is."
    
    hide Bella neutral at left
    
    c "If you want, I can show you guys some cool face paints. Do you want to try?~"
    
    s "Hehehe...Sure, what can you make?"
    
    c "Whatever it is that you want.~"
    
    "Cynthia begins to talk with a sultry voice. It makes me quite uncomfortable when she talks like this..."
    
    hide Cynthia neutral
    hide Sam neutral at right

    with dissolve
    
    "We spend the next hour or so messing around with face paints and  making jewelry with paperclips."

    show Sam neutral
    
    s "We can wash these off with water right?"
    
    show Cynthia talking at right
    
    c "No, it stains your skin permanently like tattoo. You'd have to get surgery to remove it."
    
    show Sam talking
    
    s "SERIOUSLY?!?"
    
    show Cynthia neutral at right
    
    c "No, it's washable, hypoallergenic, and completely safe."
    
    show Ari talking at left
    
    a "Of course, it is not anything too dangerous like that, Sam."
    
    hide Ari talking at left
    show Bella neutral at left
    
    b "Hehe, yeah. Of course she couldn't get anything that dangerous in her hands easily. Right?"
    
    show Cynthia talking at right
    c "Shhh...You don't tell anyone where you got your stuff from."
    
    s "Really?"
    
    show Cynthia happy at right
    c "You're too easy to tease!"
    
    show Sam embarrassed
    s "Err..."
    
    b "You tease me all the time. It's nice seeing you being teased for a change."
    
    show Sam neutral
    
    s "Yeah, yeah. Very funny."
    
    c "Hehe.~"
    
    "Cynthia gives a playful chuckle as she wipes off the face paint off me with a soft cloth."
    
    show Cynthia neutral at right
    
    c "There, although i've smeared it a little over your face."
    
    s "Oh, please."
    
    c "A little bit here, and there. Here you go, all clean. Take a look."
    
    "Cynthia gives me a mirror."
    
    s "That got cleaned way too nicely! It really comes off that easily?"
    
    c "You could add layers to make it stain resistant, but it does come off that easily with a makeup remover wipe."
    
    s "Oh, cool! Wait..."
    
    "I check my fingers and see they have been painted on."
    
    s "How'd you?"
    
    c "Nicely done Ari! That looks great! He didn't even notice you as well."
    
    show Ari neutral at left
    
    a "I did as you requested."
    
    s "Oh, come on Ari! You were in it too?"
    
    a "Hehe...I have to admit it is amusing to toy with you as well."
    
    s "Give me a break, already!"
    
    hide Ari neutral at left
    hide Cynthia neutral at right
    hide Sam neutral
    
    "We clean up all the makeup and face paint we used up as we noticed it was already quite late."
    
    with dissolve
    with fade
    
    scene bg sidewalk
    
    "We all head home together after a 'fun' day messing around in the club."
    
    show Bella neutral
    
    b "All right guys! That was a great day at the club! I'll see you guys next Thursday and we now meet at Tuesdays and Thursdays. Text me if you can't make it so I can tell the supervisors. See you guys later!"
    
    hide Bella neutral
    
    "Bella waves goodbye and we all head back home."
    
    "Today was quite something. I got to know about Cynthia and her little club."
    
    "She's also really skilled in makeup and stuff like that, although I know nothing about fashion and the most fashionabl thing I wear is my short sleeves."
    
    "I definitely should spend time with Ari and Bella too, as they also are just as interesting and odd as Cynthia."
    
    "Who knows what tomorrow might bring? I can only question..."
    
    #stop music fadeout 1.0
    with dissolve
    with fade

#Chapter 1S: An Only Child
label Ch1S:
    
    with dissolve
    with fade
    
    show Cynthia neutral
    
    c "Something really simple like family to talk about?"
    
    show Sam neutral at right
    
    s "I don't know, I just thought of something."
    
    c "Okay!"
    
    c "Well, you've met my mom and dad, my mom's an ob-gyn and my dad is an architect."
    
    s "Wow really? What's an ob-gyn?"
    
    show Ari neutral at left
    
    a "A health care specialist who deals with the health of the female reproductive system."
    
    "Ari replies in the background as he's reading some books."
    
    hide Ari neutral at left
    
    c "Basically, she takes care of women delivering their babies."
    
    s "Oof. What a job."
    
    c "I also have an older brother who works as an IT for multiple companies and an older sister who is a journalist."
    
    s "Got any younger siblings?"
    
    c "A younger brother and sister, both are in elementary school."
    
    s "You've got four other siblings?"
    
    c "Only my older sister moved out, everyone still lives in my house along with my grandparents."
    
    s "Sheesh, a huge family!"
    
    c "My grandma was a therapist and she would kill us we put her in a nursing home seeing as she once worked in them."
    
    s "Hehe..."
    
    c "Overall, everything is fine for me with them, how about your family?"
    
    c "You said earlier that you're an only child. Does that bother you sometimes?"
    
    s "..."
    
    "I stay silent, knowing that I have to admit it."
    
    c "I don't understand your struggle of being an only child, but I can empathize with the fact that you're lonely most of the time."
    
    c "I couldn't imagine a day all alone at home with my many siblings."
    
    s "That's why I mostly hang out with Bella."
    
    c "But most of the time, you're still home by yourself."
    
    show Sam sad at right
    
    s "..."
    
    c "Do you still want to talk about it?"
    
    hide Sam sad at right
    hide Cynthia neutral
    
menu:
    
    "Should I continue?"
    
    "Yes.":
        jump Ch1SY
        
    "No.":
        jump Ch1No
        
#Ch1S Accepted
label Ch1SY:

    $ Ch1S_active = True
    $ persistent.Ch1SCG_unlocked = True

    #stop music fadeout 1.0
    #play music bitterness loop
    
    show Sam sad
    
    s "Yea, I can talk about it."
    
    show Cynthia neutral at right
    
    c "Alright, just know you don't have to share anything you don't want to. I would understand if you need your privacy. I know I would want to keep some things private."
    
    s "Yeah, that's cool i'm the son of a famous businesswoman who made billions of real estate, but I gotta say, it's cold to live behind that shadow."
    
    show Bella talking at left
    
    b "What do you mean?"
    
    s "I just don't see myself doing anything remotely close to amazing like my mom. I can't really follow in her footsteps as I just don't see myself in business like she does."
    
    hide Bella talking at left
    show Ari talking at left
    
    a "So, what do you want to do?"
    
    show Ari neutral at left
    
    s "Err....God, I don't know! I'm mediocre at best as a student, I can't seem to be able to be good at a lot of things, and I don't know what to do with my life."
    
    s "You guys have your parents to look to for advice, I don't even see my mother for a year or so. She wasn't even able to come to my birthday and only talked to her through the phone for 10 minutes."
    
    s "My mom, also just got divorced for the third time, life has been rough, okay? Especially in my family."
    
    show Cynthia sad at right
    hide Ari neutral at left
    show Bella sad at left
    
    b "Sam..."
    
    s "..."
    
    b "It's okay, Sam. We can't really understand how that feels, but we're here to help you."
    
    c "That's right, you can let it all out."
    
    s "..."
    
    s "Alright, i'll let loose for a while."
    
    with dissolve
    with fade
    
    hide Bella sad at left
    hide Sam sad
    hide Cynthia sad at right
    
    scene bg cgdonnamoore
    
    s "You definitely know my mom, Donna Moore, even though you've never met her right?"
    
    c "We hear about her in the news."
    
    a "She's the CEO of the multi-billionaire real estate company. She innovated urban planning and housing systems in communities changing the landscape of realty." 
    
    a "She appeared on a plethora magazines for her accomplishments."
    
    s "You guys know more about her than I know of her."
    
    b "How can you say that?"
    
    s "She rarely comes home, like once a year or so for a week, then she's back to work."
    
    c "Oh, dear."
    
    s "Yeah, my mom has a butler and a maid to look after me and help me get to school, but I just really miss her."
    
    s "She wasn't always working like this. Before she became as big as she is now, she would sacrifice so much of her time from work to go home early."
    
    s "Now, i'm in high school, and she's just constantly working. Things change, I guess."
    
    a "Truly she trusts you more to be able to handle yourself now."
    
    s "Yeah, I get it, but I just want her to come home every now and then. Not once a year."
    
    s "Look, I love my mom just like a lot of people do, but I hate her with how she's such a workaholic."
    
    s "Then, i'm looked at to be her heir and follow in her footsteps and become another businessman."
    
    s "I just can't."

    with dissolve
    with fade
    
    scene bg clubroom
    
    show Sam neutral
    
    s "Sorry to dump it all on you guys, but you can see it kinda bothers me when I hear about my mom."
    
    show Cynthia talking at right
    
    c "Why would that be?."
    
    s "I have...issues with her."
    
    show Cynthia neutral at right
    show Bella neutral at left
    
    b "We'll get through it. We promise."
    
    hide Bella neutral at left
    hide Cynthia neutral at right
    hide Sam neutral
    
    "We spend the rest of the time for the club meeting just making small talk with each other, as we found ourselves unable to find much to talk about aside from school."
    
    show Bella neutral
    
    b "Alright! I hope you guys had fun learning about each other as club members. Hopefully we do become great friends with each other! I'll see you guys tomorrow and at the next meeting!"
    
    "Ari and Cynthia exchange goodbyes with everyone and head out. I begin to pack up my things as well, but Bella stops me as I was about to leave the room."
    
    b "Sam, I need to talk to you before you go."
    
    s "Ok, what is it?"
    
    b "I didn't know that's how you felt with your mom before. It really shocked me that you really opened up to show us that."
    
    s "I'm just as surprised as you. Also, it's been like this with my mom for a while. I guess I just really had to let it out."
    
    b "Well, thanks for sharing with us, and with me as your best friend."
    
    b "I swear i'll do anything to help you patch things up with your mom. Just know that your also like family to me. You're not alone."
    
    s "Thanks, Bella. I really can't thank you enough."
    
    b "Now come on you big drama king, let's head home."
    
    hide Bella neutral
    
    "And so, Bella and I head home casually talking about school and other small talk as if nothing had really happened." 
    
    "It did cheer me up a little to go back into the crazy swing of things between us from my little dramatic moment."
    
    "I really surprised myself with how I really chose to open myself up to others and it made me feel good about venting." 
    
    "Perhaps I should really do that more often and maybe i'll be able to actually patch things up with Mom."
    
    "I don't know how things might change from here on out, I just hope it's for the better."

#End of Chapter 1S
    jump Ch2

#Chapter 1N: Overdramatization
label Ch1No:
    
    "After that, the conversation completely died. I just stood there completely mute and had nothing to talk about."
    
    "I step outside the club room for a while..."
        
    with dissolve
    with fade
    
    #stop music fadeout 1.0
    scene bg hallway

    "Bella soon follows suit after me."
    
    show Bella neutral
    
    b "Are you alright, Sam?"
    
    show Sam sad at left
    
    s "..."
    
    b "Sam?"
    
    s "I'll be honest, I just didn't feel like hanging around for a while."
    
    b "Really?"
    
    s "I don't know, it felt really awkward to be in that situation."
    
    b "How so?"
    
    s "It felt like I shouldn't be there. I don't know why, but I just needed to step out."
    
    b "Okay, but I want to do anything so it doesn't feel awkward to be in the club. Also, you belong there. Everyone does."
    
    b "I'm trying to make this club so you don't feel out of place here."
    
    s "..."
    
    b "Well, i'll just leave you be for a while."
    
    hide Bella neutral
    hide Sam sad at left
    
    "Bella heads back into the clubroom, leaving me by myself on the hallway floor."

    with dissolve
    
    "I don't know why I chose to step out in the first place, yet here I am. I take a second to look back how I even got here in the first place."
    
    "I'm in this club which is supposed to be a peer club where we just hang out together, yet it feels wrong to me."
    
    "For one, it happened so fast, I was pushed by Bella to join and start a club overnight."
    
    "Two, I have to talk to two other people I hardly know, it was really awkward to even open up a conversation at first, even with Bella."
    
    "And three, I guess i'm just not feeling myself today. It feels weird to feel as if i'm not even in control of myself, but it's happening."
    
    "I might just be a little crazy right now, but I don't want anyone to bother me right now." 
    
    "Everything seems to move way too fast and a little dramatic at times, it just doesn't feel as if things really aren't happening naturally for me."

    with dissolve
    with fade
    
    scene bg clubroom
    #play music playful loop
    
    "I get back into the clubroom to try talking to everyone again, but every conversation just ended in small talk."
    
    "Everytime I try to make conversation, it just ends quickly in silence."
    
    "For once, i'm speechless as I don't know what to do."
    
    "I'm not even sure I should even be here. I'd rather see myself going home."
    
    show Bella talking
    
    b "How's it going so far guys?"
    
    show Cynthia talking at right
    
    c "This doesn't seem to get us anywhere."
    
    show Ari sad at left
    
    a "..."
    
    b "Hmmm....Ooh, I know what could be a good icebreaker!"
    
    c "What would that be?"
    
    b "Let's find and share our favorite poems!"
    
    c "Really? Is that a good idea?"
    
    b "I just joined the poetry club and this is the first thing that we did. We really got to know everyone and their style and taste in poetry!"
    
    b "Come on, it'll be fun!"
    
    hide Cynthia talking at right
    show Sam neutral at right
    
    s "Alright, i'll give it a try."
    
    b "Great! Let's take 15 minutes to go look for our favorite poems!"
    
    "All of us get on our phones to go look for poems except Ari, who got out a small notebook and started writing his own poem."
    
    "I really don't know what poem to choose, so I just looked up one of the most popular poems online."
    
    hide Sam neutral at right
    hide Ari sad at left
    hide Bella talking
    
    "15 minutes pass, then Bella calls us together."
    
    with dissolve
    
    show Bella neutral
    
    b "Alright! It's time to share our poems! Again we'll share poems together 1-on-1, so it feels really personal and avoid anyone being too shy to share."
    
    show Cynthia neutral at left
    
    c "Makes sense I guess. Let's see what you guys picked then."
    
    hide Bella neutral
    hide Cynthia neutral at left
    
    "I go around and share my poem with everyone. I just chose a poem by this popular poet and it looked simple enough." 
    
    "I liked it myself, but I really couldn't understand completely what it said. What's so special about the end of a sidewalk?"
    
    "Everyone really liked my poem and I really like everyone else's poems but I couldn't say much other than that and every conversation ended with me just saying 'I liked it'."
    
    show Bella neutral
    
    b "So, what did you think Sam?"
    
    show Sam sad at left
    
    s "I liked it."
    
    b "Okay, but you don't seem like you do. Are you alright?"
    
    s "I just need some time alone."
    
    "Again, I step out of the room for some alone time."
    
    hide Bella neutral
    hide Sam sad at left
    
    scene bg hallway
    #stop music fadeout 1.0
    
    "I'm just not feeling myself right now. I feel out of place with everyone there, even with Bella."
    
    "Maybe I shouldn't have come here today. I think I forced myself too much to be here."
    
    "After a few minutes I just blankly stare at the floor, then I decided to head back in the room."
    
    "I take a peek through the door first before entering."
    
    show Bella neutral at left
    
    b "So what did you think?"
    
    show Cynthia talking at right
    
    c "It's ok, I guess..."
    
    b "Ok?"
    
    c "It just seems too simple-minded in its style and word choice."
    
    b "It's simple, but it's complex from how simple it is."
    
    c "Sure, but it would be better if more complex vocabulary was used. It would have more meaning to it rather than just using very simple words."
    
    b "Using bigger and more words would only make it more confusing and not necessarily make it better! I think it should be straight to the point when you tell a story like that."
    
    c "It's only confusing when you don't think when you actually read. A poem can mean many things to a reader and that's the beauty of it."
    
    b "What do you mean actually reading?"
    
    c "Actually paying attention to what you read, of course you're too young to understand that yet."
    
    b "Are you belittling me?"
    
    c "If that's how you see it."
    
    b "Just because I have a more simple taste and style doesn't make it not worth looking at! I'll have you know Ari and Sam like my poem."
    
    c "If you say so. They're porbably just being polite. Ari and Sam actually liked my poem."
    
    b "They like my poems better!"
    
    c "No, they appreciate mine more."
    
    b "Shut up!"
    
    c "Oh, this little girl is telling me to shut up?"
    
    b "Yeah, be quiet you bimbo!"
    
    "Suddenly, both Bella and Cynthia are enraged from their insults."
    
    show Ari talking
    
    a "Please, can we just calm down here-"
    
    c "Backoff! This is between me and her."
    
    b "Is it now?"
    
label redo_Ch1BE:
    
    "Should I intervene?"
    
menu:
    
    "Yes.":
        jump Ch1BE
        
    "No.":
        "Are you sure?"
menu:
    
    "Yes.":
        jump Ch1D
        
    "No.":
        jump redo_Ch1BE
        
                
#Ch1BE: Boring Ending I
label Ch1BE:
    
    show Sam talking
    
    s "Stop! Why are you guys fighting? What the heck just happened?"
    
    show Bella sad at left
    
    b "Ack...Sam! Umm...It was just a misunderstanding."
    
    show Cynthia sad at right
    
    c "Urk..."
    
    s "What?"
    
    c "Err..."
    
    b "It was a small disagreement."
    
    s "Don't act like it was something small, I know that wouldn't be the case if I saw you guys yelling at each other."
    
    b "..."
    
    c "...I'm sorry. I take back what I said. I shouldn't have been so thoughtless of being too highly criticizing and speaking badly of you."
    
    b "I'm sorry too for taking what you said too personally and should not reacted as I did."
    
    s "Okay, that's enough."
    
    "They were quick enough to catch on to apologize, but I know this doesn't solve the problem."
    
    s "I heard a fair amount of it already. Aside from the insults and what I can tell, Cynthia called out Bella for her different style in poetry and Bella is mad at Cynthia for being too quick to judge."
    
    c "..."
    
    b "..."
    
    "The two fall silent."
    
    s "Look Cynthia, I know both of you are very passionate about poetry from how you described your different styles, but everyone is entitled to their own opinion." 
    
    s "The beauty of it is freely expressing yourself through words in your own way. She has a simple and different style, but it doesn't make her style invalid."
    
    s "Let's just agree on that together, okay? Bella can make poems with the best of them." 
    
    s "I know you're also experienced in the art, but she has a case to be made too. She was passionate enough to join the poetry club to explore her interest just give her some credit."
    
    s "Bella, I know you aren't the best person in taking criticism, but Cynthia has some fair points. You should also be more considerate of accepting her criticism."
    
    s "Neither of you are fully right, but also neither of you are completely wrong. You guys shouldn't fight over something simple as this." 
    
    s "We're supposed to be friends right? We're gonna be stuck with each other for a while."
    
    s "Now, can we all just shake hands and get along?"
    
    show Bella neutral at left
    show Cynthia neutral at right
    
    "The two look at each other, this time with more eased expressions and shake hands."
    
    b "I'm sorry, let's just start over from that, okay? I forgive you."
    
    c "Likewise, I guess I just assumed too much. I forgive you too."
    
    s "Jeez, now that's over I can relax."
    
    "I let out a huge sigh of relief for diffusing the situation."
    
    s "That was just an overly dramatic stupid little fight between you guys!"
    
    s "But i'm glad you guys made up."
    
    b "I'm sorry Sam, the stress just got to me and I snapped. I'll try to keep a cool head for you as a good club president should."
    
    c "Sigh...I was just too harshly direct with her. I have met some people who are just annoyingly bad, so i'm sorry for being direct."
    
    b "Come on, let's clean this mess up."
    
    hide Bella neutral at left
    hide Cynthia neutral at right
    
    "Bella and Cynthia begin cleaning up and rearranging the desks in the clubroom."
    
    hide Sam talking
    show Ari neutral
    
    a "Thanks for stepping in there, Sam. You sure know how to deal with a tense situation like such. I feel ashamed for not being able to do the same."
    
    s "I saw you try to get between them, you did what you could. Don't feel bad about it."
    
    a "Okay. Thanks for you consolation."
    
    s "Phew...Well, today was something. I think we'll still get along even though it got a little ugly there."
    
    a "Really? How so?"
    
    s "I know it doesn't make sense sometimes, but some people say opposites attract."
    
    a "What do you mean?"
    
    s "They are completely different in how they express themselves, but it could show they could be best friends. I hope, if it gets close to a situation like this, they'll be able to still be friends and grow as friends."
    
    a "Hm. There is wisdom in your words."
    
    s "Oh no, it's just something I kinda picked up when I saw people who are friends."
    
    a "I see...Do you like to observe others as a pastime?"
    
    s "You mean people-watching? Yea, all the time."
    
    a "Interesting...I presume that's how you are able to sense people's feeling with such proficiency."
    
    s "I guess it just comes naturally."
    
    a "...Alright."
    
    hide Ari neutral
    
    "The four of us clean up the clubroom to tidy things up, but two hours of club time really passed by quickly that it was already time to go home."
    
    with dissolve
    with fade
    
    scene bg sidewalk
    
    "Today I got to see how scary Bella and Cynthia are as scuffled. Hopefully they do get along even though Cynthia may not like Bella at first."
    
    "I guess everything was a little too much for me. I'll try to take it easy with everyone when it comes to talking to them. Who knows what kind of sides i'll see from them."
    
#End of Chapter 1: Boring Ending
    jump Ch2
    
#Ch1D: Diverged Ending Pt. I
label Ch1D:
    
    $ Ch1D_active = True
    $ renpy.block_rollback()
    
    "Cynthia slaps Bella across the face in anger."
    
    c "Show some respect!"
    
    b "I'll show you respect!"
    
    "Bella in return slaps Cynthia twice as hard."
    
    c "Oh, you insolent-"
    
    "Quickly the two begin fighting in anger. Their slapping quickly turn into punching. Ari tries to intervene between them."
    
    show Ari talking
    
    a "Please, stop hurting each other, this is too far!"
    
    show Ari sad
    
    "Ari stands between them only to catch a heavy punch from Cynthia, knocking the wind out of him."
    
    a "Urk..."
    
    hide Ari sad
    
    "Ari collapses to the ground..."
    
    "Cynthia and Bella stop their fight to check on Ari with me, who's on the ground wheezing."
    
    show Sam talking
    
    s "Ari! Are you alright?"
    
    c "Oh my gosh, i'm so sorry! I-"
    
    b "We better stop this before we get in trouble with the supervisor. Let's get Ari to the nurses' office."
    
    a "I'll be alright, just let me rest for a while."
    
    "Ari speaks as he's gasping for air."
    
    c "Sigh..."
    
    b "We'll settle this later, but for now just keep it to yourself, Cynthia. I'll head to the nurses' office for an ice pack."
    
    hide Bella talking at left
    
    "Bella leaves the room for the nurses' office."
    
    c "...I think i'll just head home for now. I'll settle this with her tomorrow."
    
    hide Cynthia talking at right
    
    "Cynthia packs up her things and leaves the room."
    
    show Ari neutral at left
    
    a "Urk...At least they stopped for now. I am afraid that only temporarily settles the unhappy relationship brewing between them."
    
    s "...I should have stopped them. Then you wouldn't have gotten hurt."
    
    a "Think nothing of it. You should not place the blame on yourself."
    
    show Sam sad
    
    s "You'll be alright?"
    
    a "Do not worry about me. I will clean things up here. I sense you are not in a pleasant mood after this. I suggest you spend some time alone and go home."
    
    s "...Fine, i'll just go do that. Sorry."
    
    hide Sam sad
    hide Ari neutral at left
    
    with dissolve
    with fade
    
    scene bg hallway
    
    "I was about to head home after this fight happened, until I catch a glimpse of Bella and Cynthia talking to each other in the hallway. I only take a small peek around the corner to observe them."
    
    show Cynthia talking at left
    show Bella talking at right
    
    c "I think we've already established that we don't like each other."
    
    b "With the way you insulted me and my class, you flirting with Sam, and how you belittle me, yeah I see that."
    
    b "I see you flirt with every guy you see just to get your way you despicable-."
    
    c "Let's just work this out okay?"
    
    b "Hmph."
    
    c "Sam would definitely not like us fighting and you obviously don't want to lose him right?"
    
    b "Urk..."
    
    c "Let's just pretend none of this happened, okay? Let's play nice around your friend."
    
    b "You better keep to that promise."
    
    show Cynthia happy at left
    
    c "Happy to settle that properly!"
    
    hide Cynthia happy at left
    
    "Cynthia struts away as Bella stands with her fists tightened."
    
    b "Why that flirting b-."
    
    hide Bella talking at right
    
    "Bella storms off at a different direction."
    
    scene bg sidewalk
    
    "I head home after the incident and spend time mulling it over."
    
    "We were lucky enough to be sent off with a warning by the teacher as nobody was harmed." 
    
    "Ari got knocked, but he turned out to be completely fine after a short rest. Bella and Cynthia are surely unhappy with each other, but hopefully things will be fine with them."

    "I felt like I wasn't really me today. I should have stepped in to stop them, but I was just to scared to do that."
    
    "I shouldn't have been because that was my friends that was just fighting. What kind of friend am I then?"
    
    "I guess i'll try to settle things with everyone if I can next time..."
    
    with dissolve
    
    "The next day on the walk to school to pick up Cynthia, the two girls meet face to face."
    
    show Bella happy at left
    show Cynthia happy at right
    
    c "Glad we settled this responsibly. Right Bella?"
    
    b "Right. I will just continue with my duties as president of the club. Let's just forget this incident ever happened."
    
    c "What incident?"
    
    b "Exactly."
    
    "It's obvious to see there is tension between the two, but they seem to have made a ceasefire..."
    
    show Ari sad
    
    a "..."
    
    "I can sense the anger between them behind those nonchalant smiles. Hopefully it doesn't get any worse as it is for them. It also shows in Ari's frown that it truly makes him unhappy as well to see them be like this."
    
    hide Ari sad
    hide Bella happy at left
    hide Cynthia happy at right
    
    with dissolve
    with fade
    #stop music fadeout 1.0

#End of Chapter 1: Diverged Ending
    jump Ch2Alt

#Chapter 2: The Butterfly Effect
label Ch2:
    
    with dissolve
    with fade
    #play music regularday loop
    
    scene bg sidewalk
    
    "After the first few months of being in the club, i'll admit I actually really enjoy hanging out at school now that to me, there's a good reason to go to school."
    
    "There's a place for me to do stupid stuff with friends and not just myself."
    
    "I really started to grow closely as friends to Ari and Cynthia and Bella helping me out."
    
    "We spend the first half of the semester just hanging out, telling stupid stories, and complaining together on how disgusting the school is."
    
    "At first, it was really awkward talking to each other, but then it didn't."
    
    "Before I knew it, we we're closer than we thought as friends throwing jokes at each other."
    
    show Bella talking at left
    show Sam neutral
    
    b "I can't find my pin in my backpack anywhere..."
    
    s "Really? It's right there."
    
    b "Where?"
    
    s "Under there."
    
    b "Under where?"
    
    show Sam happy
    
    s "Hehehehe..."
    
    b "Haha, very funny."
    
    show Cynthia talking at right
    
    c "Do you really have any better jokes?"
    
    hide Bella talking at left
    show Ari talking at left
    show Sam neutral
    show Cynthia neutral at right
    
    a "Ooh. I have one."
    
    c "Let's hear a better joke."
    
    a "Okay, I will give it a try."
    
    a "Hmmm...I got it!"
    
    a "Why do chemists make such bad doctors?"
    
    s "Why?"
    
    a "Because if you cannot Helium or Curium, you Barium!"
    
    c "Heheh, not bad."
    
    s "Hehe, what?"
    
    show Ari neutral at left
    
    a "It's elementary!"
    
    s "Right..."
    
    hide Sam neutral
    show Bella neutral
    hide Ari neutral at left
    hide Cynthia neutral at right
    
    b "He's got puns to boot that."
    
    "Aside from my bad jokes, this is now how every morning goes for me."
    
    "Walking to school with 3 other friends, just casually talking about all kinds of stuff and joking around."
    
    "I'll admit we talk about both the weiredest things and the most boring things from time to time, but there's always something. Sometimes we also ask really serious questions."
    
    hide Bella neutral
    show Sam talking
    
    s "It's weird that I haven't really asked this or known too much about this, but where are you going after high school, guys?"
    
    s "To be honest, I have no clue what i'm gonna do."
    
    show Bella neutral at right
    
    b "That's quite a question. I know a lot of us will be going to college, but i'm just gonna go to the community college here. I see myself going into journalism, I really like working in the school newspaper."
    
    s "Are an editor for it?"
    
    b "Yea, I work on the club news articles."
    
    show Cynthia neutral at left
    
    c "Nice. Really thinking of going pro as a writer?"
    
    b "Yeah, I write blogs all the time so I already have some experience."
    
    s "That's really neat! What about you, Cynthia?"
    
    c "My brothers will put me through college, so I feel fortunate for that. I'd say I would go into business."
    
    b "What kind of business?"
    
    c "Don't really know yet, I just wanna make some dough."
    
    s "You're really good at making clothes and costumes right? Thinking of something like that?"
    
    c "If it brings me big money, yeah."
    
    s "Alright then. What about you, Ari?"
    
    hide Sam neutral
    show Ari talking
    
    a "I have aspirations to become a doctor, so my path would be towards undergraduate college into medical school."
    
    c "Really big goals there, but what about student loans? Paying those off from med school will take years."
    
    hide Ari talking
    show Sam neutral
    
    s "But he'll be a doctor, so he'll get tons of money to pay that off. Right?"
    
    c "Perhaps, but it's difficult to get high paying jobs even as a doctor. My mom has friends who are nurses who still work year after year to pay them off. I hear some are still working to pay them off."
    
    s "Yikes."
    
    b "Ari's really smart though, he's definitely gonna get a whole bunch of scholarships to pay for all of that."
    
    s "Hehehe, I see it now. 'Dr.Kagawa'! It's a nice ring huh? You got this, buddy."
    
    hide Cynthia neutral at left
    show Ari neutral at left
    
    a "Thanks, Sam."
    
    s "As for me, I don't see myself doing much. Probably gonna just take over my mom's business."
    
    b "Really? Don't you want to do something else?"
    
    s "Not taking after her business? That will go down nicely with my mother."
    
    b "There's gotta something out there that you're good at and enjoy doing, not just what your mom forces you to do."
    
    s "I really don't know what to do with my life."
    
    a "You will find your answer to that question as long as you keep trying."
    
    hide Ari neutral at left
    show Cynthia neutral at left
    
    c "It'd be nice if you could just go into any job you want and not have to worry about making money, huh?"
    
    s "Hmmm...Maybe."
    
    "Silence falls for a brief moment between us as we ponder Cynthia's remark."
    
    s "Oh, we're already here."
    
    hide Cynthia neutral at left
    hide Sam neutral
    hide Bella neutral at right
    
    with dissolve
    with fade
    
    scene bg schoolyard
    
    show Cynthia neutral at left
    show Bella neutral
    show Ari neutral at right
    
    s "See you guys same time after school?"
    
    b "Yeah, we have a club meeting today."
    
    a "As planned, you can see me there."
    
    c "Yeah, i'll be there."
    
    s "Okay, i'll see you guys later!"
    
    hide Ari neutral at right
    hide Cynthia neutral at left
    
    "Cynthia and Ari leave for class."
    
    b "Sam, can I talk to you for a second, just you and me?"
    
    s "Sure."
    
    "I follow Bella to a quiet spot in the hallway."
    
    with dissolve
    with fade
    #stop music fadeout 1.0
    
    scene bg hallway
    show Bella neutral
    show Sam neutral at right
    #play music maintheme loop
    
    b "I have an honest question to ask you. Please just answer me honestly."
    
    s "Sure."
    
    b "Do you genuinely enjoy being in the club? I know I forced you into it, but I just really want to know if this worked out. I didn't want you thinking I pushed you into this."
    
    "I'm stunned she came out and asked this question to me. Perhaps she was too scared to ask it before, but as promised, I answer her as honestly as I can."
    
    s "I truly am glad that I came here with you. You did nudge me into joining the club with you, but I found that I actually really enjoy spending time with you guys."
    
    s "In fact, i'm kinda grateful you introduced me to Cynthia and I got to meet Ari. At first, I wanted to just stay home and play videogames, but you showed there's more to just being locked up in a classroom here."
    
    s "Plus, I always really liked hanging out with you, Bella. You're my best friend."
    
    show Bella embarrassed
    
    b "Hehe...Thanks. Even though you're always the one looking after me."
    
    s "Even when i'm looking after you complete mess."
    
    show Bella happy
    
    b "I'm not such a mess, okay?"
    
    "Bella laughs in joy from my thoughts of the club."
    
    show Bella neutral
    
    b "I'm glad you like hanging out with us. I just want you to be happy."
    
    show Sam embarrassed at right
    
    s "Looks like you're the one looking after me."
    
    b "Sam, you're blushing."
    
    "I quickly turn around, completely embarrassed from blushing."
    
    show Sam talking at right
    
    s "Let's just get to class, okay?"
    
    b "Okay!"
    
    hide Bella neutral
    hide Sam talking at right
    
    "Bella and I head our separate ways to our classes."
    
    "I get through my classes in anticipation of going back to the club."
    
    with dissolve
    with fade
    #stop music fadeout 1.0

    scene bg classroom
    #play music playful loop
    
    "After my last class of the day, I head out of the classroom in a hurry. As usual, Bella is standing out in the hallway waiting for me."
    
    show Bella neutral
    show Sam neutral at right
    
    b "Hey, Sam!"
    
    s "Hey."
    
    b "Walk with me to the clubroom?"
    
    s "Fine, since we're heading to the same place."
    
    hide Sam neutral at right
    with dissolve
    with fade
    
    scene bg clubroom
    
    show Bella neutral
    
    "Bella and I walk down to the clubroom and see Ari and Cynthia are already there waiting for us."
    
    show Cynthia neutral at right
    
    c "About time you guys showed up. You kept me waiting!"
    
    show Ari neutral at left
    
    a "Take your time. We're here early because our classes are closer to the clubroom than yours."
    
    s "Okay, then. Let's get going."
    
    b "So, for today's club meeting! We won't do anything special today. Let's just treat this as a study hall or just simply hang out."
    
    s "Really? You just don't have anything on the agenda?"
    
    b "I gotta get stuff ready for the school culture festival! As class president, I have to keep up with my work!"
    
    "Oh yeah, Bella won in a landslide victory in being president for our class. She really showed off her willingness to work and was really popular with everyone. Especially the teachers."
    
    "Now she's working with the student council to set up the festival for the school and our parents to enjoy."
    
    s "Okay then. I'll just hang out if that's the case."
    
    a "If that's the case, I will continue my studies for my classes."
    
    c "Mmm, I think i'll just enjoy some books for today. Feel free to join me Sam.~"
    
    "Cynthia and Ari go back to what they were doing before."
    
    hide Cynthia neutral at right
    hide Ari neutral at left
    
    "I guess I really don't have anything better to do other than just sit down and stare at the window."
    
    b "Sam?"
    
    s "Yeah? What's up?"
    
    b "I know i've got work as class president, but don't you have anything to do today?"
    
    s "Not really."
    
    b "Well, think about it. The holidays are coming up, so maybe that could give you some ideas."
    
    s "Hmmm..."
    
    with dissolve
    with fade
    hide Bella neutral
    
label Ch2Alt:
if Ch1D_active:
    
    scene bg clubroom
    #play music playful loop
    
    "The next couple of months, the entire group talked less and less. Bella and Cynthia can't stand being next to each other, so Cynthia doesn't walk to school with us. "
    
    "Cynthia still shows up at club meetings, but only talks when Bella isn't in the room. Ari is completely silent and everytime I try to start a conversation, it just dies really quickly."
    
    "Still I head over to the clubroom with Bella hoping the next one will be better."
    
    "Apparently, Bella has work to do for some of her teachers so today's club activities is to just have a study hall. " 
    
else:
    "What should I do..."
    
menu:
    "Who should I hang out with?"
        
    "Ari!":
        jump Ch2A
        
    "Bella!":
        jump TrueFork2
            
    "Cynthia!":
        jump Ch2C

#Chapter 2A: Natural Teacher
label Ch2A:
    
    with dissolve
    with fade
    
    show Ari neutral
    
    a "Hello, Sam. You chose to study here with me?"
    
    s "Might as well, since I have nothing better to do and midterms are coming up."
    
    a "Fair rationale."
    
    "I look over Ari's shoulder and see a large stack of books lying on the floor."
    
    s "What are you studying?"
    
    a "Calculus, the mathematical study of change."
    
    s "Like what?"
    
    a "Studying the rates at which something increases or decreases, change in position, all kinds of changes in values."
    
    "I look over to read the book he was reading and see the page is riddled with numbers and symbols to which make me think it's a completely different alien language."
    
    s "Are you sure you're not studying Latin or some other crazy language and this is math?"
    
    a "Those Greek symbols and many others have their own meaning, you know. Also, yes this is math and not Latin."
    
    s "Err...Can we go with math more in my level, like Algebra?"
    
    a "Why certainly, it's the hardest part of Calculus, so it would benefit me to review with you."
    
    s "So the crazy symbols and formulas isn't the hard part in that crazy math?"
    
    a "Having a basic foundation in any subject is crucial for upper level study. It is not always the new material that is the most difficult at many times, but rather using what you know."
    
    s "..."
    
    a "Do you want to go over Algebra with me? I will try to elucidate as clearly as possible."
    
menu:
    "Ask for Ari's help?"
        
    "Yes":
        jump Ch2AY
            
    "No":
        jump Ch2No
            
#Chapter 2A Accepted
label Ch2AY:

    $ Ch2A_active = True
    $ persistent.Ch2ACG_unlocked = True
    
    a "Alright, let us begin."
    
    "With pen and pencil ready, for once i'm ready to learn something in school."
    
    a "So, what do you need help with?"
    
    s "So from my Algebra class, we're working with quadratics or finding x when you can't factor it at all."
    
    a "They force you to just learn the quadratic formula I assume."
    
    s "Yeah, that. Some weird, complicated formula."
    
    a "The quadratic formula? That is not too complicated. Here, I will derive it for you so you can understand it."
    
    s "Derive? What does that mean? Also, that looks complicated with all those letters and symbols."
    
    a "I will show you where it comes from so it does not look like a foreign language to you."
    
    a "Take out a pencil and a sheet of paper and follow my lead."
    
    "I promptly do so."
    
    hide Ari neutral
    
    scene bg cgnaturalteacher
    
    a "It is very simple. First, let us start out with our basic quadratic formula, ax^2 + bx + c = 0."
    
    a "Our goal is to isolate x, so first let's subtract c to get our x terms on one side."
    
    s "Okay, then what?"
    
    a "From here, we complete the square"
    
    s "How do we do that?"
    
    a "First, we divide everything by a."
    
    a "Add (b/2a)^2 to both sides."
    
    s "Wait, why do we add that to both sides? Also, why specifically adding that?"
    
    a "What you do on one side, you have to do to the other side."
    
    a "We add (b/2a)^2 because we want to rewrite the expression with our x terms to a square."
    
    a "So we get, (x + b/2a)^2. To complete the square, just simply take the coefficient, or the number in front of the x that is not squared, multiply the denominator or divide it by 2, then square the entire fraction."
    
    a "This is a general factor so it works everytime."
    
    a "Take the square I got and expand it so you see what I mean."
    
    s"..."
    
    "I try to quickly do the math in my head..."
    
    s "Oh! It does work!"
    
    a "It is because you add two of the same thing when you factor the same thing when you distribute. Then the coefficient of the term with the x that is not squared is two times the number without an x squared."
    
    a "Do you see the pattern?"
    
    s "Mhm..."
    
    "I actively try to take notes of everything he's said so far in explaining this."
    
    a "Math has a lot of patterns, the more you see them, the easier it is to think through it. Similarly to how you would solve some puzzles in your games right?"
    
    a "The same idea is there."
    
    a "Now, you rewrite that ugly expression on the right by rewriting (b/2a)^2 to b^2/4a^2. You will see the fractions cancel out later, so just bear with me."
    
    a "Get a common denominator, or bottom number, so multiply -c/a with multiplying it with 4a/4a."
    
    s "Why do we do that?"
    
    a "To make it look nicer to work with the denominator to get everything over on fraction."
    
    a "So we get (b^2-4ac)/4a^2. Now they're all over one bottom number."
    
    a "Take the square root of both sides to get rid of the quantity squared on the left. Do not forget your plus or minus sign since it is a square."
    
    a "When taking the square root of a fraction, you can take the square root of both the top and the bottom, not just the fraction."
    
    s "What do you mean since it's a square?"
    
    a "Meaning it can be either positive or negative and still have the same thing when it is squared."
    
    s "Right."
    
    a "The bottom number of the right side becomes 2a."
    
    a "Get everything to the right side by subtracting b/2a."
    
    a "Clean it up because there's a common denominator and there we go. Everything is equal to x. Now you can solve any quadratic."
    
    s "What the heck? That was like magic!"
    
    a "When you understand where everything comes from, you can understand how to solve any problem."
    
    a "I am not keen on memory, but my strength comes from being able to think through concepts, that is what colleges look for. They want to see students who think, not just memorize. That is the difference between college and high school."
    
    a "Of course, you do not need to know all of that yet, but I just want you to know why it works. Do you understand?"
    
    a "Still, there are quicker ways to solve quadratics than using this formula all the time, but knowing where this formula comes from shows that you know how to look at the problems from many angles."
    
    "I go over my notes to go through the entire lesson from Ari to try to completely understand what he means."
    
    "He makes me practice using the formula on some easy problems then really hard problems..."
    
    "I start to see the patterns and the lesson becomes a revelation."
    
    s "Huh. That does make sense."
    
    a "Yes, math is very logical."
    
    scene bg clubroom
    show Sam talking
    show Ari neutral at right
    
    s "So what are we really gonna use this for? Knowing all these numbers and stuff?"
    
    a "Calculators and other programs do this for us nowadays, but the effectiveness of a machine is only as effective as its user."
    
    a "These types of calculations can be used in various applications." 
    
    a "Maximizing profits and lowering cost in businesses, tracking changes in temperature outside to predict next day's forecast, checking the arc of a projectile when fired like firing a cannon, and other applications."
    
    s "That seems like a stretch."
    
    a "It is a little bit of a 'stretch', but something like this can be used in many ways and many situations. You just have to know how to use it."
    
    a "For now, you are just concerned about passing midterms, so focus on that as a driving force to study."
    
    a "What I said will make more sense when you learn more skills."
    
    s "Thanks for the lesson, Ari. Taught me more than what I paid attention to in class. My teacher is too boring to listen to."
    
    a "That should tell you to listen more in class then. Anyways, it was no problem to teach you."
    
    s "I don't know, I feel like I understood it better when you're the one teaching. The way you teach makes sense and I like how you give the clear reason why we do things."
    
    a "Perhaps your teacher just has a much different teaching style from what you are used to."
    
    s "You're kinda a natural when it comes to teaching! Hey, can you help me with other stuff too?"
    
    a "I will give you any help I can provide."
    
    with dissolve
    
    "For the next couple hours or so, I spend the entire afternoon studying with Ari for all my classes."
    
    "I really understood the stuff from class better coming from him than my other teachers. He really takes good notes I guess."
    
    "From English to Science, then Spanish, I actually got a better grasp on how to do actually study from Ari's tips on studying."
    
    show Ari neutral at right
    show Sam embarrassed
    
    a "How do you study, Sam? Just curious."
    
    s "I just do my homework in the kitchen while eating some snacks. That's if I even choose to do my homework."
    
    a "I suppose you also procrastinate."
    
    s "Guilty."
    
    show Sam neutral
    
    s "Homework is boring. I don't get what to do on most of it anyway. Some of my teachers could care less about what they're teaching."
    
    show Ari talking at right
    
    a "Well firstly, change your mindest of how you think of doing homework."
    
    a "I like to think of homework as practice rather than work. It should help you learn the material through application. Once you go through the motions, it becomes natural."
    
    a "Secondly, get started on the homework right away in class, while the material is fresh in your memory, so you have an idea of what you need to do."
    
    s "That makes sense, but what if you don't even know what to do right away?"
    
    a "Ask around. Your teacher, classmates, friends. It's just homework, it should be easy enough for someone to figure it out."
    
    s "That's when we look up the answer."
    
    a "That's fair, but the important thing is to learn or at least have an idea of how to go about it."
    
    a "Thirdly, space out your time doing homework. It is not fun sitting down for hours on end just doing nothing, but homework."
    
    s "You're saying it's easier to do it from time to time."
    
    a "Yes. It is more effective because retention, or how well you understand it, gets better when you practice more often. Right?"
    
    a "Lastly, work smarter, not harder. Do the easy stuff first, then the hard stuff. For some people, it works better the other way. Figure out what works best for you."
    
    s "Yea, you're definitely better at school than I am, but I will try all those things to get better."
    
    a "It is just a matter of work ethic and discipline. Work is what you make of it."
    
    s "I guess I could learn a thing or two from you and Bella."
    
    a "You are only a freshman, so you have plenty of time to learn how to work. You will improve over time."
    
    show Ari neutral at right
    
    "The bell rings from the classroom."
    
    a "Well, that is all the time we have for today's club meeting and lesson. Hopefully you learned something."
    
    s "Yeah, definitely learned how bad I am at studying, that's for sure."
    
    a "A master of something was once a student. You have to start from somewhere."
    
    s "Mhm. Can I ask you to tutor me again on other stuff? You seem to know a lot about, pretty much everything."
    
    a "Well, I do not even speak Spanish, but I was able to teach you because I know French."
    
    s "Well, that's neat."
    
    a "Anyways, i'll be glad to tutor you on anything I can. Just meet with me next time I see you in the club. I need to go on ahead."
    
    s "Alright! I'll see you later, man."
    
    a "You take care, now."
    
    hide Ari neutral at right
    
    "Ari waves us goodbye and heads out of the clubroom."
    
    show Bella neutral at left
    
    b "Hey, Sam! It's time to head home from the club. What did you do today?"
    
    s "Ari tutored me for math and other stuff."
    
    b "Really? That's great! Did it go well?"
    
    s "He taught me more than what my math teacher taught me in class today, so yeah. I learned a lot from him. He was a really good teacher."
    
    b "It's only natural he's good at academic stuff. He's in the academics team and he got first place in a bunch of contests for math, science, and other stuff." 
    
    b "He won first in the national contest last week and he's going on to the international contests."
    
    s "Seriously?! This guy is insanely smart!"
    
    show Cynthia neutral at right
    
    c "Really. He's a prodigy. He was all over the school newspaper for it."
    
    s "And he tells me there's always someone smarter than him. I can't imagine who that could be."
    
    c "Not to mention he's the same age as you, Sam."
    
    b "He's definitely smart, but he's really shy. He hardly talked to anyone during the interview with the school news or even the teachers."
    
    s "What do you mean?"
    
    b "He was really quiet and was shaking the entire time, even when interviewing with me. Poor guy probably had stage fright."
    
    s "He doesn't feel shy when he's with us."
    
    c "Perhaps you can help him with that?"
    
    s "I'll try to. That's the least I can do when he's teaching me stuff."
    
    b "Let's all head home, now. Ari went on ahead."
    
    hide Cynthia neutral at right
    hide Sam neutral
    hide Bella neutral at left
    
    with dissolve
    with fade
    
    scene bg sidewalk
    
    "We head home and just casually talk about how our day went. I spent most of my time with Ari today, that I feel out of touch when I ask Bella and Cynthia how their day went."

if Ch1A_active:
        
    "Bella and I see Cynthia home leaving the two of us alone."
    
    show Sam neutral
    show Bella sad at left
    
    b "Sam, can I ask you a favor?"
    
    s "What is it?"
    
    b "Take care of Ari for us."
    
    show Sam sad
    
    s "Okay, but why do you ask me that?"
    
    b "I think you're the closest person to him right now as you have been spending a lot of time with him."
    
    b "I had to interview him a week ago for the newspaper and met with him in private. He didn't say much, but I could tell that he's been feeling really sad recently."
    
    s "Really? Why?"
    
    b "He said he was happy that he did really well in the contests, but he didn't sound too happy. Just an empty smile."
    
    s "How could you tell?"
    
    b "Sometimes I felt the same way too."
    
    s "..."
    
    "A moment of silence passes."
    
    b "You taught me how to read people, because you were there when he was feeling down."
    
    b "I saw you talk to Ari first on the first day of the club. He just sat in the corner with a sad look and kept to himself. He wouldn't even talk to me or Cynthia when I tried to approach."
    
    b "However, when you talked to him and cheered him up. You showed us how to help."
    
    b "I want to be able to help Ari, but I don't know too much of what I could do."
    
    b "Kinda pathetic that the club president can't even help her member."
    
    b "I feel really guilty to ask this of you, but please just help him."
    
    s "..."
    
    show Sam talking
    
    s "Of course. He's my friend."
    
    s "I understand that you feel bad, but you shouldn't. It's hard knowing what to do to help. In fact, i'm happy you asked me for help."
    
    show Sam happy
    
    s "We'll help him together. You can count on me."
    
    show Bella happy at left
    
    b "You're a really nice guy, Sam. I'm glad I have you."
    
    show Sam neutral
    
    s "Don't worry about it now. Let's just go home."
    
    hide Sam neutral
    hide Bella happy at left
    
    "We both head home with a bittersweet mood."
    
else:
    
    "I suppose i'll try spending time with the others too. I'll just look forward to what the next day brings."
    
#End of Chapter 2A
    jump Ch3
    
label TrueFork2:
    
    with dissolve
    with fade
    show Bella neutral
    show Sam neutral at right
    
    b "Hey, Sam! So, what's up?"
    
    s "Not much."
    
    s "I don't know what to do today, so is it okay if I..."
    
menu:
    "Hang out with you today?":
        jump Ch2B
        
    "Help me with something?":
        jump Ch2S

#Chapter 2B: Heavy Lifting
label Ch2B:
    
    b "No, i'm really busy. The cultural festival for the school is coming up and there definitely isn't enough of me or enough of the student government to set everything up."
    
    b "We've got all kinds of clubs showing for the entire thing and I need to organize the booths for all 20 clubs coming to the festival along with three outside organizations sponsoring the event."
    
    b "It's all really stressful! I can't seem to figure out a good system to work with everyone."
    
    s "Oof. That's a lot to work with."
    
    show Bella embarrassed
    
    b "Perhaps I was way over my head when I decided to become class president and do all of this."
    
    s "You did say you wanted to try all of those things. You're also in the poetry club, the school newspaper, theater club, and choir on top of it all right?"
    
    show Bella sad
    
    b "I can't even keep my head straight on what I need to do in everything else."
    
    "Bella lets out a sigh in a deflated spirit."
    
    "It shows that not only she's really stressed, but also she's exhausted and overwhelmed."
    
    b "Is there anything else you needed?"
    
menu:
    "Should I Help Bella?"
        
    "Yes":
        jump Ch2BY
            
    "No":
        jump Ch2No
            
#Chapter 2B Accepted
label Ch2BY:

    $ Ch2B_active = True
    $ persistent.Ch2BCG_unlocked = True
        
    with dissolve
    with fade
    
    s "No, actually. I should be asking that to you."
    
    show Bella talking
    
    b "Huh?"
    
    s "Let me help you with all that stuff you're doing for the festival."
    
    s "No. In fact, let me do everything for you."
    
    b "I can't let you do that, i'd be shirking in my duties as class president."
    
    s "Like you can be our class president right now with how exhausted and stressed you are. You won't make very clear decisions and get anything done like that." 
    
    b "No, it's okay-"
    
    s "No, it's not okay. You need some rest right now. I see you're always working before, during, after school that you can't even focus on your school work."
    
    show Bella embarrassed
    
    b "Urk..."
    
    s "Just let me take care of you, just like always."
    
    show Sam talking at right
    
    "I start singing along to quote my favorite song..."
    
    s "Lean on me, when you're not strong.~"
    
    s "And i'll be your friend.~"
    
    s "I'll help you carry on~"
    
    s "For it won't be long~"
    
    s "'Til I'm gonna need~"
    
    s "Somebody to lean on.~"
    
    #Reference: Bill Withers - Lean on Me
    
    show Bella happy
    
    b "Awww. Sam, you have to be cheesy like that?"
    
    show Sam embarrassed at right
    
    s "What?"
    
    b "Thanks."
    
    show Sam happy at right
    
    s "You can count on me."
    
    with dissolve
    with fade
    
    scene bg hallway
    
    show Bella talking
    show Sam neutral at right
    
    b "Be ready to use a good amount of elbow grease today. We're carrying heavy stuff today. We need to carry boxes of food, papers, props, machines, and a bunch of other stuff."
    
    s "Can't we just use the hand trucks?"
    
    b "Sure, if you can get your hands on one. The school staff is already using all of those to carry stuff."
    
    s "So, we're just gonna have to carry them ourselves?"
    
    b "Yeah. Some need to be taken out of closets and storages, from the trucks, all over the place."
    
    s "Yikes."
    
    b "Hmm. So, where should we start?"
    
    s "Getting all the help we can. Student government only consists of like 20 people right? Along with the school staff with their hands full, you guys are still swamped."
    
    s "Let's make it easier on everyone by getting more hands on deck."
    
    s "Many hands make light work."
    
    b "Okay, but where are we gonna get more people to help?"
    
    show Cynthia talking at left
    
    c "Don't you guys know anyone in this school? Geez."
    
    c "I guess i'll have to get you guys some of my people to help you out."
    
    s "Cynthia!"
    
    c "I know people that know people and so forth. If you need people, just ask me."
    
    b "Really? You would do that for us?"
    
    show Cynthia neutral at left
    
    c "Just give an incentive, and i'll work my way with words.~"
    
    b "Hmmm...How about some food and refreshments like pizza and donuts? We'll have plenty at the festival!"
    
    c "Perfect. I'll talk to them."
    
    hide Cynthia neutral at left
    
    s "Well that worked out nicely."
    
    show Ari talking at left
    
    a "If you need coordination and organizing, I can give you a hand in working with everyone."
    
    a "I can serve as you secretary."
    
    b "Really? Thanks so much. That would help me out so much."
    
    a "Just give me a list of what needs to be done and the people I need to meet with. I will organize things on your behalf."
    
    b "Okay, let me just talk with Sam for a while to get him started. Go see my advisor and ask her for details."
    
    hide Ari talking at left
    
    "Ari bows and heads out to go meet with Bella's advisor."
    
    s "There ya go. See? It all worked out."
    
    b "You definitely inspire others."
    
    s "Me? What did I do?"
    
    b "You're so kind in helping that you inspire others to help. That's really cool about you."
    
    show Sam embarrassed at right
    
    s "Come on, let's get started. What do I need to lift."
    
    hide Sam embarrassed at right
    hide Bella talking
    
    scene bg cgheavylifting
    
    "Bella sends me to start carrying a bunch of props and decorations."
    
    s "Geez these boxes have to weigh at least 30 pounds or so and it's just a bunch of props."
    
    "Cynthia comes back not too long after and has brough a bunch of her classmates and friends over to help."
    
    c "You need reinforcements?"
    
    b "Okay, perfect! Just have everyone wear some of these stickers to know you guys are helping out with the staff. We'll have the food and stuff ready later."
    
    c "Come on guys! Let's get to work already."
    
    "Everyone quickly organizes to get to work."
    
    a "I've sent some of the officers to organize workers by role. I've given the officers and some workers walkie-talkies to help everyone talk to each other to make working with each other easier."
    
    s "Where'd you get the walkie-talkies?"
    
    a "I quickly bought a cheap set at the store to use."
    
    a "Communication is essential for a team to work."
    
    a "Also, i've arranged the posters and flyers for the festival with the other officers as well."
    
    b "You work fast."
    
    "After a few minutes, we're all organized into teams based on roles and put to work right away."
    
    "It only takes an entire hour and a half for the whole company to prepare the gym for tonight's festival. All the stands are decorated with props with their respective club." 
    
    "Paper mache rapiers for the fencing club, notebooks and pens for the poetry club, etc."
    
    b "Thanks so much for your help guys! Please help yourself to some snacks and refreshments from the catering. Although save some for everyone else coming to the festival!"
    
    a "Well that was done quite efficiently, especially with the amount of volunteers."
    
    c "Mhm. We got so much done. I just went ahead and started snacking because there wasn't much left for me to do."
    
    s "Up and down the stairs carrying a couple dozen pounds of props has got me beat."
    
    b "Well you can take a break now, Sam. You've done good work today!"
    
    s "Thanks. I'll gladly take a couple donuts for a snack."
    
    "We all take a short break and then prepare for visitors for the festival."
    
    "The festival was huge as not only a bunch of clubs and students were there, but also parents and neighbors came to check it out."
    
    "Food stands, attractions, showcases, there was a lot prepared for the festival. With a lot of visitors to match the amount of stuff in the festival, I would say it was a hug success."
    
    "Bella, Cynthia, Ari, and I also took time to enjoy the festival ourselves."
    
    "Cynthia spent most of her time in the local orphanage's booth talking to the foster kids, Ari spent most of his time painting with the art club. It left Bella and I just with each other for a while."
    
    b "Hey, Sam can I talk to you for a bit?"
    
    scene bg hallway
    
    show Bella neutral
    show Sam neutral at right
    
if Ch1B_active:
    b "I'm really thankful for you helping me out today."
    
    s "I'm always looking out for you, so it's become second nature for me now."
    
    b "You're too nice to me, Sam. You really don't need to be doing this much for me."
    
    s "I've always been stuck with you and you've always been a mess."
    
    b "And you're always looking after this mess."
    
    s "Of course."
    
    show Bella embarrassed
    
    b "I'm really tired after today, can you take me home today? I'll text Ari that i'm heading home early."
    
    s "Sure. We usually go home together anyway."
    
    scene bg sidewalk
    
    "Bella and I head home together, but she had a really hard time walking that I had to carry her on my back after a while, since she was so exhausted."
    
    "I take her to her house where her parents saw her to bed. Promptly after I head home, but from time to time I came to check on her."
    
    "I'm really concerned for Bella as she was overly exhausted from working today. Most likely because she's not getting enough rest from all the work she does."
    
    "I should look after her more closely before she works herself too hard. She likes to work, but at this point, it is to a fault."
    
    "Hopefully she doesn't push herself too hard."
    
    "I'll have to see what tomorrow brings. I'll gladly help her through it."
    
else:
    b "Thanks so much for your help today, Sam."
    
    b "Really you helped me out more than you know today."
    
    s "No problem. Call me anytime you need my help again. You can always count on me."
    
    b "I'm rather exhausted today. I'm going home early today. Tell the others okay? I'll see you around."
    
    hide Bella neutral
    
    "Bella heads home early. Probably had a very long day today. I hang out at the festival with Cynthia and Ari for a while, then we helped out with cleaning up and covered for Bella."
    
    with dissolve
    with fade
    
    scene bg sidewalk
    
    "Today was a long day. It was a lot of work, I guess, but I was really happy to help Bella out in the festival."
    
    "I also head home really exhausted from today. A lot happened for today, so I sympathize with Bella feeling exhausted."
    
    "It was fun working with everyone today, it'll be more fun spending time with everyone, but for today i'm really tired."
    
    "I'm still looking forward to what happens tomorrow..."
    
#End of Chapter 2B
    jump Ch3
    
#Chapter 2C: Page by Page
label Ch2C:
    
    with dissolve
    with fade
    
    show Cynthia neutral
    show Sam neutral at right
    
    s "Hey, Cynthia. What are you doing?"
    
    c "Just reading whatever."
    
    s "What kind of books are you reading? They're not like the college textbook Ari is reading is it?"
    
    c "No, I can't understand science and stuff. I'd rather just read for a story."
    
    s "Well what's the book you're reading about?"
    
    c "It's about a love triangle between a guy and two other girls in high school. The guy really likes one girl, but the other girl has a secret crush on him."
    
    s "What kind of crazy story is that?"
    
    c "It was really popular at the library so I decided to go check it out."
    
    c "Do you want to read it with me?"
    
menu:
    "Read with Cynthia?"
        
    "Yes":
        jump Ch2CY
            
    "No":
        jump Ch2No

#Chapter 2C Accepted
label Ch2CY:

    $ Ch2C_active = True
    $ persistent.Ch2CCG_unlocked = True

    c "Cool. Just pull up a chair."
    
    s "Okay."
    
    "I pull up a chair from a nearby desk and sit next to Cynthia."
    
    c "No, come closer. You won't get a good look of the pages from there."
    
    hide Cynthia neutral
    hide Sam neutral at right
    
    scene bg cgpagebypage
    
    "She pulls me closer to her to the point where my shoulders are directly touching hers."
    
    c "There we go.~"
    
    c "Don't worry I won't bite, but no guarantees."
    
    s "Right. So what kind of book are we reading?"
    
    c "It's a basic romance novel. Really it's very cliche in how it pitches the story, but for some reason it's really popular."
    
    c "What kinds of books do you usually read?"
    
    "I was always just watching the movie version of the book fully knowing it leaves parts out, and the only 'books' that I usually read are just comics and manga."
    
    "I quietly answer to hide my shame."
    
    s "Comics and manga."
    
    c "That's cool. I don't read much of those but i've read some manga before. Mostly just drama and romance."
    
    s "Romance and drama is really favorite types of stories?"
    
    c "Clearly. I think I watch too many soap operas and dramatic movies, so my preference in reading is pretty much the same."
    
    s "It's kinda the same way with me. I like to watch action movies so superhero comics and action manga are a close favorite."
    
    c "Well, maybe I can change your mind and make you read other stuff."
    
    s "This better not be really overdramatic stuff. I feel like we've seen it all already."
    
    c "It's kinda like that at times, but yeah I understand what you mean."
    
    c "Let's just start at the beginning so you understand the plot so you can get over the cheesy and overly dramatic scenes."
    
    "Cynthia and I start reading the story to each other. At first we start off at a fair pace, then I notice Cynthia begins to pick up the pace and starts to read aloud quite quickly."
    
    s "Take it easy, i'm not reading as fast as you are."
    
    c "Oh, sorry. I'll take it a bit slower for you."
    
    "Slowly Cynthia and I begin to read at the same pace."
    
    "..."
    
    c "It's a slow pace at first."
    
    s "That's only the first part."
    
    c "Lots of books do start slow, but I like stories that jump right into the action. Character exposition is nice, but I like it when we don't know much at first to begin with and learn about them more as the book progresses."
    
    s "I guess that's fair. Let's move on to the next chapter and see if it does move on faster."
    
    "We continue reading back to the pace we unspokenly agreed to."
    
    "Indeed the book picked up speed as a lot of stuff happens in the next part as the author did not hesitate to let loose."
    
    "Confessions come out abruptly for both of the girls, accidents and dangerous events happen really fast leaving you asking what happened."
    
    "I look over and see Cynthia is completely absorbed in the book in the confession of one of the girls."
    
    "Cynthia comes closer to me and begins to hold my arm tightly and pushes her chest against it."
    
    s "Umm, Cynthia?"
    
    c "Yea?"
    
    "She's snuggled up next to me in a very awkward position, but she was so into the book, she didn't even realize."
    
    s "You're awfully close to me."
    
    c "Oh, sorry about that. It just got really intense that I tend to just grasp something when it gets like that. Does it bother you?"
    
    "It's really awkward, but it kinda doesn't bother me that much."
    
    s "Not really, it's fine if you want to."
    
    c "Okay."
    
    "She turns back to the book to try to hide her embarrassment."
    
    "..."
    
    "We continue on to the last part of the book and it was even more intense than the second leading up to the decision between the two maidens for the main character."
    
    c "Mmmm..."
    
    "Cynthia clearly anxious to turn the page about the big decision of the story."
    
    "We turn the page and..."
    
    s "It just ends like that?"
    
    c "A cliffhanger! Oh how evil."
    
    s "They just leave us hanging like that?"
    
    c "Authors do this all the time to make readers buy their next book in their series, but it also spurs a lot of fanfiction."
    
    s "Are they any good usually?"
    
    c "Rarely, most of them are garbage."
    
    s "Oh."
    
    c "Overall a really exciting book even though it's a really cliche love triangle for a plot."
    
    c "However, for such a simple plot, i've never read such a genuine and dramatic story."
    
    s "Really? That's how you would rate the book? A lot of stuff just happened so quickly in the book."
    
    c "I've already read a lot of these types of books before and they like to write a lot like this. Sometimes they're all the same. This book, however, was really good in spite of all that."
    
    s "Hmm..."
    
    c "It's eerie."
    
    s "What?"
    
    c "This type of story sounds really familiar. I don't know from where i've seen something like this, but I recognize it."
    
    s "Really?"
    
    "Cynthia stares into my eyes once more with a dazed look. This time I stare back at her with a similarly dazed look."
    
    c "Mmm..."
    
    s "Cynthia?"
    
    c "They say you can stare into another person's soul through their eyes. Do you believe that?"
    
    s "I don't understand what that means."
    
    c "Mmm..."
    
    c "Do you feel weird staring back at me like this?"
    
    s "I won't lie, it does feel awkward."
    
    c "Anything else?"
    
    s "I-"
    
    "I stutter to say what I want to say to Cynthia as I am completely embarrassed and confused on how to act in a situation like this."
    
    s "I don't know what to say."
    
    c "Then just don't say anything and just keep staring back at me."
    
    "Stare back I did. I completely surrender myself to the locked gaze of Cynthia."
    
    "Our eyes lock for that brief moment that feels longer than 30 seconds should."
    
    c "Sam, I-"
    
    "Cynthia giggles a little bit."
    
    scene bg clubroom
    
    show Sam embarrassed at right
    show Cynthia happy
    
    c "You're completely red, Sam"
    
    "I don't even notice that my face has turned bright red from embarrassment and I quickly turn my face to hide."
    
    s "Er..."
    
    s "No i'm not!"
    
    c "Say that all you want, but your face can't lie!"
    
    s "Geez.."
    
    "She continues to giggle."
    
    c "You really make it easy for me to tease you."
    
    s "You and your mind games, you're just completely messing with me."
    
    "Her giggling stops for a second and she talks in a regular tone."
    
    show Cynthia neutral
    
    c "I'm not just completely messing with you."
    
    show Sam neutral at right
    
    s "I don't even know if that's true."
    
    c "I meant to say-"
    
    show Bella neutral at left
    
    b "Hey, guys! Can we all come together for a second?"
    
    s "What?"
    
    c "Nevermind. Let's go meet up with Ari."
    
    hide Cynthia neutral
    
    s "Bella!"
    
    b "What?"
    
    with dissolve
    with fade
    
    show Ari neutral at right
    
    a "Alright. So what is your announcement that should be brought to our attention?"
    
    show Bella talking at left
    
    b "The student government is hosting a culture festival and a lot of the school clubs will be there. It goes down this Thursday since it's taking us quite a while to get everything set up."
    
    b "Ari, Cynthia, I was wondering if you guys want to represent our club to try to recruit more members."
    
    show Sam talking
    
    s "More people to our club? Do you think that's a good idea?"
    
    hide Ari neutral at right
    show Cynthia talking at right
    
    c "No, that's not a good idea."
    
    b "Really? Sam? Ari?"
    
    hide Sam talking
    show Ari talking
    
    a "I have to admit, I do appreciate the club more when it is just us as its sole members."
    
    hide Ari talking
    show Sam talking
    
    s "To be honest, I only joined because of you at first, Bella. It wouldn't be the same if it wasn't just us."
    
    s "I don't want to sound selfish, but I really like it when it's just us four."
    
    c "It feels more intimate like this. I meet with people and have a lot of friends, but you guys aren't the same compared to everyone else."
    
    show Cynthia neutral at right
    show Bella sad at left
    
    b "Hmm..."
    
    s "Sorry to shoot your idea down like that, but it seems we all agree on it."
    
    show Bella happy at left
    
    b "It seems that's what everyone wants. If it's what you guys want, who am I to disagree? In fact, i'm happy you guys really feel that way about the club."
    
    b "I was afraid you guys didn't like each other that much and might like to see other people."
    
    show Sam neutral
    
    s "That's great you agree. Thanks for understanding."
    
    show Bella neutral at left
    
    b "I still have to be at the festival, so will you guys go to the festival with me?"
    
    s "Sure!"
    
    "Cynthia stares at Bella's eyes for a brief moment then lets out a small giggle."
    
    c "So that's what you're afraid of."
    
    b "Huh?"
    
    c "Nevermind. I'll be there too. I'll see you guys there."
    
    hide Cynthia neutral at right
    
    "Cynthia quickly packs up and leaves the room."
    
    b "Okay, see ya!"
    
    show Ari neutral at right
    
    a "I will also attend. Thank you for inviting us."
    
    hide Ari neutral at right
    
    "Ari bows and leaves the room."
    
    s "I guess that settles it."
    
    s "I'll head out too. Don't take your pitch too seriously Bella. You we're just proposing an idea to the club. It's okay we didn't like it, since you show that you are concerned for us."
    
    b "Okay. Thanks, Sam."
    
    s "Come on. Let's head home."
    
    "Bella and I head home for the day."
    
    hide Sam neutral
    hide Bella neutral at left
    
    with dissolve
    with fade
    
    scene bg hallway
    
if Ch1C_active:
    
    "A few days later, the cultural festival finally takes place and the girls and I happily enjoyed the festival."
    
    "Ari actually couldn't make it to the festival since he got sick with a cold and stayed home for the day leaving me with the girls."
    
    "I could tell there was some sort of rivalry forming between them as continously both of them keep tugging at me for attention."
    
    "The three of us promptly head home after the festival's end and I walk the two of them back home leaving me completely exhausted."
    
    "Perhaps I now understand why Cynthia stares at me with such a daze now."
    
    "Does she have a crush on me and sees Bella as a huge rival?"
    
    "Now it sounds like the love triangle crisis in the book Cynthia and I read together..."
    
    "Maybe. Or it's just another mind game of hers."
    
    "I'll admit I feel really close with Bella as a close friend, but i'm starting to be also close to Cynthia that i'm left confused."
    
    "Perhaps I should spend more time with Cynthia..."
    
else:
    
    "A few days later, the cultural festival finally takes place and the four of us happily enjoyed the festival."
    
    "I've been spending a lot of time with Cynthia lately that I spend most of my time in the festival with her."
    
    "Perhaps I should spend some of my time with the others, because I feel bad when someone does get left out..."
    
#End of Chapter 2C
    jump Ch3

#Chapter 2S: Writing Together
label Ch2S:
    
    b "Really? Are you sure?"
    
menu:
    "Let Bella help?"
        
    "Yes":
        jump Ch2SY
            
    "No":
        jump Ch2No
            
#Chapter 2S Accepted
label Ch2SY:

    $ Ch2S_active = True
    $ persistent.Ch2SCG_unlocked = True
    
    show Bella neutral
    show Sam sad at right
    
    s "Yeah, but I don't know how to go about it."
    
    b "Go about what?"
    
    s "I think you're the only one here who gets this."
    
    b "Is it about your mom?"
    
    s "Mmm."
    
    "I nod in agreement."
    
    s "Winter break and Christmas is coming up and I just heard from her that she can't come home for it. Again."
    
    "I clench my fists."
    
    s "Ever since I started high school, she went on even more business trips. I get she takes work seriously, but I miss her."
    
    s "Ever since she hit it big, she hasn't been coming home."
    
    "I sigh a little."
    
    b "She's gotta come home sometime, don't worry."
    
    s "Sure, but she's changed. The last time I talked to her, it didn't end pretty."
    
    b "I'm guessing things haven't changed ever since."
    
    s "Nope."
    
    b "Hmm..."
    
    show Bella talking
    
    b "I know what would be a good thing to do?"
    
    s "What?"
    
    b "Talk to her. Write her a letter."
    
    s "Really? That seems too simple, also she's just gonna ignore my email in her inbox of millions of other emails."
    
    b "No, like actually write her a letter in pen and paper."
    
    s "I don't see why you think this might work."
    
    b "For one, it could show that you really made an effort in writing it so that it feels more personal."
    
    b "Also, it would be more likely that she reads it as it doesn't get lost like an email in a huge inbox."
   
   show Bella neutral
   
    b "It's old-fashioned, but I really appreciate it when people still take time and effort to send letters like that."
    
    b "My family still sends letters to each other like that. It feels more genuine."
    
    show Sam neutral at right
    
    s "That actually sounds like a great idea if you put it like that."
    
    s "Threre's a problem though."
    
    b "What's that?"
    
    s "I haven't written a letter on paper before."
    
    hide Bella neutral
    hide Sam neutral at right
    
    scene bg cgwritingtogether
    
    b "Seriously?"
    
    s "I'm much more used to just writing emails now."
    
    b "Fine. Get out a nice pen and a clean sheet of paper. This time, i'm the one helping you."
    
    s "Yeah, by all means."
    
    "I take out a sheet of notebook paper and a pencil."
    
    b "No! You need a clean sheet like printer paper and a really nice pen! It won't look nice like that!"
    
    s "Oh come on."
    
    b "Here. I'll give you what you need. Good thing I keep spare stuff like this."
    
    "Bella takes out a rather fancy calligraphy pen, a blank sheet of paper, and an envelope."
    
    b "Let's get started!"
    
    "I grab the pen and as I was about to write, Bella quickly grabs my hand."
    
    b "What are you doing?"
    
    s "I'm writing! That's what i'm suppossed to do right?"
    
    b "Have you even thought about what you're going to write about?"
    
    s "Urk."
    
    b "Think about what you're going to do first before you do it. Also, this is a pen, not a pencil."
    
    "Bella takes a notecard and a pencil."
    
    b "What are we writing about?"
    
    s "Isn't it obvious?"
    
    b "You have to be specific. Writing about a certain point will make it easier to get your message across. Also, I bet your mom would want it to get straight to the point."
    
    s "Okay. Let's make it simple."
    
    s "It's about wishing happy holidays even though she's abroad."
    
    b "Good. Next what do you want to address?"
    
    s "Ummm."
    
    "I stop for a minute to think of where she might be right now."
    
    s "Last time I checked, she's going to France for a month to make some deals with companies."
    
    b "We could go with a French theme!"
    
    s "Let's not do that. Let's just stick to a simple Christmas theme from here."
    
    b "Okay."
    
    s "I want to wish her a happy Christmas even though she's far away from home."
    
    s "I'll wish her safe travels and a peaceful time there, and-"
    
    "I stutter as I realize this isn't all that I really want to say to her."
    
    b "And what, Sam?"
    
    "I silently mutter the word."
    
    b "What?"
    
    s "I want her to come home. I miss her so much."
    
    s "I know we had a little disagreement over me starting school here, but I wanted this."
    
    b "Sam?"
    
    "I pause and take in what I just said."
    
    s "Before I started this year, my mom wanted us to move over to France."
    
    s "I told her that I didn't want to move anymore. I had moved about 4 times before moving here and staying for a while."
    
    s "I met you and became friends with you for about how long now?"
    
    b "I think about six years."
    
    s "I said some things that I regret saying to her. She left for work and I haven't talked to her since."
    
    b "I still think you should talk to her though."
    
    s "I'm still mad at her though."
    
    "I clench my fists tighter, but Bella puts her hand over mine and unclenches them."
    
    b "Tell that to her through the paper."
    
    s "..."
    
    b "Come on. I'll write with you."
    
    s "..."
    
    "I hesitantly look at the paper, then look at her face. For a brief moment, we stare at each others' eyes which seem to make the moment last longer."
    
    b "Sam?"
    
    s "Okay. I'll write with you."
    
    "Bella nods and we both start writing."
    
    "Bella coaches me on grammar, spelling, and looks over at my writing style. Of course, I make a lot of grammatical and spelling mistakes along the way, but Bella really liked my style of writing."
    
    b "Sam, the way you write is-"
    
    s "What about it?"
    
    b "It's beautiful. You have such a bittersweet tone."
    
    s "What is bittersweet about this?"
    
    b "You write with sadness, yet still write as if you are still happy, hoping for the next day."
    
    s "Does it really look like that?"
    
    "I look over the paper to see my first rough draft and indeed, she describes my style perfectly."
    
    s "I guess it's hard for myself to see that."
    
    "I finish writing my rough draft and Bella and I look over it a couple of times..."
    
    b "This is perfect. You really made a nice letter here. Not only it's genuine, bittersweet, it's totally you."
    
    b "This wouldn't be the same when typed through an email."
    
    s "It's just words on a paper."
    
    b "It says that it's much more than that. Believe me."
    
    b "Now let's actually print it with that calligraphy pen I gave you onto the blank paper."
    
    "I take the pen and begin to make strokes and rewrite my letter."
    
    b "You're a natural with that pen. You always had really nice handwriting."
    
    s "I play a lot of videogames and draw a lot. I guess it comes to me naturally."
    
    "I finish rewriting my draft, put the date and address on the paper."
    
    b "Now all that's left is to sign it."
    
    s "Right."
    
    "I sign my name at the bottom as meticulously and neatly as I can in my finest penmanship."
    
    b "You could make art with that."
    
    s "Are you sure you're just saying all of this or is it just to encourage me?"
    
    "Bella is taken aback by my remark."
    
    b "No, really! This really is a nice letter that you wrote. I'm saying this truthfully. I wouldn't lie to you like that. We've known each other for quite a while now! You would know if I told you that what you made is garbage."
    
    s "Okay."
    
    b "Since when are you not confident?"
    
    s "All the time. You on the other hand, are always confident."
    
    b "Don't be like that. You really are awesome, okay? Now be proud about what you made."
    
    "I look over my finished letter, then start to smile."
    
    s "Why did you make me do this again?"
    
    "We both start to giggle."
    
    b "Because, i'm helping you this time. It's for your own good."
    
    "We let the ink dry on the paper after a couple minutes. Bella folds the letter and puts it into the envelope. She stamps the envelope with a stamp and seals the folds with an intricate seal."
    
    "I place my stamp with my address and place a stamp with my mom's work address in her office in France."
    
    b "There we go."
    
    s "That seal, is it yours?"
    
    b "Yeah, it's my family's seal. It was passed down from my grandfather's ancenstors."
    
    s "It looks nice."
    
    b "Just take that to the post office or a mailbox to your mom. I think you know how to do that at least."
    
    s "What?"
    
    "Bella giggles a little bit."
    
    b "Sam?"
    
    s "Yeah?"
    
    b "Can you just stare at my eyes for a while?"
    
    "A rather weird request coming from Bella. I wonder why she would ask me of this."
    
    s "Why?"
    
    b "It felt weird a while ago when we did it, but I want to feel it again."
    
    "So, I stare at her eyes and she stares back."
    
    "Suddenly, I understand what she meant by a weird feeling. I peer into her clear green eyes..."
    
    "What was a brief moment felt like a day."
    
    "Our stare is broken by the sound of the bell."
    
    scene bg clubroom
    
    show Bella embarrassed
    show Sam embarrassed at right
    
    b "Ack! Wait, that's just the bell."
    
    s "Ah."
    
    s "We probably should get going. You've got more work today for the festival tomorrow right?"
    
    b "Umm..Yeah."
    
    show Ari neutral at left
    
    a "Hello, you two. I trust you two enjoyed yourselves today at our meeting?"
    
    b "Uh..."
    
    s "Yes, Ari. Anyways, what's up?"
    
    a "That's good. I was just about to head home to let you know. I hear the culture festival is coming up, so i'll see you guys there."
    
    b "R-right! I'll see you soon Ari!"
    
    a "Take care, everyone!"
    
    hide Ari neutral at left
    
    "Ari bows and heads out the door."
    
    show Cynthia neutral at left
    
    c "You guys sure did 'enjoy' yourselves over here, playing Romeo and Juliet."
    
    s "Umm.."
    
    c "I'm heading out too. I'll see you guys there at the festival too."
    
    b "Oh, okay. I'll see you Thursday, Cynthia!"
    
    show Cynthia happy at left
    
    c "You two are too cute together, you know? For sure you two will be a couple."
    
    s "Huh? Wait what?!"
    
    "Bella only stands embarrassed and mute beside me."
    
    c "Anyways, see you there!"
    
    hide Cynthia happy at left
    
    "Cynthia hums a little song as she heads out the door."
    
    c "I guess i'll you there too, Bella."
    
    b "Umm...Yeah."
    
    "Both of us are too embarrassed to say any more."
    
    hide Bella embarrassed
    hide Sam embarrassed at right
    
    with dissolve
    with fade
    
    scene bg hallway
    
if Ch1S_active:
    "It's the day of the festival, and I get to the festival first where we agreed to meet. I see Cynthia arrive before the others."
    
    show Cynthia neutral
    show Sam neutral at right
    
    c "Hey, Sam."
    
    s "Hey, Cynthia. You're here early like me."
    
    #Continue Script Work on Ch1S 11/27
    
else:
    "The whole club goes to the culture festival where we all enjoy ourselves with the food, games, and other festivities."
    
    "We were all exhausted after the festival. Bella tried to eat too much food, Cynthia danced along to the dancers, I played too many of the games, and Ari was just purely exhausted."
    
    "Still, it was a fun day for us. We head home from school together and head our separate ways for today. I wonder what the next day will bring."
    
#End of Chapter 2S
    jump Ch3
    
#Chapter 2N: The Culture Festival
label Ch2No:
    
    s "Nevermind, actually. I just need some time alone."
    
    "The next few minutes of the conversation results in it dying out. I just go to another seat and stare at the window to pass time."
    
#Chapter 3:Murphy's Law
label Ch3:

    # This ends the game.

    return