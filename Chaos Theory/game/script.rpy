#Chaos Theory: A Visual Novel by Mark Perez

#Storyboarding and Development by Mark Perez

#Art by ...

#Music by ...

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
    
    #image Sam neutral = "Sam_neutral.png"
    
    #image Sam happy = "Sam_happy.png"
    
    #image Sam sad = "Sam_sad.png"
    
    #image Sam embarrassed = "Sam_embarrassed.png"
    
    #image Sam talking = "Sam_embarrassed.png"
    
    #image Sam crying = "Sam_crying.png"
    
    
    
    #image Bella neutral = "Bella_neutral.png"
        
    #image Bella happy = "Bella_happy.png"
    
    #image Bella sad = "Bella_sad.png"
        
    #image Bella embarrassed = "Bella_embarrassed.png"
    
    #image Bella talking = "Bella_talking.png"
    
    #image Bella crying = "Bella_crying.png"
    
    
        
           
    #image Ari neutral = "Ari_neutral.png"
    
    #image Ari happy = "Ari_happy.png"   
    
    #image Ari sad = "Ari_sad.png"
    
    #image Ari embarrassed = "Ari_embarrassed.png"
    
    #image Ari talking = "Ari_talking.png"
    
    #image Ari crying = "Ari_crying.png"


    
    #image Cynthia neutral = "Cynthia_neutral.png"
    
    #image Cynthia happy = "Cynthia_happy.png"
    
    #image Cynthia sad = "Cynthia_sad.png"

    #image Cynthia embarrassed = "Cynthia_embarrassed.png"
    
    #image Cynthia talking = "Cynthia_talking.png"
    
    #image Cynthia crying = "Cynthia_crying.png"
    
#Background Scenes (14)

    #image bg schoolyard = "sidewalk.jpg"
    
    #image bg classroom = "clasroom.jpg"
    
    #image bg hallway = "hallway.jpg"
    
    #image bg clubroom = "clubroom.jpg"
    
    #image bg schoolfield = "schoolfield.jpg"
    
    #image bg frontboard = "frontboard.jpg"
    
    #image bg closet = "closet.jpg"
    
    #image bg lounge = "lounge.jpg"
    
    #image bg festival = "festival.jpg"
    
    #image bg mall = "mall.jpg"
    
    #image bg conferencecenter = "conferencecenter.jpg"
    
    #image bg park = "park.jpg"
    
    #image bg tower = "tower.jpg"
    
    #image bg barrenfield = "barrenfield.jpg"
    
#Character Graphics (9)

    #image bg cghardwork = "hardwork.jpg"
    
    #image bg cgfrisbeefun = "frisbeefun.jpg"
    
    #image bg cgdonnamoore = "donnamoore.jpg"
    
    #image bg cgqueencynthia = "queencynthia.jpg"
    
    #image bg cgwritingtogether = "writingtogether.jpg"
    
    #image bg cgheavylifting = "heavylifting.jpg"
    
    #image bg cgnaturalteacher = "naturalteacher.jpg"
    
    #image bg cgpagebypage = "pagebypage.jpg"
    
    #image bg cgunspokenfeelings = "unspokenfeelings.jpg"
    
    #image bg cgmother = "mother.jpg"
    
    #image bg cgheatedsituation = "heatedsituation.jpg"
    
    #image bg cgaccident = "accident.jpg"
    
#Ending Images (7)
    
    #image bg samsnote = "Sam_ending.jpg"
    
    #image bg arisletter = "Ari_ending.jpg"
    
    #image bg bellaspoem = "Bella_ending.jpg"
    
    #image bg cynthiasdiary = "Cynthia_ending.jpg"
    
    #image bg samsaddress1 = "Boring_ending.jpg"
    
    #image bg samsaddress2 = "Diverged_ending.jpg"
    
    #image bg myletter = "True_ending.jpg"
    
#Background Music (7)

define audio.maintheme = "maintheme.ogg"

define audio.regularday = "regularday.ogg"

define audio.sweetly = "sweetly.ogg"

define audio.playful = "playful.ogg"

define audio.bitterness = "bitterness.ogg"

define audio.emotion = "emotion.ogg"

define audio.trouble = "trouble.ogg"
    
label start:

