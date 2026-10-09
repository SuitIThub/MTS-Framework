# The quest system is archived; no quest definitions ship with the framework.
# load_quests is a no-op for call-site / start-flow compatibility.

label load_quests:
    if not quest_manager:
        $ quest_manager = QuestManager()
    return
