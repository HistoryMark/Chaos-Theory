#Episode 6: Chapters 2B & 2S
label TrueFork2:
    
    with dissolve
    with fade
    show Bella neutral
    show Sam neutral at right
    
    b "Hey, Sam! So, what's up?"
    
    s "Not much."
    
    s "I don't have much to do today, but is it okay if I..."
    
menu:
    "Hang out with you today?":
        jump Ch2B
        
    "Get your help with something?":
        jump Ch2S

#Chapter 2B: Heavy Lifting
label Ch2B:
    
    b "No, I'm really busy. The club festival for the school is coming up and there definitely isn't enough of me or enough of the student government to set everything up."
    
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
    
if Ch1A_active:
    jump Pass2B
    
elif Ch1B_active:
    jump Pass2B
    
elif Ch1C_active:
    jump Pass2B
    
elif Ch1S_active:
    jump Pass2B

else:
    
    "..."
    
menu:
    "Should I Help Bella?"
        
    "Yes":
        jump Ch2BY
            
    "No":
        jump Ch2No
            
#Chapter 2B Accepted
label Ch2BY:

label Pass2B:

    $ Ch2B_active = True
    $ persistent.Ch2BCG_unlocked = True


    with dissolve
    with fade
    
    s "No, actually. I should be asking that to you."
    
    show Bella talking
    
    b "Huh?"
    
    s "Let me help you with all that stuff you're doing for the festival."
    
    s "No. In fact, let me do everything for you."
    
    b "I can't let you do that, I'd be shirking in my duties as class president."
    
    s "Like you can be our class president right now with how exhausted and stressed you are. You won't make very clear decisions and get anything done like that." 
    
    b "No, it's okay-"
    
    s "No, it's not okay. You need some rest right now. I see you're always working before, during, after school that you can't even focus on your school work."
    
    show Bella embarrassed
    
    b "Urk..."
    
    s "Just let me take care of you, just like always."
    
    show Sam talking at right
    
    show Bella happy
    
    b "Awww. Sam, you have to be cheesy like that?"
    
    show Sam embarrassed at right
    
    s "What?"
    
    b "Thanks, anyway."
    
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
    
    s "Getting all the help we can. Student government only consists of like 10 people right? Along with the school staff with their hands full, you guys are still swamped."
    
    s "Let's make it easier on everyone by getting more hands on deck."
    
    s "Many hands make light work."
    
    b "Okay, but where are we gonna get more people to help?"
    
    show Cynthia talking at left
    
    c "Don't you guys know anyone in this school? Geez."
    
    c "I guess I'll have to get you guys some of my people to help you out."
    
    s "Cynthia!"
    
    c "I know people that know people and so forth. If you need people, just ask me."
    
    b "Really? You would do that for us?"
    
    show Cynthia neutral at left
    
    c "Just give an incentive, and I'll work my way with words.~"
    
    b "Hmmm...How about some food and refreshments like pizza and donuts? We'll have plenty at the festival!"
    
    c "Perfect. I'll talk to them."
    
    hide Cynthia neutral at left
    
    s "Well that worked out nicely."
    
    show Ari talking at left
    
    a "If you need coordination and organizing, I can give you a hand in working with everyone."
    
    a "I can serve as you secretary."
    
    b "Really? Thanks so much. That would help me out so much."
    
    a "Just give me a list of what needs to be done and the people I need to meet with. I will organize things on your behalf."
    
    b "Okay, let me just talk with Sam for a while to get him started. Go see my teacher and ask her for details."
    
    hide Ari talking at left
    
    "Ari bows and heads out to go meet with Bella's teacher."
    
    s "There ya go. See? It all worked out."
    
    b "You definitely inspire others."
    
    s "Me? What did I do?"
    
    b "You're so kind in helping that you inspire others to help. That's really cool about you."
    
    show Sam embarrassed at right
    
    s "Come on, let's get started. What do I need to lift?"
    
    hide Sam embarrassed at right
    hide Bella talking
    
    with dissolve
    with fade
    
    #scene bg cgheavylifting
    
    "Bella sends me to start carrying a bunch of props and decorations."
    
    s "Geez these boxes have to weigh at least 30 pounds or so and it's just a bunch of props."
    
    "Cynthia comes back not too long after and has brough a bunch of her classmates and friends over to help."
    
    c "You need reinforcements?"
    
    b "Okay, perfect! We'll have the food and stuff ready later."
    
    c "Come on guys! Let's get to work already."
    
    "Everyone quickly organizes to get to work."
    
    a "I have sent some of the officers to organize workers by role along with some walkie-talkies to help everyone talk to each other to make working with each other easier."
    
    s "Where'd you get the walkie-talkies?"
    
    a "I always come prepared."
    
    s "You seriously have anything for any occasion."
    
    a "Communication is essential for a team to work."
    
    a "Also, I've arranged the posters and flyers for the festival with the other officers as well."
    
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
    
    "Food stands, attractions, showcases, there was a lot prepared for the festival. With a lot of visitors to match the amount of stuff in the festival, I would say it was a huge success."
    
    "Bella, Cynthia, Ari, and I also took time to enjoy the festival ourselves."
    
    "Cynthia spent most of her time in the local orphanage's booth talking to the foster kids, Ari spent most of his time painting with the art club. It left Bella and I just with each other for a while."
    
    b "Hey, Sam can I talk to you for a bit?"
    
    s "Sure."
    
    scene bg hallway
    
    show Bella neutral
    show Sam neutral at right
    
    s "I don't know why you've got to just talk with only me all the time."
    
    b "I don't know, it's just I feel most comfortable with you, like I can talk about anything."
    
    s "Okay."
    
    s "Anyways, you really needed our help today."
    
    s "Don't tell me you were going to do that much work for the festival with just by yourself and only a handful of people from the student government?"
    
    b "It was a lt of work, but I was okay with handling that much work!"
    
    s "You wouldn't get enough done."
    
    s "You see, you need a strong support system in pretty much everything."
    
    b "I guess so, but I just didn't want to bother anyone with pushing some work on to you and the others."
    
    s "I'm only in one club and I don't do much in class other than sleep in class. I have so much free time, it's not a bother at all if you ask for my help."
    
    s "Yeah, I guess I'm kinda lazy, but I kinda mean it when I would be happy to help you out."
    
    s "I really have nothing better to do."
    
    b "You really have nothing to do?"
    
    s "Nope, I've already cleared all the games I bought last week and none of the games being pumped out right now are any good."
    
    s "I literally only sleep and play videogames in class and my teachers could care less."
    
    b "Oh."
    
    s "You're in all these clubs and student government to have a good résume for college, right?"
    
    b "Gotta look good in every possible way on the applications, Sam. That's why I'm doing so much."
    
    s "Let me tell you it doesn't have to be that hard to get into college."
    
    s "You may not have the money yourself, but the way I see it, what really counts when getting into college are two big things."
    
    s "Connections and scores."
    
    b "What?"
    
    s "You can get a lot of jobs, grants, and pretty much a lot of stuff as long as you know the right people."
    
    s "Scores are pretty standard as they only accept people who are actually half-decent at school."
    
    s "But, I'm pretty certain they only take people who can actually pay for it."
    
    s "No use giving service when you can't pay, right?"
    
    s "If you don't have the money yourself, grants and scholarships can come in."
    
    s "You can get a better leverage on people giving you money when they know you."
    
    b "I guess that makes sense, but grades and experience still matters too right?"
    
    s "Yeah, but people are more inclined to help out people they know."
    
    s "Especially when they know who and where their money is getting put to good use."
    
    s "They're investing in your education, so you can do great things."
    
    s "It all ties back to business."
    
    s "My mom stresses this all the time."
    
    s "You gotta know people, so your people can tell their people, their people's people, and so forth."
    
    s "Next thing you know, everyone knows you and knows how good you are."
    
    s "After all, you still gotta know some teachers since you need letters of recommendations from them, so colleges can get a good feel of who you are in the class."
    
    b "Right."
    
    s "So it's cool you're in all these clubs, but you don't need to be in so many to have everyone know your name."
    
    s "You're trying too hard in a sense."
    
    b "You really think so?"
    
    s "Yeah, and it's not just college, but also in getting a job, or applying for anything."
    
    b "What makes you think it works like that for everything? I'm pretty sure college isn't as hard from getting a job."
    
    s "The thing is, people don't see how similar everything can be."
    
    s "Pretty sure college isn't too differnt from high school, except nobody's telling us we have to go to class everyday."
    
    s "You still wake up, go over more material, do homework, all that stuff."
    
    b "Hmm...You're right."
    
    s "Don't stress so much about college. We're still in high school."
    
    s "Not much really ever changes. You'll always be ready when the time comes."
    
    s "After all, I'm still doing decent in class even though I sleep through it. Did the same thing in middle school and did just fine."
    
    s "C's get degrees too, you know?"
    
    s "You probably will do more impressive stuff than I am, though."
    
    b "You're already pretty impressive, Sam."
    
    s "What, why?"
    
    b "For somebody who just plays videogames, sleeps through class, and likes to play around like a kid, you say some pretty off the wall stuff."
    
    s "I just see things differently, but sure."
    
    show Bella happy
    
    b "Well that's pretty cool still."
    
    "Bella just smiles and giggles."
    
    show Sam embarrassed at right
    
    s "Anyways, do you wanna talk about anything else?"
    
    show Sam neutral at right
    
