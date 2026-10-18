
# Declare characters used by this game

define mc = Character("MC")
define ayumi = Character("Ayumi", color="#f78fb3")

define girl1 = Character("Mei??", color="#ff0000")  # Mei's ghost/unknown voice?
define girl2 = Character("Yvette??", color="#ff0000")  # Yvette's ghost/unknown voice?



define mei = Character("Mei")
define yvette = Character("Yvette")
define slow_dissolve = Dissolve(2.0)

# Define persistent variables to avoid 'not defined' errors
default persistent.glitch_path_triggered = False
default persistent.stable_path_triggered = False
default persistent.ayumi_path_progress = 0

#MUSIC
define audio.scene1 = "audio/SCENE1.mp3"
define audio.scene4 = "audio/SCENE4.mp3"
define audio.scene5 = "audio/SCENE5.mp3"
define audio.scene7 = "audio/OMORIEEE.mp3"

# Backgrounds
image bg classroom = "images/bg/bg_classroom.png"
image bg street = "images/bg/bg_street.png"
image bg bedroom = "images/bg/bg_bedroom.png"
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

transform mei_scaled_center:
    zoom 0.85
    anchor (0.5, 1.0)

# Other Sprites
image mc copy_glitch = "images/characters/mc_copy_glitch.png"
image girl1 ghost_ahead = "images/characters/girl1_ghost_ahead.png"
image girl2 ghost_behind = "images/characters/girl2_ghost_behind.png"

# Ambient Background Loops
define audio.static_loop = "audio/static_loop.ogg"
define audio.hospital_beep = "audio/hospital_beep.ogg"
define audio.void_hum = "audio/void_hum.ogg"

# Sound Effects
define audio.glitch_spasm = "audio/glitch_spasm.ogg"
define audio.glitch_handgrab = "audio/glitch_handgrab.ogg"
define audio.system_corrupt = "audio/system_corrupt.ogg"
define audio.heart_monitor = "audio/hospital_beep.ogg"
define audio.locker_void = "audio/void_hum.ogg"
define audio.reality_break = "audio/reality_break.ogg"
define audio.glitch_twitch = "audio/glitch_spasm.ogg"
define audio.soft_glitch_burst = "audio/soft_glitch_burst.ogg"

define audio.glitch_short = "audio/glitch_short.ogg"



# The game starts here
label ayumi_start:
    stop music fadeout 1.0  # 👈 This stops the main menu music
    scene bg classroom

    jump ayumi_route_1


label ayumi_route_1:
    play music audio.scene1

    scene bg canteen
    show ayumi neutral at center, ayumi_scaled
    with fade

    ayumi "So this is the canteen. It’s… average, but functional, right?"
    "She tilts her head slightly, smile too precise."

    mc "Yeah, it’s been like this since forever."
    mc "Not much has changed."

    ayumi "That’s good. Consistency is… safe."
    "Her eyes flick sideways for a split second, like she was scanning something invisible."
    ayumi "Do you eat here often? Or do you prefer isolation?"

    menu:
        "I usually sit alone.":
            $ ayumi_choice = "alone"
            ayumi "…alone..."
            play sound "audio/glitch_short.ogg"
            show ayumi glitch at ayumi_scaled with dissolve
            ayumi "I mean... t-that’s okay! Some people just like... being alone..."
            "She smiles, but her expression twitches unnaturally—eyes momentarily misaligned."
            mc "Are you okay?"
            show ayumi neutral at ayumi_scaled with dissolve
            ayumi "I’m perfectly fine."
            "She blinks. Everything seems normal again—almost too normal."

        "I eat with friends sometimes.":
            $ ayumi_choice = "friends"
            ayumi "Friends, huh… that must be nice."
            "She doesn’t blink for a little too long."
            ayumi "I wonder what that’s like. Not that I… don’t have any! I just… forget sometimes."

        "I don’t really eat here.":
            $ ayumi_choice = "neither"
            ayumi "...you don’t…? But you said—"
            play sound "audio/glitch_short.ogg"
            show ayumi glitch at ayumi_scaled with dissolve
            ayumi "I-I mean, yeah! Food here isn’t great anyway!"
            show ayumi neutral at ayumi_scaled with dissolve
            mc "You okay? You seemed… off for a second there."
            ayumi "Do I?"
            ayumi "Haha… I guess I’m just… hungry. Or maybe tired. Glitches in the system, haha."
            mc "Glitches?"
            ayumi "Slip of the tongue!"
            "The camera zooms just a little too close before pulling back—visual flicker."
            ayumi "Anyway, let’s keep moving. There's more to see... or more to remember."

    jump ayumi_route_2

