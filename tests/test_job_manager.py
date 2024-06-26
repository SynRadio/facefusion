import pytest

<<<<<<< HEAD
from facefusion.jobs.job_manager import init_jobs, clear_jobs, create_job, submit_job, submit_jobs, delete_job, delete_jobs, find_job_ids, move_job_file, add_step, remix_step, insert_step, remove_step, get_steps, count_step_total, set_step_status, set_steps_status
=======
from facefusion.job_manager import init_jobs, clear_jobs, create_job, submit_job, submit_jobs, delete_job, delete_jobs, find_job_ids, move_job_file, add_step, remix_step, insert_step, remove_step, get_steps, set_step_status, set_steps_status
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
from .helper import get_test_jobs_directory


@pytest.fixture(scope = 'function', autouse = True)
def before_each() -> None:
	clear_jobs(get_test_jobs_directory())
	init_jobs(get_test_jobs_directory())


def test_create_job() -> None:
<<<<<<< HEAD
	args_1 =\
	{
		'source_path': 'source-1.jpg',
		'target_path': 'target-1.jpg',
		'output_path': 'output-1.jpg'
	}

	assert create_job('job-test-create-job') is True
	assert create_job('job-test-create-job') is False

	add_step('job-test-submit-job', args_1)
	submit_job('job-test-create-job')

	assert create_job('job-test-create-job') is False


def test_submit_job() -> None:
	args_1 =\
	{
		'source_path': 'source-1.jpg',
		'target_path': 'target-1.jpg',
		'output_path': 'output-1.jpg'
	}

	assert submit_job('job-test-submit-job') is False

	create_job('job-test-submit-job')

	assert submit_job('job-test-submit-job') is False

	add_step('job-test-submit-job', args_1)

	assert submit_job('job-test-submit-job') is True
	assert submit_job('job-test-submit-job') is False


def test_submit_jobs() -> None:
	args_1 =\
	{
		'source_path': 'source-1.jpg',
		'target_path': 'target-1.jpg',
		'output_path': 'output-1.jpg'
	}
	args_2 =\
	{
		'source_path': 'source-2.jpg',
		'target_path': 'target-2.jpg',
		'output_path': 'output-2.jpg'
	}

=======
	assert create_job('job-test-create-job-1') is True
	assert create_job('job-test-create-job-1') is False

	submit_job('job-test-create-job-1')
	submit_job('job-test-create-job-2')

	assert create_job('job-test-create-job-1') is False


def test_submit_job() -> None:
	assert submit_job('job-test-submit-job-1') is False

	create_job('job-test-submit-job-1')
	create_job('job-test-submit-job-2')

	assert submit_job('job-test-submit-job-1') is True
	assert submit_job('job-test-submit-job-1') is False


def test_submit_jobs() -> None:
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	assert submit_jobs() is False

	create_job('job-test-submit-jobs-1')
	create_job('job-test-submit-jobs-2')

<<<<<<< HEAD
	assert submit_jobs() is False

	add_step('job-test-submit-jobs-1', args_1)
	add_step('job-test-submit-jobs-2', args_2)

	assert submit_jobs() is True
	assert submit_jobs() is False


def test_delete_job() -> None:
	assert delete_job('job-test-delete-job') is False

	create_job('job-test-delete-job')

	assert delete_job('job-test-delete-job') is True
	assert delete_job('job-test-delete-job') is False
=======
	assert submit_jobs() is True


def test_delete_job() -> None:
	assert delete_job('job-test-delete-job-1') is False

	create_job('job-test-delete-job-1')
	create_job('job-test-delete-job-2')

	assert delete_job('job-test-delete-job-1') is True
	assert delete_job('job-test-delete-job-1') is False
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275


def test_delete_jobs() -> None:
	assert delete_jobs() is False

	create_job('job-test-delete-jobs-1')
	create_job('job-test-delete-jobs-2')

	assert delete_jobs() is True


<<<<<<< HEAD
@pytest.mark.skip()
def test_find_jobs() -> None:
	pass