#Prologue: An Ordinary Day

    scene bg sidewalk
    play music regularday loop
    
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
                                                                   
    "This silly exchange is how every morning goes during school."
    
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
    
    "Bella' voice grows louder as she continues of her speech about school"
    
    b "It's a place to celebrate and live life while we're young!"
    
    show Sam neutral at right
    
    s "Well, that was an overly dramatic way to put it."
    
    show Bella neutral
    
    b "It's true though, we only experience these 4 years once!"
    
    s "No, it's what we see in another 4 years in college and then for 50 years in a job."
    
    s "Just sitting, 'working', and being told to not break anything."
    
    b "There's more to school than just that! Also, it's just what you make of it, Sam. Speaking of which, are you joining any clubs this year?"
    
    s "No, and I'd like to keep it that way. I'll just spend my 8 hours in the prison called 'school' and take my leave."
    
    b "Oh come on! That's no fun at all! You used to love to play and do all sorts of things in junior high!"
    
    s "Yeah, but it was only to get into trouble. I'd rather just keep to myself rather than have some people yell at me now."
    
    b "I won't take 'no' for an answer! Come with me after school, I'll take you to go see some clubs."

    show Bella happy
    
    b "Well, we're here at the schoolyard! I'm bummed we don't have any classes together, but I still want to see you afterschool, okay? I'll see you then!"
    
    hide Bella happy
    
    "Before I can protest, she runs off to her classes."
    
    s "Ack...Okay, whatever, i'll indulge her."
    
    "I swear my story definitely sounds like the start to every shounen anime i've watched."
    
    "But this is reality, and the lives of real people are actually boring."

    s "Well, that's enough monologue wallowing about how boring everything here is. Time for another day of school..."

    hide Sam neutral
    with dissolve
    with fade
    
    scene bg classroom
    
    show Sam neutral
    
    s "Phew, finally the teacher stopped droning on and on. I know she's trying to clear with eveything, but there's always the idiots who will ask the same questions."
    
    "With that, the another school day ended with seemingly endless classes."
    
    "As I was about to leave the classroom to go meet with Bella, I catch the glare of a student with a pained look on his face right at the doorway."
    
    stop music fadeout 1.0
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
    play music playful loop
    
    "I meet up with Bella in the hallway to see her waiting for me outside my classroom."
    
    s "You're really serious with forcing me to join a club aren't you?"
    
    b "Come on, you've got the time and energy! Let's get you doing something!"
    
    "Bella takes my hand to go look at the various clubs in school."   
       
    with dissolve
    with fade

    b "How about the science club? You get to do cool experiments and show off your research!"
                                                                                              
    s "I would have to do research for a project of my choice about 'principles that broadens the horizons', huh?"
       
    "I try to read the club poster with enthusiasm, but it only came out sarcastically."
                                                                                        
    b "Yeah, you get to explore scientific concepts ranging from ecology, like studying the environment, to inorganic chemistry, like learning about metals!"
                                                                                                            
    s "Yeah, no, i've already had my fair share of lab accidents.."

    b "Err...Don't worry, there's other clubs that might interest you."

    with dissolve
    with fade

    b "How about the fencing club? You learn how to fence and use a sword for sport and defense!"
                                                                                                            
    s "Of course, you definitely want to see me with a sword..."
    
    with dissolve
    with fade

    b "How about the literature club? You get to read, write, and analyze varying works of literature from manga to modern novels!"
    
    s "I'm not exactly keen with a pen...I'm sure i'll end up writing chicken scratch the whole time."
    
    with dissolve
    with fade

    show Bella talking at left
    stop music fadeout 1.0
    
    b "There's gotta be a club you're somewhat interested in, Sam! Please at least try one out before saying no!"
    
    s "I'd rather be at home playing videogames than messing around in school."
    
    show Bella happy at left
    
    b "Come on, Sam! For me? Please?"
    
    s "..."
    
    b "Would you join if it was just me and a small group of friends?"
    
    s "...Maybe."
    
    b "Hmm...I've got an idea, wait here. I'm gonna ask a teacher something about the clubs."
    
    "Bella rushes over to the teachers' office with a smile."
    
    with dissolve
    with fade
    
    play music maintheme loop
    
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
    
    stop music fadeout 1.0
    hide Sam neutral
    
    scene bg sidewalk
    
    show Sam neutral
    
    "Here I was on my way home just casually walking home from school, then I saw another student from my class walking home from school."
    
    s "Hmm..he looks familiar..."
    
    show Ari sad at right
    
    sms "...."
    
    "He's carrying a bunch of books while blankly staring at the ground..."
    
    s "Why's he carrying all those books home? There can't be that much work in class already! Must be really a nerd."
    
    "As he was standing there stone-faced, a bunch of kids run past him and knock his books out of his arms, his glasses flying, and landing on the ground, but he didn't even react."
    
    "The kids run off not even knowing of their small accident, but he doesn't even raise a single complaint. Just another pained look."
    
    "Gathering courage, I walk over to him and start gathering his things for him."
    
    play music bitterness loop
    
    s "Are you okay? Those kids didn't even realize they knocked you over. Here's your glasses."
    
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
    
    stop music fadeout 1.0
    
    "He takes half of the books and carries them entrusting me with the other half."
    
    s "Anyway, I saw you earlier, you're from the same class from me, Ari, wasn't it?"
    
    play music regularday loop
    
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

    a "I reside in the city with my aunt as my only companion and guardian, but she's occupied with work frequently. I'm studying here and the rest of my family is still back home in Japan."

    s "Oh...I live with my family here, but I never see my parents much because they're working, so I guess we kinda have that in common. Also, you speak English way too well to be Japanese."

    a "I was born and raised here by my aunt, so it comes natural to me."
    
    s "Oh, cool!"

    s "You said you were in dual-enrollment classes, you really take school very seriously, huh? I admire that, but I don't see myself doing that."

    a "Why not?"

    s "You plan to be a lawyer, engineer, or doctor?"

    a "I aspire to be a profesional surgeon as my family hopes me to be."

    s "It's hard for me to find motivation to even get up for school. I'll probably just end up working at a bar, or shop, but I don't see that much as a problem. I just don't see myself having much potential and i'm mediocre at best with everything in school."

    a " There is probably something you are proficient and passionate about, you just have to find it and work hard. Everyone has limitless potential and anything can change."

    a "I want to be able to help people. It is not about the skills or the work that matters, rather it is the drive to achieve a goal and fulfill your life with a purpose."

    "I could only stand mute, without a response."

    a "Sorry, I know it sounds rather cliche, but I think it is the truth. I know it would be dreadful working over 50 years with an occupation you despise, and I would like to live through those 50 years of work on my terms, doing what I love doing."

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

    stop music fadeout 1.0
    show Sam happy
    play music maintheme loop

    s "Yeah, friend! I would be happy if you came!"

    show Ari happy at right

    a "Friend?"

    s "I know we just met, but yeah, friend! You seem like a cool person, and it would help you to know someone in school, so yeah friend! How about it?"

    "He stares at me with sheer joy."

    a "Yeah, friend. I will converse with you later."

    hide Ari happy at right
    stop music fadeout 1.0

    "Ari waves as we exchange goodbyes for the day. I head home with newfound happiness."
    
    s " He talks quite oddly and overly formal, but he's a cool guy. It ought to be interesting with him around."

    show Sam neutral at left

    "I head home and see Bella and an unfamiliar face waiting for me at the gate."

    play music regularday loop
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
    stop music fadeout 1.0
    play music maintheme loop

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
    
    stop music fadeout 1.0

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
    play music maintheme loop
    
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
    
    stop music fadeout 1.0
    with dissolve
    with fade
    
    scene bg schoolyard
    play music regularday loop
    
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
    scene bg clubroom
    stop music fadeout 1.0
    play music maintheme loop
    
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
    stop music fadeout 1.0
    play music playful loop
    