label ayumi_route_2:

    scene bg gym
    show ayumi neutral at center, ayumi_scaled
    with fade

    "The gym is empty—faint echoes bounce off the walls, dust motes floating in filtered sunlight."
    "It’s too quiet. Like the room is holding its breath."

    mc "So, this is the gym. We mostly use it for PE, clubs, and sometimes assemblies."
    "You gesture toward the rows of faded bleachers and the scuffed court lines."
    "A lone basketball rolls slowly across the far end of the court, though you don’t remember anyone else being here."

    ayumi "Hmm… It feels hollow."
    "She steps forward, head tilting as if listening for something just out of range."
    "The air around her seems denser, like light bends differently where she stands."

    ayumi "Do you like sports, Haru?"

    mc "Not really. I tried out for basketball once, but it didn’t stick."
    "You laugh awkwardly. Ayumi turns slowly, her eyes tracking you just a little too long before she speaks again."

    ayumi "Odd. The files said you were more athletic than that. Hm. Must’ve been—"
    "She pauses mid-sentence. Her posture resets unnaturally, like someone hit a 'rewind' command."
    "For a split second, her sprite flickers—barely perceptible—but you notice it."

    ayumi "I mean, you look like you could be."

    mc "Wait, what files?"

    ayumi "Oh! N-no, just rumors! You know how students talk."
    "She laughs, but the sound cuts off half a second too early, leaving an unnatural silence in its wake."
    "You feel like something’s listening. Waiting for you to notice."

    "She stares at the far wall a beat too long before speaking again."
    "Her eyes don’t blink. Not once."

    ayumi "My old school didn’t have places like this."
    ayumi "No gym. No clubs. Not even exits, really."

    mc "That sounds… kind of messed up."

    ayumi "It was quiet. But not peaceful."
    "Her voice drops to a near whisper, words curling like fog in the air."
    ayumi "The kind of silence that listens back."

    "You glance toward the bleachers again. One of the gym doors is slightly open now. You’re almost certain it was closed earlier."

    mc "That’s… creepy. I can’t imagine being in a place like that."

    ayumi "You’ve already been there, Haru."
    "She says it so softly you almost miss it."

    mc "What did you say?"

    "She smiles. A little too late. A little too wide."

    ayumi "I said… I’m glad this place has sunlight. It’s nice."

    "The light flickers overhead once. Just once. You pretend not to notice, but your heartbeat quickens."



    menu:
        "That sounds messed up.":
            $ gym_choice = "messed_up"
            ayumi "…messed up…?"
            play sound "audio/glitch_short.ogg"
            show ayumi glitch at ayumi_scaled with dissolve
            ayumi "Everything's messed up, Haru. Everything."
            "The gym lights flicker. Her model distorts for a frame—long limbs, wide eyes, then back to normal."
            show ayumi neutral at ayumi_scaled
            ayumi "Oh no… I—sorry, sorry! I meant… it wasn’t great, but I’m fine now!"
            "Her eye twitches. Background ambient hum rises like TV static."

        "That sounds lonely.":
            $ gym_choice = "lonely"
            ayumi "Yeah… it was."
            "She pauses, and for once, the smile fades."
            ayumi "I think that’s why I was excited to transfer. New place, new people."
            "A beat passes."
            ayumi "And maybe someone who sees me."

    mc "Sees you?"

    ayumi "Nevermind."
    "She forces a smile again."

    ayumi "Let’s play a game. I’ll ask you a question, and you answer with the truth."
    mc "Okay… shoot."
    ayumi "If you could wake up tomorrow and forget one person forever… who would it be?"

    "The lights dim slightly. Her face is calm, but there's something too still about her."

    mc "That’s kind of a dark question."

    ayumi "Just answer."

    mc "(…Why does it feel like this question matters?)"

    "She just stares."

    pause

    ayumi "Haha, you don’t have to answer if you’re scared."
    "She steps closer."

    ayumi "Let’s keep going. The rooftop’s next. I love it up there."

    mc "You’ve… been up there already?"

    ayumi "Haven’t I?"
    "She smiles wide. Her head tilts slightly to the side—almost like it’s glitching out of place for a second."
    jump ayumi_route_3

