import os

def write_file(working_directory, file_path, content):

    # get the absolute path of the directory : abspath or relative apth   
    def  get_directory_path(working_directory, file_path):
        if file_path.startswith("/"):
            return file_path
        else:
            return os.path.join(working_directory, file_path)

    def check_exists(check_dict):
        path = check_dict["path"]
        file_type = check_dict["type"]
        print(f'- checking {path} - {file_type}')
        if os.path.exists(path):
            print(f'{path} exists')
            if file_type == "file":
                return os.path.isfile(path)
            elif file_type == "directory":
                return os.path.isdir(path)
            else:
                return False
        else:
            return False
        

    def out_of_dir(working_directory, file):
        working_directory = os.path.abspath(working_directory)
        file = os.path.abspath(file)
        return os.path.commonpath([working_directory, file]) != working_directory


    file_path = get_directory_path(working_directory, file_path)
    check_list = [
        { 'path':working_directory, 'type':'directory'},
    ]
    for check in check_list:
        if check_exists(check):
            pass
        else:
            return f'Error: "{check["path"]}"not found or is not a {check["type"]}'
    if out_of_dir(working_directory, file_path):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        return f'Error: {e.strerror}'
    else:
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'