menu:
    
    "Who should I go hang out with?"
    
    "Ari!":
        jump Ch1A
    
    "Bella!":
        jump Ch1B
        
    "Cynthia!":
        jump TrueFork1

#Chapter 1A: Sam and Ari

label Ch1A

    show Sam neutral at right
    
    s "Hey, Ari! We already kinda know each other, so for now let's just hang out. What's going on?"
    
    show Ari neutral
        
    a "Just reading some material for my classes. Would you be interested in reading about thermodynamics?"
    
    show Sam embarrassed at right
    
    s "Thermo-what now?"
    
    a "Thermodynamics, studying the transfer of energy through systems."
    
    s "In simple terms that would be..."
    
    a "Looking at how objects heat up and cool down."
    
    show Sam neutral at right
    
    s "Oh, cool. For what class is this for?"
    
    a "It could be applicable to many different fields of sciences, but I am reading this for Biology, Chemistry, and Physics."
    
    s "I never saw any of this complicated stuff in Chemistry, is this for your college classes?"
    
    a "Indeed, that would explain the complexity of the material."
    
    s "Is it easy for you? I really didn't like Chemistry..."
    
    a "Relatively speaking with my experience and my aptitude for higher level sciences, yes I find it fairly simple to understand fundamental physics at a collegiate level."
    
    s "You're just extremely smart, aren't you?"
    
    a "There's always someone smarter than you. I am just another student like many others."
    
    s "Ok, but who is smarter than you around here?"
    
    a "I may seem very knowledgeable about the sciences, but in actuality, I am only just a savant at these types of subjects."
    
    show Sam embarrassed at right
    
    s "What does savant mean?"
    
    show Ari talking
    
    a "It describes a person that is only skilled at one talent."
    
    show Sam neutral at right
    
    s "Really?"
    
    show Ari embarrassed
    
    a "I still have trouble engaging in a conversation with others, composing and dictating a speech, and many other skills. I have much yet to learn."
    
    s "You're a genius though! Not a lot of highly students even at your level would be able to easily understand stuff like that!"
    
    show Ari neutral
    
    a "True, but I feel as if I do not have the aptitude to be skilled in many other things."
    
    s "Come on, you gotta be a little athletic, right?"
    
    a "I am rather feeble."
    
    s "I don't think so, I think you're stronger than you look."
    
    s "Also, I think you're short changing yourself, I bet you're really amazing at a bunch of stuff if you tried."
    
    a "..."
    
    hide Sam neutral at right
    
