# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mei = Character("Mei", color="#d580fc") #Gorl 1
define yvette = Character("Yvette", color="#c9a0dc") #Gorl 2
define ayumi = Character("Ayumi", color="#f78fb3") #Gorl 3
define mc = Character("Haru") #Torpe

#MUSIC
define audio.scene1 = "audio/SCENE1.mp3"
define audio.scene4 = "audio/SCENE4.mp3"
define audio.scene5 = "audio/SCENE5.mp3"
define audio.scene7 = "audio/OMORIEEE.mp3"

# Backgrounds
image bg classroom = "images/bg/bg_classroom.png"
image bg street = "images/bg/bg_street.png"
image bg bedroom_night = "images/bg/bedroom_night.png"
image bg hallway = "images/bg/hallway.png"
image bg gym = "images/bg/bg_gym.png"
image bg garden_day = "images/bg/bg_garden_day.png"
image bg garden_sunrise = "images/bg/bg_garden_sunrise.png"
image bg rooftop = "images/bg/bg_rooftop.png"
image bg canteen = "images/bg/bg_canteen.png"

image bg hallway_glitch_window = "images/bg/hallway_glitch_window.png" #DONE
image bg hallway_distort = "images/bg/hallway_distort.png" #DONE
image bg hospital_flash = "images/bg/hospital_flash.png" #DONE
image bg hallway_unravel = "images/bg/hallway_unravel.png" #DONE
image bg between_space = "images/bg/between_space.png" #DONE
image bg auditorium_glitched = "images/bg/auditorium_glitched.png"#DONE
image bg white_void = "images/bg/white_void.png" #DONE

image flash_overlay = "images/bg/flash.png" #DONE

image bg dark_hallway = "images/bg/dark_hallway.png" #DONE
image bg data_collapse = "images/bg/data_collapse.png" #DONE
image bg hallway_breaking = "images/bg/hallway_breaking.png" #DONE
image bg glitch_auditorium = "images/bg/auditorium_glitched.png" #DONE
image bg texture_glitch_corridor = "images/bg/hallway_unravel.png" #DONE
image bg white_void_glitch_platforms = "images/bg/white_void.png" #DONE
image bg broken_home_screen = "images/bg/broken_home_screen.png" #DONE
image bg ayumi_v0_1_forest = "images/bg/ayumi_v0_1_forest.png" #DONE
image bg shard_sprites = "images/bg/ayumi_v0_1_forest.png" #DONE
image bg white_void_final = "images/bg/white_void.png" #DONE
image bg data_destruction_final = "images/bg/data_destruction_final.png" #DONE
image bg hallway_end = "images/bg/hallway_unravel.png" #DONE
image bg black = "images/bg/black.png"
image bg rooftop_night = "images/bg/rooftop_night.png"
image bg rooftop_day = "images/bg/rooftop.png"
image bg court = "images/bg/court.png"

image bg environment_hallway_bloody = "images/bg/hallway_glitch_window.png"

# Ayumi
transform ayumi_scaled:
    zoom 0.2
    anchor (0.5, 1.0)

image ayumi angry = "images/characters/char_ayumi_angry.png"
image ayumi sad = "images/characters/char_ayumi_sad.png"
image ayumi happy = "images/characters/char_ayumi_happy.png"
image ayumi neutral = "images/characters/char_ayumi_neutral.png"

image ayumi glitch = "images/characters/char_ayumi_glitch.png"
image ayumi normal = "images/characters/char_ayumi_neutral.png"
image ayumi quiet = "images/characters/char_ayumi_neutral.png"
image ayumi serious = "images/characters/char_ayumi_angry.png"
image ayumi walk_backwards = "images/characters/char_ayumi_neutral.png"
image ayumi glitch_earring = "images/characters/ayumi_glitch_earring.png"
image ayumi crack_smile = "images/characters/char_ayumi_happy.png"
image ayumi grab_hand = "images/characters/char_ayumi_sad.png"
image ayumi whisper = "images/characters/char_ayumi_neutral.png"
image ayumi stand_up = "images/characters/char_ayumi_neutral.png"
image ayumi sit_floor = "images/characters/char_ayumi_neutral.png"
image ayumi glitch_twitch = "images/characters/ayumi_glitch_twitch.png"
image ayumi open_locker = "images/characters/char_ayumi_sad.png"
image ayumi shadow_stretch = "images/characters/ayumi_shadow_stretch.png"
image ayumi nose_bleed = "images/characters/ayumi_nose_bleed.png"
image ayumi v0_plain = "images/characters/ayumi_v0_plain.png"

image ayumi neutral_night = "images/characters/char_ayumi_neutral_night.png" 
image ayumi sad_night = "images/characters/char_ayumi_sad_night.png" 
image ayumi happy_night = "images/characters/char_ayumi_happy_night.png" 
image ayumi angry_night = "images/characters/char_ayumi_angry_night.png"

