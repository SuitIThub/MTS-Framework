init -6 python:
    import re
    from itertools import product
    from deprecated import deprecated

    registered_vote_events = []

    ########################
    # region legacy stubs -- #
    ########################

    @deprecated(version='0.2.3', reason="Legacy journal vote proposal; kept for save compatibility.")
    class PTAProposal:
        """
        Legacy PTA proposal wrapper for old journal vote scheduling.

        Kept so existing saves can unpickle. Cleared on load via
        ``clean_legacy_vote_proposal``. New content stores a live
        ``Unlockable`` in ``voteProposal`` instead.
        """

        def __init__(self, journal_obj=None, action: str = "unlock"):
            self._journal_obj = journal_obj
            self._action = action

    def clean_legacy_vote_proposal():
        """
        Drop legacy ``PTAProposal`` (or other non-Unlockable) values from
        ``voteProposal`` so old saves do not keep obsolete scheduled votes.
        """
        proposal = get_game_data("voteProposal")
        if proposal is not None and not isinstance(proposal, Unlockable):
            set_game_data("voteProposal", None)

    # endregion
    ########################

    ##############################
    # region probability methods #
    ##############################

    def get_end_choice(*votes: str) -> str:
        """
        Gets the end choice based on the votes.

        Args:
            *votes (str): ``\"yes\"``, ``\"no\"``, ``\"ignore\"``, or ``\"veto\"``.

        Returns:
            str: ``\"yes\"``, ``\"no\"``, or ``\"veto\"``.
        """

        if len(votes) == 0:
            return 'no'
        if 'veto' in votes:
            return 'veto'
        elif votes.count('yes') + votes.count('ignore') >= len(votes) / 2:
            return 'yes'
        else:
            return 'no'

    # endregion
    ##############################

###################################
# region PTA Event Registry ----- #
###################################

init -1 python:
    pta_discussion_storage = FragmentStorage("pta_discussion")
    pta_vote_storage = FragmentStorage("pta_vote")
    pta_end_storage = FragmentStorage("pta_end")

init 1 python:

    pta_meeting_event = EventComposite(2, "pta_meeting", [pta_discussion_storage, pta_vote_storage, pta_end_storage], 
        TimeCondition(weekday = 5, daytime = 1),
        PTAObjectSelector("vote_proposal"),
        Pattern("base", "images/events/pta/regular meeting/pta <secretary_level> <school_level> <step>.webp"))

    # PTA discussions
    pta_discussion_1_event = EventFragment(3, "pta_discussion_1")
    
    pta_discussion_storage.add_event(
        pta_discussion_1_event
    )

    pta_vote_unregistered_1_event = EventFragment(2, "pta_vote_unregistered_1",
        JournalNRVoteCondition(),
        Pattern("vote", "images/events/pta/regular meeting/pta_vote <school_level> <name>.webp"))

    pta_vote_nothing_1_event = EventFragment(2, "pta_vote_nothing_1",
        CompareCondition("vote_proposal", None))

    pta_vote_storage.add_event(
        pta_vote_unregistered_1_event,
        pta_vote_nothing_1_event,
    )

    # PTA end meeting
    pta_end_meeting_1_event = EventFragment(2, "pta_end_meeting_1")
    
    pta_end_storage.add_event(
        pta_end_meeting_1_event
    )


    time_check_events.add_event(
        pta_meeting_event, 
    )

# endregion
###################################

###############################
# region Regular Events ----- #
###############################

label pta_meeting (**kwargs):
    $ begin_event(no_gallery = True, **kwargs)

    $ schoolLevel = get_level("school_level")
    $ secretaryLevel = get_level("secretary_level")

    $ kwargs = load_kwargs_values(kwargs, schoolLevel = schoolLevel, secretaryLevel = secretaryLevel)
    $ image = convert_pattern("base", **kwargs)

    $ image.show(0)
    subtitles "You enter the conference room."
    subtitles "All representatives already gathered and wait for you."
    $ image.show(1)
    headmaster "Thank you all for gathering today."

    $ image.show(2)
    headmaster "First point for today. Does someone have anything to discuss today?"

    call composite_event_runner(**kwargs) from _call_composite_event_runner_pta_meeting_1

