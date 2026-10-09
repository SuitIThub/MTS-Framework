# The game starts here.

label start ():

    $ set_dissolve()

    $ lifecycle_registry.begin_check()

    call load_stats from start_1
    call load_schools from start_2
    call load_characters from start_7
    call load_items from start_8
    call load_pictograms from start_11
    call load_situations from start_9
    call load_unlockables from start_10
    call load_buildings from start_3
    call load_maps from start_12

    $ fix_modifier()
    $ fix_quests()

    $ check_event_selectors()

    $ i = 0
    while i < len(start_methods):
        call expression start_methods[i] from _call_expression_2
        $ i += 1

    # after the mod loaders, so mod-defined items still have their definitions
    $ inventory_manager.check_missing_items()

    if situation_manager is not None:
        $ situation_manager.reconcile_orphan_situations()
    $ lifecycle_registry.finalize_check()

    $ update_intro_flag()

    # label intro is no event, so begin_event hasn't bound the Person speakers yet
    $ bind_event_speakers()

    call intro from _call_intro

label splashscreen:
    menu:
        "This game is not suitable for children or those who are easily disturbed.\n\nBy playing this game you agree that you are 18 years of age or older."

        "I am 18 years of age or older.":
            pass
        "I am not 18 years of age or older.":
            $ renpy.quit()

    return

init python:
    
    ###########################################
    # --- Version Compatibility Functions --- #
    ###########################################

    def fix_quests():
        global quest_manager
        if quest_manager is None:
            quest_manager = QuestManager()
        quest_manager.run_effect_init()
        quest_manager.check_task_type("event")

    def fix_modifier():
        """
        Ensures the default money modifiers exist (also on old saves).
        """

        if get_modifier('monthly_budget', 'money', 'payroll_monthly') == None:
            set_modifier('monthly_budget', Modifier_Obj('Budget', "+", 1000), stat = 'money', collection = 'payroll_monthly')

        if get_modifier('teacher_pay', 'money', 'payroll_weekly') == None:
            set_modifier('teacher_pay', Modifier_Obj('Teacher', "+", -150), stat = 'money', collection = 'payroll_weekly')

    def fix_schools():
        """
        Loads the school stat holder. Called from load_schools and get_school.
        """

        load_character("school", "School", charList, {
            'stats_objects': {
                "corruption": Stat(CORRUPTION, 0),
                "inhibition": Stat(INHIBITION, 100),
                "happiness": Stat(HAPPINESS, 12),
                "education": Stat(EDUCATION, 9),
                "charm": Stat(CHARM, 8),
                "reputation": Stat(REPUTATION, 7),
            }
        })

    def check_event_selectors():
        for event in event_register.values():
            event.check_selectors()

    ###########################################

label after_load:
    $ log_separator()
    $ log_separator()

    $ lifecycle_registry.begin_check()

    call load_stats from after_load_1
    call load_schools from after_load_2
    call load_characters from after_load_7
    call load_items from after_load_8
    call load_pictograms from after_load_11
    call load_situations from after_load_9
    call load_unlockables from after_load_10
    call load_buildings from after_load_4
    call load_maps from after_load_12

    $ clean_legacy_journal_objects()
    $ clean_legacy_quests()

    $ check_event_selectors()

    $ fix_modifier()
    $ fix_quests()
    ####################################

    $ i = 0
    while i < len(start_methods):
        call expression start_methods[i] from _call_expression_3
        $ i += 1

    # after the mod loaders, so mod-defined items still have their definitions
    $ inventory_manager.check_missing_items()

    if situation_manager is not None:
        $ situation_manager.reconcile_orphan_situations()
    $ lifecycle_registry.finalize_check()
    
    if contains_game_data("names") and "headmaster" in get_game_data("names"):
        $ headmaster_first_name = get_game_data("names")["headmaster"][0]
        $ headmaster_last_name = get_game_data("names")["headmaster"][1]

    #################
    # load all events
    $ after_load_event_check('daily', None, time_check_events)
    $ after_load_event_check('office_building', office_building_events, office_building_general_event)
    $ after_load_event_check('school_building', sb_events, sb_general_event)
    #################

    $ update_intro_flag()
    # a save made outside an event may still hold the static Character speakers
    $ bind_event_speakers()
    # situation flags may have changed in code since the save
    if situation_manager is not None:
        $ situation_manager.sync_flag_pauses()

    return

label open_patreon_link_from_menu():
    # """
    # Opens the patreon page in the default browser
    # """

    $ renpy.run(OpenURL(patreon))
    call screen main_menu


label open_discord_link_from_menu():
    # """
    # Opens the discord page in the default browser
    # """

    $ renpy.run(OpenURL(discord))
    call screen main_menu


label open_wiki_link_from_menu():
    # """
    # Opens the wiki page in the default browser
    # """

    $ renpy.run(OpenURL(wiki))
    call screen main_menu