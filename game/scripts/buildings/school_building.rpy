##############################################
# region School Building Event Handler ----- #
##############################################

init -1 python:
    set_current_mod('base')

    sb_general_event = EventStorage("school_building", "school_building", fallback = Event(2, "school_building.after_general_check"))
    register_highlighting(sb_general_event)

    #### Default school building events
    # available targets: patrol
    sb_events = {}
    add_storage(sb_events, EventStorage("patrol", "school_building", fallback_text = "There is nobody here."))

    sb_bg_images = BGStorage("images/background/school building/bg.webp")

init 1 python:
    set_current_mod('base')

    ####################
    # Example Event
    # Priority 3 = regular event. Conditions decide when it can fire;
    # see the Events and Conditions wiki pages for everything available.
    example_event = Event(3, "example_event",
        TimeCondition(weekday = "d", daytime = "c"),
        LevelCondition("1+", "school"))

    sb_events["patrol"].add_event(example_event)

# endregion
##############################################

############################################
# region School Building Entry Point ----- #
############################################

label school_building ():
    call call_available_event(sb_general_event) from school_building_4

label .after_general_check (**kwargs):
    call call_event_menu (
        "What to do in the School?",
        sb_events,
        default_fallback,
        character.subtitles,
        bg_image = sb_bg_images,
    ) from school_building_3

    jump school_building

# endregion
############################################

#######################################
# region School Building Events ----- #
#######################################

label example_event (**kwargs):
    $ begin_event(**kwargs)

    $ jane = Person["jane_doe"]

    subtitles "You walk through the corridors of the school building."

    jane "Good morning, headmaster!"
    headmaster "Good morning. How are classes going?"

    menu:
        jane "Pretty well, actually. Did you want something?"

        "Encourage her.":
            headmaster "Keep up the good work."
            jane "I will!"
            call change_stats_with_modifier(happiness = SMALL) from _call_change_stats_with_modifier_example_1
        "Send her back to class.":
            headmaster "Off you go, the bell is about to ring."
            call change_stats_with_modifier(education = SMALL) from _call_change_stats_with_modifier_example_2

    $ end_event('new_daytime', **kwargs)

# endregion
#######################################