# Yvette
transform yvette_scaled:
    zoom 0.2
    anchor (0.5, 1.0)

image yvette happy = "images/characters/char_yvette_happy.png"
image yvette happy_afternoon = "images/characters/char_yvette_happy_afternoon.png"
image yvette happy_night = "images/characters/char_yvette_happy_night.png"

image yvette sad = "images/characters/char_yvette_sad.png"
image yvette sad_afternoon = "images/characters/char_yvette_sad_afternoon.png"
image yvette sad_night = "images/characters/char_yvette_sad_night.png"

image yvette neutral = "images/characters/char_yvette_neutral.png"
image yvette neutral_afternoon = "images/characters/char_yvette_neutral_afternoon.png"
image yvette neutral_night = "images/characters/char_yvette_neutral_night.png"

image yvette angry = "images/characters/char_yvette_angry.png"
image yvette angry_afternoon = "images/characters/char_yvette_angry_afternoon.png"
image yvette angry_night = "images/characters/char_yvette_angry_night.png"

image yvette glitch = "images/characters/char_yvette_angry_two.png"
image yvette ghost = "images/characters/girl2_ghost_behind.png"




# Mei
transform mei_scaled:
    zoom 0.2
    anchor (0.5, 1.0)

image mei happy = "images/characters/char_mei_happy.png"
image mei happy_afternoon = "images/characters/char_mei_happy_afternoon.png"
image mei happy_night = "images/characters/char_mei_happy_night.png"

image mei sad = "images/characters/char_mei_sad.png"
image mei sad_afternoon = "images/characters/char_mei_sad_afternoon.png"
image mei sad_night = "images/characters/char_mei_sad_night.png"

image mei neutral = "images/characters/char_mei_neutral.png"
image mei neutral_afternoon = "images/characters/char_mei_neutral_afternoon.png"
image mei neutral_night = "images/characters/char_mei_neutral_night.png"

image mei angry = "images/characters/char_mei_angry.png"
image mei angry_afternoon = "images/characters/char_mei_angry_afternoon.png"
image mei angry_night = "images/characters/char_mei_angry_night.png"

image mei glitch = "images/characters/char_mei_glitched.png"
image mei ghost = "images/characters/girl1_ghost_ahead.png"

#sound effect
define audio.fling = "audio/throwaway.mp3"
define audio.rustle = "audio/rustlingclothes.mp3"
define audio.footsteps = "audio/footsteps.mp3"

#push
transform push_once:
    linear 0.4 xoffset -450

transform push_hard:
    linear 0.09 xoffset -950

# The game starts here.

label start:

    stop music fadeout 1.0

    play music audio.scene1

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene hallway
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mei neutral at center, mei_scaled
    with dissolve

    # These display lines of dialogue.

    mei "—And then the teacher just gave me detention for asking a question! Can you believe that?"

    mc """ 
    (Wait, what? What’s going on?)
    
    (Did I miss something…?)
    """

    show mei neutral at center, mei_scaled

    mei "Anyway, you never told me how your day was! Spill it, mister quiet boy."
    mc "I… it was fine, I guess? Just kind of a blur."
    
    mei "A blur? You sound like an old man. You're like, twenty, not seventy."

    "She leans closer, her breath warm."

    show mei neutral at center, mei_scaled
    mei "You’re not skipping sleep again, are you?"
    
    mc "No, just… got a bit of a headache. I think."
    
    mei """
    Oooh, is that why you're spacing out?
    
    Or maybe you’re just distracted by me~
    """
    
    mc "You’re kind of hard to ignore."
    
    show mei neutral at center, mei_scaled
    mei """
    Damn right I am. So hey—tomorrow. Wanna hang out after school?
    
    We can hit that new arcade, or just vibe. Up to you.
    """
    
    mc """
    I’ll think about it.
    
    (Why do I feel like I’ve had this conversation before?)
    """


label prologue_scene2:
    # Scene 2 start

    stop music

    scene bgblack with fade 
    pause (1.0)

    "Later"
    scene bg street
    with fade

    mc"
    (It’s peaceful. Almost too peaceful.)"

    """
    You step toward your door, keys in hand—

    but a voice cuts through the silence.
    """

    play sound "<from 0 to 2>audio/footsteps.mp3" volume 2.0
    show yvette neutral_afternoon at center, yvette_scaled
    yvette "You’re home late."

    mc "Oh—Yvette. I didn’t see you there."

    yvette "I just stepped out. Grocery run."

    "Her tone is calm, almost flat, but not unfriendly."

    mc "Same uniform, huh? Don’t you ever change after class?"

    yvette "It’s just easier this way. I don’t mind."
    
    show yvette happy_afternoon at center, yvette_scaled
    "She looks at you, something unreadable in her expression."
    
    yvette "You still remember when we used to walk home together every day?"
    
    mc "Yeah… it feels like a long time ago."

    yvette  "It wasn’t. Not really."
    "She glances away." 
    yvette "Tomorrow—do you want to hang out? Just us."

    mc "Maybe. I’m not sure what I’m doing yet."
    
    show yvette sad_afternoon at center, yvette_scaled
    yvette "Alright. Just… think about it."
    play sound "<from 6 to 8>audio/footsteps.mp3" volume 2.0
    "She turns and walks down the street, fading into the quiet."



