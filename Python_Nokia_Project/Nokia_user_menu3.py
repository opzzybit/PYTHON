def main_menu(running):
    while running:
        print()
        string_menu = """
    =========NOKIA 5510==================

                MENU

                press
    1.  profile
    2.  Phone Book
    3.  Call register
    4.  Chat
    5.  Message
    6.  Call divert
    7.  Settings
    8.  Calculator
    9.  Games
    10. Music
    11. Clock
    12. Reminders
    13. Sim Service
    14. Tones
    15. Service
    00. Exit Application

    =====================================
    """

        print(string_menu)
        option = input("Enter your option (or 00 to exit): ")

        match option:
            case "1":
                running = profile_menu(running)

            case "2":
                running = phonebook_menu(running)

            case "3":
                running = callregister_menu(running)

            case "4":
                chat_menu()

            case "5":
                running = message_menu(running)

            case "6":
                running = call_divert_menu(running)

            case "7":
                running = settings_menu(running)

            case "8":
                running = calculator_menu(running)

            case "9":
                running = games_menu(running)

            case "10":
                running = music_menu(running)

            case "11":
                running = clock_menu(running)

            case "12":
                running = reminders_menu(running)

            case "13":
                sim_service_menu()

            case "14":
                running = tones_menu(running)

            case "15":
                service_menu()

            case "00":
                running = False
                print("Exiting application. Goodbye!")

    return running

def profile_menu(running):
    profile_loop = True

    while profile_loop and running:
        profile = """
 ========PROFILE========

1. General MODE

2. Silent

3. Meeting

4. outdoor

5. Customize
0. Back to main menu
00. Exit application
"""
        print(profile)
        phone_profile = input("Enter your option: ")

        match phone_profile:
            case "1":
                general_mode_menu()

            case "2":
                silient_mode_menu()

            case "3":
                meeting_mode_menu()

            case "4":
                outdoor_mode_menu()

            case "5":
                running = customize_mode_menu(running)

            case "0":
                profile_loop = False

            case "00":
                running = False

    return running

def general_mode_menu():
    match "1":
        case "1":
            general_mode = """
      GENERAL MODE

   GENERAL MODE ACTIVATED !!!!!!

"""
            print(general_mode)

def silient_mode_menu():
    match "2":
        case "2":
            silent = """
      SILENT MODE

   SILENT MODE ACTIVATED !!!!!!

"""
            print(silent)

def meeting_mode_menu():
    match "3":
        case "3":
            meeting = """
      MEETING MODE

   MEETING MODE ACTIVATED !!!!!!

"""
            print(meeting)

def outdoor_mode_menu():
    match "4":
        case "4":
            outdoor = """
      OUTDOOR MODE

   OUTDOOR MODE ACTIVATED !!!!!!

"""
            print(outdoor)

def customize_mode_menu(running):
    customize_loop = True

    while customize_loop and running:
        customize = """
      CUSTOMIZE YOUR VOLUME

1. Increase Ringtone volume

2. Increase keyboard volume

3. Reduce Ringtone volume

4. Reduce Keyboard volume

0. Back to profile menu
00. Exit application
"""
        print(customize)
        customize_volume = input("Enter your option: ")

        match customize_volume:
            case "1":
                print("RINGTONE VOLUME INCREASED  !!!!!!")

            case "2":
                print("KEYBOARD VOLUME INCREASED !!!!!!!")

            case "3":
                print("RINGTONE VOLUME REDUCED !!!!!!!")

            case "4":
                print("KEYBOARD VOLUME REDUCED !!!!!!! ")

            case "0":
                customize_loop = False

            case "00":
                running = False

            case _:
                print("OPTION NOT FOUND")

    return running

