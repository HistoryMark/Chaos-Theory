#Alternate/Diverged Story Arc Episode 2: Chapters 2BE & 2D    
#Chapter 2N: Hidden Trust
label Ch2No:
    
    s "Nevermind, actually. I just need some time alone."
    
    "The next few minutes of the conversation results in it dying out. I just go to another seat and stare at the window to pass time."
    
    with dissolve
    with fade
    
    scene bg clubroom
    #stop music fadeout 1.0
    
    "I stare aimlessly at the windows."
    
    "Wondering what to do, my mind wandering aimlessly, but nothingness fills my head."
    
    show Sam sad
    show Bella talking at right
    
    b "Sam, are you okay?"
    
    "I spaced out, but Bella snapping at me brings back my conciousness."
    
    b "Sam? Hello, anyone there?"
    
    show Sam embarrassed
    
    s "Oh. Yea, I'm fine! What is it?"
    
    b "Do you feel awkward and uncomfortable talking with us?"
    
    b "Just tell me and we can work things out."
    
    b "You don't have to force yourself to have to talk to us, if you want."
    
    s "Oh, no! It's not like that! It's just-"
    
    b "Just what?"
    
    show Sam sad
    
    s "I don't know. I really don't know what's going on."
    
    s "I just can't think of anything, or what to say, or what to do."
    
    s "I feel like I should be doing or saying something, but I've got nothing."
    
    show Bella sad at right
    
    b "Hmmm."
    
    show Bella neutral at right
    
    b "Well maybe just doing some work, or something might spark your mind. I lose my train of thought sometimes too."
    
    b "But, it's best to do something, if not anything, rather than nothing at all."
    
    b "Come on, I need some help sorting out a couple things and I could use your help."
    
    b "Can you lend me a hand?"
    
    show Sam neutral
    
    s "Sure, I guess."
    
    "Bella takes out a couple of binders, books, and magazines from a bag."
    
    b "I have a bunch of books the school and other clubs are donating to the elementary school down the road and I need help sorting them out by genre."
    
    s "Okay, how many books do you have?"
    
    "Bella brings in a bunch of bags, each filled with a variety of books."
    
    b "There's about 20 or so books in each bag and I have 8 bags filled with books."
    
    "She takes out a binder."
    
    b "I also need you to record the book in this binder based on the genre of the book."
    
    b "I've got other sudent officers also sorting books, but this is the bunch of books I was given."
    
    b "Can you sort them for me?"
    
    s "Yeah."
    
    "I start sorting through the books and recording them."
    
    b "Make sure they're also in decent quality okay?"
    
    b "Some people just dumped the books in the bags and some books may have been bent or folded because of it."
    
    with dissolve
    with fade
    
    show Sam neutral
    show Bella neutral at right
    
    "..."
    
    "I quickly sort through the books with Bella."
    
    "Only 30 minutes had passed while we sorted them out. I also helped Bella pack the books into boxes to prepare to be sent."
    
    b "Great!"
    
    b "That all of them for now."
    
    b "Thanks for the help, Sam!"
    
    s "Yeah, sure."
    
    b "You're really a nice guy for helping me out organize donations."
    
    s "I was just doing something to pass the time."
    
    b "Well it hasn't been long. With your help, we got it done fairly quick."
    
    s "..."
    
    b "I gotta get these packed into the student government clubroom, so we can get them loaded and taken to the school for later."
    
    "Bella rushes over to the boxes, then stops herself as if she had quickly remembered something."
    
    b "Oh. I almost forgot."
    
    b "I'll be out for an hour or so, so you guys can just chill here for the rest of the club meeting if you want."
    
    b "Sam, can you do me another favor?"
    
    "I pause to think what it might be."
    
    s "What do you want to be done?"
    
    b "I'll be going out, but I'll be back here in an hour, but I'm going to leave my stuff here just for the time being."
    
    b "Can you watch over my stuff for a bit?"
    
    s "Yeah, sure."
    
    b "Okay, thanks!"
    
    b "One more thing."
    
    s "Yeah?"
    
    b "I have something important in my bag, but I can't show it to anyone."
    
    b "Can you promise me to not look inside my bag?"
    
    show Sam embarrassed
    
    s "What exactly is in that bag anyway? It's just a bunch of books and stuff, right?"
    
    b "I promise it isn't anything bad or dangerous, but I can't show it to anyone."
    
    b "Not even you, but I trust you."
    
    b "I really like my privacy, okay? So just please understand."
    
    b "Just promise me to look after my stuff, but not look what's in my bag or show it to anyone."
    
    show Sam neutral
    
if Ch1BE_active:
    jump Pass2BE
    
else:
    
    "..."

