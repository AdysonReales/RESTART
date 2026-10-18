#MEI ROUTE

transform nod_once:
    linear 0.2 yoffset 10
    linear 0.2 yoffset 0

label mei_start:
# SCENE 1 – HALLWAY (AFTER CLASS)

    play music audio.scene1
    scene bgblack with fade 
    pause (1.0)
    scene bg hallway

    "The bell rings. Students flood the halls."

    show mei happy at center, mei_scaled
    with dissolve

    mei """
    *grabbing your wrist* “There you are! Okay, you’re mine today. 
    
    I saved you from the abyss of small talk with the new girl. 
    
    You owe me something sweet. Or like, emotional validation. Dealer’s choice.
    
    """

    "She’s walking backwards while talking, practically vibrating with energy."

    mei """
    I swear, if one more teacher asks me if I’ve been sleeping—like, no ma’am, just vibing through my slow spiral into burnout. 
    
    Look at these eyebags, they’re Chanel.

    """

    "She pauses, turns on her heel and leans in close"

    show mei sad at center, mei_scaled
    with dissolve
    mei "Real talk though. Do you think I’m… too much?"

    menu:
        "Nah, I like your energy. It's real":
            jump good_choice1

        "Honestly? Yeah, kinda.":
            jump bad_end
# 🡢 Dialogue Options:

#  “Nah, I like your energy. It's real.”

#  “Honestly? Yeah, kinda.” → BAD END triggers immediately
#Obob mo boi baket T_T

# If good:
    label good_choice1:
# She blinks, surprised, then grins.

    show mei happy at center, mei_scaled
    mei "Damn, okay. That’s… weirdly reassuring. Don’t get used to me being this sincere."

    "She gives you a light punch on the arm, then spins and skips ahead."

# SCENE 2 – GYM BLEACHERS (SUNSET)

    scene bg court with fade

    "You and Mei sit in the empty gym, sunset bleeding in through cracked windows. Mei was lying across two bleachers, legs hanging over the side."

    show mei neutral_afternoon at center, mei_scaled 
    with dissolve
    mei "So I totally bombed my physics quiz, but like… what even is gravity if not a suggestion?"

    play sound "audio/throwaway.mp3"
    "She throws a juice box at you just because"

    show mei sad_afternoon at center, mei_scaled
    with dissolve
    mei "Y’know what’s funny? I talk like this all the time, right? But sometimes I feel like I’m screaming in a crowded room and nobody hears me. Like I’m buffering emotionally."

    "She sits up slowly."

    mei "If I vanished, would anyone notice?"

# 🡢 Dialogue Options:

# “I would. Without a doubt.”

#  “Maybe. Depends how loud the vanishing was.” → BAD END triggers immediately

    menu:
        "I would. Without a doubt.":
            jump good_choice2

        "Maybe. Depends how loud the vanishing was.":
            jump bad_end

# If good:

label good_choice2:

    "She bites her lip, nodding slowly."

    show mei neutral_afternoon at nod_once, center, mei_scaled
    with dissolve

    mei "Okay… okay, I wasn’t ready for that kind of answer. You’re messing me up a little."

    "She throws herself backward dramatically."

    show mei happy_afternoon at center, mei_scaled
    mei "Thanks though. Seriously."

# SCENE 3 – ROOFTOP (LATE NIGHT)

    scene bg rooftop_night
    with fade

    "The wind’s picking up. Mei sits near the edge of the rooftop, legs dangling off the side. A dim vending machine light glows behind her."

    show mei neutral_night at center, mei_scaled
    with dissolve
    mei "Used to come up here when I felt like exploding. It’s like… I can scream and the sky won’t judge me."

    "She hands you a half-eaten pack of gum"

    show mei sad_night at center, mei_scaled
    mei """
    Sometimes I think I act like this so no one ever gets close enough to see the mess. Like, if I keep dancing, no one will ask me to stop and talk.

    But you’re still here. That’s gotta mean something.
    """

    menu:
        "It means I see you. For real.":
            jump good_choice3

        "You’re not hiding it that well.":
            jump bad_end

label good_choice3:

    show mei happy_night at center, mei_scaled
    with dissolve
    "Mei exhales, head leaning onto your shoulder."
    show mei sad_night at nod_once, center, mei_scaled
    mei "...don’t disappear, okay?"

    show bg rooftop_night

# Fade out to early sunrise glow.

#  GOOD ENDING: “STAY”
# On the rooftop, the sun rises gently behind them.

    show bg rooftop_day

    show mei happy at center, mei_scaled
    with dissolve
    pause(1.0)
    mei "You didn’t leave when I got quiet. That’s… kind of insane."

    play sound "<from 0 to 2.75>audio/rustlingclothes.mp3"

    "She laughs—nervous and warm—and finally takes off her hoodie, tossing it beside her."

    mei "Guess I can stop pretending, just for a bit."

    "She looks at you"

    mei "Thanks for staying."

    scene bg black with fade
    centered "Some people don’t need saving. Just someone to sit with them while it rains."
    pause (1.0)
    centered "GOOD END"
    pause (1.0)

    jump end

    label bad_end:
    # bad end
    
    show mei neutral at center, mei_scaled
    pause (0.5)
    show mei happy at center, mei_scaled
    with dissolve
    pause(0.5)
    mei "I see"
    
    show mei angry at center, mei_scaled
    with dissolve
    pause (0.4)
    play sound "audio/soft_glitch_burst.ogg" volume 0.4
    
    show mei glitch at center, mei_scaled
    with vpunch
    pause(0.5)
    
    show mei neutral at center, mei_scaled
    with hpunch
    pause (0.4)
    
    show mei glitch at center, mei_scaled
    with vpunch
    pause(0.3)
    
    show mei neutral at center, mei_scaled
    with hpunch
    pause (0.3)
    
    show mei glitch at center, mei_scaled
    with vpunch
    pause(0.3)
    with vpunch

    label end:

    return