if Ch1B_active:
    b "I'm really thankful for you helping me out today."
    
    s "I'm always looking out for you, so it's become second nature for me now."
    
    b "You're too nice to me, Sam. You really don't need to be doing this much for me."
    
    s "I've always been stuck with you and you've always been a mess."
    
    b "And you're always looking after this mess."
    
    s "Of course."
    
    show Bella embarrassed
    
    b "I'm really tired after today, can you take me home today? I'll text Ari that I'm heading home early."
    
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
    hide Sam neutral at right
    
    "Bella heads home early. Probably had a very long day today. I hang out at the festival with Cynthia and Ari for a while, then we helped out with cleaning up and covered for Bella."
    
    with dissolve
    with fade
    
    scene bg sidewalk
    
    "Today was a long day. It was a lot of work, I guess, but I was really happy to help Bella out in the festival."
    
    "I also head home really exhausted from today. A lot happened for today, so I sympathize with Bella feeling exhausted."
    
    "It was fun working with everyone today, it'll be more fun spending time with everyone, but for today I'm really tired."
    
    "I'm still looking forward to what happens tomorrow..."
    
#End of Chapter 2B
    jump Ch3
    
#Chapter 2S: Writing Together
label Ch2S:
    
    b "Really? Are you sure?"
    
if Ch1A_active:
    jump Pass2S
    
