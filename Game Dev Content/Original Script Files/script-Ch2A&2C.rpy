#Episode 7: Chapters 2A & 2C
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
    
if Ch1A_active:
    jump Pass2A
    
elif Ch1B_active:
    jump Pass2A
    
elif Ch1C_active:
    jump Pass2A
    
elif Ch1S_active:
    jump Pass2A

else:
    
    "..."
    
menu:
    "Ask for Ari's help?"
        
    "Yes":
        jump Ch2AY
            
    "No":
        jump Ch2No
            
#Chapter 2A Accepted
label Ch2AY:
    
label Pass2A:

    $ Ch2A_active = True
    $ persistent.Ch2ACG_unlocked = True
    
    a "Alright, let us begin."
    
    "With pen and pencil ready, for once I'm ready to learn something in school."
    
    a "So, what do you need help with?"
    
    s "So from my Algebra class, we're working with some weird formula. You know what, I'll just show you."
    
    "I take out my phone and look up material from my class."
    
    a "You do not have your own notes or your textbook from class?"
    
    s "I don't take notes or bring my books at all. I just don't understand what they're saying."
    
    s "...Here."
    
    a "Ah, alright. I will derive it for you so you can understand it."
    
    s "Derive? What does that mean? Also, that looks complicated with all those letters and symbols."
    
    a "I will show you where it comes from so it does not look like a foreign language to you."
    
    a "Take out a pencil and a sheet of paper and follow my lead."
    
    "I promptly do so."
    
    hide Ari neutral
    
    with dissolve
    with fade
    
    #scene bg cgnaturalteacher
    
    a "It is very simple. I will try to explain every aspect of it."
    
    "Ari goes through the material from class and takes notes based on it, explaining every single step."
    
    "I feel completely lost in what he's trying to show me until I begin to realize he's explaining everything similarly."
    
    a "Do you see the pattern?"
    
    s "Mhm..."
    
    "I actively try to take notes of everything he's said so far in explaining this."
    
    a "Math has a lot of patterns, the more you see them, the easier it is to think through it. Similarly to how you would solve some puzzles in your games right?"
    
    s "Like going through every 'water level'?"
    
    a "Uh...Sure. The same idea is there."
    
    a "It is mostly logical. Every step should make sense to you from start to finish."
    
    "I look over my notes on what' he's done so far and it still doesn't look like anything what the teacher or the notes on my phone look like."
    
    s "Right now, what you have looks nothing like what the online notes do."
    
    a "Well, what have we done so far?"
    
    s "Just really basic stuff like simplifying the numbers and stuff."
    
    a "It makes sense to make it look easier to solve before actually trying to solve it right?"
    
    s "Oh, okay. How does it make it easier to solve?"
    
    a "Clean it up because there's a common denominator, and..."
    
    "Ari continues to work through the problem and in just a couple of steps, he's already solved the problem, remarkably less steps than the other notes."
    
    s "What the heck? That was like magic!"
    
    a "Not magic, just looking at the problems differently."
    
    s "You got any more shortcuts like that you can show me?"
    
    a "Certainly."
    
    "Ari continues to teach me a bunch of shortcuts."
    
    s "That's pretty neat, but you could have just shown me that formula instead of going through all of that."
    
    a "When you understand where everything comes from, you can understand how to solve any problem."
    
    a "Of course, you do not need to know all of that yet, but I just want you to know why it works. Do you understand?"
    
    "I go over my notes to go through the entire lesson from Ari to try to completely understand what he means."
    
    "I start to see the patterns and the lesson becomes a revelation."
    
    s "Huh. That does make sense."
        
    s "Yeah...I'm actually getting this."
    
    scene bg clubroom
    show Sam talking
    show Ari neutral at right
    
    s "So what are we really gonna use this for? Knowing all these numbers and stuff?"
    
    a "These types of calculations can be used in various applications." 
    
    a "Maximizing profits and lowering cost in businesses, tracking changes in temperature outside to predict next day's forecast, checking the arc of a projectile when fired like firing a cannon, and other applications."
    
    s "That seems like a stretch. Do have to do crazy calculations like that all the time? Doesn't computers do that for us already?"
    
    a "You just have to know when, where, and how to use it. Calculators and machines do computations for us, but what use is it when we do not know which function to use?"
    
    a "Anyways, you are just concerned about passing midterms, so focus on that as a driving force to study."
    
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
    
    a "Yes. It is more effective because you improve more when you practice more often. Right?"
    
    s "Alright, then."
    
    a "Lastly, work smarter, not harder. Do the easy stuff first, then the hard stuff. For some people, it works better the other way. Figure out what works best for you."
    
    s "Yeah, you're definitely better at school than I am, but I will try all those things to get better."
    
    a "It is just a matter of work ethic and discipline. Work is what you make of it."
    
    s "I guess I could learn a thing or two from you and Bella."
    
    show Ari neutral at right
    
    a "You are only a freshman, so you have plenty of time to learn how to work. You will improve over time."
    
    s "Well, I hope so because I'll need to."
    
    with dissolve
    
    "I continue to work out problems and still find all the material really hard, I'm kinda demoralized from how it's been going in math class."
    
    "I look over my notes with frustration and repeatedly look over them, only to be frustrated even more."
    
    show Sam talking
    
    s "I'm getting better at this, but it won't be enough in time."
    
    a "Are you worried about your progress?"
        
    s "Yeah, I'm kinda worried about midterms coming up. I keep almost passing the tests so far in math and I still don't get everything."
    
    s "I'm actually freaking out."
    
    a "You are very anxious at the tests?"
    
    s "I know it's kinda overreacting sometimes, but literally everyone in the class freaks out everytime at the beginning of every test."
    
    a "What do you mean?"
    
    s "Come on, you are not freaked out before a test?"
    
    a "A test is just another grade. In addition, all the material in the test is content you should have learned or mastered at that point."
    
    a "It will not be the end of the world if you fail."
    
    show Sam neutral
    
    s "Well, in my case I've been failing all this time, so I think it's justified."
    
    show Ari angry at right
    
    a "That right there."
    
    s "What?"
    
    a "That is why a lot of students do not realize."
    
    show Ari talking at right
    
    a "A self-fulfilling prophecy."
    
    s "Prophecy?"
    
    a "I think, therefore, I am."
    
    a "A lot of students here still struggle with studying, but they struggle even more with having a positive mindset."
    
    a "It is a vicious cycle."
    
    a "Students are given material, they procrastinate, do absolutely horrible on the test, then think the material is overly difficult."
    
    a "Repeat."
    
    a "Hence, their poor performance continues and everyone freaks out in the beginning of the tests thinking of never doing well."
    
    s "Well, yeah. School isn't for everyone, Ari. A lot of people are just stupid, like me."
    
    a "I do not think we are all just stupid. I believe that everyone here has potential to do well. It is just the lack of willpower."
    
    s "Yeah, okay. We don't take school as seriously as you do, but what if you still tried your best and still fail horribly?"
    
    a "Have you ever thought there was something you were doing wrong and not the system?"
    
    a "There are faults such as the teacher not being as experienced to teach or you are just unable to understand it their way, but there is clearly stopping you from learning it, right?"
    
    a "The biggest thing everyone usually does wrong is think that everything is pass or fail."
    
    a "Either you have it, or you do not."
    
    a "Success is not like that."
    
    a "It took me countless hours to learn English. I had trouble putting sentences together and pronouncing soft and hard consonants for the longest time."
    
    a "It does not matter that you fail." 
    
    a "In fact you will fail multiple times. We make mistakes as humans."
    
    a "What matters is that you keep trying and keep thinking that the next time you try, you will get it and keep moving forward."
    
    a "Success is only possible from many failures."
    
    a "So stop freaking out and thinking you will fail because you indeed will fail if you think that way and be stuck failing."
    
    a "Be dilligent in your work and always strive to do your best, then you will be the best."
    
    a "Believe that you will do well regardless of the grade because at the end of the day, there will be only one person responsible for how you did on that test."
    
    a "It is yourself."
    
    a "If you did your best, then what else is there to say?"
    
    a "If not, then try harder."
    
    s "You say that, but I don't believe that you say you have to fail many times to succeed. You've always succeeded."
    
    s "Plus, some teachers are just really horrible at teaching and some stuff is just too hard and we're just not prepared well enough for the material."
    
    a "These are not my words, rather my mother's."
    
    a "I will tell you her story from this."
    
    show Ari sad at right
    
    a "She works as a pediatrician in a hospital in Tokyo."
    
    s "That's great, she's a doctor for kids right?"
    
    a "Right. It was not easy for her to get there."
    
    a "To be a licensed doctor of any specialty you have to pass a board examination run by the government. Pass rates range from about 40 percent to only 5 percent on those exams."
    
    a "My mother took the same pediatry license examination test 3 times and had failed all three attempts."
    
    a "She was constantly judged by her peers and classmates just because my family comes from a very poor background."
    
    a "Some told her she was not cut out to be a doctor, or that she does not deserve to be there."
    
    a "Just because she was a poor woman."
    
    a "Well, funnily enough, there was a huge scandal over the test results from the examination and it turns out from her last attempt of the exam, she actually passed."
    
    a "Not only that, she was in the highest percentile in the exam."
    
    show Sam talking
    
    s "What?!"
    
    a "More on her background, she was actually homeschooled by herself, went through college and medical school solely on scholarships."
    
    s "No internet, no computers, no nothing?"
    
    show Sam neutral
    
    a "Not even a teacher, she taught herself from borrowing books from the local library, passed a college entrance exam by herself before she was 18."
    
    a "Graduated college with a degree, graduated medical school, and became a doctor."
    
    a "After all of that, she just tells me this:"
    
    a "It is only over when you give up."
    
    a "She was a much stronger student than I am."
    
    a "Sorry for that overly long story and lecture."
    
    a "I just find it funny the overreactions from just one test. We have so many chances here as high school students and we have so much freedom to change or start over."
    
    a "We should not be so afraid to fail, because we need to fail to succeed."
    
    "Ari sighs."
    
    show Ari crying at right
    
    a "That is what she always told me whenever I felt like things were not going well."
    
    show Sam sad
    
    s "Uh, Ari?"
    
    "I notice Ari starts crying a little."
    
    s "Are you okay?"
    
    a "..."
    
    a "Ah, I am quite alright."
    
    s "Something happen?"
    
    a "I...miss my mother."
    
    a "...I miss my family."
    
    a "It has been so long since I have seen them."
    
    a "Not that I do not like my aunt, in fact I love her despite not seeing her much."
    
    "Ari wipes his tears."
    
    show Ari neutral at right
    
    "The bell rings from the classroom."
    
    a "Well, that is all the time we have for today's club meeting and lesson. Hopefully you learned something."
    
    s "Yeah, definitely learned how bad I am at being a student, that's for sure."
    
    s "Also, I hope you see your family soon. I bet things must be complicated if you can't see them much."
    
    a "Thank you."
    
    a "A master of something was once a struggling student like you. You have to start from somewhere."
    
    s "Mhm. Can I ask you to tutor me again on other stuff? You seem to know a lot about, pretty much everything."
    
    a "Well, I do not even speak Spanish, but I was able to teach you because I know French."
    
    s "Seriously?"
    
    a "Anyways, I would be glad to tutor you on anything I can. Just meet with me next time I see you in the club. I need to go on ahead."
    
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
    
    b "He won first in the academic state contest last week and he's going on to the national contests."
    
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
    
    b "I don't know, but I have a feeling something happened to him personally, maybe his family or something, because he just tried to dodge pretty much all the questions I gave him."
    
    b "He said he was happy that he did really well in the contests, but he didn't sound too happy."
       
    b "Just an empty smile."
    
    s "How could you tell?"
    
    b "Sometimes I felt the same way too."
    
    s "..."
    
    "A moment of silence passes."
    
    b "I saw you talk to Ari first on the first day of the club. He just sat in the corner with a sad look and kept to himself. He wouldn't even talk to me or Cynthia when I tried to approach."
    
    b "However, when you talked to him and cheered him up."
    
    b "I want to be able to help Ari, but I don't know too much of what I could do."
    
    b "Kinda pathetic that the club president can't even help her member."
    
    b "I feel really guilty to ask this of you, but please just help him."
    
    s "..."
    
    show Sam talking
    
    s "Of course. He's my friend."
    
    s "I understand that you feel bad, but you shouldn't. It's hard knowing what to do to help. In fact, I'm happy you asked me for help."
    
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
        
    "We head home and just casually talk about how our day went. I spent most of my time with Ari today, that I feel out of touch when I ask Bella and Cynthia how their day went."
    