#####################
# region DISCUSSION #

label pta_discussion_1 (**kwargs):
    $ begin_event(no_gallery = True, **kwargs)


    $ image.show(3)
    headmaster "No? Alright then lets jump straight to the next point."

    $ end_event('new_daytime', **kwargs)

# endregion
#####################

###############
# region VOTE #

label pta_vote_nothing_1 (**kwargs):
    $ begin_event(no_gallery = True, **kwargs)

    $ end_event('new_daytime', **kwargs)

label pta_vote_unregistered_1 (**kwargs):
    $ begin_event(no_gallery = True, **kwargs)

    $ unlockable = get_value("vote_proposal", **kwargs)
    if not isinstance(unlockable, Unlockable):
        $ end_event('new_daytime', **kwargs)

    $ votes = unlockable.roll_votes()
    $ end_choice = get_end_choice(*votes)
    $ obj_title = unlockable.get_title()
    $ obj_type = unlockable.type_key
    $ obj_desc = unlockable.get_descriptions()
    $ vote_probability = int(unlockable.get_vote_probability() * 100)

    $ image = convert_pattern("base", **kwargs)

    $ image.show(4)
    if obj_type == "rule":
        headmaster "Today I want to put to vote a change in the schools ruleset."
        headmaster "I want to implement the Rule: [obj_title]."
    elif obj_type == "club":
        headmaster "Today I want to put to vote if we want to open a new club at the school."
        headmaster "I want to open the [obj_title]."
    elif obj_type == "building":
        headmaster "Today I want to put to vote on the [obj_title]."
    else:
        headmaster "Today I want to put [obj_title] to a vote."

    $ image.show(5)
    $ pta_desc_i = 0
    while pta_desc_i < len(obj_desc):
        $ desc_text = obj_desc[pta_desc_i]
        headmaster "[desc_text]"
        $ pta_desc_i += 1

    $ image.show(6)
    headmaster "Support among the stakeholders sits at about [vote_probability] percent."
    headmaster "Please cast your vote now."

    $ image.show(7)
    $ yes_count = votes.count("yes")
    $ no_count = votes.count("no")
    headmaster "The ballots are in. [yes_count] in favor, [no_count] against."

    call pta_vote_result(unlockable, end_choice, True) from _call_pta_vote_result_unregistered_1

    $ end_event('new_daytime', **kwargs)

# endregion
###############

##############
# region END #

label pta_end_meeting_1 (**kwargs):
    $ begin_event(no_gallery = True, **kwargs)

    $ image = convert_pattern("base", **kwargs)

    $ image.show(7)
    headmaster "It seems like that's all we have for today."
    headmaster "I thank you all for coming."

    $ end_event('new_daytime', **kwargs)

# endregion
##############

label pta_vote_result (unlockable, end_choice, with_comment = False):

    if not isinstance(unlockable, Unlockable):
        $ set_game_data('voteProposal', None)
        return

    $ obj_title = unlockable.get_title()

    if end_choice == 'yes':
        if with_comment:
            headmaster "With the majority of votes in favor, the proposal is accepted."

        $ set_game_data(unlockable.key + "_vote_won", True)
        $ unlockable.check_resolutions()
        if unlockable.is_unlocked():
            $ add_notify_message(f"{obj_title} has been unlocked.")
    else:
        if with_comment:
            headmaster "The proposal is rejected due to the majority of votes against it."
        $ unlockable.release_vote_money()
        $ unlockable.apply_vote_failure_penalty()

    $ unlockable.release_schedule_vote_measure()
    $ set_game_data('voteProposal', None)

    return

# endregion
###############################
