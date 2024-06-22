import sys
from time import sleep

from facefusion.typing import ErrorCode
from facefusion import process_manager
<<<<<<< HEAD
from facefusion.temp_helper import clear_temp_directory
=======
from facefusion.temp_helper import clear_temp
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
import facefusion.globals


def hard_exit(error_code : ErrorCode) -> None:
	sys.exit(error_code)


def conditional_exit(error_code : ErrorCode) -> None:
	if facefusion.globals.headless:
		hard_exit(error_code)


def graceful_exit(error_code : ErrorCode) -> None:
	process_manager.stop()
	while process_manager.is_processing():
		sleep(0.5)
	if facefusion.globals.target_path:
<<<<<<< HEAD
		clear_temp_directory(facefusion.globals.target_path)
=======
		clear_temp(facefusion.globals.target_path)
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	hard_exit(error_code)