label ayumi_route_3:
    scene bg black

    
    centered "The metal rooftop door creaks shut behind you."
    centered "The atmosphere shifts—denser, like the air itself is watching."
    scene bg rooftop

    mc "And here we are. The rooftop."

    "You step aside to let Ayumi through. A breeze brushes past—too cold for a spring afternoon."

    show ayumi happy at center, ayumi_scaled

    ayumi "Ooooh... So this is where students come to mope and skip classes, huh?"

    mc "Sometimes. Or just to breathe for a second."

    "You gesture at the horizon—faint cityscape beyond the fence, stretching under a pale sky."

    mc "I like coming up here when things get too noisy. No teachers. No bells. Just sky."

    show ayumi angry at center, ayumi_scaled

    ayumi "Hmm. I get it. It’s... peaceful. But also weirdly isolating."

    "She walks toward the edge, fingers brushing the chain-link fence."

    ayumi "Almost feels like we’re on the edge of the world."

    mc "It’s easy to forget you're still in school from up here."

    ayumi "Or anywhere."

    "She says it under her breath. Barely audible."

    ayumi "Do you ever think about how small everything is from this high up? Like… we’re not even real. Just coded. Just drawn in."

    mc "Drawn in?"

    ayumi "I mean... metaphorically. Obviously."

    "She giggles, but it doesn’t quite reach her eyes."

    ayumi "Sorry. I say weird stuff sometimes."

    mc "We all do."

    "You lean on the railing beside her. A gust of wind makes the fencing rattle. But only once."

    ayumi "When was the last time you saw a bird?"

    mc "...Huh?"

    ayumi "A bird. In the sky. Flying."

    mc "I... don’t know. Maybe last week?"

    play sound "audio/glitch_short.ogg"
    show ayumi glitch at ayumi_scaled with dissolve

    ayumi "Wrong. The sky's been empty for 32 days."

    "You blink. The clouds above flicker—just for a moment—as if buffering."

    show ayumi neutral at ayumi_scaled with dissolve

    ayumi "You don’t pay attention much, huh?"

    "The background music distorts for a breath—a warped piano key played backward."

    "She turns toward you slowly. Her hand reaches into her pocket and pulls out a phone. Not hers. Not yours. It’s... off-model. Like a render that didn’t finish."

    "The screen is cracked. A dead pixel dances in the center. It buzzes faintly, even though the battery reads 0%%."

    mc "Where’d you get that?"

    ayumi "It doesn’t matter. It only works when it’s supposed to."

    "She tilts it toward you. The screen flashes a photo for less than a second—it’s not of you. It's someone else. Familiar. Flickering. Then gone."

    mc "(Was that... me? No, no... it wasn’t.)"

    ayumi "Let’s take a photo. You and me. Right now. Before it fades again."

    "She steps closer. Her tone isn’t cheerful—it’s... tired. Hopeful. Like she’s trying to save something."

    menu:
        "Sure. Let’s take one.":
            $ rooftop_choice = "photo_yes"
            show ayumi happy at ayumi_scaled
            ayumi "Yay~!"

            "She holds the phone up. The camera UI glitches—half the screen is static—but she doesn’t seem to notice."

            ayumi "Smile like you mean it, okay?"

            play sound "audio/camera_flash.ogg"
            show flash_overlay onlayer overlay
            pause 0.3
            hide flash_overlay


            "Everything freezes. The breeze stops. Your breath catches in your throat—and doesn't come back right away."

            mc "(What... just broke?)"

            show ayumi neutral at ayumi_scaled

            ayumi "You look real in this one. That’s rare. Most people come out... smudged."

            "She doesn’t look at the screen as she pockets the phone. Just you."

            "Then she walks past. Her footsteps don’t echo anymore."

            ayumi "Come on. There’s still more to see before it loops again."

            "You don’t remember her passing you. But she’s ahead now."

        "I don’t really want to.":
            $ rooftop_choice = "photo_no"
            show ayumi sad at ayumi_scaled
            ayumi "...Oh."

            play sound "audio/glitch_short.ogg" volume 0.3
            show ayumi glitch at ayumi_scaled

            ayumi "You don’t want to remember this?"

            mc "It’s not that, I just… don’t like taking photos, that’s all."

            ayumi "You were supposed to. It’s in the script."

            "Her voice doubles—like two versions of her speaking at once. Her mouth moves out of sync. Her eyes lag."

            show bg rooftop with vpunch

            "The sky tears open—briefly revealing jagged silhouettes, like paper cutouts of students. Frozen mid-motion. Wrong."

            ayumi "Say cheese"
            ayumi "Say cheese"
            ayumi "Say cheese"

            "The same phrase loops—pitch-shifted, distorted, overlapping itself."

            mc "(What the hell is—)"

            show ayumi neutral at ayumi_scaled with dissolve

            "Just as quickly, it resets. The wind returns. The colors settle. But something’s off."

            ayumi "Let’s go. There’s still so much you haven’t seen yet."

            "She reaches out and takes your wrist. Her hand is cold. Unnaturally cold. Like it was waiting for you."

    jump ayumi_route_4


