# Rules for AdventOfCode2024

Here are some rules for collaborating on the Advent of Code challenge for 2024. 
I found these rules to be useful in speeding up the coding process - they 
are not intended to be best practice! The general idea is that we start the
programs as simple scripts. If they get more complicate we can add arguments
or pypi packages.

1. Use branches with names like 'steve/day01_part1_{blahblah}'
2. Python - unless there's a good excuse.
   - At least version 3.10 please. Ideally version 3.12.
   - No cheating with specialised PyPI packages; simple packages are fine though.
3. Each day folder is intended to be a completely standalone project.
   - Just copy and paste between days rather than try to share. I have found 
     that helps to keep up the momentum.
   - Code that is common to both parts goes in the day<n>.py file.
   - part1.py and part2.py are main programs for the separate parts. Again I have
     found that keeping these separate avoids wasting time about how the parts should
     be organised.
   - To begin with they take no arguments but as the puzzles get more 
       complex we may need to add (say) --input and --debug flags.
   - In the snippets folder the main.py snippet is an argparse template.
   - If you add arguments, remember to fix up the `Justfile`.
4. Packages are to be managed using poetry.
   - To start with we don't include it. 
   - We add it to any given day<n> folder on demand.
   - If we add it, we need to adjust the `Justfile` accordingly.
5. Our command launcher is `just`
   - To run part<n> use the command `just part<n>`
   - This command will print out the result and nothing else.
