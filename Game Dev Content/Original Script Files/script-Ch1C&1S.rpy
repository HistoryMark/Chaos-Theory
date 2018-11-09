#Episode 4: Chapters 1C & 1S
#Chapters 1C & 1S
label TrueFork1:

    show Cynthia happy
    show Sam neutral at right
    
    c "Hey, Sam! You're hanging out with me today?"
    
    show Sam talking at right
    
    s "Yeah, I haven't spent too much time with you yet and only met you when Bella introduced me to you."
    
    show Sam neutral at right
    
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
    
    c "Hmm."
    
    show Sam embarrassed at right
    
    "Cynthia stares at me for a moment, and our eyes meet. I try to get my eyes to wander somewhere else to avoid the awkwardness."
    
    show Cynthia talking
    
    c "No, keep your eyes on me. It's a little test."
    
    show Sam blushing at right
    show Cynthia neutral
    
    s "Uh...Okay."
    
    "I try to concentrate on just staring at Cynthia's eyes as she said, but found it extremely awkward."
    
    s "Urk...This is extremely awkward."
    
    show Cynthia talking
    
    c "Well, they say you find someone more attractive or likeable when you stare into their eyes quite a while."
    
    show Cynthia neutral
    
    s "Yeah, sure. Can we move on?"
    
    "She chuckles a little deviously."
    
    show Sam talking at right
    
    s "Anyway, about you, I heard you had a falling out with your last club. What happened with your club?"
    
    show Cynthia angry
    
    c "Oh, you're curious about that?"
    
    show Sam neutral at right
    
    s "It gave me something to talk about with you I guess."
    
    show Cynthia sad
    
    c "I don't want to talk about it. It wasn't fun. Let's talk about something else."
    
    show Sam sad at right
    
    s "Hmmm..."
    