#End of Chapter 2A
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
    
if Ch1A_active:
    jump Pass2C
    
elif Ch1B_active:
    jump Pass2C
    
elif Ch1C_active:
    jump Pass2C
    
elif Ch1S_active:
    jump Pass2C
    
else:
    
    "..."
    
menu:
    "Read with Cynthia?"
        
    "Yes":
        jump Ch2CY
            
    "No":
        jump Ch2No

#Chapter 2C Accepted
label Ch2CY:
    
label Pass2C:

    $ Ch2C_active = True
    $ persistent.Ch2CCG_unlocked = True

    c "Cool. Just pull up a chair."
    
    s "Okay."
    
    "I pull up a chair from a nearby desk and sit next to Cynthia."
    
    c "No, come closer. You won't get a good look of the pages from there."
    
    "She pulls me closer to her to the point where my shoulders are directly touching hers."
    
    c "There we go.~"
    
    c "Don't worry I won't bite, but no guarantees."
    
    s "Right. So what kind of book are we reading?"
    
    c "It's a basic romance novel. Really it's very cliche in how it pitches the story, but for some reason it's really popular."
    
    c "What kinds of books do you usually read?"
    
    "I was always just watching the movie version of the book fully knowing it leaves parts out, and the only 'books' that I usually read are just comics and manga."
    
    show Sam embarrassed at right
    
    "I quietly answer to hide my shame."
    
    s "Comics and manga."
    
    c "That's cool. I don't read much of those but I've read some manga before. Mostly just drama and romance."
    
    show Sam neutral at right
    
    s "Romance and drama is really your favorite types of stories?"
    
    show Cynthia happy
    
    c "Clearly. I think I watch too many soap operas and dramatic movies, so my preference in reading is pretty much the same."
    
    s "It's kinda the same way with me. I like to watch action movies so superhero comics and manga are a close favorite."
    
    c "Well, maybe I can change your mind and make you read other stuff."
    
    s "This better not be really overdramatic stuff. I feel like we've seen it all already."
    
    c "It's kinda like that at times, but yeah I understand what you mean."
    
    show Cynthia talking
    
    c "A lot of the books we read in English class nowadays have stories about dystopias and apocalypses."
    
    c "There's one book about teenagers having to fight to the death on live TV while the rest of the country starves."
    
    c "Another book where kids and teens alike are trained to fight wars from birth."
    
    c "There's a movie coming out soon based on a novel where books are banned and the government watches everyone's every move."
    
    c "Of course, stories about nuclear apocalypse are still popular with the debates in the news about other countries threatening to nuke us."
    
    show Cynthia sad
    show Sam sad at right
    
    "Cynthia sighs."
    
    c "It just doesn't even stop there."
    
    c "So far, everything I've heard about school, work, the country, and pretty much everything about life are just cruel."
    
    c "The fact that some of us will be working until we're 70 to have enough money to support ourselves during retirement."
    
    s "How about the fact that only about third of us is ready or will survive college."
    
    c "We have some of the best universities here in the US, but some of the worst public schools in the developed world."
    
    s "Also, more people are becoming obese and healthcare getting more expensive."
    
    c "Those in part with all the stuff we were fed when we were kids."
    
    s "High school definitely not like any shounen I've read in manga."
    
    c "Being poor is sometimes helpless and the poor get poorer and the rich get richer."
    
    show Sam surprised
    
    s "Really? Isn't America supposed to be the land of opportunity where if you work your butt off, you can also move up?"
    
    show Cynthia angry at right
    
    c "Go tell that to my mom who still has to pay off tons of bills with her student loans."
    
    show Sam sad
    
    s "Geez."
    
    show Cynthia sad at right
    
    c "You know, a lot of the stuff we read, see, or hear about life is just really depressing."
    
    s "We don't read anything fun and exciting in English!"
    
    c "I like romance and drama novels because it just revolves around one big happy and sometimes sad theme."
    
    s "What?"
    
    c "Love."
    
    show Sam neutral at right
    show Cynthia neutral
    
    s "Oh. I was expecting some huge answer or lecture like you'd hear in English. You're really into books and stuff."
    
    c " In a dark and scary world the news feeds us, we just need some love to cheer us up."
    
    c "Yeah, it's kinda girly that I'm really into soap operas and pretty much nothing else, but that's my reason for it."
    
    c "We constantly see just violence and grim futures in TV and movies that I've just come to really appreciate romance."
    
    s "..."
    
    s "Okay, then I'm sold. You didn't need an entire speech on why you really like romance for me to join you, but hey, at least I've come to understand why you like it so much."
    
    c "If you don't appreciate it, you don't enjoy it as much, so I did need to give you a speech."
    
    s "Geez, okay."
    
    c "I promise it's not that bad. You just need to get over the drama every now and then."
    
    c "Let's just start at the beginning so you understand the plot so you can get over the cheesy and overly dramatic scenes."
        
    hide Cynthia neutral
    hide Sam neutral at right
    
    with dissolve
    with fade
    
    #scene bg cgpagebypage
    
    c "Here."
    
    "Cynthia hands me a set of earbuds."
    
    s "What's the earbuds for?"
    
    c "There's an audiobook version of the novel, we can listen to a narrator read the story to us while we read the pages."
    
    c "That way you can really get a feel for the story."
    
    s "Ah, okay."
    
    "Cynthia grabs her own set of headphones and we start listening to the story together."
    
    "..."
    
    c "It's a slow pace at first."
    
    s "That's only the first part."
    
    c "Lots of books do start slow, but I like stories that jump right into the action."
    
    c "Character exposition is nice, but I like it when we don't know much at first to begin with and learn about them more as the book progresses."
    
    s "I guess that's fair. Let's move on to the next chapter and see if it does move on faster."
    
    "We continue reading..."
    
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
    
    "I take off the headphones."
    
    s "Are they any good usually? Anyway, here's your headphones back."
    
    c "Rarely, most of them are garbage."
    
    s "Oh."
    
    c "Overall, a really exciting book even though it's a really cliché love triangle for a plot."
    
    c "However, for such a simple plot, I've never read such a genuine and dramatic story."
    
    s "Really? That's how you would rate the book? A lot of stuff just happened so quickly in the book."
    
    c "I've already read a lot of these types of books before and they like to write a lot like this. Sometimes they're all the same. This book, however, was really good in spite of all that."
    
    s "Hmm..."
    
    c "It's weird."
    
    s "What?"
    
    c "This type of story sounds really familiar. I don't know from where I've seen something like this, but I recognize it."
    
    c "Except the story it reminds me of, is pretty amateurish and not too good from how simple-minded it was."
    
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
    
    s "No I'm not!"
    
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
    
    show Sam neutral
    show Ari neutral at right
    show Cynthia neutral at left
    
    a "Alright. So what is your announcement that should be brought to our attention?"
    
    show Bella talking at left
    
    b "The student government is hosting a club festival and all of the school clubs will be there. It goes down this Thursday since it's taking us quite a while to get everything set up."
    
    show Bella neutral at left
    
    b "I still have to be at the festival, so will you guys go..." 
    
    b "To the festival with me?"
    
    s "Sure!"
    
    show Cynthia neutral at right
    
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
    
    s "I'll head out too."
    
    b "Okay, I'll come with you."
    
    s "Come on. Let's head home."
    
    "Bella and I head home for the day."
    
    hide Sam neutral
    hide Bella neutral at left
    
    with dissolve
    with fade
    
    scene bg schoolyard
    
if Ch1C_active:
    
    "A few days later, the club festival finally takes place and the girls and I happily enjoyed the festival."
    
    "Ari actually couldn't make it to the festival since he got sick with a cold and stayed home for the day leaving me with the girls."
    
    "I could tell there was some sort of rivalry forming between them as continously both of them keep tugging at me for attention."
    
    "The three of us promptly head home after the festival's end and I walk the two of them back home leaving me completely exhausted."
    
    "Perhaps I now understand why Cynthia stares at me with such a daze now."
    
    "Does she have a crush on me and sees Bella as a huge rival?"
    
    "Now it sounds like the love triangle crisis in the book Cynthia and I read together..."
    
    "Maybe. Or it's just another mind game of hers."
    
    "I'll admit I feel really close with Bella as a close friend, but I'm starting to be also close to Cynthia that I'm left confused."
    
    "Perhaps I should spend more time with Cynthia..."
    
else:
    
    "A few days later, the club festival finally takes place and the four of us happily enjoyed the festival."
    
    "I've been spending a lot of time with Cynthia lately that I spend most of my time in the festival with her."
    
    "Perhaps I should spend some of my time with the others, because I feel bad when someone does get left out..."
    
#End of Chapter 2C
    jump Ch3