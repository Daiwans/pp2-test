import re
file_name = input("Enter the file name (e.g., row.txt): ")
try:
    # Read the data from the provided file
    with open(file_name, "r", encoding="utf-8") as file:
        data = file.read()
    # 1
    result = re.findall('a[b]*', data)
    # 2
    result = re.findall('a[b]{2,3}', data)
    # 3
    result = re.findall('[a-z]+_[a-z]+', data)
    # 4
    result = re.findall('[A-Z][a-z]+', data)
    # 5
    result = re.findall('a.*b', data)
    # 6
    data = re.sub('[ ,.]', ':', data)
    # 7
    def snake_to_camel(match):
        return match.group(1) + match.group(2).upper()
    data = re.sub('(_)([a-z])', snake_to_camel, data)
    # 8
    split_at_upper = re.split('[A-Z]', data)
    # 9
    data = re.sub('([a-z])([A-Z])', r'\1 \2', data)
    # 10
    def camel_to_snake(match):
        return match.group(1) + "_" + match.group(2).lower()
    data = re.sub('([a-z])([A-Z])', camel_to_snake, data)
    # Save the modified text to a file
    with open("editedRow.txt", "w") as file:
        file.write(data)
    print("Processing completed and saved to editedRow.txt.")
except FileNotFoundError:
    print("File not found. Please make sure the file exists in the current directory.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

