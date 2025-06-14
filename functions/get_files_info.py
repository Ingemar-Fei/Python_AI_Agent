import os

PWD = os.getcwd()
MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    file_path = os.path.join(working_directory, file_path)
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
    
def get_files_info(working_directory, directory=None):
    
    # get the absolute path of the directory : abspath or relative apth   
    def  get_directory_path(working_directory, directory):
        if directory.startswith("/"):
            return directory
        else:
            return os.path.join(working_directory, directory)
    
    directory = get_directory_path(working_directory,directory)
    # check existance of directory files
    check_list = [
        { 'path':working_directory, 'type':'directory'},
        { 'path':directory, 'type':'directory'}
    ]
    for check in check_list:
        if check_exists(check):
            pass
        else:
            return f'Error: "{check["path"]}"not found or is not a {check["type"]}'

    if out_of_dir(working_directory, directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    return '\n'.join([f'---  {directory}: ---']+list_files(directory)+['---  end  ---',''])

def check_exists(check_dict):
    path = check_dict["path"]
    file_type = check_dict["type"]
    print(f'checking {path} is a {file_type}')
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
    

def check_is_dir(directory):
    return os.path.isdir(directory)

def out_of_dir(working_directory, file):
    working_directory = os.path.abspath(working_directory)
    file = os.path.abspath(file)
    return os.path.commonpath([working_directory, file]) != working_directory

def is_a_directory(directory):
    return os.path.isdir(directory)

def list_files(directory):
    files = os.listdir(directory)
    def get_file_path(file_name):
        return os.path.join(directory, file_name)
    return list(map(lambda x: f"-  {x}: file_size={os.path.getsize(get_file_path(x))} bytes, is_dir={os.path.isdir(get_file_path(x))}",files))