# Common code will go here.
def get_file_details(file_path):
    try:
        file_details = {}

        with open(file_path, 'r') as file:
            lines = file.readlines()
            file_details["output"] = [line.strip() for line in lines]
        
        return file_details
    except Exception as e:
        return {"error": str(e)}
    

def is_ascending(line):
    numbers = get_numbers(line)
    return numbers == sorted(numbers)  

def is_decending(line):
    numbers = get_numbers(line)
    return numbers == sorted(numbers, reverse=True)  

def check_adjacent_difference(line):
    numbers =  get_numbers(line)
    for i in range(1, len(numbers)):
        diff = abs(numbers[i] - numbers[i - 1]) 
        if diff < 1 or diff > 3:  
            return False
    return True

def get_numbers(line):
    return list(map(int, line.split()))