def phonebook_menu(running):
    phonebook_loop = True

    while phonebook_loop and running:
        phone_book = """
========PHONE BOOK========

1. Search

2. Add name

3. Delete

4. Copy

5. Option

0. Back to main menu
00. Exit application
"""
        print(phone_book)
        book_page = input("Enter your option: ")

        match book_page:
            case "1":
                search_menu()

            case "2":
                add_name_menu()

            case "3":
                delete_menu()

            case "4":
                copy_number_menu()

            case "5":
                running = phonebook_settings_menu(running)

            case "0":
                phonebook_loop = False

            case "00":
                running = False

    return running

def search_menu():
    search = """
            SEARCH
abc....

       EMPTY CONTACT !!!!!!

Enter the name : ...................
 """
    print(search)
    book_page2 = input("Enter the name: ")
    book_page3 = input("Enter done: ")

    print()
    print("searching ! searching ! searching !!!!!!")

def add_name_menu():
    add_name = """
            ADD NAME
abc....

       EMPTY CONTACT !!!!!!!

Enter the name : .................
Enter phone number :.. ...............
 """
    print(add_name)
    note_page1 = str(input("Enter the name: "))
    note_page2 = str(input("Enter the number: "))

    print()
    print("CONTACT SAVED")

def delete_menu():
    delete = """
            DELETE

       EMPTY CONTACT !!!!!!
 """
    print(delete)

def copy_number_menu():
    copy_number = """
         COPY NUMBER

       EMPTY CONTACT !!!!!!!
 """
    print(copy_number)

def phonebook_settings_menu(running):
    book_settings_loop = True

    while book_settings_loop and running:
        settings = """
            SETTINGS
1. Memory status

2. view type

3. Speed type

0. Back
00. Exit application
"""
        print(settings)
        book_settings = input("Enter your option: ")

        match book_settings:
            case "1":
                memory_menu()

            case "2":
                display_menu()

            case "3":
                data_speed_menu()

            case "0":
                book_settings_loop = False

            case "00":
                running = False

    return running

def memory_menu():
    memory = """
                     MEMORY SPECIFICATIONS

- Internal Storage: 64 MB of built-in flash storage, designed for
      digital audio files (MP3 and AAC),
      holding roughly 2 hours of music or about one full album.

- Expandable Storage: None (the device does not have a memory card slot).

- Phone book Capacity: Stores up to 100 names and numbers in the device memory.

- SIM Memory: Supports an additional 250 entries on the SIM card.

- Call and Dial Memory: Accommodates 8 speed-dial and voice-dial entries,
      plus a standard call register.
    """
    print(memory)

def display_menu():
    display = """
                        DISPLAY SPECIFIACTIONS

- Screen Type: Monochrome STN graphic LCD
      (no color, purely black-and-white pixels with a green/amber backlight).

- Resolution: 84 x 48 pixels.

- Physical Size: 1.5 inches diagonally.

- Text Capacity: Accommodates up to 5 lines of text simultaneously.

- Form Factor: Positioned horizontally in a landscape orientation right
      in the center of the split QWERTY keyboard.

- Additional Visual Features: Supports dynamic font sizing, pixel-art screensavers,
      and dedicated text templates or smileys.
    """
    print(display)

def data_speed_menu():
    data_speed = """
                   NETWORK & DATA SPEED
- 2G Mobile Data: No GPRS or EDGE support. It relies on CSD (Circuit-Switched Data)
      to load primitive text-based WAP pages over a dial-up style mobile connection.

- Data Transfer Rate: CSD caps out at a maximum internet connection speed of just 9.6 kbps.

                     HARDWARE INTERFACE TRANSFER SPEED
- USB Cable Connection: It was the first Nokia phone to feature a direct Mini-USB port.
- Connection Protocol: It uses USB 1.0 (Low-Speed / Full-Speed).
- Transfer Rate: Transferring MP3 audio files from a PC into the phone's 64 MB
      memory maxes out at roughly 1.5 Mbps to 12 Mbps. Filling up the internal music drive completely takes several minutes.

                     DIALING SPEED
- Speed Dial Capacity: It supports standard 1-touch speed dialing for up to 8 custom contacts,
      mapped directly to keys 2 through 9 on the keyboard
    """
    print(data_speed)