label prologue_scene3:
    scene bgblack with fade 
    pause (1.0)

    "You enter home and go to bed but as you were about to sleep you overthink."

    play music audio.scene4

    scene bg bedroom_night with fade
    mc """
    (Why does everything feel… off?)

    (Like I’m forgetting something important.)
    """

    "You lie down, but the ceiling feels too close."
    "The shadows shift just a little too much."

    mc"(Mei wants to hang out. Yvette too. But why do I feel like it’s more than that?)"


    "A faint ringing buzzes in your ears."
    "Like a notification that never came."

    mc"""
    (What if none of this is real?)

    (No, that’s stupid. I’m just tired.)
    """

    "You close your eyes—"
    "—but you swear, for a moment, you see a smiling face in the darkness."
    pause (1.0)

    "Not Mei."
    pause (0.5)
    "Not Yvette."
    pause (0.5)
    "Someone else."
    pause (0.5)

label prologue_scene4:
    scene bgblack with fade 
    pause (1.0)
    stop music

#     THE NEXT DAY you arrived at school and still mentally caught up in yesterday’s events. As he rounds a corner, he accidentally bumps into Girl 3. She instinctively mutters, “Wtf…” under her breath, her expression briefly flickering with confusion—almost as if she glitched. But the moment she realizes it’s the MC, her entire demeanor resets. Her posture straightens, her voice shifts to a sweet, soft tone, and she smiles. “Oh my god, I didn’t see you there,” she says, as if nothing strange happened at all—leaving the MC with a lingering unease.

    scene bg hallway
    "THE NEXT DAY"

    play music audio.scene1
    mc "(Why am I so tense? It’s just another school day.)"

    "You round the corner—"
    scene bg hallway
    with hpunch
    "BUMP"

    show ayumi angry at center, ayumi_scaled
    pause(0.1)
    show ayumi glitch at center, ayumi_scaled
    pause(0.1)
    show ayumi angry at center, ayumi_scaled
    "Girl " "Wtf—"
# She glitches, just for a split second. Her form stutters.
#  Then, she resets. Smile perfect. Posture sweet.

    show ayumi angry at ayumi_scaled
    ayumi """
    Oh my god, I didn’t see you there!

    I’m so sorry—are you okay?
    """

    mc "Y-yeah. You just… surprised me."
    ayumi "I’m new here. Transfer student."
    show ayumi happy at ayumi_scaled
    with dissolve

    "She offers a hand." 
    
    ayumi "Ayumi. Let’s be friends, okay?"

    mc "(That smile is too polished... like she’s trying really hard.)"


label prologue_scene5:
    scene bgblack with fade 
    pause (1.0)
    scene bg classroom

# As the bell rings and class begins, the teacher suddenly calls on him. 

    "The bell rings. The teacher looks directly at you."

    "Teacher " """

    Haru, since you're familiar with the school, 

    would you mind showing our new transfer student around?"""

    mc "(Of course... Ayumi.)"

    show ayumi happy at center, ayumi_scaled
    with dissolve
    ayumi "I’m looking forward to getting to know you better."
    # Suddenly— fwing sound effect as Mei comes in
    hide ayumi happy
    play sound "audio/throwaway.mp3"
    show ayumi angry at push_once, center, ayumi_scaled
    pause (0.1)
    show mei happy at push_hard, right, mei_scaled
    with dissolve

    mei """
    HARUUUUUUU!! Soooooo?? Did you decide yet?
    
    We’re hanging out, right?? Come on, say yes!
    
    """

    "Your phone buzzes. A message from Yvette:"
    "Yvette " "Are you free for lunch? Rooftop. Need to talk."
    mc "(Three choices. Three girls. But why does this feel… scripted?)"

    menu:
        "-Meet Up with Yvette at the Rooftop":
            jump yvette_start
        
        "-Cut classes to meet up with Mei":
            jump mei_start

        "-Tour the school with Ayumi":
            jump ayumi_start

    label Ayumi_test:
        "test works"
        jump end_test

    label Yvette_test:
        "Test works"
        jump end_test

    label end_test:

    return