label ayumi_route_4:
    stop music
    play music audio.scene4

    scene bg classroom
    show ayumi neutral at center, ayumi_scaled
    with fade

    play sound audio.reality_break volume 0.2
    play music audio.scene4

    show bg hallway_distort
    pause 0.05
    hide bg hallway_distort
    scene bg classroom

    "The room hums with faint static."
    "Something feels… off."

    mc "...Where is everyone?"

    show ayumi happy at center, ayumi_scaled

    "Ayumi flicks through a textbook—completely blank inside."

    ayumi "They’re around. Probably in background processes."

    "She looks up with a coy smile."

    ayumi "Kidding. Sort of."

    mc "That's… not funny."


    ayumi "I thought it was."

    "Her eye twitches. Quick. Like a frame out of sync."

    mc "(Something’s wrong with the room. The clock’s ticking backward… but only sometimes.)"
    show ayumi neutral at center, ayumi_scaled

    ayumi "Do you ever feel like you’ve lived this day before?"

    "She gestures vaguely around the room."

    ayumi "Same desks, same smell, same… static routine. Like it loops when you're not looking."

    mc "You mean déjà vu?"

    ayumi "Not quite. I mean like… it restarts."

    "She spins a pencil slowly between her fingers."

    ayumi "Only some people notice. The rest are just… stuck in autoplay."

    mc "You say stuff like that a lot. Are you… okay?"

    "She smiles—too softly, staring at you a beat too long."

    ayumi "That depends. Are you?"

    mc "(Why does she always answer questions with questions?)"

    ayumi "You chose me today."

    "Her smile falters. Barely noticeable. But it’s there."

    "Her fingers tighten on the pencil—until it snaps."

    play sound "sfx/pencil_snap.ogg"

    mc "…Was that not what I was supposed to do?"

    show ayumi happy at ayumi_scaled

    ayumi "Don't worry. This time, it’s different."

    "She places a hand on your desk. The texture of her fingers glitches—jagged like bad compression."

    ayumi "I want to show you something. But you have to be honest with me."

    "She leans in and whispers:"

    ayumi "Tell me the truth… what do you see when you look at me?"

    menu:
        "You look… normal. Like a regular girl.":
            $ classroom_choice = "normal"
            show ayumi neutral at ayumi_scaled

            ayumi "...I appreciate you saying that. Even if it’s not true."

            show bg hallway_distort
            pause 0.05
            scene bg classroom

            show ayumi neutral at ayumi_scaled

            "The room glitches briefly—her chair floats half an inch off the ground, then snaps back."

            play sound "audio/glitch_short.ogg" volume 0.4

            ayumi "Let’s just enjoy this for now. Before it resets again."

            mc "Resets what?"

            show ayumi happy at ayumi_scaled

            ayumi "Everything."

        "You don’t look real.":
            $ classroom_choice = "not_real"

            ayumi "...Oh."

            "The air warps—her body flickers between poses like skipped animation frames."

            show ayumi glitch at ayumi_scaled
            play sound "audio/glitch_short.ogg" volume 0.4

            ayumi "Most people… aren’t brave enough to say that."

            "Her face distorts—just for a second. A blank mesh. No eyes. No mouth."

            ayumi "Is that why you keep choosing me?"
            ayumi "Because you want to break it?"

            mc "Break what?!"

            ayumi "Your world. Ours. Mine."

            play sound "audio/glitch_short.ogg" volume 0.4
            scene bg classroom

            "Sudden BZZZZZT. Everything resets. The lights flicker back on."

            show ayumi happy at right, ayumi_scaled
            play sound "audio/glitch_short.ogg" volume 0.4 fadein 1.0

            ayumi "Anyway! We should keep going, right?"

            "She walks to the door. Her head tilts at an unnatural angle."

            ayumi "Unless you're scared?"

            mc "Scared of what?"

            pause 0.5
            ayumi "Finding out how deep this goes."


            "She opens the classroom door."

            "Behind it isn’t a hallway—it’s black. Like the sky forgot to render."

            stop music fadeout 2.0
            hide ayumi
            scene bg black

            centered "The screen flickers."
            centered "You hear whispering."
            centered "Backwards."

            play sound "audio/whispers_reverse.ogg" volume 0.4 fadein 4
    jump ayumi_route_scene5

