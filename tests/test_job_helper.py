import os

<<<<<<< HEAD
from facefusion.jobs.job_helper import get_step_output_path
=======
from facefusion.job_helper import get_step_output_path
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275


def test_get_step_output_path() -> None:
	assert get_step_output_path('test-job', 0, 'test.mp4') == 'test-test-job-0.mp4'
	assert get_step_output_path('test-job', 0, 'test/test.mp4') == os.path.join('test', 'test-test-job-0.mp4')
