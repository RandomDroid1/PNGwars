################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on
    ## the phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-
## game menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')
            textbutton _("notes") action ShowMenu('notebook')

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        textbutton _("Notebook") action ShowMenu("notebook")
        
        textbutton _("Attributions") action ShowMenu("attributions")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of
            ## the buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better
## suit themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can
                ## be added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character,
                        ## if set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
                textbutton _(device)
            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")



screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0

#####################################
# HELP ME ITS THE NOTEBOOK SCREEN
#####################################
screen notebook():
    tag menu

    default notebookselector = "none"
    default notebookselector2 = "none"
    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Vinick") action SetScreenVariable("notebookselector", "vinick")
                textbutton _("Other") action SetScreenVariable("notebookselector", "other")
                textbutton _(notebookselector)
            if notebookselector == "vinick":
                use notebooktest
            elif notebookselector == "other":
                use mouse_help
            elif notebookselector == "gamepad":
                use gamepad_help

screen notebooktest():
    tag menu
    default notebookselector2 = "none"
    vbox:
            hbox:

                textbutton _("Vinick") action SetScreenVariable("notebookselector2", "vinick")
                textbutton _("Other") action SetScreenVariable("notebookselector2", "other")
                textbutton _(notebookselector2)
            if notebookselector2 == "vinick":
                use attributions_cali
            elif notebookselector2 == "other":
                use attributions_forest
            elif notebookselector2 == "gamepad":
                use gamepad_help

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0

################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")
#####################################
# Attributions, Attributions
#####################################
screen attributions():
    tag menu

    default page = "6"

    use game_menu(_("Attributions"), scroll="viewport"):

        style_prefix "help"
        vbox:
            spacing 23

            hbox:
                textbutton _("Page 1") action SetScreenVariable("page", "1")
                textbutton _("Page 2") action SetScreenVariable("page", "2")
                textbutton _("Page 3") action SetScreenVariable("page", "3")
                textbutton _("Page 4") action SetScreenVariable("page", "4")
                textbutton _("Page 5") action SetScreenVariable("page", "5")
                textbutton _("Page 6") action SetScreenVariable("page", "6") # more efficient way?
                textbutton _(page)
            if page == "1":
                use attributions_cali
                use attributions_oval_office
            elif page == "2":
                use attributions_vinick
                use attributions_plane
            elif page == "3":
                use attributions_forest
                use attributions_mischa
            elif page == "4":
                use attributions_sloan
            elif page == "5":
                use attributions_dogcamp
                use attributions_caine
                use attributions_doctor
            elif page == "6":
                use attributions_dogcastle
        #this can be split like the helpt screen Laggy atm
        

screen attributions_cali():
    frame:
        xsize .999
        ysize 560
        vbox:

            hbox: # General Cali Tab
                label _("Cali (All sprites)"):
                    yoffset 10
                text _("All Cali Meowford sprite images, aside for one, are done by Jim/iqsphotography on Unsplash \ncheck out his work at {a=https://unsplash.com/@iqsphotography}This Link{/a}"):
                    yoffset 10
                image _("cali sit.png"):
                    zoom .4
                    xpos -1000
                    yoffset 110
                image _("cali sidelay.png"):
                    zoom .5
                    xpos -1000
                    yoffset 100
                image _("cali lookback.png"):
                    zoom .45
                    xpos -1000
                    yoffset 125
                image _("cali lay.png"):
                    zoom .5
                    xpos -1000
                    yoffset 100
            
            hbox: # Cali Jump Tab
                label _("Cali Jump"):
                    yoffset 100
                text _("Used as a transition for President Cali, this was taken by {a=https://www.flickr.com/people/85936780@N00}Pelican on Flickrr{/a}, but can also be found on {a=https://commons.wikimedia.org/wiki/File:Calico_cat_(23454134083).jpg}wikimedia{/a}"):
                    yoffset 100
                image _("cali jump.png"):
                    zoom .5
                    xoffset -1200
                    yoffset 150