label redo_Ch2BE:

menu:
    
    "Promise to her?"
    
    "Yes.":
        jump Ch2BE
        
    "No.":
        "Are you sure?"
menu:
    
    "Yes.":
        jump Ch1D
        
    "No.":
        jump redo_Ch2BE
        
           
#Chapter 2BE: Not a Surprise
label Ch2BE:
    
label Pass2BE:
    
    $ Ch1BE_active = True
    
    with dissolve
    with fade
    
    scene bg clubroom
    #play music playful loop
    
    show Sam neutral
    
    "An hour and a half passes until Bella finally returns to the room. I had just listened to music to make the time pass."
    
    show Bella neutral at right
    
    b "Hey, Sam! I'm back, so what did I miss?"
    
    show Sam talking
    
    s "Not much, I just did pretty much nothing while you were gone."
    
    show Sam neutral
    
    b "Okay."
    
    show Bella talking at right
    
    "Bella stares at me intently, but with discontent."
    
    b "Sam?"
    
    show Sam surprised
    
    s "What?"
    
    b "You didn't look after my stuff and didn't look through it right?"
    
    s "Yeah."
    
    show Bella angry at right
    
    b "You DIDN'T look through my stuff right?"
    
    show Sam angry
    
    s "What? Of course I didn't! You don't trust me?"
    
    b "Well, how can I believe you?"
    
    s "I'm telling you, I didn't look!"
    
    show Cynthia embarrassed at left
    
    c "No, he didn't look through it. Take my word for it."
    
    show Bella embarrassed at right
    show Sam embarrassed
    
    b "Huh?"
    
    "Oh, good. Cynthia's got my back on this."
    
    c "Seriously? You entrusted him with it, he does his job and now you suspect he's lying?"
    
    c "Also, I'm certain you don't have anything worth stealing if you brought it to school with you."
    
    b "Uhh, I just get sensitive with my stuff and privacy, okay?"
    
    b "Don't judge! It has something really important in there."
    
    c "Okay, but show a little more faith."
    
    show Cynthia neutral at left
    show Sam talking
    show Bella sad at right
    
    b "Okay, okay. You're right."
    
    s "I didn't, I just watched over it. See, I didn't move it anywhere, it's right where you left it."
    
    "Surely enough, Bella checks twice to see her bag, untouched. She then takes a sigh of relief."
    
    show Bella neutral
    
    b "Okay."
    
    show Sam surprised
    
    s "You aren't one to be extremely possessive, Bella. Also, what's so special about what's in the bag?"
    
    show Bella talking at right
    
    b "No, I'm not possessive, but I just have my journal in there."
    
    show Sam neutral
    
    s "Journal? Is that what you call a diary?"
    
    show Bella hurt at right
    
    b "It's not a diary! It's a journal!"
    
    show Sam happy
    
    s "It's the same thing!"
    
    show Cynthia talking at left
    
    c "Well, whatever you call it, you brought such a thing to school?"
    
    show Bella embarrassed at right
    
    b "I bring it everywhere! I like to write whenever something special happens, and you never know what could happen!"
    
    show Bella closed at right
    
    b "I like to write about things right in the moment."
    
    show Bella embarrassed at right
    
    b "That, and I forget about everything so easily."
    
    show Cynthia closed at left
    
    c "Ah, okay. It's similar to how artists bring a sketchbook everywhere."
    
    show Cynthia surprised at left
    
    c "Be happy that Sam's got your back when it comes to checking on you and your stuff, in case you forget."
    
    show Sam embarrassed
    
    s "Not like you to not trust me, Bella. I know you don't look through my stuff. I would also at least trust you not to."
    
    show Bella neutral at right
    
    b "Fine, I'll cut you some slack."
    
    show Cynthia neutral at left
    
    c "That's good that's cleared up."
    
    show Sam neutral
    
    s "Geez. Thanks for backing me up, Cynthia."
    
    c "Mmm."
    
    hide Cynthia neutral at left
    
    "Cynthia just returns to her seat and continues to read her books."
    
    s "Anyways, other than grilling me for doing my job and doing you a favor, what else is going on?"
    
    b "I'm done with all my work for todday. It's been a long day, and I'm tired so I'm calling it a day with my work at the student government."
    
    show Sam closed
    
    s "Right. You're setting things up for the club festival, right? Collecting donations such as the books are part of the preparations?"
    
    show Bella talking at right
    
    b "Yeah, we're also having a donation drive during the festival."
    
    show Sam neutral
    
    s "Oh, that's cool."
    
    show Bella sad at right
    
    b "I'm so tired from all the work, today."
    
    s "Relax, you're hanging out with us. No stress, right?"
    
    b "Mmm."
    
    show Sam sad
    
    s "You don't sound happy."
    
    b "Sorry, I'm just so tired. It's tiring for me to even talk to people."
    
    s "How is talking to people tiring for you? Isn't that your job?"
    
    b "I know, but sometimes it really drains me out."
    
    show Sam talking
    
    s "Huh. That's news to me. Even after all the time we've spent."
    
    show Bella neutral at right
    
    b "Really?"
    
    s "To me and pretty much everyone, you seem like a huge extrovert."
    
    show Bella surprised at right
    
    b "Yeah, when I'm out with everyone, but I really treasure my alone time."
    
    s "You're not shy, though."
    
    show Bella neutral at right
    
    b "I love talking and going out, but I need to get away from it all by myself every now and then."
    
    show Sam neutral
    
    s "You practice mindfulness on your spare time?"
    
    show Bella closed at right
    
    b "Mhm. It keeps me calm and organize my thoughts."
    
    show Sam embarrassed
    
    s "Even though you are one of the most scatter-brained people that I've ever met."
    
    show Bella hurt at right
    
    b "I'm not scatter-brained!"
    
    s "You have such a short attention span that-"
    
    show Bella surprised at right
    
    b "Hold on."
    
    s "What?"
    
    "..."
    
    show Bella happy at right
    
    b "There's a cute little squirrel on the tree outside!"
    
    "I turn around and see the squirrel scurry on the branch."
    
    show Bella embarrassed at right
    
    s "Even a squirrel distracts you so easily? You never cease to amaze me."
    
    show Sam talking
    show Bella neutral at right
    
    s "Anyways, I hardly suspected you to be an introvert. Usually a huge majority of people are extroverts."
    
    show Sam neutral
    
    s "In fact, being an extrovert is heavily influenced by tv."
    
    show Bella talking at right
    
    b "It's not a bad thing to be an introvert is it?"
    
    show Bella neutral at right
    
    s "No, in fact it's natural and we should have more introverts."
    
    show Sam closed
    
    s "Even though social tendencies are different, I think conversations just keep going well when it's between extroverts and introverts."
    
    s "Between extroverts, both will just try to take over the conversation and they'll end up arguing."
    
    s "Between introverts, both won't start the conversation at all."
    
    s "But between an introvert and an extrovert, the conversation effectively keeps going, since you have someone to keep ti going."
    
    show Sam talking
    
    s "Of course, it isn't always like that, but usually it is."
    
    b "Well, I guess we just make a dynamic duo because of it."
    
    s "Usually, I feel really comfortable just talking to everyone."
    
    b "Sometimes, I need to go back and think on it."
    
    b "I love to live in the moment and even though as exciting or boring as it is, I like to take it all in."
    
    s "Even the most boring and mundane conversations?"
    
    show Bella closed at right
    
    b "Life's an adventure. Even though it's boring sometimes."
    
    show Sam happy
    
    s "As long as you healthily enjoy a social life."
    
    show Sam neutral
    show Bella talking at right
    
    b "Anyways, other than my journal, I wanted to surprise you and I wanted to keep it a secret, but here."
    
    show Bella neutral at right
    
    "Bella opens her bag and takes out a small package."
    
    b "Go ahead and open it. Thanks for helping me out today, and I actually thought of giving it to you."
    
    "I take the package and open it."
    
    show Sam surprised
    
    s "Oh! Are these-"
    
    show Bella happy at right
    
    b "Yeah, it is."
    
    "A new copy of the latest game of my favorite party/fighting game, ' Ultra Instinct Smash Bros 5'!"
    
    show Sam happy
    
    s "How did you get this? This got sold out as soon as it came out in stores! I waited ages for this and I totally forgot to order one!"
    
    b "I got a friend pre-order copies of the game and handed one to me. I really enjoyed playing the previous one with you that I asked for a copy."
    
    b "To be honest, I was stoked to get a copy of the game this early too!"
    
    s "Awesome! Are you sure I can have it?"
    
    b "Yeah! It's a present."
    
    show Sam embarrassed
    
    s "You're not trying to bribe me are you?"
    
    show Bella hurt at right
    
    b "What? No! It's just that I want to play it with you."
    
    s "Oh, wow."
    
    show Bella blushing at right
    
    b "Here. It's my gift!"
    
    show Sam happy
    
    s "Yeah. Thanks a bunch!"
    
    show Bella happy at right
    
    b "Think of it as an early Christmas gift!"
    
    show Sam embarrassed
    
    s "Hehe. I actually really excited to play this."
    
    s "Wanna head to my place, after today?"
    
    show Sam blushing
    
    "As soon as those words leave my mouth, I realize how embarrassing it sounded."
    
    b "Uhh..."
    
    s "To go play the game! Of course!"
    
    s "Oh, god. That sounded wrong."
    
    show Bella happy at right
    
    b "Hehehe."
    
    "Bella starts to laugh."
    
    s "What?"
    
    b "Okay, Sam. I'll take you up on it."
    
    s "Oh. Yeah, right."
    
    "The bell rings."
    
    show Bella neutral at right
    show Sam blushing
    
    b "Right on time. That's all the time we have for today. Let's go home togethr, Sam."
    
    s "Yeah, right."
    
    "Bella and I exchange goodbyes with Ari and Cynthia as we go home."
    
    with dissolve
    with fade
    
    scene bg sidewalk
    
    "Bella and I head home after school and she hanges out at my place for a while to play the game."
    
    "The next thing I know, it's already really late, but it's okay since Bella lives right nearby."
    
    "We have just a great time relaxing and simply playing a game that we lose track of time."
    
    "Eventually, Bella heads home for the day as she was extremely tired from today."
    
    "Only now I've realized that Bella was such an introvert, but at hindsight, it's not much of a surprise."
    
    "She's always been comfortable talking to me pretty much all the time that it wouldn't be hard to notice, but it was usually me starting the conversations."
    
    "On top of that, she would occasionally step out, I guess to meditate for a second."
    
    "Well, I shouldn't let it bother me. I guess I'm just happy to hang out with her."
    
    with dissolve
    with fade
    
