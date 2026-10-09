init -1 python:
    set_current_mod('base')
    def after_load_event_check(location: str, events: Dict[str, EventStorage], general_event: EventStorage):
        
        general_event.check_all_events()
        if events != None:
            map(lambda x: x.check_all_events(), events.values())

    after_event_check = Event(2, "time_event_check.after_event_check")

    time_check_events = EventStorage("time_check_events", "misc", fallback = after_event_check)

init 1 python:
    set_current_mod('base')
    new_daytime_event = Event(2, "check_new_daytime",
        DaytimeChangedCondition("daytime"))

    new_day_event = Event(2, "check_new_day",
        TimeCondition(daytime = 1),
        DaytimeChangedCondition("day"))

    new_week_event = Event(2, "check_new_week",
        TimeCondition(weekday = 1, daytime = 1),
        DaytimeChangedCondition("week"))

    new_month_event = Event(2, "check_new_month",
        TimeCondition(day = 1, daytime = 1),
        DaytimeChangedCondition("month"))

    new_year_event = Event(2, "check_new_year",
        TimeCondition(day = 1, month = 1, daytime = 1),
        DaytimeChangedCondition("year"))

    game_over_happiness_event = Event(1, "game_over_happiness", 
        StatCondition(happiness = "0-"))

    game_over_education_event = Event(1, "game_over_education", 
        StatCondition(education = "0-"))

    game_over_reputation_event = Event(1, "game_over_reputation", 
        StatCondition(reputation = "0-"))

    check_prof_event = Event(2, "check_missing_proficiencies",
        NOT(ProficiencyCondition('math')))

    time_check_events.add_event(
        new_daytime_event,
        new_day_event,
        new_week_event,
        new_month_event,
        new_year_event,
        game_over_happiness_event,
        game_over_education_event,
        game_over_reputation_event,
    )
    

############################
# region Daily Check ----- #
############################

label time_event_check ():
    hide screen school_overview_map
    hide screen school_overview_stats
    hide screen school_overview_buttons

    # Before the time events, so the first post-intro morning already runs without
    # the intro flag. Here and not in new_day: a day can also change in new_daytime
    # (night -> morning), which never passes new_day.
    $ update_intro_flag()

    call empty_label from time_event_check_1

label .after_temp_event_check (**kwargs):

    call call_available_event(time_check_events, 0, True) from time_event_check_2

label .after_event_check (**kwargs):
    return

# endregion
############################

#############################
# region Game Over Events - #
#############################

label game_over_happiness (**kwargs):
    $ begin_event()

    show screen black_error_screen_text ("")

    nvl clear

    nv_text "The students happiness plunged to an all-time low."
    nv_text "The students are revolting and protesting against you, demanding the school board to fire you."
    nv_text "The school board has no choice but to fire you."
    nv_text "You are now unemployed and have to find a new job."

    $ MainMenu(confirm=False)()
label game_over_education (**kwargs):
    $ begin_event()

    show screen black_error_screen_text ("")

    nvl clear

    nv_text "The school board noticed the lack of education and the low grades of the students."
    nv_text "They decided to fire you and hire a new headmaster."

    $ MainMenu(confirm=False)()

label game_over_reputation (**kwargs):
    $ begin_event()

    show screen black_error_screen_text ("")
    
    nvl clear

    nv_text "Your bad reputation made it into the news."
    nv_text "The school board put under pressure by the public, decided to fire you."

    $ MainMenu(confirm=False)()

label check_missing_proficiencies:
    # $ begin_event(no_gallery = True, **kwargs)

    $ hide_all()

    $ call_custom_menu_with_text("The headmaster has no proficiencies set. Please assign a proficiency to the headmaster.", character.subtitles, False,
        MenuElement("Math", "Math", SetProficiencyEffect('math', level = 1), "math" not in headmaster_proficiencies.keys()),
    override_menu_exit = "map_entry")

# endregion
#############################

###################################
# region Daily Check Events ----- #
###################################

label check_new_daytime (**kwargs):
    call change_stats_via_modifier('daytime_change') from _call_change_daytime_via_modifier
    $ situation_manager.check_passives(**kwargs)
    $ situation_manager.check_resolutions(**kwargs)
    call drain_situation_events from _call_drain_situation_events_new_daytime
    return

label check_new_day (**kwargs):
    $ situation_manager.tick_resolution_breather()
    call change_stats_via_modifier('daily') from _call_change_daily_via_modifier
    $ situation_manager.check_passives(**kwargs)
    $ situation_manager.check_resolutions(**kwargs)
    call drain_situation_events from _call_drain_situation_events_new_day
    return

label check_new_week (**kwargs):
    call change_stats_via_modifier('weekly') from _call_change_weekly_via_modifier
    call change_stats_via_modifier('payroll_weekly') from _call_change_payroll_weekly_via_modifier
    return

label check_new_month (**kwargs):
    call change_stats_via_modifier('monthly') from _call_change_monthly_via_modifier
    call change_stats_via_modifier('payroll_monthly') from _call_change_payroll_monthly_via_modifier
    # $ change_stat(MONEY, 1000)

    return

label check_new_year (**kwargs):
    call change_stats_via_modifier('yearly') from _call_change_yearly_via_modifier
    call change_stats_via_modifier('payroll_yearly') from _call_change_payroll_yearly_via_modifier
    # $ change_stat(MONEY, 1000)

    return

# endregion
###################################