=======
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
def test_find_job_ids() -> None:
	create_job('job-test-find-job-ids-1')
	create_job('job-test-find-job-ids-2')
	create_job('job-test-find-job-ids-3')

	assert find_job_ids('drafted') == [ 'job-test-find-job-ids-1', 'job-test-find-job-ids-2', 'job-test-find-job-ids-3' ]
	assert find_job_ids('queued') == []
	assert find_job_ids('completed') == []
	assert find_job_ids('failed') == []

	move_job_file('job-test-find-job-ids-1', 'queued')
	move_job_file('job-test-find-job-ids-2', 'queued')
	move_job_file('job-test-find-job-ids-3', 'queued')

	assert find_job_ids('drafted') == []
	assert find_job_ids('queued') == [ 'job-test-find-job-ids-1', 'job-test-find-job-ids-2', 'job-test-find-job-ids-3' ]
	assert find_job_ids('completed') == []
	assert find_job_ids('failed') == []

	move_job_file('job-test-find-job-ids-1', 'completed')

	assert find_job_ids('drafted') == []
	assert find_job_ids('queued') == [ 'job-test-find-job-ids-2', 'job-test-find-job-ids-3' ]
	assert find_job_ids('completed') == [ 'job-test-find-job-ids-1' ]
	assert find_job_ids('failed') == []

	move_job_file('job-test-find-job-ids-2', 'failed')

	assert find_job_ids('drafted') == []
	assert find_job_ids('queued') == [ 'job-test-find-job-ids-3' ]
	assert find_job_ids('completed') == [ 'job-test-find-job-ids-1' ]
	assert find_job_ids('failed') == [ 'job-test-find-job-ids-2' ]

	move_job_file('job-test-find-job-ids-3', 'completed')

	assert find_job_ids('drafted') == []
	assert find_job_ids('queued') == []
	assert find_job_ids('completed') == [ 'job-test-find-job-ids-1', 'job-test-find-job-ids-3' ]
	assert find_job_ids('failed') == [ 'job-test-find-job-ids-2' ]


def test_add_step() -> None:
	args_1 =\
	{
		'source_path': 'source-1.jpg',
		'target_path': 'target-1.jpg',
		'output_path': 'output-1.jpg'
	}
	args_2 =\
	{
		'source_path': 'source-2.jpg',
		'target_path': 'target-2.jpg',
		'output_path': 'output-2.jpg'
	}

	assert add_step('job-test-add-step', args_1) is False

	create_job('job-test-add-step')

	assert add_step('job-test-add-step', args_1) is True
	assert add_step('job-test-add-step', args_2) is True

	steps = get_steps('job-test-add-step')

	assert steps[0].get('args') == args_1
	assert steps[1].get('args') == args_2
<<<<<<< HEAD
	assert count_step_total('job-test-add-step') == 2
=======
	assert len(steps) == 2
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275


def test_remix_step() -> None:
	args_1 =\
	{
		'source_path': 'source-1.jpg',
		'target_path': 'target-1.jpg',
		'output_path': 'output-1.jpg'
	}
	args_2 =\
	{
		'source_path': 'source-2.jpg',
		'target_path': 'target-2.jpg',
		'output_path': 'output-2.jpg'
	}

	assert remix_step('job-test-remix-step', 0, args_1) is False

	create_job('job-test-remix-step')
	add_step('job-test-remix-step', args_1)
	add_step('job-test-remix-step', args_2)

	assert remix_step('job-test-remix-step', 0, args_2) is True

	steps = get_steps('job-test-remix-step')

	assert steps[0].get('args') == args_1
	assert steps[1].get('args') == args_2
	assert steps[2].get('args').get('source_path') == args_2.get('source_path')
	assert steps[2].get('args').get('target_path') == args_1.get('output_path')
	assert steps[2].get('args').get('output_path') == args_2.get('output_path')
<<<<<<< HEAD
	assert count_step_total('job-test-remix-step') == 3
=======
	assert len(steps) == 3
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275


def test_insert_step() -> None:
	args_1 =\
	{
		'source_path': 'source-1.jpg',
		'target_path': 'target-1.jpg',
		'output_path': 'output-1.jpg'
	}
	args_2 =\
	{
		'source_path': 'source-2.jpg',
		'target_path': 'target-2.jpg',
		'output_path': 'output-2.jpg'
	}
	args_3 =\
	{
		'source_path': 'source-3.jpg',
		'target_path': 'target-3.jpg',
		'output_path': 'output-3.jpg'
	}

	assert insert_step('job-test-insert-step', 0, args_1) is False

	create_job('job-test-insert-step')
	add_step('job-test-insert-step', args_1)
	add_step('job-test-insert-step', args_1)

	assert insert_step('job-test-insert-step', 1, args_2) is True
	assert insert_step('job-test-insert-step', -1, args_3) is True

	steps = get_steps('job-test-insert-step')

	assert steps[0].get('args') == args_1
	assert steps[1].get('args') == args_2
	assert steps[2].get('args') == args_1
	assert steps[3].get('args') == args_3
