from typing import List
<<<<<<< HEAD
import glob
import os
import tempfile

import facefusion.globals
from facefusion.filesystem import remove_directory, move_file, create_directory


def get_temp_file_path(file_path : str) -> str:
	_, extension = os.path.splitext(os.path.basename(file_path))
	temp_directory_path = get_temp_directory_path(file_path)
	return os.path.join(temp_directory_path, 'temp' + extension)


def move_temp_file(file_path : str, move_path : str) -> bool:
	temp_file_path = get_temp_file_path(file_path)
	return move_file(temp_file_path, move_path)
=======
from pathlib import Path
import glob
import os
import shutil
import tempfile

import facefusion.globals
from facefusion.filesystem import is_file, is_directory


def get_temp_file_path(target_path : str) -> str:
	_, target_extension = os.path.splitext(os.path.basename(target_path))
	temp_directory_path = get_temp_directory_path(target_path)
	return os.path.join(temp_directory_path, 'temp' + target_extension)


def get_temp_directory_path(target_path : str) -> str:
	target_name, _ = os.path.splitext(os.path.basename(target_path))
	temp_directory_path = os.path.join(tempfile.gettempdir(), 'facefusion')
	return os.path.join(temp_directory_path, target_name)
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275


def get_temp_frame_paths(target_path : str) -> List[str]:
	temp_frames_pattern = get_temp_frames_pattern(target_path, '*')
	return sorted(glob.glob(temp_frames_pattern))


def get_temp_frames_pattern(target_path : str, temp_frame_prefix : str) -> str:
	temp_directory_path = get_temp_directory_path(target_path)
	return os.path.join(temp_directory_path, temp_frame_prefix + '.' + facefusion.globals.temp_frame_format)


<<<<<<< HEAD
def get_base_directory_path() -> str:
	return os.path.join(tempfile.gettempdir(), 'facefusion')


def create_base_directory() -> bool:
	base_directory_path = get_base_directory_path()
	return create_directory(base_directory_path)


def clear_base_directory() -> bool:
	base_directory_path = get_base_directory_path()
	return remove_directory(base_directory_path)


def get_temp_directory_path(file_path : str) -> str:
	file_name, _ = os.path.splitext(os.path.basename(file_path))
	base_directory_path = get_base_directory_path()
	return os.path.join(base_directory_path, file_name)


def create_temp_directory(file_path : str) -> bool:
	temp_directory_path = get_temp_directory_path(file_path)
	return create_directory(temp_directory_path)


def clear_temp_directory(file_path : str) -> bool:
	temp_directory_path = get_temp_directory_path(file_path)
	return remove_directory(temp_directory_path)
=======
def create_temp(target_path : str) -> None:
	temp_directory_path = get_temp_directory_path(target_path)
	Path(temp_directory_path).mkdir(parents = True, exist_ok = True)


def move_temp(target_path : str, output_path : str) -> None:
	temp_file_path = get_temp_file_path(target_path)

	if is_file(temp_file_path):
		if is_file(output_path):
			os.remove(output_path)
		shutil.move(temp_file_path, output_path)


def clear_temp(target_path : str) -> None:
	temp_directory_path = get_temp_directory_path(target_path)
	parent_directory_path = os.path.dirname(temp_directory_path)

	if not facefusion.globals.keep_temp and is_directory(temp_directory_path):
		shutil.rmtree(temp_directory_path, ignore_errors = True)
	if os.path.exists(parent_directory_path) and not os.listdir(parent_directory_path):
		os.rmdir(parent_directory_path)
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
