import os, sys, shutil, json, re, platform, subprocess

from core.system import directory





def replace_extension(path, extension = '.png'):

    """
    Description:
        Replace file's extensions
    """

    return os.path.splitext(path)[0] + extension

def delete(path):

    """
    Description:
        Delete file if it exists
    """

    try:
        if exists(path): os.remove(path)
    except Exception as e: print(e)

def exists(path):

    """
    Description:
        Check if path is file on the system
    """

    if os.path.isfile(path): return True
    else: return False

def copy(source, destination):

    """
    Description:
        Copy file from source to destination
    """

    try:
        if exists(source): shutil.copy(source, destination)
    except Exception as e: print(e)

def find_in_directory(path, file_name):

    """
    Description:
        Find file_name in the path recursively and if you find it
        return its absolute path and if not return None
    """

    path_out = None    
    for subdir, dirs, files in os.walk(path):
        for file in files:
            if file == file_name: return os.path.join(subdir, file)
    return path_out

def find_in_directory_by_subname(path, subname, case_sensitivity = False):

    """
    Description:
        Find file_name in the path recursively and if you find it
        return its absolute path and if not return None. with case_sensitivity
        turned off subname "_mesh" in "puppy_Mesh.fbx" will be a hit, while
        if it is turned on, this will not be True
    """
 
    path_out = []
    for subdir, dirs, files in os.walk(path):
        for file in files:
            if case_sensitivity:
                if subname in file:
                    path_out.append(os.path.join(subdir, file))
            else:
                if subname.lower() in file.lower():
                    path_out.append(os.path.join(subdir, file))
    return path_out

def extract_file_name(absolute_path, extension = True):

    """
    Description:
        Extract file_name from the absolute file path. Return file_name with
        extension if extension = True, otherwise return just file_name
    """

    file_name = os.path.basename(absolute_path)
    if not extension: file_name = file_name.split('.')[0]
    return file_name

def extract_extension(absolute_path, with_dot = True):

    file_name = os.path.basename(absolute_path)
    extension = file_name.split('.')[1]
    if with_dot: extension =  '.' + extension
    return extension

def extract_parent_folder(filepath):
    filepath = filepath.replace('\\', '/')
    return '/'.join(filepath.split('/')[:-1])

def find_in_path(file_name):

    """
    Description:
        Find file_name in path. If file is found return its full
        path and if not return False
    """

    path_out = False
    for path in sys.path:
        if os.path.isfile(os.path.join(path, file_name)):
            path_out = os.path.join(path, file_name)
    return path_out

def find_files_with_extension(path, extension, files = None):

    """
    Description:
        Recursively finds all files in the path directory and subsequent
        directories, that have the extension given.
        Variable extension can be a list of extensions or a singular string.
        Returns a list of paths that match.
    """

    if files is None: files = []

    for p in os.listdir(os.path.abspath(path)):
        p = os.path.join(path, p)
        if os.path.isdir(p): files = find_files_with_extension(p, extension, files)
        else:
            if get_extension(p) in extension: files.append(p)
    return files

def get_extension(file): return file.split('.')[-1]

def create(path):
    try:
        fp = open(path, 'x')
        fp.close()
    except Exception as e: print(e)

def read_json(path):
    with open(path, 'r') as fp: return json.load(fp)
    
def write_json(path, data):
    with open(path, 'w') as fp: json.dump(data, fp, indent = 4)

def append_to_json(path, data):
    with open(path, 'a') as fp: json.dump(data, fp, indent = 4)

def find_files_with_name(input, name, files = None, recursive = False):

    """
    Description:
        Recursively finds all files in the path directory and subsequent
        directories, that have the name given.
        Variable name can be a list of names or a singular string.
        Returns a list of paths that match.
    """
    recursive_valid = recursive and tf_directory.find_in_path(input)
    list_valid = not recursive
    valid = recursive_valid or list_valid

    if not valid:
        # TODO: use tf_error
        print('Invalid input. Please make sure input is a path if recursive is True.')
        return False
    if files is None:
        files = []

    if recursive:
        for p in os.listdir(os.path.abspath(input)):
            p = os.path.join(input, p)
            if os.path.isdir(p): files = find_files_with_name(p, name, files)
            else:
                if name in p: files.append(p)
        return files
    else:
        input = [file for file in input if name in file]
        return input
    
def is_valid_windows_filename(filename):
    # Windows filenames cannot contain any of the following characters:
    # < > : " / \ | ? *
    if re.search(r'[<>:"/\\|?*]', filename): return False

    # Windows filenames cannot end with a dot or space
    if filename[-1] in ('.', ' '): return False

    # Windows filenames cannot be reserved filenames:
    # CON, PRN, AUX, NUL, COM1, COM2, COM3, COM4, COM5, COM6, COM7, COM8, COM9,
    # LPT1, LPT2, LPT3, LPT4, LPT5, LPT6, LPT7, LPT8, and LPT9
    reserved_names = ['CON', 'PRN', 'AUX', 'NUL'] + ['COM%d' % i for i in range(1, 10)] + ['LPT%d' % i for i in range(1, 10)]
    if filename.upper() in reserved_names: return False

    # If the filename passes all of the above checks, it is valid.
    return True

def open_file_location(file_location):

    system = platform.system()
    
    if system == "Windows": os.startfile(file_location.replace('/', '\\'))
    elif system == "Linux": subprocess.Popen(['xdg-open', file_location])
    else: print("Opening file location not supported on this system.") # TODO: use tf_error