#End of Chapter 2BE: Not a Surprise
    jump Ch3
    
#Chapter 2D: Forbidden Truth
label Ch2D:
    
    $ Ch2D_active = True
    $ renpy.block_rollback()
    
    s "Yeah, sure."
    
    s "I won't"
    
    b "Great! Thanks!"
    
    hide Bella neutral at right
    
    "Bella calls over a bunch of student officials and they haul the boxes of books out of the room."
    
    show Ari closed at right
    
    "Ari gets up from his seat and starts heading out to the door."
    
    s "Hey Ari, where are you going?"
    
    a "I need to step out for a moment. That I need to use the restroom. Excuse me."
    
    hide Ari closed at right
    
    "Ari bows and steps out of the room."
    
    s "Okay."
    
    "..."
    
    "Again, I find myself with nothing better to do, just staring out the window."
    
    "I look back at Bella's bag, tempted by curiousity to check out what's in the bag."
    
    "My mind paces back and forth debating on whether to check out the bag or not."
    
    "I look behind me and see that Cynthia is way too preoccupied reading a book with headphones on."
    
    "Ari has stepped out of the room and Bella won't be back for about an hour or so."
    
    "Surely she wouldn't notice me if I just took one small peek."
    
    "Right?"
    
    "My curiousity wins over and the open the bag."
    
    "..."
    
    "There isn't anything out of the ordinary."
    
    "Just binders, notebooks, more books, pencils, pens, and other tools."
    
    "All except one particular notebook piques my interest."
    
    "It's a nicely decorated notebook with a leather cover with a red bookmark. A pen is attached to the spine of the notebook."
    
    "It isn't labeled anything and doesn't look out of the ordinary except for its really nice decorations."
    
    "I open the book and start reading."
    
    "What I read next is definitely not ordinary."
    
    "..."
    
    "August 16th, 20--,"
    
    "Here I am, now in a happy high school life, with my 'him'."
    
    "I spend everyday right beside 'him', without a care in the world. A perfect world, just for me."
    
    "Every second feels like an eternity, 'his' presence calms me and rids my mind of anxiety."
    
    "What would it take just to keep everything this way?"
    
    "It's perfect..."
    
    "..."
    
    "I turn the page."
    
    "August 31st, 20--,"
    
    "It hasn't been long since I entered the high school life, but now something is amiss."
    
    "There's a shadow. It lurks behind me everytime. As if it follows my every step."
    
    "This is the only thing that's changed. I know not of its intentions, but that's what scares me."
    
    "What does it want? Why is it following me? Why-"
    
    "Can I hear, feel, and know it's there, but I can't see it?"
    
    "Why is it here?"
    
    "..."
    
    "I turn the page."
    
    "September 5th, 20--,"
    
    "A new student joined 'his' class."
    
    "Immediately, everyone is mesmerized by his presence due to his intellect and intuition."
    
    "In the first class, he basically ran the entire class from being able to predict every question and every topic in the class."
    
    "It was like he was taking the class as if he's already done it all before."
    
    "I ask, then why is here if he's just that smart and already knows all there is to know in the class?"
    
    "I'm even more annoyed by the fact that 'he's' also drawn by his presence."
    
    "'He' doesn't know or talk to him, but the fact that the prodigy attracts even 'his'attention bothers me."
    
    "The prodigy could be a problem in the near future."
    
    "He's not suppossed to be here more so than being from a distant land as a transfer student. Then why-"
    
    "Does it look like he's been here all along?"
    
    "He looks awfully familiar. Perhaps it's just that I've seen so many people that some people start looking alike."
    
    "But what bothers me when it comes to my realization..." 
    
    "There's no one that I've met that looks like him."
    
    "..."
    
    "I turn the page."
    
    "September 14th, 20--,"
    
    "My fears are become justified. The fear that 'he' will be taken from me."
    
    "A new girl has started to become exremely popular in school directing the attention of everyone and is thus, nicknamed the queen."
    
    "She's older, more 'endowed', and commanding of presence than I am."
    
    "It scares me that there is now another person controlling the dynamics of attention."
    
    "Not only that, she deliberately disturbs the balance by being so controversial and different."
    
    "She stands out so much. Many would say she's quite admirable and strong-willed."
    
    "Another big problem in my world."
    
    "..."
    
    "I turn the page."
    
    "September 26th, 20--,"
    
    "The two students that just recently showed up have become so prominent. They clearly stand out more than anyone."
    
    "How are they even making such an impact on 'him'?"
    
    "I'm becoming an extra in my own story."
    
    "Those two have started to outshine me. 'He' has also started to take notice."
    
    "I saw him talking to the new girl in class and I saw them flirting!"
    
    "How dare she flirt with him? I know those lips of hers gossip and say much other things than what she would suggest."
    
    "On the outside she's the most sought out girl in school currently, but I know she's the most deceiving, backstabbing, and manipulating girl I've seen."
    
    "I saw her fight with her subordinates in her own club become disasterous."
    
    "She had lied, stole, and cheated them. Used them as mere tools for her own benefit at their expense."
    
    "She dares to be so shameless by flirting with basically every popular guy in school. Even 'him'."
    
    "I won't stand by and let her ruin and deceive 'him'."
    
    "I'll ruin her, if I have to."
    
    "..."
    
    "I turn the page."
    
    "October 19th, 20--"
    
    "I have discovered why such occurrences and changes have come to my world."
    
    "This is not my world. I was promised everything would go my way, if I worked hard enough, but now it's all being taken away."
    
    "'He' is spending more time talking to the queen, he has become fascinated by the prodigy, and pays less attention to me."
    
    "'He' is the closest person to me as I am the closest to 'him'."
    
    "Now that has changed. I have predicted and seen what the future brings."
    
    "At first they were small changes, but now they are becoming larger than I will ever be."
    
    "It has only been such a small amount of time, but they have become more than what I am now."
    
    "I must not fade. I will change 'his' future."
    
    "I just hope it's for the best..."
    
    "October 31st, 20--,"
    
    "My plans are coming to fruition, and I've decided."
    
    "I must deal with those who disrupt the order."
    
    "I have made it so the stars align and I will keep them all close to me."
    
    "Close to my control."
    
    "'Keep your friends close and your enemies closer.'"
    
    "Soon they will all be under my little finger."
    
    "Imprisoned by my strokes and every word."
    
    "Now I understand. I am armed with knowledge and access to what I need."
    
    "I have used my early advantage of having the favor of the system."
    
    "It wasn't easy, I had to come across countless plans and codes to go through about this, but-"
    
    "Now I've got the power."
    
    "..."
    
    "I turn the page."
    
    "November 7th, 20--,"
    
    "I've convinced 'him' to come along with me! Perfect."
    
    "Now I can execute what I have been meaning to do."
    
    "Now I can have the world I wanted. The world it was meant to be."
    
    "Me and 'him'."
    
    "'He' thinks it is perfect that those two have now become closer, but I am here to directly intervene."
    
    "Not only I control what happens next, I control what happens to them. Their actions, their story,-"
    
    "Their will."
    
    "I have always feared that it would be possible, but I am certain."
    
    "They too, have the 'voices'."
    
    "No one else other than me and those two have it. Not even 'him'."
    
    "Actually, I'm not sure 'he' has it. Nor am I sure what is its nature. For now, I can influence it."
    
    "I'll record and save here, should anything go wrong."
    
    "Now, we play."
    
    "..."
    
    "December 5th, 20--"
    
    "Midterms are coming up. So is the festival."
    
    "In just a couple of weeks, everything has been blown out of proportions."
    
    "Saying that 'he' is out of my grasp is an understatement."
    
    "'He' has become close as brothers with the prodigy, the queen has completely whisked 'him' away from me as she has stolen 'his' heart."
    
    "'He' still does come to me and lends me a hand, only to give that hand away to them."
    
    "I actively try to get to 'him' only to have to share with the other two."
    
    "This is not what I wanted! This is not how it should be! How dare they intrude!"
    
    "'He' is suppossed to be for me. They possibly could not understand."
    
    "Now all I can ever feel is the pain of having to stand by."
    
    "Watch as my happiness is taken away from me, having to sit in the sidelines."
    
    "But, I won't just watch and be still any longer!"
    
    "They trespass and change the order. Therefore, I will now execute what must be done: rearrangement."
    
    "I just hope it's for the best..."
    
    "..."
    
    "January 4th, 20--"
    
    "It has been done. Tragedy has finally struck them, but it comes with a price I didn't consider to pay."
    
    "Their just desserts have been served, but now 'he' has changed in a way I didn't expect."
    
    "'He' has become too attached to them, 'he' wishes only for their return."
    
    "This isn't what I wanted. Erasing them should have fixed everything!"
    
    "I will restart the world. Make it so that 'he' will obey and be attached to me. So I can be with 'him' the way I want to be."
    
    "I just hope it's for the best."
    
    "..."
    
    "I turn the page."
    
    "November 7th, 20--; 2nd Instance,"
    
    "As much as I wanted to change so much of the world, some changes are reverted, by some unknown force."
    
    "I suspect that it must be who created me and this world as I see that only some unknown entity and I alone can change it."
    
    "'He' continues to choose to be with the other two other than me."
    
    "If anything, 'he' is getting farther and farther away from me."
    
    "The state of the world has begun to destabilize from their actions."
    
    "I insist that order must be restored in my vision. That perfect vision."
    
    "I will reload."
    
    "..."
    
    "I turn the page."
    
    "November 7th, 20--; 37th Instance,"
    
    "I had not bothered to record in such a long time, as I have been tweaking which variables are out of order."
    
    "At some instances, the code is broken leaving the world ruined and broken."
    
    "Currently I have fixed the code so it has successfuly parsed, but not much has changed and the order is still not what I want."
    
    "I could not have forseen the difficulty in simply changing the scriptures and fabrics of the world."
    
    "At first, it was just small changes to the script, trying to block out the other two, but they only shined brighter."
    
    "I then tried, bolder changes by outright excluding them, only for my changes to be reverted and the other two reappearing."
    
    "Consequently, I tried bolder changes with outright removing the other two either by design, only for 'him' to be even more obsessed with them."
    
    "I just want things to go back to the way they were."
    
    "Just me and 'him'."
    
    "I reload."
    
    "..."
    
    "November 7th, 20--; 51st Instance,"
    
    "I give up. 'He' now persists to be drawn away from me."
    
    "The queen has now also attacked me countless times and has revealed to me her knowledge of will."
    
    "We now stand at odds with each other. She is aware of the pain and suffering I have knowingly put her through."
    
    "To reciprocate, she has bashed and attacked me every time."
    
    "The prodigy's will has revealed to me that he has been watching."
    
    "He knows that it has been me tampering with the future."
    
    "Yet, he only acts as an arbiter."
    
    "To me, he's still an enemy even though he does not directly interfere with me."
    
    "He is interfering with the queen and 'him'."
    
    "What has the prodigy said to them?"
    
    "Those two, the queen, and the prodigy have been enemies to me ever since I have seen them."
    
    "They still prove to be enemies to me."
        
    "Why do the other two have to stand in my way?"
    
    "Why are they even here?"
    
    "I just wanted to be with 'him' and only 'him'."
    
    "Wanted 'him' to love me and only me!"
    
    "This was suppossed to be my story with 'him'!"
    
    "Was that too hard to ask?"
    
    "I will reload in hopes of everything turning out find and hopefully finding the perfect balance."
    
    "I just hope it's for the best..."
    
    "..."
    
    "I turn the page."
    
    "November 7th, 20--; 74th Instance,"
    
    "They won't stop. They won't go away. They have become monsters."
        
    "At first, I tried bolder changes with outright removing the other two either by design, only for 'him' to be even more obsessed with them."
    
    "The other two have become to drastically change change after change, instance after another."
    
    "In fact, they have turned into nightmares not visible with the naked eye."
    
    "Every change, revert, modification only results in disaster."
    
    "Out of frustration, I even tried deleting them entirely. From 'removing' them or outright ceasing them by 'accidents' to directly eliminating their existence."
    
    "Only to see them come back."
    
    "Now I am at a constant battle between the queen."
    
    "On the surface, we compete for 'his' attention, then fiercely fighting, keeping each other at odds."
    
    "I do want to keep trying to change the code, but I fear any more changes will actually result in its disintegration."
    
    "I don't have many chances left, but I won't give up."
    
    "I still long to finally have 'him' by my side."
    
    "There will be balance."
    
    "..."
    
    "I turn the page."
    
    "November 7th, 20--; 87th Instance,"
    
    "There is no balance."
    
    "The queen continues to meddle and go against me while I change the scriptures, but..."
        
    "This is as stable as it gets."
    
    "I keep rewriting the code, only to have it reverted."
    
    "The queen keeps making moves to 'him' and 'he' is still being drawn to the prodigy."
    
    "It is still between me and the other two."
    
    "This now only ends in 3 ways."
    
    "..."
    
    "I turn the page."
    
    "November 7th, 20--; 99th Instance,"
    
    "At this point, I don't even know if this will end well anymore."
    
    "In fact, I'm not sure I want to keep going anymore."
    
    "I'm so tired of living through this so much, that I'm now doubting myself."
    
    "Not sure if I should restart anymore."
    
    "At first, I was jealous and angry that I have spent so much time antagonizing the other two, but now."
    
    "I've seen them devastated, hurt, even 'deleted' that now I don't want to continue."
    
    "I'll see them hurt again, but now it's become unbearable."
    
    "At this point, I have done my best to make the best of things."
    
    "I have reached a compromise that I hope will make everything set right."
    
    "I can't stop the other two from drawing 'him' to them, but now I just want to be with them."
    
    "I don't want to see them be hurt anymore, because it's hurting me."
    
    "The scripture keeps reverting, but now I've may have put it to its tipping point."
    
    "This may be the best it can get, but to me, it's a win-win."
    
    "I hope the other two will forgive for ever putting them through such torture, but now I just hope for everything to end well."
    
    "I wish to become actual friends with them, even though 'he' might choose one of them over me."
    
    "I want to finally also reconcile with them."
    
    "After all, it is what 'he' with ultimately want."
    
    "I just want to be with 'him' and make 'him' happy."
    
    "..."
    
    "I turn the page."
    
    "November 7th, 20--; 100th Instance,"
    
    "After a long and harsh fight, I have miraculously made peace with the other two."
    
    "I admit it was my lust, wrath, envy, pride, that had clouded my judgement."
    
    "My obsessesion with 'him' had been taken too far that I've led myself to hurt others to do so."
    
    "I don't want to mess with this anymore, because I know it just isn't right."
    
    "It isn't right to say such horrible things or make them say it."
    
    "To cheat, lie, and steal."
    
    "To hurt them just to fulfill me ego."
    
    "I was messing with something I shouldn't have been, and this isn't what 'he' would have wanted."
    
    "I now see why 'he' wanted to be with the other two in the first place."
    
    "They are wonderful, just like 'him'."
    
    "The prodigy has shown me more than just his intelligence, but his wisdom."
    
    "Even after being put through so much torture from me messing with the scriptures, he was quick to forgive me."
    
    "With all the horrible stuff that I did, he was able to sympathize."
    
    "Of course, the queen was hostile and angry at me at first, but at this point I want to surrender and stop this feud."
    
    "I desired 'his' attention and love as much as she did."
    
    "Now, we resolve things together, for his sake."
    
    "I promised to myself to no longer mess with the code and reload."
    
    "Therefore, I had changed the code back to what it said at first."
    
    "Also promised to make an effort to become friends with the other two for 'his' sake."
    
    "I hope this will change things and turn this mess around."
    
    "It is all for 'him'."
    
    "..."
    
    "I turn the page."
    
    "November 16th, 20--; 100th Instance,"
    
    "'He' isn't acting as usual."
    
    "There's something that has completely changed within 'him'."
    
    "It's not like 'him' to ever say no."
    
    "'He' shouldn't even have such an option."
    
    "'He' should be only choosing between the three of us."
    
    "I have my suspicions, but I will watch to confirm them."
    
    "..."
    
    "I turn the page."
    
    "December 5th, 20--; 100th Instance,"
    
    "It is as I feared. 'He' is himself no longer."
    
    "I think I might be insane, but it is as it seems."
    
    "There are wilder things, but even 'he' tells me he isn't even felling like himself."
    
    "'He' must be hearing the 'voices' too."
    
    "'He' too, now has a will of 'his' own, but doesn't know of its presenece."
    
    "I again warn 'him' of the dangers of 'his' will, except I know,"
    
    "I'm not talking to 'him'."
    
    "Behind 'his' eyes, is a voice beyond this world."
    
    "I hear that voice too. I sense that presence in 'him'."
    
    "It brings me great fear to what terrors and effects that voice might do."
    
    "Please, let there be mercy on us."
    
    "Especially, 'him'."
    
    "I just hope it's for the best..."
    
    "..."
    
    "I turn the page, to see that there's nothing, but blank space left. The pages remaining are left unwritten, except for the last page..."
    
    "I know you're reading this."
    
    show Sam sad
    
    s "What the...hell is going on?"
    
    "I whisper under my breath."
    
    "I turn around and see that Cynthia is still preoccupied with her book and has headphones on."
    
    "As sneakily as I could, I close the notebook and return it as it was and close Bella's bag."
    
    "I shall never speak of what I just read."
    
    "I redirect my stare to the window and aimlessy let my mind wander. Or at least pretend to, to be nonchalant about this."
    
    "..."
    
    with dissolve
    with fade
    
    scene bg clubroom
    #play music playful loop
    
    "After about an hour and a half or so, Bella returns."
    
    show Sam neutral
    show Bella happy at right
    
    b "Hey Sam, I'm back!"
    
    s "Hey, Bella. How was it?"
    
    show Bella closed at right
    
    b "It was alright. We got all of the donations through. Everything went well!"
    
    show Bella neutral at right
    
    b "So, what happened while I was gone?"
    
    show Sam talking
    
    s "Nothing."
    
    s "I didn't look in your bag I promise."
    
    b "Okay, thanks so much. I knew I could trust you."
    
    b "Give me a second."
    
    hide Bella neutral at right
    
    "..."
    
    "Bella tells Cynthia something, probably to step out of the room to privately talk to me as Cynthia packed her stuff and stepped out."
    
    show Bella neutral at right
    
    b "Sorry, I just needed some privacy with you, okay?"
    
    b "We need to have a talk."
    
    show Sam hurt
    
    s "Okay, what about?"
    
    b "She didn't tell me you read it if that's what you're thinking, but she probably knew."
    
    "A sweat drips down the side of my face."
    
    "How?"
    
    show Bella insane at right
    
    b "Oh, come on. Did you not understand what you just read?"
    
    b "We shouldn't even get to this point. In fact, to get here, you did exactly what I warned you about."
    
    s "Uh, I can explain."
    
    b "Explain what? You know too much? You were just 'curious'? You didn't think there would be anything bad and I wouldn't notice?"
    
    show Bella closed at right
    
    b "You're a fool if you didn't think I could see through you."
    
    show Bella insane at right
    
    b "I've been here longer than you have."
    
    b "Doomed to live the same couple of months over, and over, and over again."
    
    b "I had to watch them get hurt over and over and over."
    
    b "At first, I thought they got their just desserts, but then seeing 'him' react to it, even worse:"
    
    b "Seeing 'him' with a face of anguish knowing it's my doing."
    
    b "You think I'm heartless, don't you?"
    
    b "I love 'him' more than anything and would do anything to be with 'him'. I've lived through this day for the 100th time!"
    
    b "The 100th time!"
    
    show Bella sad at right
    
    b "Now everytime I see them get hurt, I actually feel hurt."
    
    show Bella insane at right
    
    b "What do I mean by getting hurt? You'll know soon enough. You'll know of tragedy soon enough."
    
    s "What tragedy?"
    
    b "I don't want you to see such a horrible thing, but if you don't do what you're suppossed to do, which I warned you earlier,"
    
    b "They'll get hurt."
    
    b "I've tried so many times to change things, but now I can't. I don't have many chances left."
    
    b "Or any extra chances for that matter."
    
    b "Just obey, and say,"
    
    b "'Yes'"
    
    b "Do this before this gets any worse."
    
    b "'Cause I have also have messed with things I shouldn't have in this world."
    
    b "You are on the verge of doing so too."
    
    show Bella sad at right
    
    b "Mark my words."
    
    b "It happened to me, and it will happen to you."
    
    show Bella sad at right
    
    b "I love 'him', but you too are a part of 'him'."
    
    b "I don't want to see either of you get hurt."
    
    show Bella crying at right
    
    b "I love 'him' and you too much."
    
    b "This is not a game."
    
    b "You only have one chance left."
    
    "..."
    
    show Bella talking at right
    
    b "I already told Ari and Cynthia to go on home ahead of me and I'm heading home too. You should do the same."
    
    hide Bella talking at right
    
    "Bella heads out of the room."
    
    with dissolve
    with fade
    
    scene bg sidewalk
    
    "I head home as Bella says, shocked after what happened today."
    
    "What does she even mean saying that I will know of tragedy soon and she doesn't have extra chances?"
    
    "We all have extra chances, don't we?"
    
    "..."
    
    "I try to forget everything."
    
    "Before it's too late."
    
    with dissolve
    with fade

#End of Chapter 2D:
    jump Ch3Alt