menu:

    "Should I help Ari?"
    
    "Yes":
        jump Ch1AY
        
    "No":
        jump Ch1No

#Ch1A Accepted
label Ch1AY

    $ Ari_Ch1 = True 

    show Sam neutral
    
    s "Come on, Ari! You've gotta be a genius at other things too other than there-mo-dee-nameks!"
    
    show Ari neutral at right
    
    a "Thermodynamics. Anyway, I guess it would not hurt to try other things. What do you suppose we should try?"
    
    s "Oh, shoot. I didn't think I would get this far."
    
    s "Have you ever played ultimate frisbee?"
    
    a "No, but I do at least have the knowledge of it."
    
    s "Come on, i'll show you and the girls how to play."
    
    show Bella neutral at left
    
    b "Hey, Sam! What's up?"
    
    s "Is it okay if we go out to the field today and play ultimate frisbee?"
    
    hide Ari neutral at right
    show Cynthia neutral at right
    
    c "That sounds like fun, sure why not?"
    
    b "Seems like everyone is up for it. I'll just ask my teacher if it's okay."
    
    hide Bella neutral at left
    show Ari neutral at left
    
    a "Might as well start gathering our belongings to move to the field."
    
    s "Right."
    
    hide Ari neutral at left
    hide Sam neutral
    hide Cynthia neutral at right
    
    "And so, we got the okay from Bella's teacher and got together to play some frisbee at the field."
    
    with dissolve
    
    scene bg schoolfield
    
    show Bella neutral at right
    
    b "This part of the field isn't used by anyone most times and the baseball team isn't meeting today, so lucky for us."
    
    show Sam neutral
    
    s "I know, what timing right?"
    
    show Cynthia neutral at left
    
    c "So, teach us how to play frisbee Sam."
    
    hide Cynthia neutral at left
    hide Bella neutral
    
    show Sam talking
    
    s "Alright, so the rules are simple."
    
    s "We make 2 teams, each team has to try to pass the frisbee to each teammate and reach their own end of their field. When the other team intercepts it, or a team gets to their end the other team gets their turn with the frisbee and starts off at the scoring team's end or where the frisbee was intercepted."
    
    s "If the frisbee is dropped and nobody catches it, it goes back to the team and the player who threw it and has 3 other tries to pass it to a teammate until the frisbee goes to the other team and starts right where the other team left off and switches sides towards their end of the field."
    
    s " You gotta try to score by passing to and coordinating with your teammate to get the frisbee to your end during your turn with the frisbee and try to stop the other team when they have the frisbee."
    
    s "For our little game, it's a best of 3."
    
    s "It seems a lot of rules, but you'll get the hang of it."
    
    show Sam neutral
    
    s "So what should the teams be?"
    
    show Bella neutral at left
    
    b "How about you and I Sam make a team, and Ari and Cynthia are the other team?"
    
    show Cynthia neutral at right
    
    c "I have no objections."
    
    hide Bella neutral at left
    show Ari neutral at left
    
    a "Likewise."
    
    s "Ok, that's it I guess. Now let's start!"
    
    hide Ari neutral at left
    hide Sam neutral
    hide Cynthai neutral at right
    
    with dissolve
    
    scene be cgfrisbeefun
    
    s "Come on, Bella, let's show em what we've got!"
    
    c "Alright Ari, show them we're no slouches either."
    
    a "I will do my best."
    
    b "Alright we've got the frisbee first!"
    
    "The game starts off without a hitch, Bella gets a good pass to me and we pass to each other to make it to the half way point of the field."
    
    c "We have a slight beginner's disadvantage here, but that won't stop me!"
    
    "Cynthia tries to block my pass to Bella, but I still got to throw the frisbee."
    
    b "I got it!"
    
    "With blinding speed, Ari intercepts the frisbee swiftly."
    
    a "Now, it's my turn!"
    
    "Ari nods and makes hand signals to Cynthia motioning her to move for a pass."
    
    s "Like I don't know what you're doing!"
    
    "I sprint to try to intercept Ari's throw with Bella trying to block it, his feint catches both Bella and I off guard."
    
    "Ari quickly passes the frisbee at a low angle and Cynthia catches the frisbee while diving."
    
    "Ari doesn't waste time to reposition himself for another pass."
    
    "Cynthia tries to quickly pass to Ari, but fumbles with her throw."
    
    c "Whoops!"
    
    "The frisbee flies at a crescent towards the ground, but Ari sprints to catch it just in time."
    
    s "Not, bad! We've got to be in our A game with this!"
    
    "The volley starts to go back and forth with the frisbee switching sides very frequently."
    
    "Cynthia isn't very accurate with throwing the frisbee nor is she good at catching, but does make up for it with being able to communicate well with Ari using hand signals. Ari really doesn't talk much, but does communicate through hand signals."
    
    "Bella is quick to move around the field a lot and I am very precise at throwing and catching the frisbee, only to have Ari with his sneaky moves to intercept it."
    
    "We take a timeout to talk with our teammates as no one has scored yet and need a small break."
    
    s "Haahhh...Haahhh. Ari isn't making it easy at all! He's really good at intercepting our passes!"
    
    b "..Haahhh... Yeah, even I have a hard time keeping up with him. Cynthia does a good job to keep up with him."
    
    s "We gotta step it up a notch! They aren't making it easy, even though they're new to this."
    
    "We continue onto the field to continue the match. Cynthia compliments us for our good play, Ari is still silent, but with a smirk on his face."
    
    "Second half of the game, Ari has shown that he's showed Cynthia some maneuvers and has completely shut down our blocking strategy! Within 5 passes, Ari scores the first goal."
    
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
    
    show Bella embarrassed
    
    b "Luckily no one got hurt and no one was in the room where the frisbee flew through. Apparently the frisbee knocked off a small bunch of beakers in the lab."
    
    show Sam embarrassed at right
    
    s "Well good that no one got hurt."
    
    b "It was an accident so we don't have to serve detention, but we still have to pay for the broken equipment."
    
    s "Oh crap. I got it, although my parents won't be too happy with that. It's my fault anyway. How much for the beakers?"
    
    b "You broke 3 large beakers, the teacher told me you owe $100 or so."
    
    s "Urk..."
    
    show Sam neutral at right
    
    s "It's okay, i'll try not to be so accident prone next time. Did you guys at least have fun with frisbee, although we won't be doing it for a long while?"
    
    hide Bella embarrassed
    show Cynthia neutral
    
    c "Yeah, it was fun until you broke some stuff."
    
    show Ari neutral at left
    
    a "It was quite exhilirating."
    
    s "You're not only really athletic, you're really cunning with those maneuvers."
    
    s "And you say you're only good at science stuff."
    
    show Ari embarrassed at left
    
    a "Come on, let's go help clean up the mess we made now."
    
    s "Right."
    
    hide Sam neutral at right
    hide Cynthia neutral
    hide Ari embarrassed at left
    
    "And so, we spent the rest of the afternoon cleaning up the broken glass and apologized to the science teacher in that classroom. He let me off the hook with having to pay for the beakers, because he just ordered more anyway. Still awfully nice of him to let me go."
    
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
    
    "As I spend more time with Ari, he starts to speak up a little more and has become less shy with us. It's nice seeing him really open up. It's nice seeing him really shine as from before he was a quiet and shy person. Hopefully I get to know more about him.."

