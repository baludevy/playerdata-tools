import os
import shutil


def delete_file(filename: str):
    os.remove(filename)


def rename_file(old_name: str, new_name: str):
    os.rename(old_name, new_name)


def make_backup(filename: str):
    shutil.copy(filename, f"{filename}.backup")
