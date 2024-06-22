<<<<<<< HEAD
import subprocess
import pytest

import facefusion.globals
from facefusion.typing import Args
from facefusion.download import conditional_download
from facefusion.filesystem import copy_file
from facefusion.jobs.job_manager import init_jobs, clear_jobs, create_job, submit_job, submit_jobs, add_step
from facefusion.jobs.job_runner import run_job, run_jobs, run_steps, finalize_steps, collect_output_set
from .helper import get_test_jobs_directory, get_test_examples_directory, get_test_example_file, get_test_output_file, prepare_test_output_directory, is_test_output_file
=======
import os
import subprocess
import tempfile
import pytest

from facefusion.typing import Args
from facefusion.download import conditional_download
from facefusion.job_manager import init_jobs, clear_jobs, create_job, submit_job, submit_jobs, add_step
from facefusion.job_runner import run_job, run_jobs, run_steps, finalize_steps, collect_merge_set
from .helper import get_test_jobs_directory, get_test_examples_directory, get_test_example_file, prepare_test_output_directory
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275


@pytest.fixture(scope = 'module', autouse = True)
def before_all() -> None:
	conditional_download(get_test_examples_directory(),
	[
		'https://github.com/facefusion/facefusion-assets/releases/download/examples/source.jpg',
<<<<<<< HEAD
		'https://github.com/facefusion/facefusion-assets/releases/download/examples/target-240p.mp4'
	])
	subprocess.run([ 'ffmpeg', '-i', get_test_example_file('target-240p.mp4'), '-vframes', '1', get_test_example_file('target-240p.jpg') ])
	facefusion.globals.output_audio_encoder = 'aac'
=======
		'https://github.com/facefusion/facefusion-assets/releases/download/examples/target-240p.mp4',
		'https://github.com/facefusion/facefusion-assets/releases/download/examples/target-1080p.mp4'
	])
	subprocess.run([ 'ffmpeg', '-i', get_test_example_file('target-240p.mp4'), '-vframes', '1', get_test_example_file('target-240p.jpg') ])
	subprocess.run([ 'ffmpeg', '-i', get_test_example_file('target-1080p.mp4'), '-vframes', '1', get_test_example_file('target-1080p.jpg') ])
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275


@pytest.fixture(scope = 'function', autouse = True)
def before_each() -> None:
	clear_jobs(get_test_jobs_directory())
	init_jobs(get_test_jobs_directory())
	prepare_test_output_directory()


def process_step(step_args : Args) -> bool:
<<<<<<< HEAD
	return copy_file(step_args.get('target_path'), step_args.get('output_path'))
=======
	return 'source_path' in step_args and 'target_path' in step_args and 'output_path' in step_args
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275


def test_run_job() -> None:
	args_1 =\
	{
		'source_path': get_test_example_file('source.jpg'),
		'target_path': get_test_example_file('target-240p.mp4'),
<<<<<<< HEAD
		'output_path': get_test_output_file('output-1.mp4')
=======
		'output_path': get_test_example_file('output.mp4')
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	}
	args_2 =\
	{
		'source_path': get_test_example_file('source.jpg'),
		'target_path': get_test_example_file('target-240p.mp4'),
<<<<<<< HEAD
		'output_path': get_test_output_file('output-2.mp4')
=======
		'output_path': get_test_example_file('output.mp4')
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	}
	args_3 =\
	{
		'source_path': get_test_example_file('source.jpg'),
		'target_path': get_test_example_file('target-240p.jpg'),
<<<<<<< HEAD
		'output_path': get_test_output_file('output-1.jpg')
=======
		'output_path': get_test_example_file('output.jpg')
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	}

	assert run_job('job-test-run-job', process_step) is False

	create_job('job-test-run-job')
	add_step('job-test-run-job', args_1)
	add_step('job-test-run-job', args_2)
<<<<<<< HEAD
	add_step('job-test-run-job', args_2)
