init -98 python:
    cheat_mode = False
    nude_vision = 2
    sfw_mode = False
    event_selection_mode = False
    INT64_MAX = 2**63 - 1

    location_event_register = {}
    event_register = {}
    event_register_by_max_level = {}
    fragment_storage_register = {}

    # Optional remote files, downloaded on start when the player allows it in
    # the options (see download_members / download_message). Empty = disabled.
    members_url = ""
    message_url = ""

    members = ""
    download_members()

    message = ""
    download_message()

    # get_mod_list()
    
    repair_mod_list()
    available_keys = ['base']
    active_mod_key = ''
    mod_count = {}

    translation_texts = {}

    start_methods = []

init -95 python:
    get_translations()

default hide_gui = False

# (day, month, year) the free roam starts; before it the "intro" flag is set,
# which pauses flag-bound events and situations (see the Events wiki).
define intro_end_date = (1, 1, 2023)

default rules = {}
default buildings = {}
default clubs = {}
default charList = {
    'staff': {},
}

default person_storage = {}

default quests = {}
default all_quests = {}
default goals = {}
default tasks = {}
default task_check = {}
default category_quest = {}

default money = Stat(MONEY, 1000)

default reserved_money = {}

default time = Time()
default stat_data = {}

default gameData = {}
default is_in_replay = False
default replay_data = {}

default event_data = {}

default dialogue_manager = None
default quest_manager = None

default inventory_manager = None

default shopping_cart = {}
default item_delivery = {}
default item_purchases = {}

default last_daytime = None
default last_daytime_by_key = {}

default overview_events_available = {
    'school_building':  False,
    'office_building':  False}
default overview_highlight_available = {
    'school_building':  False,
    'office_building':  False}


# map ambience (see map_overview)
define audio.forest_ambience = "forest-ambience.mp3"
define audio.night_ambience = "night-ambience.mp3"

default available_proficiencies = ['math']
default headmaster_proficiencies = {}

init -99:
    default default_names = {
        'headmaster': ('Alex', 'Smith'),
        'secretary': ('Sam', 'Taylor'),
        'vendor': ('Vendor', ''),
    }

    default headmaster_first_name = default_names['headmaster'][0]
    default headmaster_last_name = default_names['headmaster'][1]

    define character.dev = Character(
        "Developer",
        # window_background = get_textbox(),
        who_color = "#00ff11",
        what_color = "#ffffff",
        what_size = 28,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.headmaster = Character(
        "[headmaster_first_name] [headmaster_last_name]",
        #window_background = None,
        who_color = "#ffffff",
        what_color = "#ffffff",
        what_size = 28,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.headmaster_whisper = Character(
        "[headmaster_first_name] [headmaster_last_name]",
        #window_background = None,
        who_color = "#ffffff",
        what_color = "#ffffff",
        what_size = 28,
        what_italic = True,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.headmaster_shout = Character(
        "[headmaster_first_name] [headmaster_last_name]",
        who_suffix = " (shouting)",
        #window_background = None,
        who_color = "#ffffff",
        what_color = "#ffffff",
        what_size = 28,
        what_bold = True,
        # what_outlines=[( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.headmaster_thought = Character(
        "[headmaster_first_name] [headmaster_last_name]",
        who_suffix = " (thinking)",
        #window_background = None,
        who_color = "#ffffff",
        what_color = "#ffffff",
        what_size = 28,
        what_italic = True,
        what_prefix = "(  ",
        what_suffix = "  )",
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.secretary = Character(
        "Sam Taylor",
        #window_background = None,
        who_color = "#c71585",
        what_color = "#ffffff",
        what_size = 28,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.secretary_whisper = Character(
        "Sam Taylor",
        who_suffix = " (whispering)",
        #window_background = None,
        who_color = "#c71585",
        what_color = "#ffffff",
        what_size = 28,
        what_italic = True,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.secretary_shout = Character(
        "Sam Taylor",
        who_suffix = " (shouting)",
        #window_background = None,
        who_color = "#c71585",
        what_color = "#ffffff",
        what_size = 28,
        what_bold = True,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.teacher = Character(
        "Teacher",
        #window_background = None,
        who_color = "#00ced1",
        what_color = "#ffffff",
        what_size = 28,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.teacher_shout = Character(
        "Teacher", 
        who_suffix = " (shouting)",
        #window_background = None,
        who_color = "#00ced1",
        what_color = "#ffffff",
        what_size = 28,
        what_bold = True,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.teacher_whisper = Character(
        "Teacher", 
        who_suffix = " (whispering)",
        #window_background = None,
        who_color = "#00ced1",
        what_color = "#ffffff",
        what_size = 28,
        what_italic = True,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )

    define character.vendor = Character(
        "Vendor",
        #window_background = None,
        who_color = "#601561",
        what_color = "#ffffff",
        what_size = 28,
        # what_outlines = [( 1, "#000000", 0, 0)],
        retain = False,
    )

    define character.parent = Character(
        "Parent",
        #window_background = None,
        who_color = "#e6e6fa",
        what_color = "#ffffff",
        what_size = 28,
        # what_outlines = [( 1, "#000000", 0, 0)],
        retain = False,
    )
    define character.examiner = Character(
        "Examiner",
        #window_background = None,
        who_color = "#f5deb3",
        what_color = "#ffffff",
        what_size = 28,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.regional = Character(
        "Region Manager",
        #window_background = None,
        who_color = "#4169e1",
        what_color = "#ffffff",
        what_size = 28,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.sgirl = Character(
        "School Girl",
        #window_background = None,
        who_color = "#8a2be2",
        what_color = "#ffffff",
        what_size = 28,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.sboy = Character(
        "School Boy",
        #window_background = None,
        who_color = "#008000",
        what_color = "#ffffff",
        what_size = 28,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.crowd = Character(
        "Crowd",
        #window_background = None,
        what_color = "#ffd700",
        what_size = 28,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.crowd_whisper = Character(
        "Crowd",
        who_suffix = " (whispering)",
        #window_background = None,
        what_color = "#ffd700",
        what_size = 28,
        what_italics = True,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.crowd_shout = Character(
        "Crowd",
        who_suffix = " (shouting)",
        #window_background = None,
        what_color = "#ffd700",
        what_size = 28,
        what_bold = True,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
    )
    define character.subtitles = Character(
        None,
        #window_background = None,
        what_color = "#ffffff",
        what_size = 28,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
        what_xalign = 0.5,
        what_textalign = 0,
        what_layout = 'subtitle'
    )
    define character.subtitles_Empty = Character(
        None,
        window_background = None,
        what_color = "#ffffff",
        what_size = 28,
        # what_outlines = [( 1, "#000000", 0, 0 )],
        retain = False,
        what_xalign = 0.5,
        what_textalign = 0,
        what_layout = 'subtitle'
    )

    define character.nv_text = Character(None, kind=nvl, what_text_align=0.5, what_xalign=0.5)