def callregister_menu(running):
    callregister_loop = True

    while callregister_loop and running:
        call_register = """
    ========CALL REGISTER========

       Insert your sim !!!!!!

1. Missed calls

2. Call duration

3. Clear log

0. Back to main menu
00. Exit application
"""
        print(call_register)
        print()
        register = input("Enter your option: ")

        match register:
            case "1":
                print("EMPTY CONTACT !!!!!!!")

            case "2":
                print("EMPTY CONTACT!!!!!!")

            case "3":
                print("EMPTY CONTACT !!!!!!")

            case "0":
                callregister_loop = False

            case "00":
                running = False

    return running

def chat_menu():
    chat = """
   ========CHAT========

   Welcome to chat box

         KINDLY
     INSERT YOUR SIM

"""
    print(chat)

def message_menu(running):
    message_loop = True

    while message_loop and running:
        message = """
  ========MESSAGE========

1. Write message

2. Inbox

3. Outbox

4. Send items

5. Drafts

6. Picture message

0. Back to main menu
00. Exit application
"""
        print(message)
        phone_message = input("Enter your option: ")
        print()

        match phone_message:
            case "1":
                print("NO SIM TO MOVE FURTHER !!!!!!!")

            case "2":
                print("EMPTY INBOX !!!!!!!!")

            case "3":
                print("EMPTY OUTBOX !!!!!!!!")

            case "4":
                print("NO ITEM UNTIL THERE IS SIM !!!!!!!!!!!")

            case "5":
                print("EMPTY DRAFT  !!!!!!")

            case "6":
                print("NO PICTURE MESSAGE YET  !!!!!!")

            case "0":
                message_loop = False

            case "00":
                running = False

    return running

def call_divert_menu(running):
    call_divert_loop = True

    while call_divert_loop and running:
        call_divert = """
 =============CALL DIVERT============

1. Divert all voice calls

2. Divert when busy

3. Divert when not answered

4. Divert when phone off

5. cancel all divert

0. Back to main menu
00. Exit application
"""
        print(call_divert)
        divert = input("Enter your option: ")
        print()

        match divert:
            case "1":
                print("NO SIM TO MOVE FURTHER !!!!!!!")

            case "2":
                print("EMPTY SIM CASE")

            case "3":
                print("NO SIM FOUND ")

            case "4":
                print("NO SIM FOUND")

            case "5":
                print("EMPTY DIVERT !!!!!!")

            case "0":
                call_divert_loop = False

            case "00":
                running = False

            case _:
                print("OPTION NOT FOUND")

    return running

def settings_menu(running):
    settings_loop = True

    while settings_loop and running:
        settings = """
=============SETTINGS============

1. Call settings

2. Phone settings

3. Security settings

4. Restore factory settings

0. Back to main menu
00. Exit application
"""
        print(settings)
        device_settings = input("Enter your option: ")

        match device_settings:
            case "1":
                running = call_settings_menu(running)

            case "2":
                running = phone_settings_menu(running)

            case "3":
                user_password = security_settings_menu()

            case "4":
                restore_setting_menu()

            case "0":
                settings_loop = False

            case "00":
                running = False

    return running

def call_settings_menu(running):
    call_settings_loop = True

    while call_settings_loop and running:
        calls_settings = """
       CALL SETTING

1. Automatic redial

2. Call waiting

3. Speed dialing

0. Back to settings
00. Exit application
"""
        print(calls_settings)
        setting_input = input("Enter your option: ")
        print()

        match setting_input:
            case "1":
                print("AUTOMATIC REDIAL ACTIVATED !!!!!!!")

            case "2":
                print("EMPTY CALL TAKEN")

            case "3":
                print("SPEED DIALING ACTIVATED")

            case "0":
                call_settings_loop = False

            case "00":
                running = False

            case _:
                print("NO SIM FOUND")

    return running