elif Ch1B_active:
    jump Pass2S
    
elif Ch1C_active:
    jump Pass2S
    
elif Ch1S_active:
    jump Pass2S

    
else:
    
    "..."
    
menu:
    "Let Bella help?"
        
    "Yes":
        jump Ch2SY
            
    "No":
        jump Ch2No
            
#Chapter 2S Accepted
label Ch2SY:
    
label Pass2S:

    $ Ch2S_active = True
    $ persistent.Ch2SCG_unlocked = True
    
    show Bella neutral
    show Sam sad at right
    
    s "Yeah, but I don't know how to go about it."
    
    b "Go about what?"
    
    s "I think you're the only one here who gets this."
    
    b "Is it about your mom?"
    
    show Sam crying at right
    
    s "Mmm."
    
    "I nod in agreement."
    
    show Sam talking at right
    
    s "Winter break and Christmas is coming up and I just heard from her that she can't come home for it. Again. After saying she's not gonna make it to thanksgiving."
    
    "I clench my fists."
    
    show Sam angry at right
    
    s "I get she takes work seriously, but I just want her to at least come home every now an then."
    
    "I sigh a little."
    
    show Bella talking
    
    b "She's gotta come home sometime, don't worry."
    
    show Sam sad at right
    
    s "The last time I talked to her, it didn't end pretty."
    
    s "It's been always chilly between me and her, actually."
    
    s "She's been an workaholic for pretty much the entirety of my life."
    
    s "Always just telling me she'll be home soon."
    
    show Bella sad
    
    b "Yeah, you tell me all the time how you hate how your mom almost always never comes home."
    
    "I pause for a second to organize my thoughts."
    
    s "I just don't understand."
    
    show Bella talking
    
    b "Don't understand what?"
    
    show Sam talking at right
    
    s "Why everyone is so obsessed."
    
    b "Obsessed with what?"
    
    show Bella neutral
    
    s "Working so much."
    
    s "It even shows from you guys."
    
    show Sam surprised at right
    
    s "Ari pretty much studies all the time, you're always occupied with club stuff, and I always see Cynthia working on something."
    
    b "Everyone has their reasons for working, for some people, they have to work to even keep living."
    
    show Sam sad at right
    
    s "Okay, but there's also some of us that are completely worked up in working to work."
    
    show Sam talking at right
    
    s "People that say that I 'love' work."
    
    s "Everyone doesn't need to work that much."
    
    show Sam sad at right
    show Bella talking
    
    b "What do you mean by that?"
    
    b "Work gives us something productive to do with our daily life. We gotta work everyday to make ends meet, get things done, do all kinds of good stuff."
    
    b "You know, we work hard in school so we can get a good job, then work a good job for enough money for family."
    
    b "Life's not easy, so we gotta work hard."
    
    show Bella neutral
    show Sam talking at right
    
    s "I get that, but I just don't like how we focus so much on work."
    
    show Sam sad at right
    show Bella angry
    
    b "Are you looking for excuses to be lazy?"
    
    show Bella neutral
    show Sam talking at right
    
    s "No, it's not like that."
    
    s "It's just I'm fairly certain we shouldn't enslave our lives to work."
    
    show Sam closed at right
    
    s "Weird, huh? My mom's a businesswoman so it's her life's work to make money, yet here is her son preaching about being lazy."
    
    show Sam sad at right
    
    s "..."
    
    show Bella talking at right
    
    b "Sam, what are you saying?"
    
    show Sam talking
    show Bella neutral at right
    
    s "I just want life to be all about something else other than working all the time."
    
    s "Instead of just worrying about making money everyday, and more about enjoying it, you know?"
    
    show Bella talking at right
    
    b "Some of us actually like our work, though."
    
    show Sam neutral at right
    show Bella neutral at right
    
    s "That's awesome, but just chilling at home and friends is pretty important too."
    
    show Sam closed at right
    
    "I sigh."
    
    show Sam neutral at right
    
    s "I don't know. Too much stress to do well in school or work annoys me sometimes."
    
    show Bella closed
    
    b "Hmm."
    
    show Bella talking
    
    b "It's what we gotta do now and later in life. We're not kids anymore. In a couple years after we're done with high school we'll be in college or even working."
    
    b "It isn't far down the road, now."
    
    s "I just think that everyone's in too much of a hurry to grow up."
    
    show Sam closed at right
    
    s "Heh. I wish we could be kids for a little longer."
    
    show Bella sad
    
    b "Hmm..."
    
    show Sam happy at right
    
    s "Like be able to enjoy a kiddie meal without guilt when I'm like 20 or something."
    
    show Bella happy
    
    b "Ha!"
    
    "Bella laughs."
    
    b "Of course, you can! Although, the toys aren't as cool as they used to be!"
    
    show Sam embarrassed at right
    
    s "Yeah, the toys we got in the kiddie meals were the best back then."
    
    show Bella talking
    
    b "You know what would be a good thing to do?"
    
    show Sam talking at right
    
    s "What?"
    
    show Sam neutral at right
    show Bella closed
    
    b "Write her a letter."
    
    b "Tell her how you really feel."
    
    show Bella neutral
    show Sam talking at right
    
    s "Really? That seems too simple, also she's just gonna ignore my email in her inbox of millions of other emails."
    
    b "No, like actually write her a letter in pen and paper."
    
    b "All that good stuff you just said, give that to her."
    
    s "I don't see why you think this might work."
    
    b "For one, it could show that you really made an effort in writing it so that it feels more personal."
    
    b "Also, it would be more likely that she reads it as it doesn't get lost like an email in a huge inbox. She might actually have to physically sort and read it."
   
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
    
    with dissolve
    with fade
    
    #scene bg cgwritingtogether
    
    b "Seriously?"
    
    s "I'm much more used to just writing emails now."
    
    b "Fine. Get out a nice pen and a clean sheet of paper. This time, I'm the one helping you."
    
    s "Yeah, by all means."
    
    "I take out a sheet of notebook paper and a pencil."
    
    b "No! You need a clean sheet like printer paper and a really nice pen! It won't look nice like that!"
    
    s "Oh come on."
    
    b "Here. I'll give you what you need. Good thing I keep spare stuff like this."
    
    "Bella takes out a rather fancy calligraphy pen, a blank sheet of paper, and an envelope."
    
    b "Let's get started!"
    
    "I grab the pen and as I was about to write, Bella quickly grabs my hand."
    
    b "What are you doing?"
    
    s "I'm writing! That's what I'm suppossed to do right?"
    
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
    
    "I sign my name at the bottom as meticulously and neatly as I can."
    
    b "You could make art with that."
    
    show Sam sad at right
    
    s "Are you sure you're just saying all of this or is it just to encourage me?"
    
    "Bella is taken aback by my remark."
    
    b "No, really! This really is a nice letter that you wrote. I'm saying this truthfully. I wouldn't lie to you like that. We've known each other for quite a while now! You would know if I told you that what you made is garbage."
    
    s "Yeah, you'd jump on it and roast me all day if it was."
    
    b "Since when are you not confident?"
    
    s "All the time. You on the other hand, are always confident."
    
    b "Don't be like that. You really are awesome, okay? Now be proud about what you made."
    
    b "Also, you're definitely confident in simple stuff like just talking to people and making friends."
    
    b "You've always looked to me as overly confident. That's how you met me after all. Confident enough to talk to a shy girl who didn't have anyone come to her party."
    
    "She remarks about our first meeting again and the nostalgia returns to me."
    
    show Sam neutral at right
    
    "I look over my finished letter, then start to smile."
    
    s "Why did you make me do this again?"
    
    "We both start to giggle."
    
    b "Because, I'm helping you this time. It's for your own good."
    
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
    
    b "Umm...Yeah."
    
    show Ari neutral at left
    
    a "Hello, you two. I trust you two enjoyed yourselves today at our meeting?"
    
    b "Uh..."
    
    s "Yes, Ari. Anyways, what's up?"
    
    a "That's good. I was just about to head home to let you know. I hear the club festival is coming up, so I'll see you guys there."
    
    b "R-right! I'll see you soon Ari!"
    
    a "Take care, everyone!"
    
    hide Ari neutral at left
    
    "Ari bows and heads out the door."
    
    show Cynthia neutral at left
    
    c "You guys sure did 'enjoy' yourselves over here, playing Romeo and Juliet."
    
    s "Oh shut up! It's not like that!"
    
    c "I'm heading out too. I'll see you guys there at the festival too."
    
    b "Oh, okay. I'll see you Thursday, Cynthia!"
    
    show Cynthia happy at left
    
    c "You two are too cute together, you know? For sure you two will be a couple."
    
    s "Huh? Wait what?!"
    
    "Bella only stands embarrassed and mute beside me."
    
    c "Anyways, see you there!"
    
    hide Cynthia happy at left
    
    "Cynthia hums a little song as she heads out the door."
    
    s "I guess I'll you there too, Bella."
    
    b "Umm...Yeah."
    
    "Both of us are too embarrassed to say any more."
    
    hide Bella embarrassed
    hide Sam embarrassed at right
    
    with dissolve
    with fade
    
    scene bg hallway
    
