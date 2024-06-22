import os
<<<<<<< HEAD

from facefusion.temp_helper import get_base_directory_path
from facefusion.typing import JobStatus
from facefusion.filesystem import is_file, is_directory, remove_directory, create_directory


def is_test_job_file(file_path : str, job_status : JobStatus) -> bool:
	return is_file(get_test_job_file(file_path, job_status))


def get_test_job_file(file_path : str, job_status : JobStatus) -> str:
	return os.path.join(get_test_jobs_directory(), job_status, file_path)


def get_test_jobs_directory() -> str:
	return os.path.join(get_base_directory_path(), 'test-jobs')


def get_test_example_file(file_path : str) -> str:
	return os.path.join(get_test_examples_directory(), file_path)


def get_test_examples_directory() -> str:
	return os.path.join(get_base_directory_path(), 'test-examples')


def is_test_output_file(file_path : str) -> bool:
	return is_file(get_test_output_file(file_path))


def get_test_output_file(file_path : str) -> str:
	return os.path.join(get_test_outputs_directory(), file_path)


def get_test_outputs_directory() -> str:
	return os.path.join(get_base_directory_path(), 'test-outputs')


def prepare_test_output_directory() -> bool:
	test_outputs_directory = get_test_outputs_directory()
	remove_directory(test_outputs_directory)
	create_directory(test_outputs_directory)
	return is_directory(test_outputs_directory)
=======
import shutil
import tempfile

from facefusion.typing import JobStatus
from facefusion.filesystem import is_file


def get_test_jobs_directory() -> str:
	return os.path.join(tempfile.gettempdir(), 'test-jobs')


def get_test_examples_directory() -> str:
	return os.path.join(tempfile.gettempdir(), 'test-examples')


def get_test_outputs_directory() -> str:
	return os.path.join(tempfile.gettempdir(), 'test-outputs')


def prepare_test_output_directory() -> None:
	shutil.rmtree(get_test_outputs_directory(), ignore_errors = True)
	os.mkdir(get_test_outputs_directory())


def get_test_job_file(file : str, job_status : JobStatus) -> str:
	return os.path.join(tempfile.gettempdir(), 'test-jobs', job_status, file)


def get_test_example_file(file : str) -> str:
	return os.path.join(tempfile.gettempdir(), 'test-examples', file)


def get_test_output_file(file : str) -> str:
	return os.path.join(tempfile.gettempdir(), 'test-outputs', file)


def is_test_job_file(file : str, job_status : JobStatus) -> bool:
	return is_file(get_test_job_file(file, job_status))


def is_test_output_file(file : str) -> bool:
	return is_file(get_test_output_file(file))
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