def phone_settings_menu(running):
    phone_settings_loop = True

    while phone_settings_loop and running:
        phonesettings = """
       CALL SETTING

1. Language settings

2. Confirm SIM service action

3. Network selection

4. Welcome note

0. Back to settings
00. Exit application
"""
        print(phonesettings)
        setting_in = input("Enter your option: ")

        match setting_in:
            case "1":
                language_menu()

            case "2":
                print()
                print("NO SIM FOUND YET. INSERT A SIM")

            case "3":
                print()
                print("""
             NETWORK SELECTION

SIM 1 : [NONE]

SIM 2 : [NONE]

DEFAULT : [NONE]

""")

            case "4":
                welcome_note_menu()

            case "0":
                phone_settings_loop = False

            case "00":
                running = False

            case _:
                print()
                print("OPTION NOT FOUND")

    return running

def language_menu():
    print("""
           LANGUAGE OPTIONS

1. English

2. Arabic

3. Spanish

4. Japanese

5. Chinese
""")
    language = input("Enter your option: ")

    match language:
        case "1":
            print("LANGUAGE CHANGED TO ENGLISH !!!!!!!")

        case "2":
            print("LANGUAGE CHANGED TO ARABIC")

        case "3":
            print("LANGUAGE CHANGED TO SPANISH")

        case "4":
            print("LANGUAGE CHANGED TO JAPANESE")

        case "5":
            print("LANGUAGE CHANGED TO CHINESE")

        case _:
            print("OPTION NOT FOUND")

def welcome_note_menu():
    print("""
Welcome to Nokia 5510. It is actually the best phone

you would get to see , promising you with all your

possible desires, pleasure , and imaginations

Thank you for choosing this product !!!!!!.
""")

def security_settings_menu():
    security_settings = """
       SECURITY SETTINGS

     RESET PASSWORD
"""
    print(security_settings)
    reset_password = input("Enter your option: ")

    return reset_password

def restore_setting_menu():
    print()
    print("""
       RESETTING YOU PHONE !!!!!!!!!!

""")

def calculator_menu(running):
    calculator = """
 =========OPZZY BIT  CALCULATOR=======

FIRST NUMBER--

OPERATOR--

SECOND NUMBER--

[1]      [2]         [3]      [/]

[4]      [5]         [6]      [*]

[7]      [8]         [9]      [%]

[0]      [+]         [-]

0 : BACK                     00 : EXIT
"""
    print(calculator)

    number1 = input("Enter first number: ")

    if number1 == "0":
        return running

    if number1 == "00":
        return False

    number1 = int(number1)

    print()
    operator = input("Enter Operator: ")[0]

    print()
    number2 = input("Enter second number: ")

   

    number2 = int(number2)

    print()

    match operator:
        case '+':
            result4 = number1 + number2
            print("ANS : ", result4)
            print()

        case '/':
            result2 = number1 / number2
            print("ANS : ", result2)
            print()

        case '*':
            result5 = number1 * number2
            print("ANS : ", result5)
            print()

        case '%':
            result6 = number1 % number2
            print("ANS : ", result6)
            print()

        case '-':
            result = number1 - number2
            print("ANS : ", result)
            print()

        case '^':
            result3 = number1 ^ number2
            print("ANS : ", result3)
            print()

    return running

def games_menu(running):
    game_loop = True

    while game_loop and running:
        game_menu = """
===============WELCOME TO GAME STATION=================

               press

1. Snake game

2. Bounce ball

3. Quiz

0. Back to main menu
00. Exit application
"""
        print(game_menu)
        game = input("Enter game of your choice: ")

        match game:
            case "1":
                snake_game_menu()

            case "2":
                bounce_ball_game_menu()

            case "3":
                quiz_game_menu()

            case "0":
                game_loop = False

            case "00":
                running = False

    return running