screen attributions_oval_office():
    frame:
        xsize .999
        ysize 900
        vbox:            
            hbox: # bg office tab
                label _("Oval Office Background"):
                    yoffset 10
                text _("Used as a background in the starting sequence, this was taken by {a=https://unsplash.com/@chapelbeach}Donghun Shin/chapelbeach on Unsplash{/a}"):
                    yoffset 10
                image _("bg office.jpg"):
                    zoom .05
                    xoffset -1200
                    yoffset 100
            hbox:
                label _("Oval Office Background 2"):
                    yoffset 150
                text _("Used as an alternate background when Cali Meowford enters the scene this was taken by White House Photographers and is {a=https://commons.wikimedia.org/wiki/File:Empty_Oval_Office_in_The_White_House.jpg?uselang=en#Licensing}public domain{/a}"):
                    yoffset 150
                image _("bg ovalofficeoverlook.jpg"):
                    zoom .05
                    xoffset -1125
                    yoffset 250
            hbox:
                label _("Oval Office Chairs"):
                    yoffset 300
                text _("Used to give Cali Meowford somewhere to sit while yapping your ear off. Taken by Michael Barera, and can be found on {a=https://commons.wikimedia.org/wiki/File:Lyndon_Baines_Johnson_Library_and_Museum_July_2017_5_%28The_Oval_Office%29.jpg}on Wikimedia{/a}"):
                    yoffset 300
                image _("bg ovalofficesit.jpg"):
                    zoom .055
                    xoffset -1200
                    yoffset 350

screen attributions_vinick():
    frame:
        xsize .999
        ysize 600
        vbox:
            hbox: # Vinick Sit
                label _("Vinick Sit"):
                    yoffset 10
                text _("Used as the first sprite the player sees, Vinick Meowstrong is the best silly guy. Anyway, this was taken by {a=https://unsplash.com/@vidak}Vidak on Unsplash{/a}"):
                    yoffset 10
                image _("vinick idle.png"):
                    zoom .5
                    xoffset -1225

            hbox: # Vinick Sit
                label _("Vinick Look Up")
                text _("Used as another Vinick sprite. this was taken by {a=https://unsplash.com/@luschetinger}Luísa Schetinger{/a} on{a=https://unsplash.com/photos/black-cat-on-white-floor-l8rgI_gH1YU}  Unsplash{/a}")      
                image _("vinick lookup.png"):
                    zoom .4
                    xoffset -1100
                    yoffset 35
screen attributions_plane():
    frame:
        xsize .999
        ysize 550
        vbox:
            
            hbox: # bg planeseat1
                label _("Plane Seat One"):
                    yoffset 10
                text _("Used as the background when you get onto the plane. Taken by{a=https://unsplash.com/@pino_rumbero} Micheal Pointer{/a} on {a=https://unsplash.com/photos/the-inside-of-an-airplane-with-the-lights-on-r12sSEwuMJo}Unsplash{/a}"):
                    yoffset 10
                image _("bg planeseat1.jpg"):
                    zoom .04
                    xoffset -1175
                    yoffset 50
            hbox: # bg planewindow1
                label _("Plane Window"):
                    yoffset 90
                text _("Used as the background before you crash lmao. Taken by{a=https://unsplash.com/@sashafreemind} Sasha Freemind{/a} on {a=https://unsplash.com/photos/plane-window-overlooking-sea-of-clouds-cm0eSVxdLDg}Unsplash{/a}"):
                    yoffset 90
                image _("bg planewindow1.jpg"):
                    zoom .04
                    xoffset -1175
                    yoffset 150

screen attributions_forest():
    frame:
        xsize .999
        ysize 250
        vbox:
            
            hbox: # bg forest1
                label _("Forest Background"):
                    yoffset 10
                text _("Used as the background once you crash and meet the dogs. Taken by{a=https://unsplash.com/@iriser} Irina Iriser{/a} on {a=https://unsplash.com/photos/green-leafed-trees-2Y4dE8sdhlc}Unsplash{/a}"):
                    yoffset 10
                image _("bg forest1.jpg"):
                    zoom .04
                    xoffset -1175
                    yoffset 60

