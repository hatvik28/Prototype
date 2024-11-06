import re
import json

# Load bug patterns from JSON file
with open('bugs.json', 'r') as file:
    bug_patterns = json.load(file)

with open('Main.java' , 'r') as file:
    java_code = file.read()
          

def detect_bugs(java_code):
    bugs = []

    for bug in bug_patterns:
        # Compile the main pattern
        pattern = re.compile(bug["pattern"])
        matches = pattern.finditer(java_code)
        
        for match in matches:
            # Check if there's a precondition
            if "precondition" in bug:
                precondition = re.compile(bug["precondition"].replace("\\1", match.group(1)))
                # Only add the bug if the precondition is met
                if not precondition.search(java_code):
                    continue
            
            # Append the detected bug with line and code context
            line_number = java_code[:match.start()].count('\n') + 1
            code_line = java_code.splitlines()[line_number - 1].strip()
            bugs.append({
                "bug_id": bug["id"],
                "description": bug["description"],
                "line": line_number,
                "code_line": code_line
            })

    return bugs

# Run bug detection
detected_bugs = detect_bugs(java_code)

# Output detected bugs
for bug in detected_bugs:
    print(f"Bug ID: {bug['bug_id']}")
    print(f"Description: {bug['description']}")
    print(f"Line Number: {bug['line']}")
    print(f"Code Line: {bug['code_line']}")
    print("-------------------------------------------------\n")