def snake_game_menu():
    snake_game = """
============WELCOME TO SNAKE GAME======================
          Select Game Level
1. Easy

2. Normal

3. Hard
"""
    print(snake_game)
    game_level = input("Enter game level: ")

    if game_level == "1":
        print("Easy mode,here we go !!!!!!!")

    if game_level == "2":
        print("Normal mode, is getting interesting !!!!!!")

    if game_level == "3":
        print("Hard mode, you can do this  !!!!!!")

    if game_level >= "4":
        print("level not found !!!!!!")

def bounce_ball_game_menu():
    bounce_ball_game = """
===========WELCOME TO BOUNCE BALL GAME================

         Select Game Level

1. Level one

2. Level two

3. Level three
"""
    print(bounce_ball_game)
    game_level = input("Enter game level: ")

    if game_level == "1":
        print("it's just getting started !!!!!!!")

    if game_level == "2":
        print("now it's getting interesting !!!!!!")

    if game_level == "3":
        print("Let see how far you can go  !!!!!!")

    if game_level >= "4":
        print("hoops! level not found")

def quiz_game_menu():
    quiz_game1 = """
===============QUIZ TIME !!!!!!==================

There are two(5) questions only, so try your luck.

Use number to answer the questions(1,2, or 3).

EYES WILL NOT PUSH US oooo.....
          QUESTION 1
 WHIICH NUMBER IS BOTH A PERFECT SQUARE AND A PERFECT CUBE?

1. 625

2. 144

3. 729
"""
    print(quiz_game1)
    answer1 = input("Enter your answer: ")

    if answer1 == "1":
        print("Wrong !!,")
        print("Correct answer: 729")

    if answer1 == "2":
        print("Wrong !!,")
        print("Correct answer: 729")

    if answer1 == "3":
        print("CORRECT !!!!!!")

    if answer1 >= "4":
        print("Option not found")

    print()

    quiz_game2 = """
          QUESTION 2
 WHICH TREATY FORMALLY ENDED THE THIRTY YEARS' WAR IN 1648?

1. Treaty of Versailles

2. Treaty of Westphalia

3. Treaty of Tordesillas
"""
    print(quiz_game2)
    answer2 = input("Enter your answer: ")

    if answer2 == "1":
        print("Wrong !!,")
        print("Correct is answer: Treaty of Westphalia")

    if answer2 == "2":
        print("CORRECT !!!!!!")

    if answer2 == "3":
        print("Wrong !!,")
        print("Correct is answer: Treaty of Westphalia")

    if answer2 >= "4":
        print("Option not found")

    print()

    quiz_game3 = """
             QUESTION   3

What unique design feature defines the physical appearance of the Nokia 5510?

1. A sliding touch panel

2. A full QWERTY keyboard split across both sides of the screen

3. A circular rotary dialing pad

4. A completely buttonless frame
"""
    print(quiz_game3)
    answer3 = input("Enter your answer: ")

    if answer3 == "1":
        print("Wrong !!,")
        print("Correct is answer: [2]")

    if answer3 == "2":
        print("CORRECT !!!!!!")

    if answer3 == "3":
        print("Wrong !!,")
        print("Correct is answer: [2]")

    if answer3 >= "4":
        print("Option not found")

    print()

    quiz_game4 = """
             QUESTION   4

Borrowed from the classic Nokia 3310, what is the screen resolution of the Nokia 5510?

1.  84 x 48 pixels

2.  128 x 128 pixels

3.  176 x 220 pixels

4.  320 x 240 pixels
"""
    print(quiz_game4)
    answer4 = input("Enter your answer: ")

    if answer4 == "1":
        print("CORRECT !!!!!!")

    if answer4 == "2":
        print("Wrong !!,")
        print("Correct is answer: [1]")

    if answer4 == "3":
        print("Wrong !!,")
        print("Correct is answer: [1]")

    if answer4 == "4":
        print("Wrong !!,")
        print("Correct is answer: [1]")

    if answer4 >= "5":
        print("Option not found")

    print()

    quiz_game5 = """
             QUESTION   5

 Which technology did the Nokia 5510 use to browse primitive W.A.P internet pages?

1. G.P.R.S (General Packet Radio Service)

2. C.S.D (Circuit-Switched Data at 9.6 k.b.p.s)

3. Wi-Fi 1.0

4. 3G U.M.T.S
"""
    print(quiz_game5)
    answer5 = input("Enter your answer: ")

    if answer5 == "1":
        print("Wrong !!,")
        print("Correct is answer: [2]")

    if answer5 == "2":
        print("CORRECT !!!!!!")

    if answer5 == "3":
        print("Wrong !!,")
        print("Correct is answer: [2]")

    if answer5 == "4":
        print("Wrong !!,")
        print("Correct is answer: [2]")

    if answer5 >= "5":
        print("Option not found")

