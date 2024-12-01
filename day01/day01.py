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

def create_lists_from_input(data):
    list1 = []
    list2 = []

    # splitting into two operations. return characters then spaces before sorting into lists.
    for line in data:
        parts = line.split()

        list1.append(parts[0])
        list2.append(parts[1])

    return (list1, list2)