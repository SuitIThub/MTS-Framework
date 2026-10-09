#######################
# region SCREENS -----#
#######################

screen show_building_button(building_key, display, show_type):
    $ map_building = None if building_manager is None else building_manager.get_building(building_key)
    if map_building is not None:
        if display == building_key or display == "x" or building_key in display or (isinstance(display, dict) and building_key in display.keys()):
            if isinstance(display, dict):
                $ show_type = display[building_key]
            $ state = "idle" if show_type == "normal" else show_type
            $ image_text = find_loadable_image(map_building.get_image(state))
            if not image_text and state != "idle":
                $ image_text = find_loadable_image(map_building.get_image("idle"))
            if image_text:
                add image_text:
                    xpos map_building.x_pos ypos map_building.y_pos

screen show_rectangle(xpos, ypos, width, height):
    frame:
        area(xpos, ypos, width, height)


screen show_building_buttons (building, *additions, show_type = "normal", frames = []):
    # """
    # Shows a mockup map of the school with sprites from BuildingManager.

    # Closed buildings are still drawn when highlighted — this is a display tour,
    # not the interactive map (which skips closed buildings with no empty sprite).

    # # Parameters:
    # 1. building: str | List[str] | Dict[str, str]
    #     - The building to highlight.
    #     - If a list is passed, all buildings in the list will be highlighted.
    #     - If a dictionary is passed, the keys are the buildings to highlight and the values are the show_type for each building.
    #     - "x" highlights every registered building.
    # 2. *additions: str
    #     - Additional elements to show.
    #     - "stats": Show the stats bar on the top right.
    #     - "time": Show the time bar on the top right.
    #     - "journal_idle" / "journal_hover": ignored; journal lives in the stats HUD.
    # 3. show_type: str (default: "normal")
    #     - Sprite state to show.
    #     - "normal": idle sprite.
    #     - "red": highlight sprite.
    #     - "white": hover/focus sprite.
    # 4. frames: List[Tuple[int, int, int, int]]
    #     - A list of rectangles to show on the map.
    #     - Each tuple is a rectangle with the format (xpos, ypos, width, height).
    # """

    add "school_map"

    if building_manager is not None:
        for map_building in building_manager.get_buildings():
            use show_building_button(map_building.key, building, show_type)

    for rect in frames:
        use show_rectangle(*rect)

    if "stats" in additions or "time" in additions:
        use school_overview_stats(interactive=False)

# endregion
#######################