def music_menu(running):
    music_loop = True

    while music_loop and running:
        music = """
 ========MUSICS========

1. Recorder

2. Radio

3. track list

0. Back to main menu
00. Exit application
"""
        print(music)
        music_tracks = input("Enter music list of your choice: ")

        match music_tracks:
            case "1":
                recorder_menu()

            case "2":
                radio_menu()

            case "3":
                track_list_menu()

            case "0":
                music_loop = False

            case "00":
                running = False

    return running

def recorder_menu():
    recorder = """
     =====Recorder=====

      EMPTY LIST
"""
    print(recorder)

def radio_menu():
    radio = """
     ====Radio====

  EMPTY FREQUENCY LIST

  *   *   *    *   *   *   *   *
 *   *   *    *   *   *   *   *

"""
    print(radio)

def track_list_menu():
    track_list = """
   ===Track list===

   EMPTY TRACK LIST !!
"""
    print(track_list)

def tones_menu(running):
    tones_loop = True

    while tones_loop and running:
        ringtones = """
=======RING TONES========

  Select ring tone

1. Groovy blue

2. Merry X mas

3. Tape dance

4. Ring Ring

5. Mozart 40

6. Rocket

7. Play ground

8. Tick Tick

9. sunny walks

10.Toreador

0. Back to main menu
00. Exit application
"""
        print(ringtones)
        ringtone = input("Enter option: ")

        match ringtone:
            case "1":
                print("Rhythmic, blue inspired upbeat tune ")
                print("RINGING.....RINGING......RINGING.......")

            case "2":
                print("A festive holiday jingle")
                print("RINGING.....RINGING......RINGING.......")

            case "3":
                print("A rhythmic percussive tape pattern")
                print("RINGING.....RINGING......RINGING.......")

            case "4":
                print(" A standard telephone ring stimulation ")
                print("RINGING.....RINGING......RINGING.......")

            case "5":
                print("classic excerpt from Mozart symphony NO.40")
                print("RINGING.....RINGING......RINGING.......")

            case "6":
                print(" Rising pitch sound effect")
                print("RINGING.....RINGING......RINGING.......")

            case "7":
                print("A light cheerful chime like tone")
                print("RINGING.....RINGING......RINGING.......")

            case "8":
                print("A fast clock ticking alert")
                print("RINGING.....RINGING......RINGING.......")

            case "9":
                print("A smooth relaxing walking tempo tune")
                print("RINGING.....RINGING......RINGING.......")

            case "10":
                print("A dramatic march melody from Carmel")
                print("RINGING.....RINGING......RINGING.......")

            case "0":
                tones_loop = False

            case "00":
                running = False

            case _:
                print("option not found")

    return running

def clock_menu(running):
    clock_loop = True

    while clock_loop and running:
        clock = """
->->->->->->-> CLOCK <-<-<-<-<-<-<-<-<-

         Time is like a piece of gold
                select
1. Alarm

2. Clock

3. Timer

0. Back to main menu
00. Exit application
"""
        print(clock)
        world_clock = input("Enter your option: ")

        match world_clock:
            case "1":
                alarm_menu()

            case "2":
                clock_setting_menu()

            case "3":
                timer_menu()

            case "0":
                clock_loop = False

            case "00":
                running = False

    return running