screen attributions_mischa():
    frame:
        xsize .999
        ysize 300
        vbox:
            
            hbox: # mosk all
                label _("Mischa Sobaka"):
                    yoffset 10
                text _("Mischa Sobaka! The military leader of the dogs, all images of mischa are done by {a=https://unsplash.com/photos/a-brown-and-white-dog-standing-on-top-of-snow-covered-ground-WYOJaVGprZY} Adrian 'Rosco' Stef{/a}"):
                    yoffset 10
                image _("mosk stand.png"):
                    zoom .3
                    xoffset -1175
                    yoffset 60
                image _("mosk standcutoff.png"):
                    zoom .6
                    xoffset -1175
                    yoffset -75
                image _("mosk standshock.png"):
                    zoom .3
                    xoffset -1175
                    yoffset 80
                image _("mosk standside.png"):
                    zoom .4
                    xoffset -1175
                    yoffset 100
                image _("mosk standsniff.png"):
                    zoom .3
                    xoffset -1175
                    yoffset 80

screen attributions_sloan():
    frame:
        xsize .999
        ysize 1700  
        vbox:
            
            hbox: # garn lqstandangry
                label _("Small Angry Sloan"):
                    yoffset 10
                text _("Currently unused. Probably will be used for when Sloan is angry at something and far away. Taken by{a=https://unsplash.com/@gtsm} Gytis M{/a} on {a=https://unsplash.com/photos/black-and-tan-short-coat-medium-dog-on-snow-covered-ground-near-trees-during-daytime-pbf3j_MnvSo}Unsplash{/a}"):
                    yoffset 10
                image _("garn lqstandangry.png"):
                    zoom .3
                    xoffset -1175
                    yoffset 50
            hbox: # garn standlookback
                label _("Sloan Lookback"):
                    yoffset 35
                text _("Currently unused. This is also taken by{a=https://unsplash.com/@gtsm} Gytis M{/a} on {a=https://unsplash.com/photos/a-black-and-brown-dog-standing-on-top-of-a-sandy-beach-5GcNMK0iQPk}Unsplash{/a}"):
                    yoffset 35
                image _("garn standlookback.png"):
                    zoom .4
                    xoffset -1100
                    yoffset 75
            hbox: # garn sitcurious
                label _("Sloan Sit Curious"):
                    yoffset 75
                text _("Currently unused. This is also taken by{a=https://pixabay.com/users/yamabsm-1300729/} YamaBSM{/a} on {a=https://pixabay.com/photos/doberman-beauty-dog-1393918/}Pixabay{/a}"):
                    yoffset 75
                image _("garn sitcurious.png"):
                    zoom .4
                    xoffset -1100
                    yoffset 100
            hbox: # garn standalert
                label _("Sloan Stand Alert"):
                    yoffset 110
                text _("Currently used when you smack Sloan Garner. This is also taken by{a=https://unsplash.com/@malcoemi} Emily Malcolmson{/a} on {a=https://unsplash.com/photos/C1eaHeuc_mU}Unsplash{/a}"):
                    yoffset 110
                image _("garn standalert.png"):
                    zoom .4
                    xoffset -1200
                    yoffset 150
            hbox: # garn standcalm UNDONE
                label _("Sloan Stand Calm"):
                    yoffset 150
                text _("Currently unused. This is taken by{a=https://unsplash.com/es/@elv3n_} Elven Guerin{/a} on {a=https://unsplash.com/es/fotos/un-perro-se-para-y-mira-directamente-a-la-camara-nynJybuAFWo}Unsplash{/a}"):
                    yoffset 150
                image _("garn standcalm.png"):
                    zoom .4
                    xoffset -1100
                    yoffset 190
            hbox: # garn standlog UNDONE
                label _("Sloan Stand Log"):
                    yoffset 200
                text _("Currently unused, seems like a very niche use but I want to use it. This is taken by{a=https://pixabay.com/users/yamabsm-1300729/} YamaBSM{/a} on {a=https://pixabay.com/photos/doberman-dog-beauty-nature-3478787/}Pixabay{/a}"):
                    yoffset 200
                image _("garn standlog.png"):
                    zoom .4
                    xoffset -1200
                    yoffset 210
    
