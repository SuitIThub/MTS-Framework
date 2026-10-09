##############################################
# region Office Building Event Handler ----- #
##############################################

init -1 python:
    set_current_mod('base')

    # general event for the office building
    office_building_general_event = EventStorage("office_building", "office_building", fallback = Event(2, "office_building.after_general_check"))
    register_highlighting(office_building_general_event)

    #### Office Building Work Events
    # available targets: money, education, reputation
    office_building_work_event = {}
    add_storage(office_building_work_event, EventStorage("money",       "office_building"))
    add_storage(office_building_work_event, EventStorage("education",   "office_building"))
    add_storage(office_building_work_event, EventStorage("reputation",  "office_building"))

    #### Office Building Computer Events
    # available targets: shopping
    office_building_computer_event = {}
    add_storage(office_building_computer_event, EventStorage("shopping", "office_building"))

    #### Office Building Events
    # available targets: look_around, work, learn, computer
    office_building_events = {}
    add_storage(office_building_events, EventStorage("look_around",      "office_building"))
    add_storage(office_building_events, EventStorage("work",             "office_building"))
    add_storage(office_building_events, EventStorage("learn",            "office_building", ShowBlockedOption()))
    add_storage(office_building_events, EventStorage("computer",         "office_building"))

    #### Office Building Subject Learn Events
    # available targets: math
    office_building_subject_learn_events = {}
    add_storage(office_building_subject_learn_events, EventStorage("math",    "office_building", fallback_text = "There is nobody here."))

    office_building_bg_images = BGStorage("images/background/office building/bg.webp")

init 1 python:
    set_current_mod('base')

    office_building_events["computer"].add_event(
        EventSelect(3, "computer_event", "What do you want to do?", office_building_computer_event,
            TimeCondition(weekday = "d", daytime = "d"))
    )

    office_building_events["work"].add_event(
        EventSelect(3, "work_office_event", "What do you want to work on?", office_building_work_event,
            TimeCondition(weekday = "d", daytime = "d"),
            override_menu_exit = 'office_building')
    )

    office_building_subject_learn_events['math'].add_event(
        Event(3, "learn_office_event_1", ProficiencyCondition("math", level = "10-"), ValueSelector('subject', 'math')))

    office_building_events["learn"].add_event(
        EventSelect(3, "learn_subject_event", "What subject do you wanna learn?", office_building_subject_learn_events,
            TimeCondition(daytime = 1),
            MoneyCondition(500),
            override_menu_exit = 'office_building'))

    office_building_work_event["money"].add_event(
        Event(3, "work_office_money_event_1",
            TimeCondition(weekday = "d", daytime = "d")))

    office_building_work_event["education"].add_event(
        Event(3, "work_office_education_event_1",
            TimeCondition(weekday = "d", daytime = "d")))

    office_building_work_event["reputation"].add_event(
        Event(3, "work_office_reputation_event_1",
            TimeCondition(weekday = "d", daytime = "d")))

# endregion
##############################################

############################################
# region Office Building Entry Point ----- #
############################################

label office_building ():
    call call_available_event(office_building_general_event) from office_building_4


label .after_general_check (**kwargs):
    call call_event_menu (
        "What do you do?",
        office_building_events,
        default_fallback,
        character.subtitles,
        bg_image = office_building_bg_images,
    ) from office_building_3

    jump office_building

# endregion
############################################

##########################
# region Computer Events #

label office_building_computer_shopping_event(**kwargs):
    $ begin_event(no_gallery = True, **kwargs)
    
    $ shopping_cart = {}

    call screen office_building_computer_shopping_screen()

label .after_computer_shopping_screen(**kwargs):

    $ end_event("map_overview", **kwargs)


# endregion
##########################

######################
# region Work Events #

label work_office_reputation_event_1 (**kwargs):
    $ begin_event(**kwargs)

    subtitles "You decided to to some PR work, trying to improve the schools and your reputation."
    call screen black_screen_text("1h later.")
    headmaster.think "I think I found a way to make the school more appealing to the public."
    headmaster.think "I hope this will help to improve the reputation of the school."

    call change_stats_with_modifier(reputation = SMALL) from _call_change_stats_with_modifier_38

    $ end_event('new_daytime', **kwargs)

label work_office_money_event_1 (**kwargs):
    $ begin_event(**kwargs)

    subtitles "You work on checking the accounts of the school."
    call screen black_screen_text("1h later.")
    # headmaster is consumed by the terrible accounting done in the past
    headmaster.think "How can this be? This is a mess!"
    headmaster.think "I need to get this sorted out."
    headmaster.think "There is so much wrong with these accounts. It's gonna take ages to fix this."
    headmaster.think "At least I was able to find some money that was lost in the system."

    call change_money_with_modifier(get_random_int(100, 500)) from _call_change_money_with_modifier

    $ end_event('new_daytime', **kwargs)

label work_office_education_event_1 (**kwargs):
    $ begin_event(**kwargs)

    subtitles "You work on optimizing the teaching material for the students."
    call screen black_screen_text("1h later.")
    headmaster.think "I think I found a way to make the material more interesting for the students."

    call change_stats_with_modifier(
        education = SMALL, happiness = TINY) from _call_change_stats_with_modifier_39
    call change_stats_with_modifier(
        happiness = SMALL, education = SMALL) from _call_change_stats_with_modifier_40

    $ end_event('new_daytime', **kwargs)

label learn_office_event_1 (**kwargs):
    $ begin_event(no_gallery = True, **kwargs)

    $ subject = get_value('subject', **kwargs)

    $ text = get_translation(subject)

    call screen black_screen_text("You spend the entire day learning more about [text].")

    $ curr_xp = get_headmaster_proficiency_xp(subject)
    $ curr_lvl = get_headmaster_proficiency_level(subject)
    $ delta = 20
    if curr_lvl > 0:
        $ delta = math.ceil(int(100 / (curr_lvl * 10)))
    $ missing = math.floor(get_headmaster_proficiency_xp_until_level(subject))
    if missing == -1:
        $ missing = 100
    $ subtitle = f"XP: {curr_xp:.0f}% -> " + "{color=#00a000}" + f"{(curr_xp + delta):.0f}%" + "{/color}"

    if delta >= missing:
        $ delta = missing
        call screen black_screen_text_with_subtitle("[text]: Lvl. " + str(curr_lvl) + " -> {color=#00a000}" + str(curr_lvl + 1) + "{/color}", "XP: {color=#00a000}100% Level Up!{/color}")
    else:
        call screen black_screen_text_with_subtitle("[text]: Lvl. " + str(curr_lvl), subtitle)

    $ change_headmaster_proficiency_xp(subject, delta)
    call change_money(-500) from _call_change_money

    $ end_event('new_day', **kwargs)

# endregion
######################
