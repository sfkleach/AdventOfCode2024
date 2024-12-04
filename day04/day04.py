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

def get_file_raw(file_path):
    try:
        file_details = {}

        with open(file_path, 'r') as file:
            file_details["output"] = file.read().strip()  # Read the entire file as a string
        
        return file_details
    except Exception as e:
        return {"error": str(e)} 