import os, sys, re, shutil, subprocess

from pp_core.pp_system import pp_file





def exists(path): return os.path.isdir(path)

def create(path):
    if not exists(path): os.makedirs(path, exist_ok = True)
    return path

def delete(path):

    """
    Description:
        Delete directory if it exists
    """

    if exists(path):
        try: shutil.rmtree(path)
        except Exception as e: print(e)

def remove(path):
    if exists(path): os.remove(path)

def get_desktop_path(): return os.path.join(os.path.expanduser('~'), 'Desktop')

def list_files(path, extension=None): 

    if extension is None: return os.listdir(path)
    else:
        directory = path
        if type(path) == str:
            directory = os.listdir(path)

        directory = [file if pp_file.get_extension(file) == extension else None for file in directory]
        directory = list(filter(lambda file: file is not None, directory))

        return directory

def join(path, path_to_join): return os.path.join(path, path_to_join).replace("\\", "/")

def find_in_path(dir_name):

    """
    Description:
        Find dir_name in path. If directory is found return its full
        path and if not return False. Similar to tf_file.find_in_path()
    """

    path_out = False
    for path in sys.path:
        if os.path.isdir(os.path.join(path, dir_name)):
            path_out = os.path.join(path, dir_name)
    return path_out

# TODO: not working as intended
def get_script_directory():
    if getattr(sys, 'frozen', False): script_directory = os.path.dirname(sys.executable)
    elif __file__: script_directory = os.path.dirname(__file__)
    return script_directory

def get_environment_path(environment = 'ProgramData'):
    return os.path.join(os.environ[environment])

def is_valid_windows_folder_name(folder_name):

    """
    Description:
        Checks if string is a valid windows folder name.
        Variable folder_name: Input folder name string to check.
        Returns: True and folder name if valid, False and invalid characters if not valid.
    """

    pattern = r'^(?!(?:^(?:con|prn|aux|nul)$|\..*|[<>:"/\\|?*]).*$)[^\r\n<>:"/\\|?*\x00-\x1f]{1,254}$'
    match = re.match(pattern, folder_name)
    if match is None or folder_name.strip() == '':
        invalid_part = re.findall(r'(?:^(?:con|prn|aux|nul)$|\..*|[<>:"/\\|?*])', folder_name)
        return False, invalid_part[0] if invalid_part else folder_name
    return True, folder_name

def init_data_folder(folder):
    folder = folder.replace('\\', '/')
    program_data = get_environment_path("ProgramData")
    for folder in folder.split('/'):
        program_data = os.path.join(program_data, folder)
        create(program_data)
    return program_data

def get_downloads_folder():
    home = os.path.expanduser("~")  # Get the user's home directory
    if os.name == 'nt':  # Windows operating system
        downloads_folder = os.path.join(home, 'Downloads')
    else:
        downloads_folder = home
    
    return downloads_folder

def open_folder_in_explorer(path):
    subprocess.Popen(f'explorer "{path}"')

