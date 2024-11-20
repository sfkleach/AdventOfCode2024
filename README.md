# AdventOfCode2024

Repo for collaborating on the Advent of Code challenge for 2024. 

## Rules

1. Python - unless there's a good excuse.
   - At least version 3.10 please. Ideally version 3.12.
2. Each day is a completely standalone project.
   - Just copy and paste if needs be.
   - part1.py and part2.py are main programs for the separate days
   - To begin with they take no arguments but as the puzzles get more 
       complex we may need to add --input and --debug flags.
   - In the snippets folder the main.py snippet is an argparse template.
3. Packages are to be managed using poetry.
   - To start with we don't include it. 
   - We add it to each days separately on demand.
   - If we add it, we need to adjust the `Justfile` accordingly.
4. Our command launcher is `just`
   - To run part<n> use the command `just part<n>`
   - This command will print out the result and nothing else.