screen attributions_dogcamp():
    frame:
        xsize .999
        ysize 350
        vbox:
            
            hbox: # bg dogcampenterance
                label _("Dog Camp Entrance"):
                    yoffset 10
                text _("Used as the background as you enter Dog Camp. Taken by{a=https://unsplash.com/es/@iozmen} Ilker Ozmen{/a} on {a=https://unsplash.com/es/fotos/una-persona-caminando-por-una-pasarela-en-una-ciudad-KWiUwltAG18}Unsplash{/a}"):
                    yoffset 10
                image _("bg dogcampentrance.jpg"):
                    zoom .04
                    xoffset -1200
                    yoffset 100
screen attributions_caine():
    frame:
        xsize .999
        ysize 300
        vbox:
            hbox: # caine doctor doctor
                label _("Doctor Caine")
                text _("Used as the sprite for Doctor Caine when you get medical treatment. Taken by {a=https://unsplash.com/@laura_paraschivescu}Laura Paraschivescu{/a} on {a=https://unsplash.com/photos/a-dog-wearing-a-face-mask-sitting-on-a-wooden-floor-gSrrEvIaPII}Unsplash{/a}")
                image _("caine sit.png"):
                    zoom .5
                    yoffset 20
                    xoffset -1200
screen attributions_doctor:
    frame:
        xsize .999
        ysize 300
        vbox:
            hbox: # Doctors Office
                label _("Doctors Office")
                text _("Used for when the Dogs give you medical treatment. Photo by {a=https://unsplash.com/@fr0ggy5?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText>}fr0ggy5{/a} on {a=https://unsplash.com/photos/a-room-with-a-desk-phone-and-other-items-on-the-wall-717W1DqDka0?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText}Unsplash{/a}")
                image _("bg doctorsoffice.jpg"):
                    xoffset -1200
                    zoom .05
                    yoffset 50
screen attributions_dogcastle:
    frame:
        xsize .999
        ysize 800
        vbox:
            hbox: # Dogcastle
                label _("Dog Castle"):
                    yoffset 10
                text _("Is used as the Dog capitol. Is actually the Schloss in Wolfenbüttel, Germany. Photo by Jan-Herm Janßen on {a=https://en.wikipedia.org/wiki/Schloss_Wolfenb%C3%BCttel#/media/File:Wolfenbuettel_Schloss_07.jpg}Wikipedia{/a}"):
                    yoffset 10
                image _("bg dogcastleoutside.jpg"):
                    xoffset -1160
                    yoffset 60
                    zoom .2
            hbox: # dogcastlecourtyard
                label _("Dog Castle courtyard"):
                    yoffset 80
                text _("Used as the Interior of the dog's capitol. Is also actually the Schloss in Wolfenbüttel. Photo by Losch on {a=https://en.wikipedia.org/wiki/Schloss_Wolfenb%C3%BCttel#/media/File:Hofblick_im_Schloss_Wolfenb%C3%BCttel_IMG_2981.jpg}Wikipedia{/a}"):
                    yoffset 80
                image _("bg dogcastlecourtyard.jpg"):
                    yoffset 175
                    xoffset -1200
                    zoom .2
            hbox: # dogcastledoor
                label _("Dog Castle"):
                    yoffset 200
                text _("Front of the dog capitol, also the Schloss in Wolfebüttel, Germany. Photo by Brunswyk on {a=https://en.wikipedia.org/wiki/Schloss_Wolfenb%C3%BCttel#/media/File:Wolfenbuettel_Schlossportal_(2006).jpg}Wikipedia{/a}"):
                    yoffset 200
                image _("bg dogcastledoor.jpg"):
                    yoffset 270
                    xoffset -1200
                    zoom .4
                
screen attributions_template:
    frame:
        xsize .999
        ysize 1000
        vbox:
            hbox: # 
                label _("Dog Castle")
                text _("Photo by {a=wa}{/a} on {a=wa}{/a}")
                image _("bg dogcastle.jpg"):
                    xoffset -1200
## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly
        ## if config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed
## at once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using
## speech bubbles. The bubble screen takes the same parameters as the say
## screen, must create a displayable with the id of "what", and can create
## displayables with the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
