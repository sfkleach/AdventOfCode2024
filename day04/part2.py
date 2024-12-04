from day04 import *
import argparse
from pathlib import Path

def run(args):
    raw_data = get_file_details(args.input)
    grid = raw_data["output"]
    print(grid)

    # Word to search for
    word = "XMAS"

    # Define directions: (dx, dy) corresponds to change in coordinates for each direction
    directions = {
        'N': (0, -1),    
        'S': (0, 1),     
        'E': (1, 0),    
        'W': (-1, 0),   
        'NE': (1, -1),   
        'NW': (-1, -1),  
        'SE': (1, 1),    
        'SW': (-1, 1) 
    }

    # Function to check if the word "XMAS" appears starting from (x, y) in a given direction
    def find_word(grid, x, y, word):
        word_len = len(word)
        
        
        if grid[x][y] != "A":
            return False

        result = ["A"]

        dx, dy = directions["NE"]   

        new_x = x + 1 * dx
        new_y = y + 1 * dy        

        if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
                return False

        #print("1 " + grid[new_y][new_x] + " " + grid[new_y][new_x])
        if grid[new_y][new_x] != "S" and grid[new_y][new_x] != "M":
            return False       

        result.append(grid[new_y][new_x])

        dx, dy = directions["SE"]   

        new_x = x + 1 * dx
        new_y = y + 1 * dy        
       #print("w " + str(new_y) + " " + str(new_x))
        

        if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
            return False
        
        
        if grid[new_y][new_x] != "S" and grid[new_y][new_x] != "M":
            return False   
        
        result.append(grid[new_y][new_x])
        
        test = "".join(result)
        #print(test);
        if test != "AMS" and test != "ASM":
            return False

        result = ["A"]

        dx, dy = directions["NW"]   

        new_x = x + 1 * dx
        new_y = y + 1 * dy        

        #print("3")
        if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
                return False
        
        if grid[new_y][new_x] != "S" and grid[new_y][new_x] != "M":
            return False       

        result.append(grid[new_y][new_x])

        dx, dy = directions["SW"]   

        new_x = x + 1 * dx
        new_y = y + 1 * dy        

        #print("4")
        if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
                return False

        if grid[new_y][new_x] != "S" and grid[new_y][new_x] != "M":
            return False   
        
        result.append(grid[new_y][new_x])
        
        test = "".join(result)

        if test != "AMS" and test != "ASM":
            return False

        print("Thats one")
        return True

    # Function to find all occurrences of the word "XMAS" in the grid
    def find_all_occurrences(grid, word):
        occurrences = []
        
        # Loop through every cell in the grid
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                # Get two diagnals and construct the word
                if find_word(grid, x, y, word):
                    occurrences.append((x, y))  # Store the coordinates and direction

        return occurrences

    # Find all occurrences of the word "XMAS"
    occurrences = find_all_occurrences(grid, word)
    print(len(occurrences))
    

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Process some options.')
    parser.add_argument('--input', type=Path, help='Input file path')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    # Parse the arguments
    args = parser.parse_args()

    run(args)
    
if __name__ == '__main__':
    main()

