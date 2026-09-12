# launch-console

My Launch Console for the Code2College **Elite 101** prework — a small Python
program that greets you, learns your name, and loops a menu until you quit.

## Run it

```bash
python launch_console.py
```

It will ask for your name, then show a menu. Type a number and press Enter.
Pick **5** to exit.

## The menu

| Option | What it does |
| --- | --- |
| 1 | About me |
| 2 | My goals |
| 3 | Fun fact *(my own option)* |
| 4 | The product I'm eyeing *(my own option)* |
| 5 | Exit — prints a goodbye and stops the loop |

Anything that isn't 1–5 prints a reminder and shows the menu again.

## How it works

Three pieces, and that's the whole program:

- `input()` collects the name once, before the loop, so the greeting can use it.
- A `while running:` loop reprints the menu after every choice.
- An `if / elif / else` chain matches the choice. Option 5 sets `running = False`,
  which is what ends the loop.

One thing worth writing down: `input()` always returns a **string**, so every
comparison is against `"3"` and not `3`. Comparing to the number never matches.

## Credits

The greet → name → menu-loop shape is adapted from the example in the Elite 101
prework Guided Practice zone. Drafted with help from Claude (AI assistant); I
read every line, wrote my own menu options and text, and tested it before pushing.

— Shivek Saraf
