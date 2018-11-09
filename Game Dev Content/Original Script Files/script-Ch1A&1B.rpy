#Episode 3: Chapters 1A & 1B
#Chapter 1A: Sam and Ari
label Ch1A:
    
    with dissolve
    with fade
    show Sam neutral at right
    
    s "Hey, Ari! What's going on?"
    
    show Ari closed
        
    a "Just reading some material for my classes. Would you be interested in reading about thermodynamics?"
    
    show Sam talking at right
    
    s "Thermo-what now?"
    
    show Sam neutral at right
    show Ari talking
    
    a "Thermodynamics, studying the transfer of energy through systems."
    
    show Sam talking at right
    show Ari neutral
    
    s "In simple terms that would be..."
    
    show Sam neutral at right
    show Ari talking
    
    a "Looking at how things heat up and cool down."
    
    show Sam talking at right
    show Ari neutral
    
    s "Oh, cool." 
    
    "I pickup something to fiddle with and sit down next to him."
    
    show Sam closed at right
    
    s "Sorry, I like too have something to fiddle with when I sit down sometimes, ignore me."
    
    show Sam neutral at right
    show Ari closed
    
    a "Ah, I understand."
    
    show Sam talking at right
    
    s "For what class is this for?"
    
    show Ari talking
    show Sam neutral at right
    
    a "My dual-credit and college classes."
    
    show Sam talking at right
    show Ari neutral
    
    s "You're already doing college work?"
    
    show Ari closed
    show Sam neutral at right
    
    a "Indeed."
    
    show Ari neutral
    show Sam talking at right
    
    s "Is it easy for you? I really didn't like Chemistry and all that stuff looks complicated."
    
    show Sam neutral at right
    show Ari talking
    
    a "I just have experience in working with this stuff."
    
    show Sam talking at right
    show Ari neutral
    
    s "Experience?"
    
    s "Do you just study all the time?"
    
    show Ari closed
    
    a "Well, yes."
    
    s "Don't tell me that's all that you do! How does a regular day go?"
    
    show Sam neutral at right
    show Ari talking
    
    a "Wake up, prepare breakfast, review material for classes while reading the news during breakfast."
    
    show Ari closed
    
    a "Go to class, do studywork and homework during lunch, more classes."
    
    show Ari talking
    
    a "After school, I'm studying or just reading at home if I'm not needed here with club activities."
    
    show Ari closed
    
    a "Prepare dinner, more studying if I still had more work to do."
    
    show Ari talking
    
    a "Sleep around midnight and wake up at 6 in the morning."
    
    show Ari neutral
    show Sam talking at right
    
    s "So literally, all you do is study."
    
    show Ari closed
    show Sam neutral at right
    
    a "My full-time job currently is being a student."
    
    show Ari talking
    
    a "Hence why I have so much experience. I study a lot."
    
    show Ari neutral
    show Sam talking at right
    
    s "What about breaks? What do you do?"
    
    show Sam neutral at right
    show Ari talking
    
    a "Read, drink tea, listen to music, and draw. Sometimes I play chess."
    
    show Sam talking at right
    show Ari neutral
    
    s "Aren't you miserable with all that studying, though?"
    
    s "I hear people all the time that students just go crazy over college work and you're doing that kind of work in high school!"
    
    show Sam neutral
    
    "I look over his shoulder to peek at the book and I get lost in all the symbols and graphs."
    
    show Sam embarrassed
    
    s "I don't understand any of this."
    
    show Sam closed
    
    s "You're just extremely smart, probably the smartest guy around here, but all you do is study."
    
    show Sam happy
    
    s "Heck, with your smarts, you could just breeze through high school and probably college without having to study or do much."
    
    show Sam talking
    
    s "You really don't need to work that much, but why?"
    
    show Sam neutral
    show Ari talking at right
    
    a "Perhaps, but I put in a lot of effort into anything and everything, because it feels just right."
    
    show Sam talking
    show Ari neutral at right
    
    s "That's cool, but really, you don't need to be such a tryhard."
    
    s "You're already a genius."
    
    show Sam neutral
    show Ari closed at right
    
    a "There is always someone smarter than me. I am just another student like many others."
    
    show Sam talking
    
    s "If you say so, but you're definitely not like a lot of us here."
    
    show Ari sad
    
    a "..."
    
    show Sam sad
    
    "Suddenly his mood changes as he shows a downcast stare at his books."
    
    "I only meant what I said as a compliment, but it seems to have an opposite effect on him. Did I touch on something sensitive to him?"
    