menu:
    
    "Should I persist?"
    
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
    
    show Sam sad at right
    
    s "It couldn't have been that bad. Come on."
    
    c "..."
    
    show Sam talking at right
    
    s "It would make you feel better if you would talk to someone about it, even if they don't understand."
    
    s "After all, that's what I'm here for."
    
    c "..."
    
    show Sam neutral at right
    
    s "Come on...It's alright."
    
    show Cynthia sad
    
    c "You're fairly persistent. Damn it. Fine, I'll talk about it."
    
    show Sam talking at right
    
    s "Seriously, what happened?"
    
    hide Sam talking at right
    hide Cynthia sad
    
    with dissolve
    with fade
    #stop music fadeout 1.0
    #play music regularday loop
    
    #scene bg cgpresidentcynthia
    
    c "I was the president of the fashion club here and it was just a small club with 4 of my other friends."
    
    s "Fashion club? What do you guys do?"
    
    c "Design clothing, homemade jewelry, upcycling, making costumes, doing makeup tutorials, etc."
    
    s "That sounds cool!"
    
    c "Yeah, it's great, through fundraisers, the school paying us, and the other school clubs sponsoring our commisions, we could make any clothing we want and what the other clubs may need for whatever they need it for."
    
    c "The five of us worked like crazy, but really well on every aspect of making fashion. Design, material, measuring, styling, planning. Each of us had our own respective roles and we're really great at what we do."
    
    c "Not only that, we really knew each other. Jenny and Celica, the designer and stylist are in the tennis club, Ferdinand, Sarah, and I go to the same classes together. We were all good friends."
    
    s "Then what happened to split you guys up?"
    
    c "Money and each other."
    
    s "Your club gets paid by the school, commissions from other clubs, and fundraisers. Money shouldn't be a problem."
    
    c "Exactly. We get funding for our work, but the thing is it isn't equally shared as some members need more money to do their work."
    
    c "I always get the largest portion as president running things and advertising our works." 
    
    c "Ferdinand who's in charge of materials and inventory always go the second largest portion of the funding so he can buy the club whatever we needed to make our clothes."
    
    c "Jenny gets the third larger portion of the cut as the designer, Celica gets the fourth portion as a stylist, and Sarah the smallest cut for measuring."
    
    s "Ok."
    
    c "We all get paid by the remaining budget we have from funding after the project is complete, and I have to distribute our earnings."
    
    c "Sarah wanted a larger portion for her pay, but she her job is mostly simple labor. Ferdinand had used a large portion of the funding from our project as the materials were a little more expensive than usual."
    
    c "Celica argued that everyone should get a raise too if Sarah was asking for one as well, but we didn't have much money left from the completion of the project."
    
    c "The project was a bust, we didn't sell as much as we had hoped and it was an expensive project. Things got too messy as I always had a hard time keeping track of everything. They started to blame each other."
    
    c "Sarah then stopped working to protest, Celica then just tried to do everything to protest that Sarah should be kicked."
    
    c "That didn't really help, because Celica couldn't really do both her job efficiently and Sarah's correctly. Ferdinand didn't know what to do with all the mess everyone's making."
    
    c "Next thing I know, I'm left to do everything by myself."
    
    c "We had a huge argument that last for I don't even remember how long, then they had a fight. It all went to shit from there."
    
    s "A fight happened?"
    
    c "We all got sent to detention for that and the club was disbanded after that."
    
    with dissolve
    with fade
    #stop music fadeout 1.0
    #play music playful loop
    
    scene bg clubroom
    
    show Cynthia talking
    show Sam neutral at right
    
    c "I kept blaming myself for making rash decisions and not being organized. In fairness, everything was just a mess on my part; however, I see that everybody gets a little greedy around money."
    
    show Cynthia angry
    
    c "That, and group work gets annoying when not everyone is in the same page."
    
    c "I wanted to work in a team to make something cool, but..."
    
    c "I ended up having to do everything myself, one person not working at all, another not knowing what to do, and another just messing everything up."
    
    show Cynthia sad
    
    c "Just like group projects in every class I've had."
    
    c "Hell, I worked overtime and till midnight some days. Other days, it was unbearable to be here."
    
    c "Still, I wish people were just more open to work together for the sake of it."
    
    "she take a sigh to compose herself."
    
    show Cynthia neutral
    
    c "Anyways, that's my story of the fashion club in a nutshell."
    
    show Cynthia neutral
    show Sam talking at right
    
    s "Sorry to hear that happened to your little club."
    
    show Cynthia talking
    show Sam neutral at right
    
    c "As soon as we just got paid in a daily basis, everyone just expected to get paid. So when we didn't get paid as much, you see what happened with that."
    
    show Cynthia neutral
    show Sam talking at right
    
    s "I know we might not have much, but I'll find some ways we can do some of the same stuff here in our club if you would find that really cool."
    
    show Cynthia talking
    show Sam neutral at right
    
    c "Thanks, Sam, but just hanging out with you guys for the sake of hanging out is cool as it is. The fact that we can just be free to be complete weebs here."
    
    show Cynthia angry
    
    c "That reminds me, like in English class, we have to make a lot of group projects."
    
    c "That would be some of the most annoying assignments to work in because of having to work with people."
    
    c "A lot of people are just really lazy, but for some of us who actually do the work, our grades get brought down just because of some dumbasses not caring enough."
    
    c "It's one of the more annoying things around here."
    
    show Sam talking at right
    
    s "Sometimes, though, it's just people never talk or actually speak up to work together. Everyone wants to do their own thing."
    
    show Sam neutral at right
    show Cynthia talking
    
    c "Sure, but most people just don't have a good or solid idea of what to do, then what?"
    
    show Cynthia angry
    show Sam talking at right
    
    s "There some ways you could still work it out, but I honestly think that's just impossible with some people."
    
    show Cynthia closed
    show Sam neutral at right
    
    c "Well, I meet with a lot of people and have to work with them, but if there's one thing I've learned over the years here, Sam, it's this:"
    
    show Cynthia angry
    
    c "You don't trust a lot of things here."
    
    c "From the food, to the teachers, the people, this place is just one big...facade."
    
    show Sam talking at right
    
    s "Facade?"
    
    show Cynthia neutral
    show Sam neutral at right
    
    c "Yes, that's a good word to put it."
    
    show Cynthia talking
    
    c "I don't think the crowds of groupies in the hallways you see as 'friends' are actually friends."
    
    show Cynthia angry
    
    c "Some teachers don't care at all for the class by throwing tests and pop-quizzes just to make them."
    
    c "A lot of the people you see are just being nice, just to appear nice."
    
    c "Too preoccupied of looking and thinking that they're better than anyone and everyone here."
    
    c "Whatever label people call them, jocks, nerds, preps, band geeks..."
    
    c "They're all just posers. Fake people."
    
    show Sam embarrassed at right
    
    s "Yikes, who hurt you?"
    
    show Cynthia happy
    
    c "This cesspool did. Isn't school wonderful?"
    
    show Sam talking at right
    
    s "I won't say that you're wrong about everything, but..."
    
    s "I also don't like 'school', but we both know the reason why we're here right?"
    
    show Sam neutral at right
    show Cynthia talking
    
    c "You might have your reasons, but I'm just here to hopefully meet people I can actually trust."
    
    show Sam talking at right
    show Cynthia neutral
    
    s "Trust issues, much?"
    
    show Cynthia talking
    show Sam neutral at right
    
    c "Take a look at this place. Sure, I find it hard to trust people, but it's just that people are naive."
    
    c "Humans are naturally very trusting of each other and that's always been a problem."
    
    c "You can clearly see why this place sucks for a good reason."
    
    show Cynthia neutral
    show Sam talking at right
    
    s "Ah."
    
    show Sam neutral
    
    s "Well I don't think it's much, but there might be also a lot of us who feel this way, but I don't know."
    
    s "Eh, it sucks here, but just hanging out with Bella is enough for me."
    
    show Cynthia happy
    
    c "Having some friends around makes this place less unbearable."
    
    show Sam happy at right
    
    s "Yeah."
    
    show Cynthia neutral
    show Sam talking
    
    s "Anyways, Bella said you're here to sew and make costumes for cosplay right?"
    
    show Sam neutral
    show Cynthia talking at right
    
    c "Yeah. Happy to take any requests, as long as you pay me for the comission."
    
    show Cynthia blushing
    
    c "Anything that you want.~"
    
    "Cynthia begins to talk with a sultry voice. It makes me quite uncomfortable when she talks like this..."
    
    c "Here, I'll even show you my past work."
    
    "Cynthia shows me pictures of dresses and costumes she's made before. One depicts a student in a Japanese school uniform, another shows someone wearing a witch costume with a decorative hat and staff, but..."
    
    "They're very revealing..."
    
    show Sam surprised
    
    s "That's amazing! Do you also like to cosplay as your favorite anime characters?"
    
    "Cynthia shows me a picture of her cosplaying as a maid while wearing a blue wig and horns."
    
    show Cynthia blushing at right
    
    c "Of course! I've cosplayed before."
    
    show Sam embarrassed
    
    s "I'm really impressed by how well you can sew, but why do you have to make some costumes so skimpy?"
    
    show Cynthia happy at right
    
    c "It's just my style. I try to go for a cute design when I make them."
    
    s "Okay, but you also mostly make costumes for women. You make some for guys too, right?"
    
    "She shows me a picture of someone cosplaying someone familiar in one of my favorite games. Clad in a coat and armor, wearing the blond wig, and carrying the signature greatsword."
    
    show Sam surprised at right
    
    s "Even complete with the sword. That's amazing."
    
    show Cynthia neutral
    
    c "I have professional tailors that my mom knows to help me, but I do most of the design and sewing on these costumes. When I say anything, I mean virtually anything. I even make some of the propes, except the sword on that costume, I bought it from a hobby shop."
    
    show Sam neutral at right
    
    s "I'll be sure to come up with a good request, then."
    
    show Cynthia happy
    
    c "I don't have materials or time to make costumes right now, but I just bought new make-up and face paints, wanna try some?"
    
    show Sam happy
    
    s "Sure."
    
    hide Cynthia happy
    hide Sam happy at right

    with dissolve
    
    "We spend the next hour or so messing around with face paints."

    show Sam neutral
    
    s "We can wash these off with water right?"
    
    show Cynthia talking at right
    
    c "No, it stains your skin permanently like tattoo. You'd have to get surgery to remove it."
    
    show Sam talking
    
    s "Seriously?!"
    
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
    
    c "There, although I've smeared it a little over your face."
    
    s "Oh, please."
    
    hide Bella neutral at left
    hide Cynthia neutral at right
    hide Sam neutral
    
    "We clean up all the makeup and face paint we used up as we noticed it was already late."
    
    with dissolve
    with fade
    
    scene bg sidewalk
    
    "We all head home together after a 'fun' day messing around in the club."
    
    show Bella neutral
    
    b "All right guys! That was a great day at the club! I'll see you guys next Thursday and we now meet at Tuesdays and Thursdays. Text me if you can't make it so I can tell the supervisors. See you guys later!"
    
    hide Bella neutral
    
    "Bella waves goodbye and we all head back home."
    
    "Today was quite something. I got to know about Cynthia and her little club."
    
    "She's also really skilled in makeup and stuff like that, although I know nothing about fashion and the most fashionable thing I wear is my jacket."
    
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
    
    show Cynthia closed
    
    c "Okay."
    
    c "Well, my mom and dad, my mom's an nurse and my dad owns a small store."
    
    c "I also have an older brother who works as an programmer for multiple companies and an older sister who is a flight attendant."
    
    show Sam talking at right
    
    s "Got any younger siblings?"
    
    show Sam neutral at right
    show Cynthia talking
    
    c "A younger brother and sister, both are in elementary school."
    
    show Sam surprised at right
    show Cynthia neutral
    
    s "You've got four other siblings?"
    
    show Cynthia talking
    show Sam neutral at right
    
    c "Only my older sister moved out, everyone still lives in my house along with my grandparents."
    
    show Sam surprised at right
    show Cynthia neutral
    
    s "Sheesh, a huge family!"
    
    show Cynthia talking
    
    c "My grandma was a therapist and she would hellishly murder us if we put her in a nursing home seeing as she once worked in them."
    
    show Sam happy at right
    
    s "Hehe..."
    
    show Sam neutral at right
    show Cynthia neutral
    
    c "Overall, everything is fine for me with them, how about your family?"
    
    show Cynthia talking
    
    c "You said earlier that you're an only child. Does that bother you sometimes?"
    
    show Cynthia neutral
    show Sam sad at right
    
    s "..."
    
    "I stay silent, knowing that I have to admit it."
    
    show Cynthia talking
    
    c "I don't understand your struggle of being an only child, but I can empathize with the fact that you're lonely most of the time."
    
    c "I couldn't imagine a day all alone at home with my many siblings."
    
    show Cynthia neutral
    show Sam neutral at right
    
    s "That's why I mostly hang out with Bella."
    
    show Cynthia talking
    
    c "But most of the time, you're still home by yourself."
    
    show Sam sad at right
    
    s "Not entirely since my mom still has people to take care of me at home, but..."
    
    s "..."
    
    show Cynthia neutral
    
    c "I know it's a drag, but are you sure you want to continue?"
    
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
    
    s "As long as you're willing to listen to my selfish ranting."
    
    show Cynthia neutral at right
    
    c "I listen to everyone selfishly rant about themselves all the time. I just 'listen' because it's a social obligation."
    
    c "Unless you've got a story worth listening to."
    
    s "I'm the son of a CEO of a huge business, but I gotta say, it's cold to live behind that shadow."
    
    s "I just don't see myself doing anything remotely close to amazing like my mom. I can't really follow in her footsteps as I just don't see myself in business like she does."
    
    show Ari talking at left
    
    a "So, what do you want to do?"
    
    show Ari neutral at left
    show Sam talking
    
    s "Err....God, I don't know! I'm mediocre at best as a student, I can't seem to be able to be good at a lot of things, and I don't know what to do with my life."
    
    s "The only thing I've got going for me is that my mom has a lot of money, but I'm not smart, not talented, and not good at anything."
    
    hide Ari neutral at left
    show Sam sad
    show Cynthia talking at right
    
    c "Okay, but what do you do with most of your time?"
    
    show Cynthia neutral at right
    show Sam embarrassed
    
    "I look back on what my daily activities consist of only to realize I'm just a pathetic loser who lives his life on the computer."
    
    s "Playing videogames, watching anime, and messing around 'wumblr'."
    
    show Cynthia embarrassed at right
    
    c "Are you even remotely good at any aspect such as playing games or drawing anime?"
    
    s "Uh...No. I can't even draw anything better than a stick figure, I just repost a lot of crappy memes online, and I still haven't gotten out of bronze league in 'League of Legendaries'."
    
    s "I'm just an otaku."
    
    c "Well, don't feel bad about it."
    
    c "You're in an anime club, Bella's a huge weeb, Ari's hugely antisocial, and I'm just a cringy cosplayer."
    
    s "When you put it that way, I feel kinda bad that my only friends are all a bunch of anime freaks."
    
    c "Everone else are just a bunch of other kinds of freaks. Why should you care about that? What reputation do you even have if you even consider yourself as a loser?"
    
    s "Damn it."
    
    show Sam neutral
    show Cynthia talking at right
    
    c "Anyways, how can you not be good at anything? Do you dedicate yourself to practicing anything?"
    
    show Cynthia neutral at right
    show Sam embarrassed
    
    s "I just play to play. Practicing anything takes a lot of time and effort."
    
    show Cynthia embarrassed at right
    
    c "Really? No one really ever scolds you to actually spend good amounts of time and work to do something?"
    
    show Sam sad
    
    s "Uh...No."
    
    s "Honestly, I haven't been driven to do anything. I know I'm a lazy idiot, but I've fully accepted it."
    
    s "I just mess up on anything that I try, and I know I'm just bad at basically everything, so I don't bother."
    
    s "Plus, spending a lot of time and effort to do some things just aren't rewarding in the end when the end product just is really bad."
    
    s "Like the time I spent 4 hours to draw a copy of 'John Yostar' from 'JoYo' only to not even be able to draw the eyes correctly. I only got through drawing the face and gave up completely."
    
    show Cynthia angry at right
    
    c "Of course, it's not gonna turn out like you want it to the first time! What did you expect?"
    
    show Sam embarrassed
    
    s "It should be fairly easy to copy stuff right? I've seen like an entire season of 'JoYo', so what they look like should be ingrained in my mind!"
    
    show Cynthia embarrassed at right
    
    c "Really?"
    
    s "People just make it look too easy."
    
    c "You just expect to draw a huge burly guy just because you watched so much of the anime?"
    
    s "Uh...Yeah."
    
    s "I figured if I just pretty much expose myself to it, eventually I'll be a pro at it."
    
    s "I watch a lot of anime, so eventually I'll be able to draw anime crazily good."
    
    s "I play games, so eventually I'll be able to get out of bronze division."
    
    s "I just surf and read a bunch of articles on the internet, so I can argue the hell out of anyone."
    
    c "Ok, but do you actually do any studying on any of those like study actual art techniques pros use, research standard game strategies, or pay attention in English on how to argue?"
    
    s "Why do we need to do that, when you can just think about it constantly from exposing yourself?"
    
    c "So you expect it to just to come to you?"
    
    s "Eventually it should! Right?"
    
    c "..."
    
    c "Has your mom or anybody ever told you that 'God helps those who help themselves'?"
    
    c "Or even have anyone to discpline you to do stuff?"
    
    show Sam sad
    
    s "You guys have your parents to look to for advice, but I don't even see my mother for a year or so. She wasn't even able to come to my birthday and only talked to her through the phone for 10 minutes."
    
    s "..."
    
    s "Ever since, the divorce."
    
    show Cynthia sad at right
    show Bella sad at left
    
    b "Sam..."
    
    s "..."
    
    c "Just what exactly happened with you and your mom?"
    
    s "..."
    
    with dissolve
    with fade
    
    hide Bella sad at left
    hide Sam sad
    hide Cynthia sad at right
    
    #scene bg cgdonnamoore
    
    s "Things didn't end well the last time with my mom. It's been chilly ever since she divorced my dad."
    
    s "She rarely comes home, like once a year or so for a week, then she's back to work."
    
    s "Yeah, my mom still has Sebastian and Dianna around to look after me and help me get to school, but I just really miss her."
    
    c "Who are they?"
    
    s "Sebastian's my butler and Dianna's the house maid that' been there for me. Sebastian's been always around, but Dianna's new after the divorce."
    
    s "I'm cool with them, but it's just something between me and my mom."
    
    s "She wasn't always working like this. Before she became as big as she is now, she would sacrifice so much of her time from work to go home early."
    
    s "Now, I'm in high school, and she's just constantly working. Things change, I guess."
    
    a "Truly, she trusts you more to be able to handle yourself now."
    
    s "Yeah, I get it, but I just want her to come home every now and then. Not once a year."
    
    s "Look, I love my mom just like a lot of people do, but I hate her with how she's such a workaholic."
    
    c "Well, how about your dad?"
    
    s "He used to be the one watching me at home and taking care of things, and it was great having him around."
    
    s "He's just chill like I am. He does most of his work at home as a computer software engineer, so it's great that he doesn't have problems coming home."
    
    s "I can always hang out, play games, and rely on my dad to help me out with anything."
    
    s "But now, he's not there."
    
    c "What happened to force the divorce?"
    
    s "Dad and I just felt lost with mom."
    
    s "She became huge as a business woman that she's always on trips, meetings, and other stuff that she never comes home."
    
    s "The only excuse she can give me is that she promises to be there the next time."
    
    s "She's only been letting me down."
    
    c "Of course, she must always be busy. People to meet, deals to make, etc."
    
    s "Can't she jusst reschedule them? I know she can. On top of that, she's always 'promising' it, but she doesn't deliver on it."
    
    s "Dad would also be sad that he never sees her anymore that he got paranoid that she would be cheating on her."
    
    s "Mom would get angry that Dad spends too much money on a bunch of stuff. Assume that my mom is very stingy when it comes to money."
    
    s "It became the tipping point when Dad had invested a huge portion of the family savings in the stock market only to have it all lost in the recession."
    
    s "My parents argued and fought endless days and nights about it."
    
    s "Eventually, they actually had a fight."
    
    s "Right away, my mom filed a petition for divorce, but my dad had to take some time to finally make the decision to sign it."
    
    s "Both of them agreed to have Sebastian have temporary custody of me while they had to take this to court."
    
    s "You can tell how well that went for my Dad."
    
    c "The courts have always been biased towards the woman in cases like this. On top of that, she's a business woman. Easily, she was able to pay for a better lawyer."
    
    s "My Dad basically got nothing left. He's only allowed to visit me every now and then, which he does, and he gets a small portion of an alimony."
    
    "..."

    with dissolve
    with fade
    
    scene bg clubroom
    
    show Sam neutral
    
    s "It's...complicated."
    
    show Cynthia talking at right
    
    c "It ain't that complicated. You're not man enough to straight up talk to you mom about it."
    
    c "Eventually, you'll have to settle it."
    
    show Sam embarrassed
    
    s "Ouch, easier said than done. You've never met nor seen how intimidating she is to approach with stuff like that."
    
    show Cynthia neutral at right
    show Bella neutral at left
    
    b "She's right, but we'll get you through it. I promise to help you with it."
    
    b "We'll help you build courage to go stand up to your mom."
    
    show Sam neutral
    
    s "Thanks, Bella. I can be happy with the support."
    
    hide Bella neutral at left
    hide Cynthia neutral at right
    hide Sam neutral
    
    "We spend the rest of the time for the club meeting just making small talk with each other, as we found ourselves unable to find much to talk about aside from school."
    
    "..."
    
