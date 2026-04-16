import tcod.console
import tcod.context
import tcod.event
import tcod.tileset


def main() -> None:
    """Script entry point."""
    screen_width = 16
    screen_height = 16

    tilesheet1 = dict(
        width=16,
        height=16,
        path="sprites/DarkondDigsDeeper_16x16.png",
    )
    tilesheet = dict(
        width=5,
        height=3,
        path="sprites/woods-5x3.png",
        names=[
            "corner_nw",
            "top",
            "corner_ne",
            "pichu",
            "mew",
            "left",
            "grass",
            "right",
            "ground0",
            "ground1",
            "corner_sw",
            "bottom",
            "corner_se",
            "ground3",
            "ground4",
        ],
    )

    tileset = tcod.tileset.load_tilesheet(
        path=tilesheet["path"],
        columns=tilesheet["width"],
        rows=tilesheet["height"],
        # the width and height here represent the tile collumns and rows of the tilesheet, respectively, not neccesarily the pixel density thereof
        charmap=(
            num for num in range(160, 160 + tilesheet["height"] * tilesheet["width"], 1)
        ),  # starting the charmap at 160 to avoid utf-8 control characters at 0-32 and 126-59
    )

    # Create a window
    with tcod.context.new_terminal(  # New window for a console of size columns×rows.
        screen_width,
        screen_height,
        tileset=tileset,
        title="Jade is figuring shit out",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        root_console = context.new_console(magnification=2)
        char = 160
        while True:  # Main loop, runs until SystemExit is raised.
            root_console.print(x=1, y=1, string=chr(char))
            root_console.print(
                x=2,
                y=2,
                string=chr(
                    160 + tilesheet["names"].index("mew")
                ),  # the charmap starts at 160 to avoid any utf-8 control characters.
            )
            print("char: " + str(char) + ", Utf-8 encoded as: " + str(chr(char)))
            context.present(root_console, integer_scaling=True)
            # Show the console.

            # This event loop will wait until at least one event is processed before exiting.
            # For a non-blocking event loop replace `tcod.event.wait` with `tcod.event.get`.
            for event in tcod.event.wait():
                event = context.convert_event(
                    event
                )  # Sets tile coordinates for mouse events.
                print(event)  # Print event names and attributes.
                match event:
                    case tcod.event.KeyDown():
                        char += 1
                    case tcod.event.Quit():
                        raise SystemExit
                    case tcod.event.WindowResized(width=width, height=height):
                        root_console = context.new_console(magnification=2)


# The window will be closed after the above with-block exits.


if __name__ == "__main__":
    main()