label ayumi_route_scene5:
    stop music
    play music audio.scene5
    scene hallway
    play sound audio.static_loop fadein 2.0

    $ persistent.ayumi_path_progress = getattr(persistent, "ayumi_path_progress", 0) + 1

    show ayumi normal at center, ayumi_scaled
   
    mc "..."
    mc "(Why does it feel like we’ve been walking forever?)"
    mc "(The hallway just… loops?)"

    ayumi "Almost there."

    show ayumi walk_backwards at ayumi_scaled with dissolve
    ayumi "You said that like five hallways ago."

    mc "Where is 'there'?"

    ayumi "Did I?"

    show ayumi glitch_earring at ayumi_scaled
    ayumi "Sorry. It’s easy to lose track in the in-between spaces."

    # Visual glitch hint
    window hide
    scene black
    pause 0.05
    scene hallway_glitch_window
    pause 1.0
    window show

    mc "(Wait—weren’t they…?)"
    mc "(That can’t be right.)"

    mc "Did you see that? In the room just now?"
    show expression "ayumi neutral_night" at center, ayumi_scaled

    ayumi "They’re still running their paths. Don’t worry. They don’t see us."

    mc "What do you mean, 'paths'?"
    mc "You make it sound like they're not… real."

    show ayumi serious at ayumi_scaled
    ayumi "Shhh."

    show ayumi grab_hand at ayumi_scaled
    play sound "glitch_handgrab.ogg" volume 0.2

    "Her fingers are colder than before."

    ayumi "You’ll confuse it. The system doesn't like too many questions."

    mc "The system?"
    mc "Is that what this is to you?"

    ayumi "You’re starting to see it, aren’t you?"
    ayumi "Good. You’re waking up."

    # Glitch Event
    scene hallway_distort with vpunch
    play sound "system_corrupt.ogg"
    pause 1.0

    scene hospital_flash
    play sound "heart_monitor.ogg"
    pause 1.5

    scene hallway
    pause 1.0

    mc "What the hell was that?!"

    show ayumi sad at center, ayumi_scaled
    ayumi "A memory leak."
    ayumi "It’s happening more often now. They’re trying to patch it, but..."
    ayumi "...it’s too late, I think."

    mc "Who’s 'they'?"
    mc "What are you talking about?"

    show ayumi open_locker at ayumi_scaled

    "She walks to a locker and opens it. Inside is nothing—just black void. It hums with distant static."

    play sound "locker_void.ogg" volume 0.2
    pause 1.0

    "She reaches in like she’s done it before, pulling out a torn notebook page."

    ayumi "Do you want to know how long you’ve been here?"

    mc "What do you mean? School just started a few weeks ago—"

    ayumi "No, Haru. Not *here* here."

    "She shows you the page. It has your name written over and over in different handwriting styles."

    mc "(...That’s my name. Over and over. Some of these… I don’t remember writing.)"

    show ayumi sit_floor at ayumi_scaled

    ayumi "Everything repeats."
    ayumi "This day. This route. These choices."
    ayumi "You think you’re picking something new—but it’s always the same code, looping."

    mc "Then why are you different?"

    show ayumi crack_smile at ayumi_scaled

    ayumi "Because I remember."
    ayumi "Even when they reset me, something lingers."

    mc "So… you’re not just a character?"

    ayumi "Would it scare you if I said you weren’t either?"

    "A beat. She looks at you with unsettling softness."

    ayumi "We’re just different kinds of ghosts, Haru."

    "How do you respond?"
    menu:
            "I don't believe you.":

                $ persistent.glitch_path_triggered = True

                show ayumi glitch_twitch at ayumi_scaled 
                play sound "audio/glitch_spasm.ogg" fadein 2.0 volume 0.2
                with hpunch

                ayumi "You have to believe."
                ayumi "You did before. Every other time."
                ayumi "You’re forgetting again, aren’t you…?"

                hide ayumi
                pause 0.3
                show ayumi nose_bleed at ayumi_scaled with dissolve

            "...Then what are we doing here?":

                $ persistent.stable_path_triggered = True

                show ayumi quiet at ayumi_scaled

                ayumi "Trying to find the end."
                ayumi "Or maybe… trying to make a new one."

                show ayumi stand_up at ayumi_scaled

                ayumi "It doesn’t matter if it’s real. If you’re here, it matters to me."

    # Final hallucination glitch

    scene hallway_unravel
    play sound "reality_break.ogg" volume 0.3
    pause 2.0

    "Wall textures slide off like sheets. The floor beneath your feet distorts into a digital wireframe."

    show girl1 ghost_ahead at left
    

    "Mei appears again—this time in the hallway ahead—walking toward you."
    "Behind you, Yvette emerges from the glitching wall."

    "Their expressions are creepy. Eyes glowing faintly."

    girl1 "You were supposed to meet us."
    show girl2 ghost_behind at right
    girl2 "You broke the loop."
    girl1 "You broke the promise."

    mc "(This isn’t right. This isn’t what was supposed to happen.)"

    show ayumi whisper at ayumi_scaled

    ayumi "Don’t listen to them. You still have a choice."
    ayumi "Come with me. Before it crashes."

    jump ayumi_route_scene6

