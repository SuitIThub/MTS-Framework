##########################
# region Intro ----- #
##########################

# Called once from `label start` after all loaders ran.
# Replace this with your own opening.
label intro ():
    subtitles "All characters and events in this game are entirely fictional."

    $ school_name = renpy.input("Please name your School: (Default: \"Example Academy\")")
    $ school_name = school_name.strip() or "Example Academy"

    $ set_game_data("school_name", school_name)

    $ default_first_name, default_last_name = default_names['headmaster']

    $ headmaster_first_name = renpy.input("First name of your Character: (Default \"[default_first_name]\")")
    $ headmaster_first_name = headmaster_first_name.strip() or default_first_name

    $ headmaster_last_name = renpy.input("Last name of your Character: (Default \"[default_last_name]\")")
    $ headmaster_last_name = headmaster_last_name.strip() or default_last_name

    $ set_name("headmaster", headmaster_first_name, headmaster_last_name)

    # starting levels of the stat holders (see load_schools)
    $ set_level_for_char(1, "school", charList)
    $ set_level_for_char(1, "teacher", charList["staff"])
    $ set_level_for_char(1, "parent", charList)
    $ set_level_for_char(1, "secretary", charList["staff"])

    # 100 experience = proficiency level 1
    $ set_headmaster_proficiency_level('math', 100)

    $ time.set_time(day = intro_end_date[0], month = intro_end_date[1], year = intro_end_date[2], daytime = 1)
    $ update_intro_flag()

    secretary "Welcome to [school_name], headmaster. Let's get to work."

    jump map_entry

# endregion
##########################
