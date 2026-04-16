import tcod.console
import tcod.context
import tcod.event
import tcod.tileset


def main() -> None:
    """Script entry point."""
    screen_width = 16
    screen_height = 16

    tilesheet_width = 16  # this is the number of tile columns in the tilesheet
    tilesheet_height = 16  # this is the number of tile rows in the tilesheet
    tileset = tcod.tileset.load_tilesheet(
        path="sprites/DarkondDigsDeeper_16x16.png",
        columns=tilesheet_width,
        rows=tilesheet_height,
        charmap=(
            num for num in range(160, 160 + tilesheet_height * tilesheet_width, 1)
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