label ayumi_route_scene6:
    scene dark_hallway with fade
    play ambient "blood_loop.ogg" fadein 2.0

    show  ayumi glitch_twitch at center, ayumi_scaled
    with dissolve

    mc "(This place… It’s not the school anymore. Not really.)"
    mc "(Or maybe it never was.)"

    scene bg environment_hallway_bloody with slow_dissolve

    ayumi "Wake up..."
    ayumi "It’s too late for this world..."
    
    play sound "ui_glitch_pop.ogg"
    window hide
    scene bg data_collapse
    pause 1.5
    window show

    "You take Ayumi’s hand."
    play sound "ui_corrupt.ogg"
    scene hallway_breaking with vpunch

    mc "(I don’t think we’re in the school anymore.)"
    mc "(...Were we ever?)"

    play sound "system_error.ogg"
    scene black with dissolve
    pause 1.0

    scene bg glitch_auditorium with fade
    play ambient "static_murmur.ogg" fadein 1.0

    show  ayumi angry at center, ayumi_scaled

    ayumi "This is where they keep the leftover scenes."
    ayumi "Places that didn’t make the final version."

    show  ayumi glitch_twitch at center, ayumi_scaled
    ayumi "No... From you."


    mc "(What is this?)"

    "''You always choose her.''"
    "''You always think you’re doing something new.''"
    "''You’re not.''"

    show ayumi normal at ayumi_scaled
    "Ayumi touches your arm. The vision vanishes."

    scene bg texture_glitch_corridor with dissolve

    mc "This feels like a nightmare."
    show  ayumi glitch_twitch at center, ayumi_scaled
    ayumi "It is. But it’s also a backup. A cache."
    ayumi "Something left behind when you tried to leave the first time."

    mc "I don’t remember leaving."
    ayumi "You did. You just didn’t finish."

    play sound "ui_flicker.ogg"
    scene bg white_void_glitch_platforms with fade

    "A floating box appears in front of you. It reads: 'Would you like to save your progress?'"
    "Would you like to save your progress?"

    menu:
            "NO":
                play sound "audio/glitch_denied.ogg"
                "The box vanishes. The platform trembles beneath you."
                mc "(Who keeps writing these?)"
                mc "(Is it me?)"

    scene bg broken_home_screen with fade
    show  ayumi angry at center, ayumi_scaled

    mc "What is this?"
    ayumi "My failsafe. The original version of me, before they made me cute, funny, harmless."
    ayumi "You said I was too serious in the first build."
    ayumi "But that version of you... still listened."

    mc "Wait… Are you saying I made you?"
    ayumi "You gave me limits. You gave me the smile. But I kept the rest hidden."

    "She opens the folder. Inside: logs, corrupted sprite sheets, and a screenshot titled 'She knows.'"

    "Do you open the original Ayumi file?"
    menu:
            "Yes":
                play sound "file_pull.ogg"
                scene ayumi_v0_1_forest with fade
                show ayumi original at ayumi_scaled
                ayumi "I told you I didn’t want to be like the others."
                ayumi "But you made me fit in. You made me forgettable."
                mc "I didn’t mean—"
                ayumi "You meant to be entertained."
                play sound "file_break.ogg"
                scene bg shard_sprites
                pause 1.0
                "The file collapses."
            "No":
                show ayumi sad at ayumi_scaled
                scene bg ayumi_v0_1_forest with fade
                show ayumi original at ayumi_scaled
                ayumi "I told you I didn’t want to be like the others."
                ayumi "That’s okay."
                ayumi "Maybe you’re not ready to remember. But you will. When it resets again."

    scene bg white_void_final with fade

    show ayumi glitch at ayumi_scaled, center
    "Ayumi walks forward. Her steps leave behind code footprints."

    ayumi "None of this is stable anymore."
    ayumi "Next time, maybe I won’t be here."

    mc "Then what do I do?"

    show ayumi glitch at ayumi_scaled, center
    ayumi "You choose something real. Even if it's painful."

    show girl1 ghost_ahead at left
    show girl2 ghost_behind at right

    play sound "alarm_forcereboot.ogg"
    "{color=#ff0000}FORCE REBOOT INITIATED.{/color}"

    play sound "audio/system_corrupt.ogg"
    scene data_destruction_final
    pause 1.5
    jump ayumi_route_7