if Ch1S_active:
    "It's the day of the festival, and I get to the festival first where we agreed to meet. I am the last to arrive."
    
    show Cynthia neutral
    show Ari neutral at right
    show Bella neutral at left
    
    b "Hey, Sam!"
    
    s "Hey guys. Looks like we're all here."
    
    c "Usually I'm the one who's fashionably late, but you're the one who's late. It's not polite to keep ladies waiting."
    
    b "Well, arriving early or not, there's still plenty of food and fun for us to enjoy!"
    
    a "Indeed. Shall we enter?"
    
    s "Yeah, let's go in."
    
    with dissolve
    with fade
    
    hide Cynthia neutral
    hide Ari neutral at right
    hide Bella neutral at left
    
    scene bg schoolyard
    
    "We go in and enjoy the festival food and games. Most of my time there consisted of Bella and Cynthia dragging me here and there to try out something."
    
    show Cynthia neutral at left
    show Sam neutral
    
    c "Hey, Sam! Come over and dance with me!"
    
    "I spend a couple minutes dancing with Cynthia and then Bella takes me to go check out some of the food."

    hide Cynthia neutral at left
    show Bella neutral at right
    
    b "Sam, come and check out the snacks from the Greek Club!"
    
    "Bella grabs my hand to go try the pita chips and dip at the Greek Club's stand."
    
    b "These are great!"
    
    s "Yeah, pass me some of that hummus!"
    
    "Both of us enjoy some snacks for a while, but Bella is still energized and wants to try more things."
    
    b "Come on, Sam! Let's go check out the fencing club next! They're going to have a live exhibition match!"
    
    "I space out for a while, but eventually respond."
    
    show Sam talking
    
    s "Huh? What? Oh."
    
    s "Actually, you go on ahead, I'll join you later."
    
    b "Okay."
    
    hide Bella neutral at right
    
    show Sam sad
    
    "I just space out for a few minutes thinking about countless uncertainties, then Ari comes over to talk to me."
    
    show Ari neutral at left
    
    a "Ari, can I talk to you personally outside for a bit?"
    
    show Sam talking
    
    s "Huh?"
    
    "I turn and see Ari."
    
    show Sam neutral
    
    s "Sure."
    
    hide Sam embarrassed
    
    with dissolve
    with fade
    
    scene bg hallway
    
    "Ari and I both head into the hallway."
    
    show Sam sad
    show Ari neutral at right
    
    s "Hey, Ari. What's going on with you?"
    
    a "Not much, I just wanted to talk to you personally and check in with you."
    
    "Ari takes a seat beside me and we just sit down to talk."
    
    a "These past few months went by quickly, do you agree?"
    
    s "Yeah, but a lot happened. I can't even remember half of the crazy stuff that we did."
    
    a "Well, I agree. I have a hard time listing them as well."
    
    a "Tell me, do you like how your first semester of high school has gone so far?"
    
    s "It wasn't how I wanted it to go, but it was a fun semester. I met you guys all because Bella dragging me here to start a club."
    
    s "Most likely, I was just gonna do nothing in school and just play my videogames, but you guys kinda made me enjoy being here."
    
    show Ari happy at right
    
    a "That is good to hear."
    
    "I think of all that has happened in the past semester and recount some moments."
    
    s "I gotta thank you too, Ari. You've been looking out for me when I get in trouble, helping me with school, basically helping me with everything here. You're a good wingman!"
    
    a "I suppose that is a substitute for the word 'companion'. Thank you, Sam. I am just glad to help."
    
    show Ari neutral at right
    
    "I let out a deep sigh and stare at the ceiling."
    
    a "You enjoy your time here, but I can sense you still have your own conflicts."
    
    s "I don't know. I should be happy with how great everything is going in school, but I still feel anxious."
    
    a "Well, no matter what gives you stress, I will be here at your aid. Do not be afraid to rely on me."

    show Sam happy
    
    s "It's great to have you, man."
    
    hide Ari neutral at right
    hide Sam happy
    
    "Ari and I go back in and enjoy the festival with Bella and Cynthia and really have a good time. It really cheered me up which will help me get through with one of the most stressful parts of the year, finals."
    
    "With Ari, Cynthia, and Bella at my side, hopefully I'll easily get through this..."
    
else:
    
    "A few days later, the club festival finally takes place and the four of us happily enjoyed the festival."
    
    "I've been spending a lot of time with Bella lately that I spend most of my time in the festival with her."
    
    "Perhaps I should spend some of my time with the others, because I feel bad when someone does get left out..."

#End of Chapter 2S
    jump Ch3