<<<<<<< HEAD
	assert count_step_total('job-test-insert-step') == 4
=======
	assert len(steps) == 4
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275


def test_remove_step() -> None:
	args_1 =\
	{
		'source_path': 'source-1.jpg',
		'target_path': 'target-1.jpg',
		'output_path': 'output-1.jpg'
	}
	args_2 =\
	{
		'source_path': 'source-2.jpg',
		'target_path': 'target-2.jpg',
		'output_path': 'output-2.jpg'
	}
	args_3 =\
	{
		'source_path': 'source-3.jpg',
		'target_path': 'target-3.jpg',
		'output_path': 'output-3.jpg'
	}

	assert remove_step('job-test-insert-step', 0) is False

	create_job('job-test-remove-step')
	add_step('job-test-remove-step', args_1)
	add_step('job-test-remove-step', args_2)
	add_step('job-test-remove-step', args_1)
	add_step('job-test-remove-step', args_3)

	assert remove_step('job-test-remove-step', 1) is True
	assert remove_step('job-test-remove-step', -1) is True

	steps = get_steps('job-test-remove-step')

	assert steps[0].get('args') == args_1
	assert steps[1].get('args') == args_1
<<<<<<< HEAD
	assert count_step_total('job-test-remove-step') == 2
=======
	assert len(steps) == 2
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275


def test_get_steps() -> None:
	args_1 =\
	{
		'source_path': 'source-1.jpg',
		'target_path': 'target-1.jpg',
		'output_path': 'output-1.jpg'
	}
	args_2 =\
	{
		'source_path': 'source-2.jpg',
		'target_path': 'target-2.jpg',
		'output_path': 'output-2.jpg'
	}

	assert get_steps('job-test-get-steps') == []

	create_job('job-test-get-steps')
	add_step('job-test-get-steps', args_1)
	add_step('job-test-get-steps', args_2)
	steps = get_steps('job-test-get-steps')

	assert steps[0].get('args') == args_1
	assert steps[1].get('args') == args_2
<<<<<<< HEAD
	assert count_step_total('job-test-get-steps') == 2
=======
	assert len(steps) == 2
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275


def test_set_step_status() -> None:
	args_1 =\
	{
		'source_path': 'source-1.jpg',
		'target_path': 'target-1.jpg',
		'output_path': 'output-1.jpg'
	}
	args_2 =\
	{
		'source_path': 'source-2.jpg',
		'target_path': 'target-2.jpg',
		'output_path': 'output-2.jpg'
	}

	assert set_step_status('job-test-set-step-status', 0, 'completed') is False

	create_job('job-test-set-step-status')
	add_step('job-test-set-step-status', args_1)
	add_step('job-test-set-step-status', args_2)

	assert set_step_status('job-test-set-step-status', 0, 'completed') is True
	assert set_step_status('job-test-set-step-status', 1, 'failed') is True

	steps = get_steps('job-test-set-step-status')

	assert steps[0].get('status') == 'completed'
	assert steps[1].get('status') == 'failed'
<<<<<<< HEAD
	assert count_step_total('job-test-set-step-status') == 2
=======
	assert len(steps) == 2
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275


def test_set_steps_status() -> None:
	args_1 =\
	{
		'source_path': 'source-1.jpg',
		'target_path': 'target-1.jpg',
		'output_path': 'output-1.jpg'
	}
	args_2 =\
	{
		'source_path': 'source-2.jpg',
		'target_path': 'target-2.jpg',
		'output_path': 'output-2.jpg'
	}

	assert set_steps_status('job-test-set-steps-status', 'queued') is False

	create_job('job-test-set-steps-status')
	add_step('job-test-set-steps-status', args_1)
	add_step('job-test-set-steps-status', args_2)

	assert set_steps_status('job-test-set-steps-status', 'queued') is True

	steps = get_steps('job-test-set-steps-status')

	assert steps[0].get('status') == 'queued'
	assert steps[1].get('status') == 'queued'
<<<<<<< HEAD
	assert count_step_total('job-test-set-steps-status') == 2
=======
	assert len(steps) == 2
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
