from typing import Union, ContextManager
import threading
from contextlib import nullcontext

from facefusion.execution import has_execution_provider

THREAD_LOCK : threading.Lock = threading.Lock()
THREAD_SEMAPHORE : threading.Semaphore = threading.Semaphore()
NULL_CONTEXT : ContextManager[None] = nullcontext()


def thread_lock() -> threading.Lock:
	return THREAD_LOCK


def thread_semaphore() -> threading.Semaphore:
	return THREAD_SEMAPHORE


def conditional_thread_semaphore() -> Union[threading.Semaphore, ContextManager[None]]:
<<<<<<< HEAD
	if has_execution_provider('directml'):
=======
	if has_execution_provider('DmlExecutionProvider'):
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
		return THREAD_SEMAPHORE
	return NULL_CONTEXT