def alarm_menu():
    alarm = """
       ALARM

      EMPTY LIST

      ADD ALARM
"""
    print(alarm)

def clock_setting_menu():
    clock_setting = """
         CLOCK

      EMPTY LIST
"""
    print(clock_setting)

def timer_menu():
    timer = """
        TIMER

      EMPTY LIST

        ADD TIMER
"""
    print(timer)

def reminders_menu(running):
    reminder_loop = True

    while reminder_loop and running:
        reminders = """
 =========REMINDER=========

1. Add New

2. Erase

3. View  Edit

4. Edit Tone

0. Back to main menu
00. Exit application
"""
        print(reminders)
        system_reminder = input("Enter your option: ")

        match system_reminder:
            case "1":
                add_new_menu()

            case "2":
                erase_menu()

            case "3":
                view_edit_menu()

            case "4":
                running = edit_tone_menu(running)

            case "0":
                reminder_loop = False

            case "00":
                running = False

    return running

def add_new_menu():
    add_new = """
        ADD NEW

  EMPTY  TIME AND CLOCK
"""
    print(add_new)

def erase_menu():
    erase = """
      EMPTY  ADD NEW

     TO BE ERASE
"""
    print(erase)

def view_edit_menu():
    view_edit = """
   NO EXISTING REMINDER
    OR TEXT CONTENT
         FOUND
"""
    print(view_edit)

def edit_tone_menu(running):
    edit_tone_loop = True

    while edit_tone_loop and running:
        edit_tone = """
        EDIT TONE

1. Groovy blue

2. Merry X mas

3. Tape dance

4. Ring Ring

5. Mozart 40

6. Rocket

7. Play ground

8. Tick Tick

9. sunny walks

10.Toreador

0. Back to reminders
00. Exit application
"""
        print(edit_tone)
        edit_ringtone = input("Enter option: ")

        match edit_ringtone:
            case "1":
                print("Rhythmic, blue inspired upbeat tune ")
                print("RINGING.....RINGING......RINGING.......")

            case "2":
                print("A festive holiday jingle")
                print("RINGING.....RINGING......RINGING.......")

            case "3":
                print("A rhythmic percussive tape pattern")
                print("RINGING.....RINGING......RINGING.......")

            case "4":
                print(" A standard telephone ring stimulation ")
                print("RINGING.....RINGING......RINGING.......")

            case "5":
                print("classic excerpt from Mozart symphony NO.40")
                print("RINGING.....RINGING......RINGING.......")

            case "6":
                print(" Rising pitch sound effect")
                print("RINGING.....RINGING......RINGING.......")

            case "7":
                print("A light cheerful chime like tone")
                print("RINGING.....RINGING......RINGING.......")

            case "8":
                print("A fast clock ticking alert")
                print("RINGING.....RINGING......RINGING.......")

            case "9":
                print("A smooth relaxing walking tempo tune")
                print("RINGING.....RINGING......RINGING.......")

            case "10":
                print("A dramatic march melody from Carmel")
                print("RINGING.....RINGING......RINGING.......")

            case "0":
                edit_tone_loop = False

            case "00":
                running = False

            case _:
                print("option not found")

    return running

def sim_service_menu():
    sim_service = """
 =====SIM SERVICE=====

INSERT YOUR SIM

"""
    print(sim_service)

def service_menu():
    service = """
      SERVICE
"""
    print(service)

def password_menu():
    print()
    print("===========WELCOME TO NOKIA 5510=============")

    print()
    print("***CREATE A PASSWORD*****")
    print()

    first_password = input("Enter your password: ")

    print()
    user_password = first_password

    while True:
        password = input("****CONFIRM THE PASSWORD*******\n ")

        if password == user_password:
            break

        else:
            print()
            print("ENTER THE CORRECT PASSWORD")
            print()

    return user_password

def main():
    running = True

    user_password = password_menu()

    print()
    print("INSERT A SIM")

    running = main_menu(running)

    return running

main()