=======
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	add_step('job-test-run-job', args_3)

	assert run_job('job-test-run-job', process_step) is False

	submit_job('job-test-run-job')

	assert run_job('job-test-run-job', process_step) is True


def test_run_jobs() -> None:
	args_1 =\
	{
		'source_path': get_test_example_file('source.jpg'),
		'target_path': get_test_example_file('target-240p.mp4'),
<<<<<<< HEAD
		'output_path': get_test_output_file('output-1.mp4')
=======
		'output_path': get_test_example_file('output.mp4')
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	}
	args_2 =\
	{
		'source_path': get_test_example_file('source.jpg'),
		'target_path': get_test_example_file('target-240p.mp4'),
<<<<<<< HEAD
		'output_path': get_test_output_file('output-2.mp4')
=======
		'output_path': get_test_example_file('output.mp4')
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	}
	args_3 =\
	{
		'source_path': get_test_example_file('source.jpg'),
		'target_path': get_test_example_file('target-240p.jpg'),
<<<<<<< HEAD
		'output_path': get_test_output_file('output-1.jpg')
=======
		'output_path': get_test_example_file('output.jpg')
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	}

	assert run_jobs(process_step) is False

	create_job('job-test-run-jobs-1')
	create_job('job-test-run-jobs-2')
	add_step('job-test-run-jobs-1', args_1)
<<<<<<< HEAD
	add_step('job-test-run-jobs-1', args_1)
	add_step('job-test-run-jobs-2', args_2)
	add_step('job-test-run-jobs-3', args_3)
=======
	add_step('job-test-run-jobs-1', args_2)
	add_step('job-test-run-jobs-2', args_3)
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275

	assert run_jobs(process_step) is False

	submit_jobs()

	assert run_jobs(process_step) is True


@pytest.mark.skip()
def test_retry_job() -> None:
	pass


@pytest.mark.skip()
def test_retry_jobs() -> None:
	pass


def test_run_steps() -> None:
	args_1 =\
	{
		'source_path': get_test_example_file('source.jpg'),
		'target_path': get_test_example_file('target-240p.mp4'),
<<<<<<< HEAD
		'output_path': get_test_output_file('output-1.mp4')
=======
		'output_path': get_test_example_file('output.mp4')
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	}
	args_2 =\
	{
		'source_path': get_test_example_file('source.jpg'),
		'target_path': get_test_example_file('target-240p.mp4'),
<<<<<<< HEAD
		'output_path': get_test_output_file('output-2.mp4')
=======
		'output_path': get_test_example_file('output.mp4')
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	}
	args_3 =\
	{
		'source_path': get_test_example_file('source.jpg'),
		'target_path': get_test_example_file('target-240p.jpg'),
<<<<<<< HEAD
		'output_path': get_test_output_file('output-1.jpg')
=======
		'output_path': get_test_example_file('output.jpg')
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	}

	assert run_steps('job-run-steps', process_step) is False

	create_job('job-run-steps')
	add_step('job-run-steps', args_1)
<<<<<<< HEAD
	add_step('job-run-steps', args_1)
=======
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	add_step('job-run-steps', args_2)
	add_step('job-run-steps', args_3)

	assert run_steps('job-run-steps', process_step) is True


def test_finalize_steps() -> None:
	args_1 =\
	{
		'source_path': get_test_example_file('source.jpg'),
		'target_path': get_test_example_file('target-240p.mp4'),
<<<<<<< HEAD
		'output_path': get_test_output_file('output-1.mp4')
=======
		'output_path': get_test_example_file('output.mp4')
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	}
	args_2 =\
	{
		'source_path': get_test_example_file('source.jpg'),
		'target_path': get_test_example_file('target-240p.mp4'),
<<<<<<< HEAD
		'output_path': get_test_output_file('output-2.mp4')
=======
		'output_path': get_test_example_file('output.mp4')
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	}
	args_3 =\
	{
		'source_path': get_test_example_file('source.jpg'),
		'target_path': get_test_example_file('target-240p.jpg'),
<<<<<<< HEAD
		'output_path': get_test_output_file('output-1.jpg')
=======
		'output_path': get_test_example_file('output.jpg')
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	}

	create_job('job-finalize-steps')
	add_step('job-finalize-steps', args_1)
