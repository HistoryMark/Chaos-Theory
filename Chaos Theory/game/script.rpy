#Chaos Theory: A Visual Novel by Mark Perez

#Storyboarding and Development by Mark Perez

#Art by ...

#Music by Mark Perez

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

image Sam = Placeholder("boy")
    
    #image Sam neutral = "images/Sam_neutral.png"
    
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
    
    
        
image Ari = Placeholder("boy")

    #image Ari neutral = "images/Ari_neutral.png"
    
    #image Ari happy = "images/Ari_happy.png"   
    
    #image Ari sad = "images/Ari_sad.png"
    
    #image Ari embarrassed = "images/Ari_embarrassed.png"
    
    #image Ari talking = "images/Ari_talking.png"
    
    #image Ari crying = "images/Ari_crying.png"


    
    #image Cynthia neutral = "images/Cynthia_neutral.png"
    
    #image Cynthia happy = "images/Cynthia_happy.png"
    
    #image Cynthia sad = "images/Cynthia_sad.png"

    #image Cynthia embarrassed = "images/Cynthia_embarrassed.png"
    
    #image Cynthia talking = "images/Cynthia_talking.png"
    
    #image Cynthia crying = "images/Cynthia_crying.png"
    
#Background Scenes (14)

    #image bg schoolyard = "images/schoolyard.jpg"

    #image bg sidewalk = "images/sidewalk.jpg"
    
    #image bg classroom = "images/clasroom.jpg"
    
    #image bg hallway = "images/hallway.jpg"
    
    #image bg clubroom = "images/clubroom.jpg"
    
    #image bg schoolfield = "images/schoolfield.jpg"
    
    #image bg closet = "images/closet.jpg"
    
    #image bg lounge = "images/lounge.jpg"
    
    #image bg festival = "images/festival.jpg"
    
    #image bg mall = "images/mall.jpg"
    
    #image bg conferencecenter = "images/conferencecenter.jpg"
    
    #image bg park = "images/park.jpg"
    
    #image bg tower = "images/tower.jpg"
    
    #image bg barrenfield = "images/barrenfield.jpg"
    
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
#Playful Theme: TheFatRat - Unity

define audio.bitterness = "music/bitterness.mp3"
#Bitterness Theme: Cole Sipe ft.Sophia Odiorne - Innocent

define audio.emotion = "music/Scarred_HeartofLove.mp3"
#Scarred Heart (of Love) by Mark Perez
#Emotion Theme: Lindsey Stirling ft.Lzzy Hale - Shatter Me

define audio.sadness = "music/Scarred_HeartofStrength.mp3"
#Scarred Heart (of Strength) by Mark Perez

define audio.heartache = "music/heartache.mp3"
#Cynthia's Endgame Theme

define audio.insanity = "music/WhoAreYou.mp3"
#Who Are You by Mark Perez
    
