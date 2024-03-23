import os


def is_env_file_in_directory(filename):
    return filename in os.listdir()
