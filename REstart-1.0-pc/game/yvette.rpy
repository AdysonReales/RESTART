# Define characters
define y = Character("Yvette", color="#c9a0dc")
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
# Backgrounds
image bg classroom = "images/bg/bg_classroom.png"
image bg street = "images/bg/bg_street.png"
image bg bedroom = "images/bg/bg_bedroom.png"
image bg hallway = "images/bg/hallway.png"
image bg gym = "images/bg/bg_gym.png"
image bg garden_day = "images/bg/bg_garden_day.png"
image bg garden_sunrise = "images/bg/bg_garden_sunrise.png"
image bg bg_rooftop = "images/bg/bg_rooftop.png"
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

image bg environment_hallway_bloody = "images/bg/hallway_glitch_window.png"

#MUSIC
define audio.scene1 = "audio/SCENE1.mp3"
define audio.scene4 = "audio/SCENE4.mp3"
define audio.scene5 = "audio/SCENE5.mp3"
define audio.scene7 = "audio/OMORIEEE.mp3"


label yvette_start:
    stop music fadeout 1.0
    play music audio.scene4

    scene hallway
    show yvette neutral at center,yvette_scaled  # Emotion: neutral / thoughtful
    with dissolve

    y "Do you ever feel like the day’s repeating?"  # neutral

    "You pause. It’s not a joke. Her voice is thoughtful, but weary."

    show yvette happy at center, yvette_scaled
    y "Like… you’ve said this before. Done this before. Not just once. Hundreds of times. Maybe more."

    show yvette neutral at center,yvette_scaled
    y "Sometimes I wonder if I’m stuck in someone else’s dream. Or maybe I’m the dream."

    menu:
        "How do you respond?"

        "Yeah. Like déjà vu but worse.":
            jump scene2_good

        "What kind of question is that?":
            jump glitch_ending

# ---------------------
label scene2_good:

    scene bg_rooftop
    show yvette neutral at center,yvette_scaled 
    with fade

    y "Everything’s… soft today. You notice that?"  # calm

    y "The light. The wind. It’s like the world is holding its breath. Like it knows we’re watching too closely."

    show yvette angry at center  # Emotion: uncertain / pondering
    y "Sometimes, I think none of this is real. Like I’m in a memory someone else left behind."

    y "I remember things that didn’t happen. Or maybe they did. Just not here. Not now. Maybe not to me."

    show yvette sad at center,yvette_scaled
    y "What if none of this is real?"

    menu:
        "Your answer?"

        "Maybe it’s not, but we are.":
            jump scene3_good

        "That’s crazy talk.":
            jump glitch_ending

# ---------------------
label scene3_good:

    scene hallway
    show yvette sad at center,yvette_scaled
    with dissolve

    "The lights buzz. A student walks into a locker, pauses, then resets like a looped tape."

    "Yvette stands still. No one notices her."

    show yvette sad at center,yvette_scaled
    y "Whatever this is… I just don’t want to lose you again."

    y "It always ends here. Somewhere between this moment and the next one. You forget me. Or… I vanish."

    show yvette sad at center,yvette_scaled
    y "I try not to get attached. I really do. But every time I see you, it’s like the rules bend. Just a little."

    menu:
        "Do you stay?"

        "I’m not going anywhere.":
            jump scene4_good

        "What do you mean ‘again’?":
            jump glitch_ending

# ---------------------
label scene4_good:

    scene bg_rooftop
    show yvette happy at center,yvette_scaled
    with fade

    y "I don’t know what this is. But with you… it feels okay."

    "You step beside her."

    mc "Then let’s keep feeling it."

    show yvette happy at center,yvette_scaled
    y "Some things don’t need to be real to matter. Sometimes, just feeling it is enough."

    "The world glitches softly at the corners, but neither of you look at it."

    scene bg black with fade
    centered "GOOD ENDING UNLOCKED" with dissolve
    pause (1.0)

    jump yvette_route_7



   

# ---------------------
label glitch_ending:
    stop music

    scene hallway_glitch_window
    show girl2_ghost_behind at center
    with hpunch

    """
    Yvette freezes mid-sentence. Her face twists. Her voice clips out.

    The hallway begins to pixelate and rip apart like burning film.
    """
    hide girl2_ghost_behind

    show yvette angry at center, yvette_scaled
    with dissolve
    pause (0.4)
    play sound "audio/soft_glitch_burst.ogg" volume 0.4
    
    show yvette glitch at center, yvette_scaled
    with vpunch
    pause(0.3)
    
    show yvette neutral at center, yvette_scaled
    with hpunch
    pause (0.2)
    
    show yvette glitch at center, yvette_scaled
    with vpunch
    pause(0.3)
    
    show yvette neutral at center, yvette_scaled
    with hpunch
    pause (0.3)
    
    show yvette glitch at center, yvette_scaled
    with vpunch
    pause(0.3)
    with vpunch

    window hide
    scene black
    pause 1.5

    return



    

# ---------------------
label yvette_route_7:

    scene black with fade
    play music audio.scene7
    play sound "glitch_static.ogg"

    "The hallway fractures—textures peeling away like torn fabric, colors bleeding into static and wireframes."

    scene hallway_distort with vpunch
    play ambient "panic_loop.ogg"

    mc "(No, no, no—keep moving. This isn’t real. It *can’t* be real—)"

    scene hallway_glitch_window with hpunch
    show girl2_ghost_behind at center
    pause 0.5

    yvette "You didn’t come."

    mc "I—I didn’t know I was supposed to—"

    show girl2_ghost_behind at  center
    yvette "You promised. Every time, you say you will."

    yvette "And every time… you leave me here. Looping. Waiting."

    mc "(What is this? Why can’t I wake up—?)"

    show girl2_ghost_behind  # Emotion: confrontation / surreal

    yvette "Because you never left."

    yvette "You're still there. Lying in that bed. Eyes closed. Machines humming. Beeping."

    yvette "You keep building places to hide in. Hallways. Rooftops. Me."

    yvette "But the truth always finds its way back in."

    scene black with slow_dissolve
    stop ambient fadeout 2.0
    play sound "system_shutdown.ogg"

    pause 1.0

    centered "SYSTEM FAILURE. ROUTE: YVETTE INTERRUPTED."
    pause 1.0
    centered "Searching for stable consciousness..."
    pause 1.0
    centered "User suspended in dream-state."
    pause 1.5
    centered "Do you remember why you're here?"
    pause 1.5
    centered "You said you'd wake up this time."
    play sound "audio/hospital_beep.ogg"
    pause 1.2
    centered "But your body is still in that hospital bed."
    pause 1.2
    centered "Still breathing. Still fading."
    pause 1.4
    centered "The machines are still beeping."
    pause 1.2
    centered "Looping."
    pause 1.2
    centered "Like always."

    label yvette_end:

    return