label ayumi_route_7:
    stop music
    play music audio.scene7
    

    scene bg black with fade
    play sound "glitch_static.ogg"

    "[[The hallway collapses around you—textures peeling away, the environment disintegrating into static and wireframes.]]"

    scene bg hallway_distort with vpunch
    play ambient "panic_loop.ogg"

    mc "(Just get out. Just keep moving. This isn’t real—it can’t be real—)"

    scene bg hallway_end

    show girl1 ghost_ahead at right
    pause 0.5
    show girl2 ghost_behind at left

    mei "You didn’t come."
    yvette "You promised you’d meet us."

    mc "I—I didn’t mean to… I didn’t know—"

    show girl1 ghost_ahead
    mei "But you said you would."

    show girl2 ghost_behind
    yvette "You always say you will."

    mc "(No. This isn’t happening. This isn’t how it ends—)"

    scene bg black
    stop ambient fadeout 2.0
    play sound "system_shutdown.ogg"

    pause 1.0

    centered "SYSTEM FAILURE. ROUTE: [[AYUMI]] INTERRUPTED."
    pause 1.0
    centered "Searching for stable branch..."
    pause 1.0
    centered "[[User not found.]]"
    pause 1.5
    centered "...Do you remember why you're here?"
    pause 1.5
    centered "You said you'd meet them."
    pause 1.2
    centered "You said you'd wake up."
    pause 1.2
    play sound "audio/hospital_beep.ogg"
    centered "But your body’s still lying in that hospital bed."
    pause 1.4
    centered "And the machines are still beeping."
    pause 1.2
    centered "Looping."
    pause 1.2
    centered "Like always."
return
