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
    
def can_be_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False