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
    return list(map(int, str(line).split()))

class ReportController:
    def __init__(self, data):
        self.data = list(map(int, data.split())) 
        self.reports = []

        self.reports.append(data)

        self.generate_reports()
        print(self.reports)
    
    def generate_reports(self):
        for i in range(len(self.data)):
            new_report = self.Report(self.data[:i] + self.data[i+1:])
            self.reports.append(new_report)
    
    def does_report_pass(self):
        for item in self.reports:
            if is_ascending(str(item)) or is_decending(str(item)):
                if check_adjacent_difference(str(item)):
                    return True               
            else:
                continue            

    class Report:
        def __init__(self, report):
            self.report = report
        def __repr__(self):
            return f"Report({self.report})"
        def __str__(self):
            return " ".join(map(str, self.report))