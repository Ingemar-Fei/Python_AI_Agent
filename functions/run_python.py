import os
import re
import subprocess

def run_python_file(working_directory, file_path):
    
    # get the absolute path of the directory : abspath or relative apth   
    def  get_directory_path(working_directory, file_path):
        if file_path.startswith("/"):
            return file_path
        else:
            return os.path.abspath(os.path.join(working_directory, file_path))

    def check_exists(check_dict):
        path = check_dict["path"]+'/'+check_dict["name"]
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
        
    def out_of_dir(working_directory, file_path):
        working_directory = os.path.abspath(working_directory)
        file = get_directory_path(working_directory, file_path)
        print('checking out_of_dir:',working_directory,';',file)
        return os.path.commonpath([working_directory, file]) != working_directory

    if not file_path.endswith('.py'):
        return  f'Error: "{file_path}" is not a Python file.'
    check_list = [
        { 'path':'.', 'name':working_directory, 'type':'directory'},
        { 'path':working_directory, 'name':file_path, 'type':'file'}
    ]
    for check in check_list:
        if check_exists(check):
            pass
        else:
            return f'Error: {check["type"].title()} "{check["name"]}" not found'
    if out_of_dir(working_directory, file_path):
        return f'Error: Cannot execute "{file_path}" as it is outside'
    
    try:
        run_res = subprocess.run(["python", file_path],timeout=30, cwd=working_directory, capture_output=True)
        res = ''
        if run_res.stdout:
            res += f"STDOUT: {run_res.stdout.decode()}\n"
        elif run_res.stderr:
            res += f"STDERR: {run_res.stderr.decode()}\n"
        else:
            res += "No output produced\n"
        if run_res.returncode != 0:
            res += f"Process exited with code {run_res.returncode}\n"
        return res
    except Exception as e:
        return f"Error: executing Python file: {e}"