#End of Chapter 1A
     
     jump to Ch2

#Chapter 1B: School and Work

label Ch1B

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
label Ch1BY

    $ Bella_Ch1 = True

    s "How about we start with something simple to talk about?"
    
    show Bella neutral
    
    b "What should we talk about then?"
    
    s " How about we just talk about how school is going?"
    
    show Bella embarrassed
    
    b "Okay..."
    
    show Bella neutral
    
    s "Here i'll go first."
    
    s "Honestly, school has been very dull for the most part."
    
    s "Every class is boring, it feels really insulting and stupid to be in stupidly easy classes with all the other freshmen in our class."
    
    s "I just really hate how we're forced to take most of the same classes as freshmen."
    
    b "Really? I've been struggling through these classes? How is it stupidly easy for you?"
    
    s "I learned the stuff ahead of time already, my parents forced me to take summer school. It's just the same shit anyway."
    
    b "Is that why you don't even pay attention in class?"
    
    s "I don't need to! I'd rather not sit and be tortured by people who can't even read short lines of the textbook for an answer."
    
    b "I shouldn't talk anyway, I sleep through class."
    
    s "Do you even get enough sleep?"
    
    b "Aside from club activities in this club, student government, and the debate club, i've got a job to keep outside of school, I have to babysit my siblings, and I do all the chores in my house."
    
    s "That's right, you're the oldest in your family. You also work an afternoon shift at that cafe downtown."
    
    b "I don't get a lot of time to study or sleep. By the time I get home, I have to prepare dinner, clean up the house, and take my siblings to sleep. By the time I get time to myself, it's already 10 PM, and I use about 2-4 hours trying to get homework done."
    
    s "Geez, I didn't know it's gotten that rough for you."
    
    b "Well, the main reason I got that job was to start saving up for college, because my parents have no money for it."
    
    s "How are you gonna get to college if you can't even get through high school with you sanity?"
    
    show Bella sad
    
    b "Hmm...You're right. I hate to admit it, but you're right."
    
    s "Don't worry, we'll get you through it. Trust me."
    
    show Bella neutral
    
    b "Thanks, Sam."
    
    show Cynthia neutral at right
    
    c "You're still a freshman, you should enjoy your first year as it'll get harder as the years go by. You have to do much more later on, so just relax for your first year."
    
    show Ari talking at left
    
    a "Do not eat more than you can chew. You will spread yourself way too thinly to be able to do anything if you try to do everything."
    
    c "I know you want to really enjoy your high school years, but you also need to be able to enjoy sleep."
    
    b "I get what you guys are saying, but I really want to do this, it's just I have trouble keeping a schedule and managing my time."
    
    c "Babe, you need to be able to do that, you're going to die if you do that much."
    
    hide Ari talking at left
    show Sam neutral at left
    
    s "Are you really that committed to doing all of that?"
    
    
    
    

label TrueFork1

    show Cynthia happy
    
    c "Hey, Sam! You're hanging out with me today?"
    
    s "Yeah, I haven't spent too much time with you yet and only met you when Bella introduced me to you."
    
    c "Alright, so what do you wanna talk about today?"
    
menu:
    
    "What should I go with as an icebreaker?"
    
    "You":
        jump Ch1C
    
    "Family":
        jump Ch1S

#Chapter 1C: Queen Cynthia
label Ch1C


#Chapter 1S: An Only Child
label Ch1S

#Chapter 1N: Overdramatization
label Ch1No
    
    with dissolve
    scene bg hallway

    "I step outside the club room for a while..."

    "Bella soon follows suit after me."

#Chapter 2: The Butterfly Effect
label Ch2

    # This ends the game.

    return