<<<<<<< HEAD
	add_step('job-finalize-steps', args_1)
	add_step('job-finalize-steps', args_2)
	add_step('job-finalize-steps', args_3)

	copy_file(args_1.get('target_path'), get_test_output_file('output-1-job-finalize-steps-0.mp4'))
	copy_file(args_1.get('target_path'), get_test_output_file('output-1-job-finalize-steps-1.mp4'))
	copy_file(args_2.get('target_path'), get_test_output_file('output-2-job-finalize-steps-2.mp4'))
	copy_file(args_3.get('target_path'), get_test_output_file('output-1-job-finalize-steps-3.jpg'))

	assert finalize_steps('job-finalize-steps') is True
	assert is_test_output_file('output-1.mp4') is True
	assert is_test_output_file('output-2.mp4') is True
	assert is_test_output_file('output-1.jpg') is True


def test_collect_output_set() -> None:
=======
	add_step('job-finalize-steps', args_2)
	add_step('job-finalize-steps', args_3)

	assert finalize_steps('job-finalize-steps') is True


def test_collect_merge_set() -> None:
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	args_1 =\
	{
		'source_path': get_test_example_file('source.jpg'),
		'target_path': get_test_example_file('target-240p.mp4'),
<<<<<<< HEAD
		'output_path': get_test_output_file('output-1.mp4')
=======
		'output_path': get_test_example_file('output.mp4')
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	}
	args_2 =\
	{
		'source_path': get_test_example_file('source.jpg'),
		'target_path': get_test_example_file('target-240p.mp4'),
<<<<<<< HEAD
		'output_path': get_test_output_file('output-2.mp4')
=======
		'output_path': get_test_example_file('output.mp4')
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	}
	args_3 =\
	{
		'source_path': get_test_example_file('source.jpg'),
		'target_path': get_test_example_file('target-240p.jpg'),
<<<<<<< HEAD
		'output_path': get_test_output_file('output-1.jpg')
	}

	create_job('job-collect-output-set')
	add_step('job-collect-output-set', args_1)
	add_step('job-collect-output-set', args_1)
	add_step('job-collect-output-set', args_2)
	add_step('job-collect-output-set', args_3)

	output_set =\
	{
		get_test_output_file('output-1.mp4'):
		[
			get_test_output_file('output-1-job-collect-output-set-0.mp4'),
			get_test_output_file('output-1-job-collect-output-set-1.mp4')
		],
		get_test_output_file('output-2.mp4'):
		[
			get_test_output_file('output-2-job-collect-output-set-2.mp4')
		],
		get_test_output_file('output-1.jpg'):
		[
			get_test_output_file('output-1-job-collect-output-set-3.jpg')
		]
	}

	assert collect_output_set('job-collect-output-set') == output_set
=======
		'output_path': get_test_example_file('output.jpg')
	}

	create_job('job-collect-merge-set')
	add_step('job-collect-merge-set', args_1)
	add_step('job-collect-merge-set', args_2)
	add_step('job-collect-merge-set', args_3)

	merge_set =\
	{
		get_test_example_file('output.mp4'):
		[
			os.path.join(tempfile.gettempdir(), 'test-examples', 'output-job-collect-merge-set-0.mp4'),
			os.path.join(tempfile.gettempdir(), 'test-examples', 'output-job-collect-merge-set-1.mp4')
		],
		get_test_example_file('output.jpg'):
		[
			os.path.join(tempfile.gettempdir(), 'test-examples', 'output-job-collect-merge-set-2.jpg')
		]
	}

	assert collect_merge_set('job-collect-merge-set') == merge_set
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
