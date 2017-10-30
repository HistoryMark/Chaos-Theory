#Chaos Theory: A Visual Novel by Mark Perez

#Storyboarding and Development by Mark Perez

#Art by

#Music by

#Opening Cover Summary: Follow the story of these four close friends as they go through the treacherous years of high school. As they struggle with conflicts in the life of high schoolers between family, work, friends, and life itself. Will the story be just another drop in the ocean, or will it be something unexpected? Based on experiences from American high school, dive back to high school as what we expected it to be or just relive on how boring it actually was.

# Main Characters

define s = Character("Sam")

define a = Character("Ari")

define c = Character("Cynthia")

define b = Character("Bella")

# Unknown Characters

define sfs = Character("A Female Student")

define sms = Character("A Male Student")

# The game starts here.

label start:

#Prologue: An Ordinary Day

    #image bg schoolyard = "sidewalk.png"
    scene bg sidewalk
    
    "It was an ordinary day, in this ordinarily boring life as a high school student..."
    
    #image Bella neutral = "Bella_neutral.png"
    show Bella neutral
    
    sfs "Come on, Sam! We'll be late for school!"
    
    image Sam neutral = "Sam_neutral.png"
    show Sam neutral at right
    
    s "Well, we're already going to be late with that train coming by, so why bother rushing?"
    
    sfs "What train?"
    
    "The lights flash and the gates lower on the railroad crossing as the horn of the train can be heard."
    
    b "Oh, really? Just our luck!"
    
    s "You seem really out of it today, Bella. Are you getting enough sleep?"
    
    b "Er..Okay, so I only slept 4 hours last night."
                                                     
    s "Why did you stay up so late for?"
    
    #image Bella embarrassed = "Bella_embarrassed.png"
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
    
    #image Bella talking = "Bella_talking.png"
    show Bella talking
    
    b "Don't say it like that! Yeah, some people don't care about school, but I think you guys just don't understand."
    
    #image Sam sad = "Sam_sad.png"
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
    
    #image Bella happy = "Bella_happy.png"
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
    
    #image bg classroom = "clasroom.png"
    scene bg classroom
    
    show Sam neutral
    
    s "Phew, finally the teacher stopped droning on and on. I know she's trying to clear with eveything, but there's always the idiots who will ask the same questions."
    
    "With that, the another school day ended with seemingly endless classes."
    
    "As I was about to leave the classroom to go meet with Bella, I catch the glare of a student with a pained look on his face right at the doorway."
    
    #image Ari sad = "Ari_sad.png"
    show Ari sad at right
    
    sms "..."
    
    s "Umm...Are you okay?."
    
    sms "...Uhh...No, i'm fine. Sorry to make you worry. Please excuse me..."
    
    hide Ari sad 
    
    "He leaves the room in a quiet fashion."
    
    s "...Okay, then..."
    
    "I know most times people just keep to themselves, but somehow I found myself approaching someone to try to help..."

    "Then again, I remember that was the new transfer student that just got here a couple days ago. Maybe he's having a hard time getting used to things, but I don't think I should worry..."

    s "Whatever, I shouldn't let it bother me, what should bother me is that Bella is dragging me around for clubs."

    hide Sam neutral
    with dissolve
    with fade
    
    #image bg hallway = "hallway.png"
    scene bg hallway
    show Sam neutral
    show Bella happy at left
    
    "I meet up with Bella in the hallway to see her waiting for me outside my classroom."
    
    s "You're really serious with forcing me to join a club aren't you?"
    
    b "Come on, you've got the time and energy! Let's get you doing something!"
    
    "Bella takes my hand to go look at the various clubs in school."   
       
    with dissolve
    with fade

    b "How about the science club? You get to do cool experiments and show off your research!"
                                                                                              
    s "I would have to do research for a project of my choice about 'principles that broadens the horizons', huh?"
       
    "I try to read the club poster with enthusiasm, but it only came out sarcastically."
                                                                                        
    b "Yeah, you get to explore scientific concepts ranging from ecology, like studying the environment, to inorganic chemistry, like learning how firecrackers work!"
                                                                                                                    
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
    
    b "There's gotta be a club you're somewhat interested in, Sam! Please at least try one out before saying no!"
    
    s "If joining a club means joining people I don't know with something stupid as some of those activities, count me out. I'd rather be messing around by myself."
    
    show Bella happy at left
    
    b "Come on, Sam! For me? Please?"
    
    s "..."
    
    b "Would you join if it was just me and a small group of friends?"
    
    s "...Okay, you got me. Maybe because I'd rather be with people I know."
    
    "I didn't want to admit it, but if I wanted to join a club, I would want it to be with Bella, someone I actually know."
    
    b "Hmm..I've got an idea, wait here. I'm gonna ask a teacher something about the clubs."
    
    "Bella rushes over to the teachers' office with a smile."
    
    with dissolve
    with fade

    s "So, what happened?"
    
    b "I was asking if we could start a club with just us, but apparently we need at least 10 people for a club to be recognized by the school."
    
    #image Sam talking = "Sam_talking.png"
    show Sam talking
    
    s "Huh, that's a shame."
    
    "I say with a hint of sarcasm, as it's the only attitude I have over this."
    
    b "However, my teacher said she can supervise a small study group and reserve a spare room for our group if we get at least 4 people for our informal group."
    
    b "You would be fine doing something with me and 2 other friends? I know you obviously don't want to do something with a bunch of people you don't know or will have trouble getting to know."
    
    show Sam neutral
    
    s "...Fine, i'll play along with your idea..."
    
    s "You have anyone in mind to join us?"
    
    b "I have one other person that my teacher recommended, can you do me a favor and find us a fourth?"
    
    s "Er...Fine, i'll see what I can do. "
    
    b "Thanks, buddy!"
    
    hide Bella happy at left
    
    "Bella happily skips away."
    
    s "I guess I just have to deal with 2 strangers rather than have to work with 8 other people I don't know."
    
    "With that settled, I head home pondering about recruiting another student for our group."
    
    hide Sam neutral
    
    scene bg sidewalk
    
    show Sam neutral
    
    "Here I was on my way home just casually walking home from school, then I saw another student from my class walking home from school."
    
    s "Hmm..he looks familiar..."
    
    show Ari sad at right
    
    sms "...."
    
    "He's carrying a bunch of books while blankly staring at the ground..."
    
    s "Why's he carrying all those books home? There can't be that much work in class already! Must be in the honors classes..."
    
    "As he was standing there stone-faced, a bunch of kids run past him and knock his books out of his arms, his glasses flying, and landing on the ground, but he didn't even react."
    
    "The kids run off not even knowing of their small accident, but he doesn't even raise a single complaint. Just another pained look."
    
    "Gathering courage, I walk over to him and start gathering his things for him."
    
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
    
    s "Here, i'll carry some of these books for you and just give me a smile, okay? I don't like seeing sad people."
    
    "I fall over trying to lift the books, misjudging their weight."
    
    s "Hehehe...Sorry, these books are heavier than I expected! I bet you've got quite some strength to be able to carry these by yourself, or that i'm just pathetically weak. Probably the latter."
    
    image Ari neutral = "Ari_neutral.png"
    show Ari neutral at right
    
    "His sad stare livens up to a half-smile..."
    
    sms "T-thank you...Here, I will help you in assisting me."
    
    "He takes half of the books and carries them entrusting me with the other half."
    
    s "Anyway, I saw you earlier, you're from the same class from me, Ari, wasn't it?"
    
    a "Yeah...I'm sorry, i'm not good with names and I didn't catch yours."
    
    s "Well, my name's Sam. I'm 15 and a freshman at our school, you're a transfer student right?"
    
    "He nods in confirmation."
    
    s "You're also a junior if I remember right, you're stuck in that class with me because you need that to graduate right?"
    
    a " Indeed."
    
    s "Why are you carrying all these books anyway? It's only the beginning of the first half of the school year! These books are really frickin' heavy! Also, you're 15 and a junior already?"
    
    a "Yes, I started school early. Also, those books are my college textbooks for my dual-credit classes, I was taking initiative to read ahead for class."

    s "You're quite an honors student, huh? Sorry, i'm not too impressive as a student myself."

    s "Here, i'll carry these for you anyway. How far do you live from here?"
    
    a "Just three blocks from here. Thank you again for helping me. I apologize that my words do not express all of my gratitude. Here, i'll offer you some monetary reward for your deeds."
    
    s "No, it's alright. I wanted to help a fellow today. Seeing you cheer up a bit is enough. It feels good to help. Hehehe."
    
    "I walk with Ari to his house and find that he only lives a couple blocks away from my house."
    
    s "Do you seriously carry around these books and a backpack to and from school everyday?"
    
    a "It's not a big problem for me."
    
    #image Sam happy = "Sam_happy.png"
    show Sam happy
    
    s "Jeez, I guess you're really getting some serious exercise everyday. I still have trouble lifting half of these huge books!"
    
    #image Ari happy = "Ari_happy.png"
    show Ari happy at right
    
    "I let out a short chuckle, Ari's starts to chuckle too."

    show Ari neutral at right
    show Sam neutral

    "We casually get to know each other on the way home talking about school, the weather, and other small talk."

    s "So, how are you liking the city? It's really crowded, but it has its charms I would say."
    
    a "I would agree with you with the fact that it is charming, but it feels lonesome sometimes."

    s "What would make you say that?"

    a "I reside in the city with my aunt as my only companion and guardian, but she's occupied with work frequently. My parents are abroad."

    s "Oh...I live with my family here, but I never see my parents much because they're working, so I guess we kinda have that in common."

    s "You said you were in dual-enrollment classes, you really take school very seriously, huh? I admire that, but I don't see myself doing that."

    a "Why not?"

    s "You plan to be some professional like a lawyer or doctor?"

    a "I aspire to be a profesional surgeon as my family hopes me to be."

    s "It's hard for me to find motivation to even get up for school. I'll probably just end up working at a bar, or shop, but I don't see that much as a problem. I just don't see myself having much potential."

    a " There's probably something you are proficient and passionate about, you just have to find it and work hard. Everyone has limitless potential and anything can change."

    s "What, you're passionate about working with syringes and scalpels?"

    a "No, I want to be able to help people. It's not about the skills or the work that matters, rather it is the drive to achieve a goal and fulfill your life with a purpose."

    "I could only stand mute, without a response."

    a "Sorry, I know it sounds rather cliche, but I think it is the truth. I know it would be dreadful working over 50 years with an occupation you hate, and I would like to live through those 50 years of work on my terms, doing what I love doing."

    s "No, man it's fine. In fact, it's cool you see things that way."

    a "You humble me with your praise..."

    s "Man, I don't even know what to say, or even do with my life. You have a clearer idea of your life."

    a "You're a good guy, Sam. You will have a bright future ahead of you. You were brave enough to help me, who was just a stranger to you not long, you could do even more."

    s "Heh, thanks, man. I appreciate the encouragement at least."

    a "Oh, here we are. This is my house. Thanks for helping me carry my books...You helped me in more ways than one."

    s "No problem, I didn't have anything better to do and I don't think I did that much. Hehehe..."

    "I was preoccupied with helping Ari, I almost forgot about finding someone for Bella's group."

    s "Hey, Ari, are you in any clubs or do you know anyone who's free for one? I need another person for my friends' group."

    a "No, I do not know anyone in school, but you. What is it that your organization plans to accomplish?"

    s "Umm...I don't know, my friend just started a group with me and one other person. I'm guessing we just hang out with the four of us then figure what we want to do."

    #image Ari embarrassed = "Ari_embarrassed.png"
    show Ari embarrassed at right

    a "Hmmm...Okay, I might just drop in. It would be nice having something to do in my spare time at school with someone familiar. If that is okay with you..."

    show Sam happy

    s "Yeah, friend! I would be happy if you came!"

    show Ari happy at right

    a "Friend?"

    s "I know we just met, but yeah, friend! You seem like a cool person, and it would help you to know someone in school, so yeah friend! How about it?"

    "He stares at me with sheer joy."

    a "Yeah, friend. I will converse with you later."

    hide Ari happy at right

    "Ari waves as we exchange goodbyes for the day. I head home with newfound happiness."
    
    s " He talks quite oddly and overly formal, but he's a cool guy. It ought to be interesting with him around."

    show Sam neutral at left

    "I head home and see Bella and an unfamiliar face waiting for me at the gate."

    #image Cynthia neutral = "Cynthia_neutral.png"
    show Cynthia neutral at right
    show Bella neutral

    b "Hey, Sam! Did you find another person to join our group?"

    s "Yeah, his name's Ari. He's a junior in one of my classes and he lives a couple blocks from here. Anyway, who's your partner there?"

    c "Hello, my name's Cynthia and i'm a junior just like your gentleman friend. How are you?~"

    "She introduces herself with a sultry voice."

    show Sam embarrassed at left

    s "Uhh...G-good.."

    "I stammer as i'm frozen by her voice."

    c "I had a falling out with my group, so my teacher pointed me to Bella who was starting a new group with 2 others. I hope we get along together!~"

    b "Yeah! Me too, i'd like to meet Ari too! He lives nearby doesn't he?"

    "I nod."

    b "We could all walk to school together tomorrow since we all live fairly close! That way, we can get to know each other better! How does that sound?"

    show Sam neutral at left

    s "Sounds like a great idea, but we still need to find out what to do for activities for our group."

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
    
    " I never thought that I would say that I'm looking forward to school since kindergarten, but here I am. I wonder how today will go?"
    
    " As usual morning routine, I get ready for school and walk to school, meeting up with Bella along the way."
    
    show Sam neutral
    
    s "Mornin', Bella! How's it goin?"
    
    show Bella happy at left
    
    b "Fantastic! I actually got some sleep last night!"
    
    s "You got a good night's rest for once?"
    
    b "Hehe...I just couldn't wait for today to happen!"

    # This ends the game.

    return