#Anime Club: Genre Study Comedy
    
    show Cynthia neutral
    
    c "I swear I'll do anything to help you patch things up with your mom."
    
    show Sam talking at right
    
    s "Thanks, Cynthia. I really can't thank you enough."
    
    show Sam happy at right
    
    s "It's really reassuring that when stuff gets serious, I can count on someone like you to give me advice."
    
    show Cynthia happy
    
    c "Aside from advising on fashion, I love giving relationship advice. It's just right up my alley."
    
    show Cynthia neutral
    show Sam neutral at right
    
    s "Just talking about it to you and having someone listen is enough."
    
    show Cynthia closed
    
    c "Of course!"
    
    show Sam embarrassed at right
    
    s "Really, you don't need to help me or do anything with this. Listening to me be too overly dramatic is enough for me."
    
    show Sam neutral at right
    show Cynthia happy
    
    c "Now come on you big drama king, let's head home."
    
    hide Cynthiaa happy
    
    "And so, Cynthia and I head home casually talking about school and other small talk as if nothing had really happened." 
    
    "It did cheer me up a little to go back into the crazy swing of things between us from my little dramatic moment."
    
    "I really surprised myself with how I really chose to open myself up to others and it made me feel good about venting." 
    
    "Perhaps I should really do that more often and maybe I'll be able to actually patch things up with Mom."
    
    "I don't know how things might change from here on out, I just hope it's for the better."

#End of Chapter 1S
    jump Ch2