import subprocess
import sys
import pytest

from facefusion.download import conditional_download
<<<<<<< HEAD
from facefusion.jobs.job_manager import init_jobs, clear_jobs
from .helper import get_test_jobs_directory, get_test_examples_directory, prepare_test_output_directory, get_test_example_file, get_test_output_file, is_test_output_file
=======
from .helper import get_test_examples_directory, prepare_test_output_directory, get_test_example_file, get_test_output_file, is_test_output_file
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275


@pytest.fixture(scope = 'module', autouse = True)
def before_all() -> None:
	conditional_download(get_test_examples_directory(),
	[
		'https://github.com/facefusion/facefusion-assets/releases/download/examples/source.jpg',
		'https://github.com/facefusion/facefusion-assets/releases/download/examples/target-240p.mp4'
	])
	subprocess.run([ 'ffmpeg', '-i', get_test_example_file('target-240p.mp4'), '-vframes', '1', get_test_example_file('target-240p.jpg') ])


@pytest.fixture(scope = 'function', autouse = True)
def before_each() -> None:
<<<<<<< HEAD
	clear_jobs(get_test_jobs_directory())
	init_jobs(get_test_jobs_directory())
=======
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	prepare_test_output_directory()


def test_swap_face_to_image() -> None:
<<<<<<< HEAD
	commands = [ sys.executable, 'run.py', '-j', get_test_jobs_directory(), '--headless', '--frame-processors', 'face_swapper', '-s', get_test_example_file('source.jpg'), '-t', get_test_example_file('target-240p.jpg'), '-o', get_test_output_file('test-swap-face-to-image.jpg') ]
=======
	commands = [ sys.executable, 'run.py', '--frame-processors', 'face_swapper', '-s', get_test_example_file('source.jpg'), '-t', get_test_example_file('target-240p.jpg'), '-o', get_test_output_file('test-swap-face-to-image.jpg'), '--headless' ]
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275

	assert subprocess.run(commands).returncode == 0
	assert is_test_output_file('test-swap-face-to-image.jpg') is True


def test_swap_face_to_video() -> None:
<<<<<<< HEAD
	commands = [ sys.executable, 'run.py', '-j', get_test_jobs_directory(), '--headless', '--frame-processors', 'face_swapper', '-s', get_test_example_file('source.jpg'), '-t', get_test_example_file('target-240p.mp4'), '-o', get_test_output_file('test-swap-face-to-video.mp4'), '--trim-frame-end', '10' ]
=======
	commands = [ sys.executable, 'run.py', '--frame-processors', 'face_swapper', '-s', get_test_example_file('source.jpg'), '-t', get_test_example_file('target-240p.mp4'), '-o', get_test_output_file('test-swap-face-to-video.mp4'), '--trim-frame-end', '10', '--headless' ]
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275

	assert subprocess.run(commands).returncode == 0
	assert is_test_output_file('test-swap-face-to-video.mp4') is True
