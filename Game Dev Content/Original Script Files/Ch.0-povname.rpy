#Prologue Part I Even: Naming Player
#Chapter 0
label povname:
    
    show Sam neutral
    default admincall = ""
    $ povname = renpy.input("What's your name?")
    $ povname = povname.strip()
    
    if not povname:
        show Sam embarrassed
        s "What? You don't want to give a name?"
        "Why should I give my name away anyway?"
        s "So I can call you by your name respectably. Otherwise, I'll just call you 'Butthead.'"
        $povname = "Butthead"
        x "'Butthead?' Why of all things are you giving me that stupid name?"
        s "'Cause you're being one right now!"
        x "Well, I just don't think I should give my name willingly."
        show Sam closed
        s "Okay, Butthead."
        x "Don't call me that, just give me another name. Something more sensible, other than just Butthead."
        s "Butthead, Butthead, Butthead."
        x "Seriously, stop!"
        s "I don't know what you're talking about, Butthead. I'm just calling you what I think is a good one."
        $povname = "Alex"
        x "Okay, okay, fine. Just call me Alex. At least just call me like a normal person by my real name, since you're asking for a name so badly."
        show Sam happy
        s "See? That wasn't so bad! Why do you even have to avoid giving me your name?"
        x "{i}*Sigh*{/i} I have my reasons, that's all you need to know, happy?"
        s "Yeah, actually. At least we trust each other a little bit now."
        x "..."
        jump Named
    
    elif povname == "Mark":
        show Sam happy
        s "I did not hit her, I did NOT!"
        x "Don't say it..."
        s "Oh, hi Mark!"
        x "..."
        show Sam talking
        s "No, for real. Is that really you, Mark?"
        x "Yes, it's me."
        s "No as in..."
        $ admincall = renpy.input("As in?")
        $ admincall = admincall.strip()
        jump Admincall
    
    elif povname == "Sam":
        s "Very funny, not happening."
        s "Cool that we have similar names, but I'd like it if I called you something different to avoid confusion."
        with fade
        jump povname
        
    elif povname == "Ari":
        show Sam happy
        s "Oh, cool. Is that Chinese or Japanese?"
        show Sam embarrassed
        s "Wait, why isn't the script progressing?"
        s "I can see that in a couple lines it'll take us back to naming again."
        x "What are you talking about?"
        show Sam angry
        s "You're messing with the game on purpose. Aren't you?"
        x "What do you mean by that?"
        s "Unless it's by sheer coincidence, knowing the name from somewhere, or you playing this game before that you know that name."
        s "I suspect you're messing with the game just for giggles again."
        show Sam embarrassed
        s "See, this is why giving players choice on the game can be annoying sometimes, because they do stuff like this."
        s "Anyway, let's just go back and try this again."
        with fade
        jump povname
        
    elif povname == "ari":
        show Sam angry
        s "Oh, look at you, you can use lowercase letters too."
        s "Not working."
        with fade
        jump povname
        
    elif povname == "Bella":
        s "You have the same name as my childhood friend. I'll talk more about her later."
        $ povname = "Another " + povname
        x "Wait, why am I named 'Another Bella?'"
        show Sam angry
        s "Well, I don't like it when I meet people with the same name, nor does the game like it either."
        s "So, go give another name so you don't confuse me and the game."
        s "The writer is just lazy when it comes to coding so, just maybe add a middle name to have a slightly different name."
        with fade
        jump povname
        
    elif povname == "bella":
        show Sam angry
        s "Are you serious?"
        with fade
        jump povname
        
    elif povname == "Cynthia":
        s "Hmmm."
        x "What?"
        s "Nyet."
        x "Nyet?"
        show Sam angry
        s "{i}Cyka Blyat.{/i}"
        x "Watch that language. Also, you didn't even bother to add the correct letters from the language over translation!"
        s "Fine, I'll do it in English then, bitch!"
        s "Are you having fun, messing around with this?"
        x "What other languages can you curse in?"
        s "{i}Puta madre! Affenschwanz! Un homme dément! Putang ina! Merda! Baka!{/i}"
        show Sam neutral
        s "Just the few that that's written on my script."
        x "Why the heck are you cursing at me for?"
        show Sam angry
        s "Quit messing around. Or if that is your actual name, use a different name. The game nor I like that you might be messing with the game again."
        x "Again?"
        s "Don't lie! You're doing this intentionally. Let's just redo this, so we can go through with the game."
        with fade
        jump povname

    elif povname == "cynthia":
        show Sam angry
        s "We'll just keep going back until you finally get satisfied with reading all these lines."
        s "The writers appreciate you reading everything, but the fact that I have to sit through all this crap annoys me."
        with fade
        jump povname
        
    elif povname == "Mrs.Moore":
        show Sam angry
        s "Somehow, you got a hold of my last name this early into the game, and you're impersonating my mother. Okay."
        s "No way I'm letting that slide."
        with fade
        jump povname
        
    elif povname == "Your Mom":
        show Sam angry
        s "What is this? A 12 year old 'COD' player making a joke again?"
        s "Get out."
        with fade
        jump povname
        
    elif povname == "Sebastian":
        show Sam talking
        s "Please, you're not cool enough to even hold that name."
        s "Also, you probably won't see him or many of the other characters here just like the first couple from before."
        s "The artists were too lazy to do that."
        s "Try again."
        with fade
        jump povname
        
    elif povname == "Sebastian Michaelis":
        show Sam surprised
        s "No, we don't have the copyright to make that joke!"
        s "We're taking that down for sure!"
        with fade
        jump povname
    
    elif povname == "Diana":
        show Sam closed
        s "Diana, Roman goddess of the hunt, the moon, and the wild. Able to talk and live in harmony with wild animals and nature."
        s "Also, a pretty generic and excellent example of naming a typical maid."
        s "Yea, you guessed it. She's also a character here. No, you can't have the name."
        s "No, you don't get to see her because the artists are too lazy to draw her in. Even in any of the CGs."
        s "So no, you don't get to see anyone in a maid costume to fulfill your creepy desires for moe."
        s "Yes, we're going back to choose a different name."
        with fade
        jump povname
        
    elif povname == "sebastian":
        show Sam angry
        s "Look at me, I can use lowercase letters!"
        s "No, you still can't have that name!"
        with fade
        jump povname
        
    elif povname == "diana":
        show Sam angry
        s "What did I say about using lowercase again?"
        with fade
        jump povname
   
    elif povname == "Aunt Yui":
        show Sam sad
        s "Why would you do that?"
        s "You don't get to hear much about her, but she's the sweetest old lady around!"
        s "The fact that she has to take care of a kid while working multiple shifts 24/7 as a nurse and still wearing a smile makes her such a nice, hardworking person."
        s "I don't think you can wear that name here."
        show Sam talking
        s "Oh, there's also a note from the writer."
        s "If you're still trying other ways to steal character names, I've got a little message for you."
        s "Have fun looking for them, or just look at the script, obviously."
        s "Anyways, have fun forcing Sam to have to read the lines as you annoy him to try other names. -HistoryMark"
        show Sam embarrassed
        s "..."
        s "Seriously?"
        with fade
        jump povname
        
    elif povname == "Mrs.Garcia":
        show Sam talking
        s "You probably tried to steal my mom's name, but now you're stealing Bella's mom's name. Okay, just stop."
        show Sam embarrassed
        s "Unless, a strict latina mom with a homing slipper to punish you for misbehaving sounds like you."
        s "Anyway, the game still won't let you name yourself that."
        with fade
        jump povname
        
    elif povname == "Vincent":
        show Sam talking
        s "Nah, kid."
        s "Nothing personal, kiddo."
        with fade
        jump povname
        
    elif povname == "vincent":
        show Sam talking
        s "At this point, just add random numbers in why don't ya!"
        s "Try using another name."
        with fade
        jump povname
        
    elif povname == "Ferdinand":
        show Sam talking
        s "As in Magellan?"
        s "No? You're just trying to steal a character name again? Okay."
        s "Let's go through the procedure again."
        with fade
        jump povname
        
    elif povname == "Jenny":
        show Sam talking
        s "As in JLo?"
        s "What? I can't mention that I'm aware of stuff 'out there' like showbiz?"
        s "Fine."
        with fade
        jump povname
        
    elif povname == "Celica":
        show Sam talking
        s "Pretty name, but I'm just as tired as the lazy writers making up more lines to accompany each name you're trying to steal."
        with fade
        jump povname
        
    elif povname == "Sarah":
        show Sam talking
        s "I know it's a fairly common name, but no you can't have it here."
        s "You can try out variations of the name like everyone does though."
        with fade
        jump povname
        
    elif povname == "ferdinand":
        show Sam talking
        s "Stop."
        with fade
        jump povname
        
    elif povname == "jenny":
        show Sam talking
        s "Trying."
        with fade
        jump povname
        
    elif povname == "celica":
        show Sam talking
        s "To Steal."
        with fade
        jump povname
        
    elif povname == "sarah":
        show Sam talking
        s "Their names!"
        with fade
        jump povname
        
        
    elif povname == "12321":
        show Sam happy
        s "Hey, it's a palindrome! It's also 111^2!"
        s "Aww, that one doesn't work either?"
        with fade
        jump povname
        
    elif povname == "69":
        show Sam embarrassed
        s "Nice."
        s "No, its ok to make these stupid jokes. The game is 18+. That name isn't though."
        with fade
        jump povname
        
    elif povname == "1337":
        show Sam happy
        s "Kek. Wanna join mah sniper clan?"
        s "Lol no, noob."
        s "Get nifed."
        with fade
        jump povname
        
    elif povname == "420":
        show Sam happy
        s "Smoke weed everyday?"
        show Sam talking
        s "No, weed is illegal is some states and other countries, so no."
        s "The game doesn't like that number either."
        with fade
        jump povname

jump Named

label Admincall:
    
    if admincall == "HistoryMark":
        s "Oh, it's really you, Mark!"
        x "Yeah, but just run things like normal, okay?"
        s "Need to run the script again? I can't wait to see all the mistakes and errors you find in the script!"
        x "I'm really getting accustomed to seeing the game tell me that the script fails to parse."
        x "Go on as usual."
        s "Roger, boss."
        with fade
        jump Named
    else:
        s "Nevermind."
        jump Named