label start:

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
    
    b "It's true though, we only experience these 4 years once!"
    
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
    #stop music fadeout 1.0
    
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

    a "I reside in the city with my aunt, but she's occupied with work frequently. I'm studying here and the rest of my family is still back home in Japan."

    s "Oh...I live with my family here, but I never see my parents much because they're working, so I guess we kinda have that in common. Also, you speak English way too well to be Japanese."

    a "I studied that since I was 4, so I can go to school here."
    
    s "Oh, cool!"

    s "You said you were in dual-enrollment classes, you really take school very seriously, huh? I admire that, but I don't see myself doing that."

    a "Why not?"

    s "You plan to be a lawyer, engineer, or doctor?"

    a "I aspire to be a surgeon as my family hopes me to be."

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
label Ch1AY:

    $ persistent.Ch1ACG_unlocked = True

    show Sam neutral
    
    s "Come on, Ari! You've gotta be a genius at other things too other than there-mo-dee-nameks!"
    
    show Ari neutral at right
    
    a "Thermodynamics. Anyway, I suppose it would not hurt to try other things. What do you propose we should try?"
    
    s "Oh, shoot. I didn't think I would get this far."
    
    s "Have you ever played ultimate frisbee?"
    
    a "No, but I do at least have heard of it."
    
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
    
    "Cynthia isn't very accurate with throwing the frisbee nor is she good at catching, but does make up for it with being able to communicate well with Ari. Ari really doesn't talk much, but does communicate through hand signals."
    
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
    
    s "You're not only really athletic, you're really sneaky."
    
    s "And you say you're only good at science stuff."
    
    show Ari embarrassed at left
    
    a "Come on, let's go help clean up the mess we made now."
    
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
    
    "As I spend more time with Ari, he starts to speak up a little more and has become less shy with us. It's great seeing him really open up. It's even nicer to see him really shine as from before, he was a quiet and shy person. Hopefully I get to know more about him.."
    
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

    $ persistent.Ch1BCG_unlocked = True

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
    
    b "Aside from club activities in this club, student council, and the literature club, i've got a job to keep outside of school, I have to babysit my siblings, and I do all the chores in my house."
    
    s "That's right, you're the oldest in your family. You also work an afternoon shift at that cafe downtown."
    
    b "I don't get a lot of time to study or sleep. By the time I get home, I have to prepare dinner, clean up the house, and take my siblings to sleep. By the time I get time to myself, it's already 10 PM, and I use about 2-4 hours trying to get homework done."
    
    s "Geez, I didn't know it's gotten that rough for you."
    
    b "Well, the main reason I got that job was to start saving up for college, because my parents have no money for it."
    
    s "How are you gonna get to college if you can't even get through high school with your sanity?"
    
    show Bella sad
    
    b "Don't worry about it, i'll be able to handle all of this."
    
    s "If you say so, we're just worried for you."
    
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
    
    b "Today, was fun! We got to work together as a team."
    
    s "You definitely needed a team to help with that much work! Don't tell me you planned on doing that all by yourself?"
    
    b "Sorry, I didn't want to bother anyone with it."
    
    s "Dude, i'm your best friend! If you need a shoulder, i've got one for you to lean on. Don't think it's a bother, because your bothers are mine as well, okay? You're seriously going to hurt yourself from doing too much work."
    
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
    
    "Cynthia stares at me for a moment, and our eyes meet. I try to get my eyes to wander somewhere else to avoid the awkwardness."
    
    c "No, keep your eyes on me. It's a little test."
    
    s "Uh...Okay."
    
    "I try to concentrate on just staring at Cynthia's eyes as she said, but found it extremely awkward."
    
    s "Urk...This is extremely awkward."
    
    c "Well, they say you find someone more attractive or likeable when you stare into their eyes quite a while."
    
    s "You are playing mind games with me in such a way I wonder if they're games at all."
    
    c "Hehehe....."
    
    "She chuckles a little deviously."
    
    s "Anyway, about you, I heard you had a falling out with your last club. What happened with your club?"
    
    c "Oh, you are curious about that?"
    
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
    
    $ persistent.Ch1CCG_unlocked = True
    
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
    
    hide Cynthia sad
    with dissolve
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
    
    c " I always get the largest portion as president running things and advertising our works. Ferdinand who's in charge of materials and inventory always go the second largest portion of the funding so he can buy the club whatever we needed to make our clothes."
    
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
    
    c "I kept wondering what I did wrong as president, but I see that everybody gets a little greedy around money."
    
    c "I really wasn't in it for the money. I just had to find ways to get it to be able to make something. It should be driven by the want to make something, not just to make money."
    
    show Cynthia neutral
    
    c "Anyways, that's my story of the fashion club in a nutshell."
    
    c "I know you guys are different, right? You guys have this club to just hang out, and so i'll do the same."
    
    s "Kinda hard to believe the same overdramatic thing that happens to bands happened to your little club."
    
    c "I didn't think it would happen as well, but as soon as we just got paid in a daily basis, everyone just expected to get paid. So when we didn't get paid as much, you see what happened with that."
    
    show Bella talking at left
    
    b "That really sucks. You started the club right? That's how you were president?"
    
    show Bella neutral at left
    
    c "Mhm...I had to look hard for 3 other people to join me, but I found 4 other talented people up to the task."
    
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
    
    "Today was quite something. I got to know about Cynthia and her little club. She's also really skilled in makeup and stuff like that, although I know nothing about fashion and the most fashionabl thing I wear is my short sleeves."
    
    "I definitely should spend time with Ari and Bella too, as they also are just as interesting and odd as Cynthia."
    
    "Who knows what tomorrow might bring? I can only question..."
    
    #stop music fadeout 1.0
    with dissolve
    with fade

