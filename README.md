Heard that the pillow imaging library works well with tcod for making tilemaps

Got custom tilemaps working I think. For some reason when converting 0-32 to utf-8 nothing is shown on screen, and character 126 is repeated for 126-159, at which point it resumes at where I would expect it until it ends at 288 (16 squared plus 32)
  Why does it skip 0-32 and 126-159? Something relating to how the app handles utf-8 codepoints? Some limitation in utf-8 in general?

so in utf-8, 0-31 are control characters (32 is space)
as are 129-159.
Starting my mapping at 160 got rid of all problems, so we're in business! Now just to map the numbers to the entity names and we're cooking!

I'd love to eventually design a more comprehensive font that's a higher resolution and includes all utf-8 characters up to 160 (skipping control codes of course)
