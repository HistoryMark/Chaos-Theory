# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #image bg schoolyard = "schoolyard.png"
    scene bg schoolyard

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "It was an ordinary day, in this ordinarily boring life as a high school student..."
    
    #image Bella neutral = "Bella_neutral.png"
    show Bella neutral
    
    sfs "Come on, Sam! We'll be late for our first day of high school!"
    
    image Sam neutral = "Sam_neutral.png"
    show Sam neutral at right
    
    s "Well, we're already going to be late with that train coming by, so why bother rushing?"
    
    sfs "What train?"
    
    "The lights flash and the gates lower on the railroad crossing as the horn of the train can be heard."
    
    b "Oh, really? Just our luck!"
    
    s "You seem really out of it today, Bella. Are you getting enough sleep?"
    
    b "Er..Okay, so I only slept 4 hours last night."
                                                     
    s "For what? School didn't even start yet!"
                             
    b "I was binge watching the entire night and lost track of time!"
                                             
    s "Well don't bother rushing anyway, because you'll just end up sleeping in class anyway."
                                                     
    b "I don't sleep in class! I just put my head down from time to time!"
                                                                          
    s "Sure, might as well bring a pillow for those small moments."
                                                                   
    "This may be my first morning on the first day of high school, but this is how every morning goes during school."
    
    "This is the life of this ordinary kid, Sam Moore. I'm 15, a freshman in high school, to which i'm not as excited as my friend is."                                                                                                                 
    
    b "Oh, shut up, Sam! Like you even pay attention at all in class while you're wide awake!"                                                                                                                                   
    
    s "Ack..."
    
    "This scatter-brained girl is my childhood friend, Bella. She's the same age as I am."
                                                                  
    "We've lived in the same neighborhood since we were in elementary school and have been inseparable ever since."
    
    "Despite how clumsy and bad at time-management she is, she makes up for it in resilience."
        
    "She works overly hard in school, as well has juggling a job and club activities."
        
    "She's not exactly a genius, but she does study and work hard. I guess that's why she's a honor student and I'm not."
    
    b "You're not excited for your first day of high school at all, Sam?"
                                                                         
    s "Why should I? We're forced to attend school by law, and I don't feel motivated to work with a bunch of idiots in a 'class' that need to be babysat."
                                                                                                                                                           
    b "Don't say it like that! Yeah, some people don't care about school, but I think you guys just don't understand."
    
    s "Understand what? That school is just a fancy teenager day care?"
    
    b "It's a place of learning and growth! There's so much you can learn in school other than testing the teachers' patience!"
    
    s "Really?"
    
    b "It's a place where you learn about yourself and grow as a person, a place to learn skills for a bright future!"
    
    "Bella' voice grows louder as she continues of her speech about school"
    
    b "It's a place to celebrate and live life while we're young!"
    
    s "Well, that was an overly dramatic way to put it."
    
    b "It's true though, we only experience these 4 years once!"
    
    s "No, it's what we see in another 4 years in college and then for 50 years in a job."
    
    s "Just sitting, 'working', and being told to not break anything."
    
    b "There's more to school than just that! Also, it's just what you make of it, Sam. Speaking of which, are you joining any clubs this year?"
    
    s "No, and I'd like to keep it that way. I'll just spend my 8 hours in the prison called 'school' and take my leave."
    
    b "Oh come on! That's no fun at all! You used to love to play and do all sorts of things in middle school!"
    
    s "Yeah, but it was only to get into trouble. I'd rather just keep to myself rather than have some people yell at me now."
    
    b "I won't take 'no' for an answer! Come with me after school, I'll take you to go see some clubs."
    
    b "Well, we're here at the schoolyard! I'm bummed we don't have any classes together, but I still want to see you afterschool, okay? I'll see you then!"
    
    hide Bella neutral
    
    "Before I can protest, she runs off to her classes."
    
    s "Ack...Okay, whatever, i'll indulge her."
    
    s "Time for another day in school..."
    
    hide Sam neutral
    with dissolve
    with fade
    
    #image bg classroom = "clasroom.png"
    scene bg classroom
    
    show Sam neutral
    
    s "Phew, finally the teacher stopped droning on and on about the syllabus. I know she's trying to clear with eveything, but there's always the idiots who will ask the same questions."
    
    "With that, the first school day ended with seemingly endless classes."
    
    "As I was about to leave the classroom to go meet with Bella, I catch the glare of a student with a pained look on his face right at the doorway."
    
    image Ari neutral = "Ari_neutral.png"
    show Ari neutral at right
    
    sms "..."
    
    s "Umm...Are you okay?."
    
    sms "...Uhh...No, i'm fine. Sorry to make you worry, I guess it's just my natural facial expression. Please excuse me..."
    
    hide Ari neutral 
    
    "He leaves the room in a quiet fashion."
    
    s "...Okay, then..."
    
    hide Sam neutral
    with dissolve
    with fade
    
    #image bg hallway = "hallway.png"
    scene bg hallway
    show Sam neutral
    show Bella neutral at left
    
    "I meet up with Bella in the hallway to see her waiting for me outside my classroom."
    
    s "You're really serious with forcing me to join a club aren't you?"
    
    b "Come on, you've got the time and energy! Let's get you doing something!
    
    "Bella takes my hand to go look at the various clubs in school."   
       
    with dissolve
    
    b "How about the science club? You get to do cool experiments and show off your research!"
                                                                                              
    "                                                                                          
    
    # This ends the game.

    return