menu:

    "Should I keep talking to Ari?"
    
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
    
    show Ari closed
    
    a "No, Sam. You are fine." 
    
    show Ari sad
    
    a "It just reminded me of something, or rather someone..."
    
    show Ari crying
    
    "He pauses and lets out a sigh. He then stares back at his books, but then closes the book."
    
    show Sam sad at right
    
    s "I can tell something's up. What's on your mind?"
    
    a "Not much really."
    
    s "..."
    
    show Sam angry at right
    
    s "That doesn't sound convincing to me."
    
    show Sam sad at right
    
    s "Come on, man. You can just let it out. I can tell you've definitely got a lot in your mind and I want to help."
    
    s "That and I really don't have a lot going on for myself, so what's up with you?"
    
    show Sam talking at right
    
    s "I genuinely want to know how you're feeling. I don't want to not be able to empathize, and I won't let you just try to brush it off."
    
    show Sam sad at right
    
    s "You can talk to me about anything. I promise I won't tell anyone else."
    
    a "..."
    
    "Ari stays mute for a while, then finally speaks up, but rather quietly."
    
    show Ari closed
    
    a "Okay, I will."
    
    show Sam happy at right
    
    s "There you go. So, let's hear it."
    
    show Ari sad
    
    a "It is just that I have been feeling a little despondent lately. I find myself so unable to focus in my studies. It is quite hard for me to even read my class material."
    
    show Sam talking
    
    s "You seem to be still doing extremely well in class."
    
    show Sam sad at right
    show Ari talking
    
    a "Yes, but that is not the issue. Or is it? I really do not know."
    
    show Ari sad
    
    a "Recently, I have been sacrificing countless hours to studying and work."
    
    show Sam talking at right
    
    s "What do you do as a part-time job?"
    
    show Sam sad at right
    show Ari talking
    
    a "I work as a tutor at a tutor center. I would hold classes after school, then come home around 8 at night to study some more."
    
    show Sam talking at right
    show Ari neutral
    
    s "How many students do you tutor?"
    
    show Sam neutral at right
    show Ari talking
    
    a "I teach around 40 students from elementary and middle school. I work similarly to a teacher, where I have to manually hold lectures, create tests and assignments, grade papers, and more."
    
    show Sam talking at right
    show Ari neutral
    
    s "Dang. Does it sometimes get stressful?"
    
    show Sam sad at right
    show Ari talking
    
    a "It is always stressful. I do this on top of school work and club activities here."
    
    a "I have not been able to sleep a sufficient amount of hours, nor eat enough meals, nor spare any free time."
    
    a "In all, I have feel...drained and faltering in my resolve to work."
    
    show Ari sad
    
    "He stares at the ground with a blank stare similarly to how I first met him."
    
    a "No problems at work, nor at school, nor at home, but just my own personal problem of anxiety and stress."
    
    show Ari crying
    
    a "I even find it hard to get out of bed..."
    
    show Ari closed
    
    a "Sorry to make you have to listen to my rubbish. Please do not worry about me. Perhaps I just need some time alone."
    
    show Sam crying at right
    
    s "Err..."
    
    "It feels extremely wrong to just leave him like this, but I am unsure what to do."
    
    "I look over his books and see a couple of drawings on the side."
    
    show Sam talking at right
    
    s "What are you working on over here?"
    
    show Sam neutral at right
    show Ari talking
    
    a "Huh? Oh, these? I just dabble on drawing anime. Honestly, I am better off just watching anime rather than imitating it."
    
    show Ari neutral
    
    "I look over his sketches and see they are actually well-drawn. He's drawn sketches of familiar anime characters. There's still a lot of stray outlines of figures. He must've been still working on some of these."
    
    "The characters have fair proportions, really detailed features on their faces."
    
    "His style is very close to the usual anime art style with lots of details and exaggerated facial expressions."
    
    show Sam happy at right
    
    s "These are actually really good! Your art style is really close to the mainstream anime art style."
    
    show Ari talking
    
    a "I just sketch in my spare time and imitate. I only draw as a pastime and an amateur."
    
    show Sam embarrassed at right
    
    s "I'm not too good at drawing myself and I've always wanted to learn how to draw like that."
    
    show Sam talking at right
    
    s "Can you teach me how to draw like that?"
    
    show Ari embarrassed
    
    a "I am sorry, what?"
    
    show Sam embarrassed at right
    
    s "I said, can you teach me how to draw similarly to your style?"
    
    a "Why would you want to draw like me? I am only a copycat and a complete amateur in sketching. There are more interesting styles to model after in drawing anime."
    
    a "Also, I probably should go back to working on my classwork."
    
    show Sam neutral at right
    
    s "Well, I want to draw like that anyway just for fun. Also, do you have anything due tomorrow?"
    
    show Ari closed
    
    a "I am working ahead on classwork."
    
    show Ari neutral
    show Sam talking at right
    
    s "How far ahead?"
    
    show Ari closed
    show Sam neutral at right
    
    a "Ä week and a half ahead on the material."
    
    show Ari neutral
    show Sam embarrassed at right
    
    s "How did you even get that far ahead? If tomorrow's not the due date, then it's not the do date. Come on, just take a break and draw for a while. I want to be able to draw like you."
    
    show Sam happy at right
    
    s "We're in an anime club after all. We should be doing anime-related stuff and just relaxing. You're doing that stressful classwork too much. Please?"
    
    show Ari closed
    "Ari closes his textbook and starts to pick up his sketchbook, some papers, and pencils."
    
    a "I suppose. You really want to learn my style? It is not anything too impressive."
    
    show Sam closed at right
    
    s "It's more impressive than the stick figures that I can draw."
    
    show Ari happy
    show Sam neutral at right
    
    a "Alright. I suppose I can show you."
    
    hide Ari happy
    hide Sam neutral at right
    with dissolve
    with fade
    
    #scene bg cgsketching101
    
    a "So, what do you want me to sketch?"
    
    s "Uhhh...How about you sketch me in your style? Draw what I would look like in an anime?"
    
    a "Are you sure?"
    
    s "Yeah. I wanna see your actual style rather than copying a style."
    
    a "Okay, I will see what I can do."
    
    a "First things first, let us lightly draw some basic shapes to act as our skeletons in pencil."
    
    a "A wide circle for the face, straight lines for the spine, the shoulders, arms, and legs."
    
    s "So, stick figures?"
    
    a "Essentially."
    
    s "Okay, what's next?"
    
    a "I prefer to work on the face before the body. There are more details needed for the face, naturally."
    
    a "I would draw crossing lines to estimate the position of the eyes and the nose, then start drawing the outline for the hair style."
    
    "Ari starts to draw my hair. I try to copy and matach what he's drawing, but I can only make a mediocre and shaky copy of his sketch."
    
    a "After the hair, the ears, mouth, and nose to set the stage for the facial expression."
    
    "He quickly draws the facial features with little to no detail to them."
    
    a "I do not bother exaggerating those features, especially the lips for the males. There is more work to be done with the eyes and the eyebrows to express emotions."
    
    a "I draw the eyes just above the horizontal line I drew with equal space between each other the and vertical line. The nose is already drawn on the line to help visualize where the eyes should be."
    
    s "Okay. You made my eyes fairly large."
    
    a "I exaggerate the eyes and eyebrows. In fact, the eyebrows will be drawn over your hair instead of being conventionally covered."
    
    s "Also, how did you draw the eyes like that?"
    
    a "First, draw a crescent and give it a fair amount of thickness like so."
    
    "He draws a crescent and traces over it to thicken the line."
    
    a "Then a thin, slightly diagonal line at the outermost edge of the eye. Not the side closest to the nose."
    
    s "That's just the edges of the eyes, right?"
    
    a "Yes, now we draw the pupil and the iris."
    
    a "Draw an oval with a smaller oval inside. Shade the eye based on where light is shining from. Darkest shades should be from the top of the eye and the pupil. There's also a glare coming from the light and I draw that by clear bubbles like so."
    
    "He shades in the eye, then erases to represent the light glare. Meticulously, he spends a fair amount of time on the details of the eye."
    
    s "Must you really spend so much time on th eyes?"
    
    a "They are windows to one's soul and offer the most amount of expression."
    
    "I try to draw in an eye from what Ari has told me. I finish one eye and it looks fairly similar to what he has, but I forgot to draw in the other eye."
    
    s "Oh, great! It turned out well, now I gotta do it again on the other side."
    
    a "You should have added each detail one by one and kept adding details to both sides, working on them at the same time, instead of focusing on only one."

    s "Yeah, fair enough. That's probably a better idea."
    
    "I erase and redo the eyes, this time working on them simultaneously."
    
    a "Now we finish the details on the face by drawing the eybrows and any other deatils to show expression."
    
    "He draws in other details to finish his sketch of the face."
    
    a "There."
    
    "He finishes drawing my face which resembles quite a lot like me, blond hair, blue eyes, somewhat baby-faced."
    
    s "That's great, but we still have to finish the rest of the body. We spent so much time on the face alone."
    
    a "Of course, but the body is easy to draw. It is just basic clothing and anatomy. The individual features of the body are much larger and less detailed than the pieces of the face such as the eyes and hair."
    
    a "For the body, just follow the outlines for the arms and legs, the torso should match with a portion of the shoulders'length, arms and legs are simple."
    
    "Ari draws the body based on the general and basic features of my clothes. A jacket with plain bottoms and sneakers, some pockets and buttons. Again, he draws stubs for my hands while working on the small details of the clothing."
    
    s "Why do you draw stubs for where my hands should be? You have trouble drawing hands?"
    
    a "Well, yes, but I prefer to draw them last. Other than the face, the hands are hard to draw. I have finished all other details of the body, now I will draw the hands."
    
    "Ari draws a pentagon on the stubs with lines sticking out of it."
    
    s "Oh, so the pentagon is for the palm and the lines are for the fingers."
    
    a "Precisely. Always start with simple shapes, then the details."
    
    "He adds in details and he draws in the hands with ease."
    
    "He adds some details and shading to finish the sketch. I finish my sketch as I tried to copy him, but only ended up with a very rough copy."
    
    a "There we go. The finished sketch."

    s "Neat! Your sketch looks great! Mine, on the other hand, not so much."
    
    a "Urk..."
    
    "Ari looks over at his sketches with anger."
    
    a "No, no no! It is all wrong! The proportions are not matching! The torso is not large enough, the eyes are not identical! There is too much slopiness on those bangs! Shading is all over the place, the pose is not correct, and the creases on the clothing is too random! There is too much asymmetry!"
    
    a "Ugh."
    
    a "This is not good enough."
    
    s "What do you mean? Your sketch looks amazing! It looks a lot like me!"
    
    a "No, it can be better than that, but my hand still disobeys me and draws badly like this."
    
    s "At least you drew something that can pass off as artistic! I still couldn't draw the hands like you told me to and my sketch has one of the arms being too long!"
    
    s "Yours looks great."
    
    s "You're actually really good at drawing and have a really nice art style. I can't believe even you don't like your own works."
    
    "Ari sighs."
    
    a "Of course I do not. I see so many mistakes and ways that this could be improved and perfected."
    
    s "Stop being so much of a perfectionist and at least be a little bit proud that you made something!"
    
    s "I messed up so much, and you're mad that you couldn't get the eyes completely identical?"
    
    "He calms down and takes another look at his work."
    
    a "Of course, I am upset, however..."
    
    a "I will just continue to try, try, try again to perfect it."
    
    s "At least you're having fun drawing right?"
    
    a "I am. Even though I get angry at myself at times for making silly mistakes, I enjoy and find it relaxing to make something and exercise creativity."
    
    s "That's the spirit!"
    
    "Ari takes out more sheets of paper to redraw his sketch. He also sketches portraits of other people, including people that look just like him, which must be his family members."
    
    s "Do you just draw pretty much like this?"
    
    a "Mostly, yes."
    
    s "You could be a professional artist or publish some work online and get some spare money off this. You're really good."
    
    a "No, I usually do not have spare time to do so, nor do I plan to do this professionally. It is not perfect enough to be so."
    
    a "Drawing is a reather calming hobby of mine, aside from the pain of making so many mistakes. I would sketch portraits of friends and family as how I would see them."
    
    a "It makes me very happy relieved when I try to picture and draw my family. I just miss them already after I had to move here."
    
    a "..."
    
    a "Helps me remember them as if they are here right by my side."
    
    "Ari stares at the ground for a while with a longing face."
    
    s "Ari?"
    
    a "Do not mind me. That is how I see sketching as my hobby."
    
    a "Hopefully you got some inspiration and learned something from learning my style, eventhough it is not anything unique nor notable."
    
    with dissolve
    with fade
    
    scene bg clubroom
    #stop music fadeout 1.0
    #play music regularday loop
    
    show Sam happy
    show Ari neutral at right
    
    s "Yeah, I definitely got a good art lesson from you. I'll actually try to get better at drawing 'cause it was fun to draw something."
    
    s "..."
    
    show Sam talking
    
    s "So, do you feel a little better?"
    
    show Sam neutral
    show Ari closed at right
    
    "Ari takes a deep sigh."
    
    show Ari neutral at right
    
    a "Hmmm. I feel...a little better. Quite refreshing to think about drawing for a while instead of changes in enthalpy."
    
    show Ari closed at right
    
    a "Perhaps just what I needed."
    
    show Sam happy
    
    s "Well, that's good news to my ears. In a way, that was a lazy and easy way that helped me help you relax."
    
    show Ari talking at right
    
    a "Huh?"
    
    show Sam embarrassed
    
    s "I didn't know what to do. I really wanted to help you somehow with you feeling a really stressed from school and work, but I guess that was an easy fix."
    
    show Sam sad
    
    s "I know I really couldn't relate 'cause I just don't do that much work and it's not that all stressful for me, but I just wanted to help you feel better in some way I guess."
    
    s "I-"
    
    show Ari closed at right
    
    a "Sam."
    
    s "Yeah?"
    
    show Ari happy at right
    
    a "Thank you. Having a friend like you, is enough."
    
    show Sam happy
    
    "The bell rings signaling the end of the school day and closing of the school."
    
    show Ari talking at right
    
    a "I suppose that is the end of the club meeting and I must head home. I will see you tomorrow."
    
    show Ari neutral at right
    
    a "Thanks again."
    
    "Ari begins to pack up, and I do the same, but at that moment I just wanted to say something."
    
    show Sam talking
    
    s "Look, Ari. Don't push yourself so much and make yourself sad like that, okay?"
    
    show Sam sad
    
    s "You're gonna burn out if all you do is work."
    
    show Sam talking
    
    s "Work hard, play hard."
    
    show Sam closed
    
    s "I try to tell myself that when I get stuck on homework sometimes. I take a break and come back to actually have a better time working on it."
    
    show Sam talking
    
    s "I guess it's also how I keep myself out feeling down."
    
    show Sam sad
    
    s "I just notice that you take school seriously, but it might be too serious."
    
    show Sam crying
    
    s "I mean, we're still just in high school and understand you want to become a doctor, but you're already studying as if you're in med school!"
    
    show Sam talking
    
    s "Are you sure you're okay with that?"
    
    show Ari sad at right
    
    a "..."
    
    show Ari talking at right
    
    a "Studying is my life right now. It just shows how serious I take my work."
    
    show Sam sad
    
    s "Okay, but you're also still just a kid outside of school, right?"
    
    show Ari sad at right
    
    a "..."
    
    show Ari closed at right
    
    a "Even at home, I spend most of my time still studying."
    
    a "Whenever I am not studying, I do chores."
    
    show Ari talking at right
    
    a "I was raised to be productively working all the time."
    
    a "As the eldest between my siblings in my family, I was always tasked with taking care of them and assisting my parents with their work."
    
    a "I suppose I have just been raised that way."
    
    show Ari neutral at right
    show Sam sad
    
    s "To me, that's a very strict life. Do you ever take breaks?"
    
    show Ari closed at right
    
    a "Of course. In my spare time, I do more studying and reading."
    
    show Sam talking
    
    s "Okay, but do you just ever do nothing?"
    
    show Ari talking at right
    
    a "Why would you just spend spare time just to do nothing?"
    
    show Sam neutral
    
    s "That's just the thing."
    
    show Ari crying at right
    
    a "I am afraid I do not understand."
    
    show Sam talking
    
    s "We all need some time to just get away from it all. Just to take some time to not worry about anything, or not do anything, and just be alive."
    
    show Sam neutral
    show Ari talking at right
    
    a "'Be alive? '"
    
    a "We are still alive when we draw breath."
    
    show Ari neutral at right
    show Sam talking
    
    s "I mean to live more than just breathing."
    
    s "You know what I mean, right?"
    
    show Ari surprised at right
    
    a "I am afraid I still, do not understand."
    
    "Ari just gives me a bewildered look."
    
    show Sam embarrassed
    
    s "Er...I don't really know how to say it."
    
    show Sam neutral
    
    s "It's weird though. Most people, especially kids our age are fairly lazy. You are the complete opposite of lazy."
    
    show Sam talking
    
    s "It's great to be a hard worker, but it's also great to be able to relax."
    
    show Sam closed
    
    s "It helps to clear your mind, when way too much is going on sometimes."
    
    show Sam neutral
    
    s "Especially when you're dealing with something heavy like being anxious for a test."
    
    show Ari crying at right
    
    a "..."
    
    show Sam talking
    
    s "You may be an amazing student, but we're all still just kids and we're only human. We all need time to rest."
    
    show Sam happy
    
    s "I don't know. I guess it's justified that you just work really hard, but don't work too hard, okay?"
    
    show Ari neutral at right
    
    a "I suppose."
    
    show Sam neutral
    
    s "This reminds me of a story of another guy just like you. This was during his senior year and the guy was really smart too."
    
    show Sam talking
    
    s "All the classes he took were all dual-credit and college-level classes. At the top of his class, but all he did was study."
    
    s "He wasn't in any clubs, basically no social life, and didn't do anything outside of class other than study."
    
    s "Kept studying in his classes to pass his exams, except he failed all his exams for his classes that year."
    
    show Sam neutral
    show Ari talking at right
    
    a "How was he not able to show up?"
    
    show Sam talking
    show Ari sad at right
    
    s "He pulled constant all-nighters to study before the weeks of his exams."
    
    s "He slept through his alarms and din't make it to his exams on the first couple days of exam week."
    
    s "He was able to take some of them near the end of the week, but he was way too fatigued to think clearly."
    
    show Sam neutral
    show Ari talking at right
    
    a "He was not able to sleep properly?"
    
    show Sam talking
    show Ari sad at right
    
    s "Yeah, but he also went insane a couple weeks before his exams from not getting enough sleep."
    
    s "In fact, he made the unwise decision to go out and work all through the night before the day of the exams studying and contesting in a promo for a gift card to win free food for a year for 'Poultry-Fil-A'."
    
    s "He would spend countless hours of studying, and he would eat nothing, but chicken sandwiches from that fast food place."
    
    show Sam neutral
    show Ari talking at right
    
    a "What happened the morning of his first day of exams?"
    
    show Ari sad at right
    show Sam talking
    
    s "He won the giftcard, but he slept through the exams."
    
    s "His teachers and parents were asking where he was only to find out he had collapsed in the parking lot of the fast food place in his car."
    
    a "He risked getting enough sleep for the exams for a chance to win free fast food for a year?"
    
    s "He had spent all the money on the gift card after the first month."
    
    s "In the end, he had to retake the classes and repeat the year. Unable to graduate with his class for failing the classes."
    
    s "He developed and was diagnosed with insomnia and depression that he had to go to therapy and take medications for it."
    
    s "He definitely regretted all that he did that year."
    
    show Ari crying at right
    show Sam sad
    
    a "..."
    
    show Sam talking
    
    s "I know that sounds really extreme, and that I know you will take care of yourself, so you don't end up going crazy like that, but just remember to take care and take it easy sometimes."
    
    s "Of course, you've got lots of work to do, but don't be afraid to put it off sometimes to get some time off."
    
    show Sam happy
    
    s "Life isn't all work, it should have some fun."
    
    s "'You work to live, not live to work.'"
    
    show Ari neutral at right
    
    a "..."
    
    show Sam sad
    
    s "You don't have to listen to my crap, but I just..."
    
    a "Thank you, Sam."
    
    a "I am grateful for your advice."
    
    show Sam neutral
    
    s "No prob. We all need to remind ourselves things like this sometimes."
    
    show Ari neutral at right
    
    a "Sure."
    
    "Ari begins to leave for the end of the schoolday, but I follow him."
    
    show Sam happy
    
    s "Wanna head back home together? We're going teh same way anyway."
    
    show Ari happy at right
    
    a "Sure."
    
    with dissolve
    with fade
    
    scene bg sidewalk
    
    "I head home while walking with Ari on the way back and continue to carry a conversation with him."
    
    "I try to come up with something else to talk about other than my clumsiness, then I remember the fact that I've joined an anime club."
    
    show Ari neutral
    show Sam talking at right
    
    s "Anyway, aside from teaching me to draw, Bella's mentioned you're here to help use learn Japanese and you've watched a lot of anime, right? I've got to ask you, what kind of anime do you watch and what's your favorite?"
    
    show Ari closed
    show Sam neutral at right
    
    a "I prefer to watch anime with a very strong focus on philosophy, a fair amount of action, and complex plots and themes. Above all, the most important aspect is the pacing and content of each and every episode."
    
    show Ari neutral
    show Sam talking at right
    
    s "You're more on the very serious side, I guess. Also, what do you mean by the pacing and content?"
    
    show Ari talking
    show Sam neutral at right
    
    a "Fillers. I heavily dislike excessive flashbacks and episodes that diverge from the main story arc."
    
    show Ari neutral
    show Sam talking at right
    
    s "Yeah. I get that! I really hate fillers too. Especially with the mainstream shows that have been running for so long, pretty much every week just shows more flashbacks and rejected episodes as 'new episodes'."
    
    s "What's your all-time favorite?"
    
    show Ari closed
    show Sam neutral at right
    
    a "'Fullsteel Alchemist'."
    
    show Ari neutral
    show Sam happy at right
    
    s "That's a really good one! It's got good reasons that it's so highly or even the highest rated anime by a lot of critics. That show is all action, no filler. The characters, the plot, the fight scenes, it's great in all aspects."
    
    show Sam closed at right
    
    s "My all-time favorite is 'Klennad'."
    
    s "It's a really dramatic story, but it's pretty much changed me completely after watching it as the anime that defined the 'Slice of Life' genre. The many insights it gave to life, even though it's romanticized, is beautiful."
    
    show Sam neutral at right
    show Ari closed
    
    a "That is also another story worthy of high praise."
    
    show Ari neutral
    show Sam talking at right
    
    s "You've seen it right?"
    
    show Ari closed
    show Sam neutral at right
    
    a "It is a long time favorite of mine, due to the simplistic, yet deep motifs in the story."
    
    a "Poignant themes, character development, and eloquent storytelling."
    
    a "These are the elements I love to look for in my favorites."
    
    show Ari neutral
    show Sam happy at right
    
    s "Basically, stories that can really drive people to tears."
    
    show Ari closed
    
    a "I suppose that is one way to describe it."
    
    show Sam neutral at right
    
    s "But there's also the opposite side with people who just like to see action instead of the mushy stuff, but some anime just have a perfect balance."
    
    show Sam embarrassed at right
    
    s "I just felt embarrassed not talking to you about anime, even though we did join a club for it, so I guess I just slipped it in at the last minute, but it's great to meet someone with similar interests in it."
    
    show Ari closed
    
    a "I agree, but do not worry about it. We are also here to hopefully grow as friends, so feel free to talk to me about anything."
    
    show Sam happy at right
    
    s "Haha. Feel free to even talk like a bunch of snooty movie critics on anime, even though I'm just a weeb talking like I know my stuff against someone who's actually Japanese."
    
    "Ari and I finally reach his house."
    
    show Ari neutral
    show Sam talking at right
    
    s "Oh, it seems that it's your time to go."
    
    show Sam neutral at right
    show Ari talking
    
    a "It seems so. I must bid farewell for today."
    
    show Sam happy at right
    show Ari neutral
    
    s "It's been fun, but I gotta go too. I wish we had more time to just hang out with you."
    
    show Sam neutral at right
    show Ari talking
    
    a "I will be back tomorrow to meet with you. In fact, I can see you next morning on our way to school. I must go back home to go get ready for work."
    
    show Ari neutral
    show Sam happy at right
    
    s "Yeah, I'll see you tomorrow. Just take care, okay?"
    
    hide Ari neutral at right
    hide Sam neutral
    
    "I wave goodbye to Ari as I head home, anxiously waiting to meet him again the next day. Then I thought to myself, I really am enjoying myself in the club."
    
    "As I spend more time with Ari, he starts to speak up a little more and has become less shy with us. Hopefully I get to know more about him..."
    
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
    
    show Sam sad at right
    
    s "Don't say that, you're interesting."
    
    b "Yeah? In what way?"
    
    show Sam happy at right
    
    s "Err...You can drink milk through your nose!"
    
    show Bella embarrassed
    
    b "Hey! That was one time and it was an accident!"
    
    show Sam happy at right
    
    s "Hehehe..."
    
    show Bella happy
    
    b "Hehe...Okay I'll take it."
    
    show Bella blushing
    
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

    s "How about we start with something simple to talk about? In fact, you wanna just watch some anime and talk about stuff with me like we do? I mean, we are in an anime club now."
    
    show Bella neutral
    
    b "What should we talk about then? Also, what should we watch?"
    
    s "How about we just talk about how school is going? That really ties in together with this new shounen I'm really getting into."
    
    show Bella embarrassed
    
    b "Okay..."
    
    show Bella neutral
    
    b "It's a great thing we have the classroom entirely to ourselves. We can watch on the projector!"
    
    "Bella pulls down the screen and turns on the projector. She sets up the computer to start streaming anime."
    
    show Bella talking
    
    b "What's the new shounen you're talking about?"
    
    show Sam embarrassed at right
    
    s "I know it's a little cheesy and it's a little bit of a rom-com. Here, I'll put it up."
    
    "I type in the name of the show and instantly, Bella recognizes the show."
    
    show Bella embarrassed
    
    b "Oh, I've heard of that one before. I haven't gotten around to watching it, but I guess I'll get to it now. Also, I didn't know you were into rom-coms!"
    
    show Cynthia talking at left
    
    c "Did someone say rom-com?"
    
    "Cynthia chimes in."
    
    show Sam surprised at right
    
    s "Uh, yeah. I'ms pulling up a rom-com for us to watch. Wanna join in?"
    
    show Cynthia closed at left
    
    c "I'd love to! The cheesier the better! I can laugh harder the more pathetic the attempts at comedy are."
    
    show Cynthia neutral at left
    show Sam embarrassed at right
    
    s "As long as you enjoy yourself, I guess. Ari? How about you?"
    
    hide Bella embarrassed
    show Ari talking
    
    a "I like to watch shounen, but not so much of rom-coms; however, I can still appreciate a good one."
    
    s "Well, I'm on the fence with this one. On one end, it's really cheesy and one-dimensional with the plot that it's overly predictable, even with the 'plot twists', but on the other side, it's so stupid and cheesy that it's entertaining to watch."
    
    show Ari neutral
    
    a "As long as you find it entertaining and fun to watch, I will watch it with you."
    
    hide Ari neutral
    show Bella happy
    
    b "I guess we're all for it. Let's start it up."
    
    show Sam talking at right
    
    s "Just to put it out there, at the beginning ther-"
    
    show Bella embarrassed
    
    b "Sam!"
    
    "Bella calls to me."
    
    show Sam embarrassed at right
    
    s "What?"
    
    b "No spoilers! In fact, don't say anything for now. I hate it when you go out and talk about the plot like that."
    
    s "Okay, but sometimes the plot is complex, and-"
    
    b "Just let me figure it out! I like hanging out to watch anime with you, but you are like the worst when it comes to spoilers!"
    
    s "Geez, fine."
    
    b "..."
    
    show Sam closed at right
    
    s "Well, it's just there's a love tri-"
    
    show Bella angry
    
    b "Sam!"
    
    "Bella shouts at me this time."
    
    s "Okay, okay, okay, I'll stop."
    
    show Sam neutral at right
    show Bella neutral
    
    b "..."
    
    s "..."
    
    show Sam closed at right
    
    s "Themaincharacterakatheloserstereotypeasksoutthepopulargirlandsheactuallysaysyesinsteadofshuttinghimdownand-"
    
    show Bella angry
    
    b "You idiot!"
    
    show Sam hurt at right
    show Bella hurt
    "Bella chucks a book at my face knocking me off my seat, but as she threw it she trips over herself."
    
    s "Ow. I got hurt, but you also hurt yourself. Karma."
    
    b "Yeah, yeah. I just had to shut you up."
    
    show Cynthia angry at left
    
    c "Okay, that's great you two are hurting each other, but could you not have any collateral damage?"
    
    show Sam surprised at right
    
    "I look over to see that I knocked over some of Cynthia's paint bottles during my fall. One of them broke open and spilled on the floor."
    
    show Sam crying at right
    
    s "Oh shoot, sorry."
    
    "Cynthia sighs."
    
    c "Good thing there wasn't much paint left in that bottle anyway. Just stop messing around while I clean this up and-"
    
    hide Bella hurt
    show Ari closed
    
    "Ari comes over with wipes and cleaners and quickly cleans up the mess of paint."
    
    a "Do not worry, I have it taken care of. Also, you should also be worried about Bella as she fell over. She is fine despite a small bruise."
    
    hide Ari closed
    show Cynthia talking at left
    show Bella neutral
    show Sam surprised at right
    
    b "No, I'm fine. Anyways, I'm surprised Ari cleaned that up pretty quickly."
    
    c "Why do you even have cleaners with you in the first place is my question."
    
    show Cynthia neutral at left
    show Sam talking at right
    
    s "Enough messing around, we we're getting around to watching anime right?"
    
    show Sam neutral at right
    show Bella talking
    
    b "Oh, right. I'll bring it up."
    
    show Bella neutral
    "Bella brings up the snow and we start watching."
    
    hide Cynthia neutral at left
    hide Bella neutral
    hide Sam neutral at right
    with dissolve
    with fade
    
    "Sure enough, the show plays off using every archetype and generic themes presented in every generic rom-com and shounen."
    
    "We have your generic loser main character who's trying to ask out the most popular girl in school who excels in everything."
    
    "There's the shy and anti-social female counterpart who secretly likes the main character."
    
    "There's his upperclassman friend who's indifferent about any romance even though he already has his own crazy girlfriend."
    
    "Surely enough, the love triangles get convulted and complicated the couples are turned around and mix and matched leaving everyone involved confused."
    
    "The small quirk this shounen has compared to others is that all the characters are awkward to some degree and are gamers, so small remarks about the gaming industry and gaming as a hobby are made."
    
    "Not even once is school actually portrayed as it actually is just like most shounens, but I guess that's the beauty of them all."
    
    "Not having to worry about pop-quizzes, rediculous amounts of projects, assignments, annoying classes we have to take to graduate, studying and preparing for every test only to hurt our self-esteems, so the school gets more funding."
    
    "Instead, there's romance and drama. They worry about who's dating who, who's seeing who, making all kinds of friends, having all kinds of fun, without a care in the world about who's paying for the snacks."
    
    "No, we have to deal with the literal baboons, doing stupid stuff in the hallways, egotistical jerks, and the pretenders."
    
    "Shounens just make high school look like you want to enjoy life, but real life makes us want to throw it away."
    
    show Sam embarrassed at right
    
    s "As much as I loved shounens for their dramatization of how 'great' high school is, I really wish it was actually like that to dull the pain of having to be here."
    
    s "Highschool sucks and it's boring, not crazy and hectic from how much trouble they get into, but crazy and hectic in the sheer amount of stuff we have to do."
    
    show Sam talking at right
    
    s "But, then again..."
    
    s "I could care less about doing my homework, but I do enough to be passing."
    
    show Bella talking
    
    b "What are you talking about? Who says it can't be fun and crazy like that?"
    
    show Sam embarrassed at right
    
    s "It's not fun, but it's crazy in other ways, like people drinking bleach crazy."
    
    show Bella surprised
    
    b "Some people are drinking bleach? They must be out of their minds!"
    
    s "It was some stupid 'challenge' going around school. One guy actually drank bleach and posted it on 'Metube'. He started spitting out blood as he was drinking it."
    
    show Bella embarrassed
    
    b "Oh my god!"
    
    show Ari closed at left
    
    a "How excruciating and unhealthy that must be. If you must know, drinking bleach damages your esophagus and stomach leaving you unable to digest food normally."
    
    a "A surgery must be done to reroute the esophagus to be connected directly to the intestines and the patient will be unable to eat anything that is not partially or fully digested."
    
    show Sam surprised at right
    
    s "What? Ew! Why can't they use their stomach? Couldn't they just puke up or flush out the bleach?"
    
    show Ari talking at left
    
    a "Bleach is a strongly basic, adding bleach to the stomach, which is highly acidic, will neutralize digestive enzymes and damages your stomach tissues."
    
    a "The cells and proteins in the stomach need to be in acidic conditions to function, so when you add a base, you upset the pH balance in your stomach and leave them damaged or dysfunctional."
    
    a "In fact, you should also avoid regurgitating, unless told otherwise, because that will further damage your stomach and esophagus."
    
    a "In addition to rerouting the esophagus, and endoscopy and gastric lavage would be performed."
    
    s "What are those?"
    
    a "The doctors would use a machine to look inside the body to inspect the stomach and would use a vacuum to suck the contents of your stomach out through a tube."
    
    s "Geez, that's crazy. Ari, how and why do you know so much about this?"
    
    show Ari embarrassed at left
    
    a "I just have a strong knowledge of anatomy, medical procedures, and common sense to not drink bleach."
    
    a "Seriously, it is just a waste."
    
    a "The bleach that gentleman drank could have been used to whiten clothes, lighten hair color, clean kitchens, bathrooms, blood stains on a victim's carpet, and-"
    
    show Sam embarrassed at right
    
    s "Wait, what?! What did you say?"
    
    a "Ummm...I said, the bleach could have instead be used to clean clothes, kitchens, bathrooms, and other surfaces."
    
    s "No, the last thing you said before I had to cut you off!"
    
    a "Sodium Hypochlorite and Calcium Hypochlorite are the main active compounds in bleach that serve as strong bleaching agents that kill microbes and strip color-."
    
    s "Now you're outright dodging my question!"
    
    b "How did we get to talking about drinking bleach from watching a shounen anime?"
    
    hide Sam embarrassed at right
    hide Bella embarrassed
    hide Ari embarrassed at left
    
    "It gets a little hectic and crazy that it takes us a while to settle back down and go back to watching anime instead of discussing how bleach strips stuff of color, or whatever Ari's babbling about."
    
    "I go back to talking with Bella and ask her how school has been going for her."
    
    show Sam talking at right
    
    s "So aside from ranting about the overly romanticized portrayal of high school in shounens, how's school and your classes? I honestly don't do my homework most of the time, but I do enough to be passing."
    
    show Sam neutral at right
    show Bella talking
    
    b "Really? I've been struggling with everything in my classes."
    
    show Bella neutral
    
    b "Aside from club activities in this club, student council, and the literature club, I've got a job to keep outside of school, I have to babysit my siblings, and I do all the chores in my house."
    
    show Sam talking at right
    
    s "You still work at that café downtown, right?"
    
    show Sam neutral at right
    show Bella talking
    
    b "Yeah, I don't get a lot of time to study or sleep. By the time I get home, I have to prepare dinner, clean up the house, and take my siblings to sleep." 
    
    b "By the time I get time to myself, it's already 10 PM, and I use about 2-4 hours trying to get homework done."
    
    show Bella neutral
    show Sam sad at right
    
    s "Geez, it's definitely rough for you."
    
    show Bella talking
    
    b "Well, the main reason I got that job was to start saving up for college, because my parents have no money for it."
    
    s "How are you gonna get to college if you can't even get through high school with your sanity?"
    
    show Bella sad
    
    b "Don't worry about it, I'll be able to handle all of this."
    
    show Sam talking at right
    
    s "If you say so, I'm just worried for you."
    
    s "Just why do you do so much? You don't need to."
    
    show Sam sad at right
    show Bella talking
    
    b "You say that, but with just how things are on my end, it's not as easy as that."
    
    show Bella sad
    
    b "For me, I've felt like I have been pressured all my life."
    
    show Bella talking
    
    b "First it was just go to school, so you can get an education."
    
    b "Go to middle school, then high school, so you can get more education."
    
    b "Get good grades in high school, so you can get into a good college."
    
    b "Get a degree in college, so you can get a good job."
    
    b "Go do well in a job, so you can earn good money to start a family and be independent."
    
    b "Start a family, so you can have a child to take after you."
    
    show Sam crying at right
    
    s "Mmm..."
    
    show Bella crying
    
    b "With just how things are..."
    
    show Bella sad
    
    b "It costs even more now to keep a decent house with this poor economy."
    
    show Bella talking
    
    b "It's harder now to get a job because you have to go through so much of college and even more experience."
    
    b "On top of that, it's even harder to get into college."
    
    b "My family doesn't have anything to be able to send me to college, so I'm working on my own to do so."
    
    b "I gotta be in the honors society, or the student government, and a lot of clubs so I can get a leg up and be competitive in applying to college."
    
    show Bella sad
    
    b "Also, balance that with keeping up in hard classes."
    
    b "Even with all that work, I just want to..."
    
    b "..."
    
    show Bella crying
    
    b "Get away from it all."
    
    "Bella pauses with an exasperated sigh."
    
    show Bella sad
    
    b "I try to even couple that with stuff I want to be able to do with my spare time."
    
    b "Like, I do all of that work while slipping in time to watch my shows and stuff."
    
    show Bella embarrassed
    
    b "I don't get sleep, but it's the only way I've found to balance it all."
    
    b "I would say it's worth it. I got to watch the season preimers of a couple of shows reacently."
    
    show Bella happy
    
    b "Season two of 'Three Punch Man' and 'Saint Beats' came out just recently!"
    
    show Sam embarrassed at right
    
    s "You give up sleep for all of that?"
    
    show Sam surprised at right
    
    s "Also, a season two of 'Saint Beats' came out! It's been so long, and I was sure that show was too good to have a second season!"
    
    show Bella happy
    
    b "Yeah! The new season is like the afterstory to the first season."
    
    show Sam happy at right
    
    s "So, does 'Saint' finally meet the main character again? I'm definitely sure after the last scene after the credits!"
    
    b "No spoilers!"
    
    show Sam embarrassed at right
    
    s "Ack! Aside from that, you've been sacrificing sleep just to fit in binge watching anime on top of all your work?"
    
    show Bella talking
    
    b "I don't have enough time to do everything if I don't give up some sleep."
    
    show Bella sad
    
    b "But I need and want to be able to, I just-"
    
    show Sam talking at right
    
    s "Bella."
    
    show Bella talking
    show Sam sad
    
    b "Yes?"
    
    show Sam angry at right
    
    s "Geez, for your own sake, stop trying to do too much. It's just not humanly possible to do all that."
    
    show Sam embarrassed at right
    
    s "Seriously, I even have trouble doing some of my homework in time and I'm in easier classes than you!"
    
    s "You're only one person."
    
    s "You can only do so much."
    
    show Bella talking
    
    b "Don't you see?"
    
    b "You're just so much better off, so you're not as motivated as everyone here to work harder. You just can't relate."
    
    show Bella neutral
    show Sam talking at right
    
    s "No, I definitely can work hard when I need to!"
    
    show Sam sad at right
    show Bella talking
    
    b "You can't relate. You're the only here who doesn't have a job."
    
    b "I live with 4 other siblings and my parents work multiple shifts."
    
    b "I remember Ari works as a tutor aside from studying all the time."
    
    b "Cynthia has a big family, but also works like everyone in her family. If I can recall, she works in a nearby boutique."
    
    b "You're just so much better off while we all have to work. You just were born rich while everyone here just struggles."
    
    b "You..."
    
    "I sigh as a sign of resignation."
    
    show Bella angry
    show Sam sad at right
    
    s "You're right. I can't, but I still don't think everyone should be so obssessed with work."
    
    show Sam talking at right
    
    s "It's like we're all being voluntarily enslaved."
    
    show Sam sad at right
    
    s "Just like my mom, who never comes home from work except for one day a year."
    
    show Bella sad
    
    "Bella becomes silent."
    
    show Sam talking at right
    
    s "I have my own struggles too."
    
    show Sam sad at right
    
    s "..."
    
    show Sam talking at right
    
    s "It's just stupid. I would rather live a simple life rather than an overburdened life with work."
    
    s "Yeah, the money and a good job is nice, but what for?"
    
    s "You know what, I just feel empty from it."
    
    s "I'm here for a fun time, not a long time, but I've yet to figure out what to do with my life."
    
    show Sam sad at right
    show Bella talking
    
    b "You say that, but how are we all gonna earn enough to live? We all aren't as successful as your family is. Not all of us are gonna land a good job that earns enough for us to live on."
    
    b "Even if most of us here get a job, we'll all be living on debt and spend most of our life trying to pay it off."
    
    b "Only to be even deeper in debt to buy a house to live in, a car to go to work, food to eat, and whatever life throws at us."
    
    show Bella sad
    
    b "That's pretty much the story of my oldest sister."
    
    b "She works as a high school teacher in Ohio. She lives in an apartment with a couple other roomates to pay the rent together, but they still barely or don't have enough to pay the rent every month."
    
    show Bella talking
    
    b "No car, it got repo'd, her roomates are just like her, living together, trying to pay off student loans while still having enough to live on."
    
    b "Even though she got so many grants and scholarships to work as a high school teacher, she's still working to pay off her student loans after 5 years now."
    
    show Bella sad
    show Sam talking at right
    
    s "How is she still struggling to pay off student loans? She's working under the department of education, so she should have reduced cots on loans and loan forgiveness right?"
    
    show Sam sasd at right
    show Bella talking
    
    b "She does, but she doesn't get paid enough."
    
    b "It's even worse for her, because she had to retake a couple of classes. She couldn't make it to the classes for a year because she had gotten pregnant."
    
    show Bella sad
    
    b "She should have taken a gap yearinstead, but she insisted on continuing with the classes."
    
    show Bella talking
    
    b "Of course, she had lost her scholarships and benefits for working an education degree for failing that year, so she had to take loans while also working during her studies to eventaully graduate undergrad after 5 years."
    
    b "5 years later, she's still working multiple shifts on top of being a teacher."
    
    show Bella sad
    
    b "My family was fully on board and I was happy she had decided to become a teacher, but now she's stuck with debt for now."
    
    b "Last time I heard from her, it'll take her 15 years of work to pay off those student loans, but she's also taking loans to pay for her apartment and food."
    
    show Bella neutral
    
    b "On the bright side, she says she'll be debt-free by around 30 years of work with all those jobs she does on the side."
    
    show Bella angry
    show Sam talking at right
    
    s "So we're all working in hopes to someday earn enough to live on?"
    
    show Sam sad at right
    
    s "..."
    
    show Sam crying at right
    
    s "I'd rather be dead than live such a miserable life."
    
    show Bella sad
    
    b "Sam..."
    
    s "..."
    
    show Sam happy at right
    
    s "Are you gonna leave 'Hanna' hanging? If you were 'Miss Kobakashi', too overburdened with work, would you really not be able to promise to go watch her perform because of work? "
    
    show Bella crying
    
    b "Awww, dear 'Hanna'. Of course not! She's precious!"
    
    show Sam happy at right
    
    s "Anyways, at least just let me help you to lighten the work load, okay? So we can spend more time watching anime together instead of you being too swamped with work."
    
    s "If you're really that committed to try to do everything possible to spend all four years of high school just working, at least ask for my help."
    
    s "Knowing you, you'll also make me do too much for you and drive me crazy that I'll start losing sleep."
    
    show Bella happy
    
    "Bella smiles."
    
    show Sam neutral at right
    
    b "Okay, I will. Help me out okay?"
    
    s "Right."
    
    with dissolve
    
    show Sam talking at right
    
    s "So, what needs to be done?"
    
    show Bella talking
    show Sam neutral at right
    
    b "I'm going to run for student body president, so I gotta set up for my campaign."
    
    show Sam closed at right
    show Bella neutral
    
    s "Cool, I guess. It's just probably another popularity contest though."
    
    show Bella angry
    
    b "No, it's not! Student body president is a very important position!"
    
    show Sam talking at right
    
    s "What do you exactly do as student body president?"
    
    show Bella talking
    show Sam neutral at right
    
    b "As president, you preside over student council meetings, coordinate and plan student events and pep rallies, and much more!"
    
    show Sam talking at right
    
    s "Sounds way too much hoopla over deciding whether to have confetti or strobe lights in the assembly."
    
    show Sam neutral at right
    show Bella embarrassed
    
    b "Oh, don't say it like that!"
    
    show Sam talking at right
    
    s "I just don't see the hype over planning events where we're forced by the school to attend."
    
    show Sam neutral at right
    show Bella talking
    
    b "We're trying to make them fun for us."
    
    show Sam closed at right
    show Bella neutral
    
    s "In the end, it's still the teachers who have final say in things."
    
    show Bella talking
    show Sam neutral at right
    
    b "We work to negotiate with the teachers to make the events that both the students will like, but also within reason."
    
    show Sam talking at right
    show Bella neutral
    
    s "Alright, then."
    
    show Bella talking
    show Sam neutral at right
    
    b "Speaking of which, I need to go make those posters for the campaign, can you stay here and hold the meeting?"
    
    show Sam talking at right
    show Bella neutral
    
    s "No, I'll go help you out with those."
    
    show Cynthia talking at left
    
    c "I don't have anything to do right now, so I'll go too."
    
    c "I'll lend a hand in what I was suppossed to be here for."
    
    hide Sam neutral at right
    show Cynthia neutral at left
    show Ari talking at right
    
    a "I shall provide aid for your task."
    
    show Ari neutral at right
    show Bella happy
    
    b "Thanks, everyone! I really appreciate your help."
    
    hide Cynthia neutral at left
    hide Bella neutral
    hide Ari neutral at right
    
    with dissolve
    with fade
    
    #scene bg cghardwork
    
    b "Ari, go pick up some copic markers, pens, and other coloring stuff in the closet of the art club."
    
    a "Right."
    
    c "The room should be down the stairwell down the hall."
    
    "Ari and Cynthia take off to go pick up some supplies."
    
    b " Sam, stay here and help me design my posters here."
    
    s "You're asking me to design the poster? I'm not very creative and the most creative thing I've made is the 'S' sign from 6 straight lines."
    
    b "Don't worry, I'm sure we'll come up with something good together. It's better to have two heads than one."
    
    s "If you say so."
    
    "We spend about 10 minutes coming up with a basic idea for a slogan, but we come up with nothing that is worth of a small consideration."
    
    b "We gotta come up with something already!"
    
    s "I think you're trying too hard with coming up with a slogan. It has to be something simple."
    
    b "I don't know."
    
    "Ari and Cynthia return with huge boxes filled with paper, markers, and other art supplies."
    
    a "I hope this will suffice."
    
    c "It's quite a lot, but we definitely have all that we need to make our poster stand out!"
    
    s "Hey, you're back! Anyway, we're trying to come up with a campaign slogan to put on the poster."
    
    a "It seems that you have drawn what appears to be you riding a unicorn on the poster."
    
    c "A unicorn with its own clouds and rainbows, how cute! A little too cute..."
    
    s "Still need something to go with it."
    
    a "How about something simple to accompany it?"
    
    b "Something cute and that comes only in dreams. Something magical."
    
    c "Where can we go with that?"
    
    a "How about something simple, yet common?" 
    
    s "How about, 'Teamwork makes the dream work!'? Oh heck, you could to go with the joke you could promise a free pony or something."
    
    "I chuckle from my absurd remark."
    
    s "Funnily enough, that reminds me of some crazy guy running for president promising free ponies."
    
    b "Sam, that's brilliant!"
    
    s "Really? I don't think it's that good, but it is fairly simple."
    
    a "In simplicity lies complexity."
    
    s "Well now, we've got something."
    
    c "Lots of glitter!"
    
    a "Please do not add so much glitter that it makes one blind."
    
    "Equipped with an idea, copic markers, glue, and glitter, we get to work on our poster. It turns out to be quite 'something'."
    
    b "I love it!"
    
    s "Err...It's...How can I say this..."
    
    a "Cute."
    
    s "It's really girly!"
    
    c "Is that a bad thing?"
    
    s "It stands out for sure."
    
    a "Then, we have reached our objective."
    
    b "It turned out great guys! Let's get the base of the poster copied, decorated, and posted!"
    
    s "Well, she's happy with them, so it's all good."
    
    "We get the posters copied, decorated, laminated, and approved to be posted. It took quite a while to get all of this done that it was already 7PM when we got done."
    
    s "We sure did a number on the color printer and the glitter."
    
    b "Heh, I got a little carried away with the glitter."
    
    c "They all look great with glitter!"
    
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
    
    show Sam talking at left
    
    s "You definitely needed a team to help with that much work! Don't tell me you planned on doing that all by yourself?"
    
    show Sam neutral at left
    show Bella talking
    
    b "Sorry, I didn't want to bother anyone with it."
    
    show Bella neutral
    show Sam talking at left
    
    s "Dude, I'm your best friend! If you need a shoulder, I've got one for you to lean on. I'm here for you." 
    
    s "You're seriously going to hurt yourself from doing too much work."
    
    s "I know you're a little of a workaholic, but there's such as thing as too much work. You can only do so much by yourself at a time!"
    
    show Bella happy
    show Sam neutral at left
    
    b "Thanks, Sam. It means a lot."
    
    "She gives me a bright smile and again it gives we a warm feeling, but this time it feels warmer than before."
    
    b "You're..."
    
    show Bella closed
    
    b "Like a big brother, always looking after me."
    
    show Sam blushing at left
    
    s "Uhh...Yeah, that's cool."
    
    show Bella blushing
    
    b "Umm...I didn't mean anything like that! Oh..."
    
    "The warm situation quickly spun into awkwardness."
    
    s "(Ouch, just got friendzoned.)"
    
    show Bella neutral
    
    b "Anyways, thanks so much for helping me out all this time!  Sorry I haven't been able to do as much on my end other than give you more work to do."
    
    show Sam embarrassed at left
    
    s "No, it's not fine. Even after you spilled the glue, or got the printer jammed a couple times, or broke way too many of the pencil, but still happy to help."
    
    show Bella happy
    
    b "Hehe. You're too nice to me!"
    
    show Sam neutral at left
    
    "We arrive at Bella's house at the end of the exchange."
    
    show Bella neutral
    
    b "I'll see you tommorrow! I'll try to wake up early again!"
    
    show Sam embarrassed at left
    
    s "Yeah's that not likely, I already know you're staying up late again."
    
    show Bella embarrassed
    
    b "Hehe...You know me too well. Anyways, see ya!"
    
    hide Bella embarrassed
    hide Sam embarrassed at left
    
    "We exchange goodbyes for the day and I promptly head home."
    
    "It felt like it was just natural for me to help Bella, but it felt even better today for some reason. I feel as if I'm getting even close than I ever have with Bella."
    
    "Still, I got friendzoned? Or maybe she doesn't know what she really wanted to say."
    
    "Anyways, I got closer to her in some way. It was also nice for Ari and Cynthia to help as well. I probably should also try to help them out. Seeing as they helped me help Bella."
    
    "We'll see what happens and what will happen next..."
    
    #stop music fadeout 1.0
    
#End of Chapter 1B

    jump Ch2