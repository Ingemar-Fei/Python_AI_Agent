import os

def get_file_content(working_directory, file_path):

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


    MAX_CHARS = 10000
    file_path = get_directory_path(working_directory, file_path)
    check_list = [
        { 'path':working_directory, 'type':'directory'},
        { 'path':file_path, 'type':'file'}
    ]
    for check in check_list:
        if check_exists(check):
            pass
        else:
            return f'Error: "{check["path"]}"not found or is not a {check["type"]}'
    if out_of_dir(working_directory, file_path):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    try:
        with open(file_path, 'r') as file:
            file_content = file.read(MAX_CHARS)
        if len(file_content) == MAX_CHARS:
            file_content += f'\n[...File "{file_path}" truncated at 10000 characters]'
        return file_content
    except Exception as e:
        return f'Error: {e.strerror}'