#Chapter 1S: An Only Child
label Ch1S:
    
    $ persistent.Ch1SCG_unlocked = true
    
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
    hide Bella sad at left
    hide Sam sad
    hide Cynthia sad at right
    
    scene bg cgdonnamoore
    
    s "You definitely know my mom, Donna Moore, even though you've never met her right?"
    
    c "We hear about her in the news."
    
    a "She's the CEO of the multi-billionaire real estate company. She innovated urban planning and housing systems in communities changing the landscape of realty. She made it on a plethora magazines for that."
    
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
    
    "And so, Bella and I head home casually talking about school and other small talk as if nothing had really happened. It did cheer me up a little to go back into the crazy swing of things between us from my little dramatic moment."
    
    "I really surprised myself with how I really chose to open myself up to others and it made me feel good about venting. Perhaps I should really do that more often and maybe i'll be able to actually patch things up with Mom."
    
    "I don't know how things might change from here on out, I just hope it's for the better."

#End of Chapter 1S
    jump Ch2

#Chapter 1N: Overdramatization
label Ch1No:
    
    "I step outside the club room for a while..."
        
    with dissolve
    with fade
    
    #stop music fadeout 1.0
    scene bg hallway

    "Bella soon follows suit after me."
    
    show Bella neutral
    
    b "Are you alright, Sam?"
    
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
    
    "Bella heads back into the clubroom, leaving me by myself on the hallway floor."
    
    with dissolve
    
    "I don't know why I chose to step out in the first place, yet here I am. I take a second to look back how I even got here in the first place."
    
    "I'm in this club which is supposed to be a peer club where we just hang out together, yet it feels wrong to me."
    
    "For one, it happened so fast, I was pushed by Bella to join and start a club overnight."
    
    "Two, I have to talk to two other people I hardly know, it was really awkward to even open up a conversation at first, even with Bella."
    
    "And three, I guess i'm just not feeling myself today. It feels weird to feel as if i'm not even in control of myself, but it's happening."
    
    "I might just be a little crazy right now, but I don't want anyone to bother me right now. Everything seems to move way too fast and a little dramatic at times, it just doesn't feel as if things really aren't happening naturally for me."
    
    "Suddenly I hear loud voices in the clubroom. It sounds as if there is an argument going on. I get up and peer through the door into clubroom to take a look."
    
    with dissolve
    
    scene bg clubroom
    #play music playful loop
    
    show Bella talking at left
    show Cynthia talking at right
    
    b "Take it back!"
    
    c "You're just a poser."
    
    b "Urgh..."
    
    c "I agreed to join this club thinking that its club members might actually be cool."
    
    c "You just look and sound fake. The way you try to be enthusiastic about school, looking to try too hard, and you trying to be student body president and kissing up to the teachers and other people? I don't buy your act."
    
    b "What do you mean? I actually really try to do everything here!"
    
    c "Okay, sure. I see you around the school and other clubs, you aren't actually good at anything. You're not athletic, you're not good in academics, you're not good in debating, organizing, and not good at being president of this made-up club you have here."
    
    c "I've actually been a club president and you have no ideas about actually organizing things. I can tell you forced your friend Sam to join you just so you can start this club and it shows he doesn't even want to be here by running out."
    
    b "Umm..."
    
    c "I don't think you know, but this isn't working out."
    
    b "What is?"
    
    c "The club you made up. Just how badly did you bribe your teacher to make this club, then you aren't even able to organize the club and even yourself."
    
    c "I'd prefer not being laughed at, but this club right now is a joke."
    
    b "How about you just fucking shut up!"
    
    "Bella's voice into a deep shout in contrast to her regular happy high-pitched voice."
    
    b "You're just an egotistical bitch who thinks her breast implants and overpriced clothes makes her better than me."
    
    b "You know what? Fine, i'm shitty at doing a bunch of stuff, but at least my trying. I know this club isn't much, but i'm just trying to do something."
    
    c "So what? You can be student body president of your class over some stupid popularity contest?"
    
    b "It isn't a popularity contest! It's a huge position! I'm more qualified than half of those other idiots in my class anyway as I try harder than any of them could imagine as they just sit in class mindlessly at their phones!"
    
    c "You're trying to prove you're better than them? That's rich. You're not even real to begin with."
    
    b "For some whore who thinks you're better than me by messing with my campaign posters with your nasty nail polish, you shouldn't be judging who's real."
    
    c "At least my boobs are actually real you washboard!"
    
    show Ari talking
    
    a "Please, both of you should stop this meaningless argu-"
    
    b "Back off! This is between me and her."
    
    hide Ari talking
    
    "Bella pushes Ari aside and charges at Cynthia."
    
    c "Bring it on, you're not even as strong as a bunch of twigs."
    
    "A small scuffle starts to break out between the two ladies as they begin to pull each others' hair."
    
    "Ari looks to try to intervene, but only to be pushed away by the two."
    
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
    
    c "Sigh...I called her out."
    
    s "What?"
    
    c "I just wasn't happy that you weren't enjoying yourself in the club and Bella seems to have a hard time organizing things in the club and her other tasks."
    
    b "I just flipped out for being criticized over a that."
    
    s "Don't act like it was something small, I know that wouldn't be the case if I saw you guys tearing each others' hairs out."
    
    b "..."
    
    c "...I'm sorry. I take back what I said. I shouldn't have been so thoughtless of being too highly criticizing you and speaking badly of you."
    
    b "I'm sorry too for taking what you said too personally and should not reacted as I did."
    
    "The two apologize as if it was too rehearsed."
    
    s "Okay, that's enough."
    
    "They were quick enough to catch on to apologize, but I know this doesn't solve the problem."
    
    s "I heard a fair amount of it already. Aside from the insults and what I can tell, Cynthia called out Bella for not being a good club president for her poor organization and Bella is mad at Cynthia for being too quick to judge."
    
    c "..."
    
    b "..."
    
    "The two fall silent."
    
    s "Look Cynthia, I know she's not exactly too experienced at being a club president, but know she's learning and is truly trying her best. I know too well organization is not something she's very good at."
    
    s "We'll work on it together, okay? I don't know who hurt you with you accusing her acting fake, but Bella really is that hardworking and friendly. I can vouch for her there. So please, just give her some credit."
    
    s "Bella, I know you aren't the best person in taking criticism, but Cynthia has some fair points. You should also be more considerate of accepting her criticism."
    
    s "Neither of you are fully right, but also neither of you are completely wrong. You guys shouldn't fight over something simple as this. We're supposed to be friends right? We're gonna be stuck with each other for a while."
    
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
    
    s "I know it doesn't make sense sometimes, but call it tough love."
    
    a "What is such a thing?"
    
    s "Good friends are 'mean' to their friends to show they care for them. I hope, if it gets close to a situation like this, they'll be able to still be friends and grow as friends."
    
    a "Hm. There is wisdom in your words."
    
    s "Oh no, it's just something I kinda picked up when I saw people who are friends."
    
    a "I see...Do you like to observe others as a pastime?"
    
    s "You mean people-watching? Yea, all the time."
    
    a "Interesting...I presum that's how you are able to sense people's feeling with such proficiency."
    
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
    
    $ Ch1D_unlocked = True
    $ renpy.block_rollback()
    
    show Ari talking
    
    a "Please, stop hurting each other, this is too far!"
    
    show Ari sad
    
    "Ari stands between them only to catch a heavy punch from Cynthia, knocking the wind out of him."
    
    a "Urk..."
    
    hide Ari sad
    
    "Ari collapses to the ground..."
    
    "Cynthia and Bella stop their fight to check on Ari with me, who's on the ground wheezing."
    
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
    
    show Ari neutral
    
    a "Urk...At least they stopped for now. I am afraid that only temporarily settles the unhappy relationship brewing between them."
    
    s "...I should have stopped them. Then you wouldn't have gotten hurt."
    
    a "Think nothing of it. You should not place the blame on yourself."
    
    show Sam sad at left
    
    s "You'll be alright?"
    
    a "Do not worry about me. I will clean things up here. I sense you are not in a pleasant mood after this. I suggest you spend some time alone and go home."
    
    s "...Fine, i'll just go do that. Sorry."
    
    hide Sam sad at left
    hide Ari neutral
    
    with dissolve
    with fade
    
    scene bg sidewalk
    
    "I head home after the incident and spend time mulling it over."
    
    "We were lucky enough to be sent off with a warning by the teacher as nobody was harmed. Ari got knocked, but he turned out to be completely fine after a short rest. Bella and Cynthia are surely unhappy with each other, but hopefully things will be fine with them."

    "I felt like I wasn't really me today. I should have stepped in to stop them, but I was just to scared to do that."
    
    "I shouldn't have been because that was my friends that was just fighting. What kind of friend am I then?"
    
    "I guess i'll try to settle things with everyone if I can next time..."
    
    with dissolve
    with fade
    
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
    
    "I can sense the anger between them behind those noonchalant smiles. Hopefully it doesn't get any worse as it is for them. It also shows in Ari's frown that it truly makes him unhappy as well to see them be like this."
    
    "..."

#End of Chapter 1: Diverged Ending
    jump Ch2

#Chapter 2: The Butterfly Effect
label Ch2:


    # This ends the game.

    return
