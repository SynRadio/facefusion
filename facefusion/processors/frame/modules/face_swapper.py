from typing import Any, List, Literal, Optional
from argparse import ArgumentParser
from time import sleep
import numpy
import onnx
import onnxruntime
from onnx import numpy_helper

import facefusion.globals
<<<<<<< HEAD
import facefusion.jobs.job_manager
import facefusion.jobs.job_store
=======
import facefusion.job_manager
import facefusion.job_store
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
import facefusion.processors.frame.core as frame_processors
from facefusion import config, process_manager, logger, wording
from facefusion.execution import has_execution_provider, apply_execution_provider_options
from facefusion.face_analyser import get_one_face, get_average_face, get_many_faces, find_similar_faces, clear_face_analyser
from facefusion.face_masker import create_static_box_mask, create_occlusion_mask, create_region_mask, clear_face_occluder, clear_face_parser
from facefusion.face_helper import warp_face_by_face_landmark_5, paste_back
from facefusion.face_store import get_reference_faces
<<<<<<< HEAD
from facefusion.common_helper import get_first
from facefusion.content_analyser import clear_content_analyser
from facefusion.processors.frame.pixel_boost import explode_pixel_boost, implode_pixel_boost
from facefusion.program_helper import find_argument_group, suggest_face_swapper_pixel_boost_choices
=======
from facefusion.common_helper import get_argument_value, get_first
from facefusion.content_analyser import clear_content_analyser
from facefusion.processors.frame.pixel_boost import explode_pixel_boost, implode_pixel_boost
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
from facefusion.thread_helper import thread_lock, conditional_thread_semaphore
from facefusion.typing import Face, Embedding, VisionFrame, UpdateProgress, ProcessMode, ModelSet, OptionsWithModel, QueuePayload
from facefusion.filesystem import same_file_extension, is_file, in_directory, is_image, has_image, is_video, filter_image_paths, resolve_relative_path
from facefusion.download import conditional_download, is_download_done
from facefusion.vision import read_image, read_static_image, read_static_images, write_image, unpack_resolution
from facefusion.processors.frame.typing import FaceSwapperInputs
from facefusion.processors.frame import globals as frame_processors_globals
from facefusion.processors.frame import choices as frame_processors_choices

FRAME_PROCESSOR = None
MODEL_INITIALIZER = None
NAME = __name__.upper()
MODELS : ModelSet =\
{
	'blendswap_256':
	{
		'type': 'blendswap',
		'url': 'https://github.com/facefusion/facefusion-assets/releases/download/models/blendswap_256.onnx',
		'path': resolve_relative_path('../.assets/models/blendswap_256.onnx'),
		'template': 'ffhq_512',
		'size': (256, 256),
		'mean': [ 0.0, 0.0, 0.0 ],
		'standard_deviation': [ 1.0, 1.0, 1.0 ]
	},
	'ghost_256_unet_1':
	{
		'type': 'ghost',
		'url': 'https://github.com/facefusion/facefusion-assets/releases/download/models/ghost_256_unet_1.onnx',
		'path': resolve_relative_path('../.assets/models/ghost_256_unet_1.onnx'),
		'template': 'arcface_112_v1',
		'size': (256, 256),
		'mean': [ 0.0, 0.0, 0.0 ],
		'standard_deviation': [ 1.0, 1.0, 1.0 ]
	},
	'ghost_256_unet_2':
	{
		'type': 'ghost',
		'url': 'https://github.com/facefusion/facefusion-assets/releases/download/models/ghost_256_unet_2.onnx',
		'path': resolve_relative_path('../.assets/models/ghost_256_unet_2.onnx'),
		'template': 'arcface_112_v1',
		'size': (256, 256),
		'mean': [ 0.0, 0.0, 0.0 ],
		'standard_deviation': [ 1.0, 1.0, 1.0 ]
	},
	'ghost_256_unet_3':
	{
		'type': 'ghost',
		'url': 'https://github.com/facefusion/facefusion-assets/releases/download/models/ghost_256_unet_3.onnx',
		'path': resolve_relative_path('../.assets/models/ghost_256_unet_3.onnx'),
		'template': 'arcface_112_v1',
		'size': (256, 256),
		'mean': [ 0.0, 0.0, 0.0 ],
		'standard_deviation': [ 1.0, 1.0, 1.0 ]
	},
	'inswapper_128':
	{
		'type': 'inswapper',
		'url': 'https://github.com/facefusion/facefusion-assets/releases/download/models/inswapper_128.onnx',
		'path': resolve_relative_path('../.assets/models/inswapper_128.onnx'),
		'template': 'arcface_128_v2',
		'size': (128, 128),
		'mean': [ 0.0, 0.0, 0.0 ],
		'standard_deviation': [ 1.0, 1.0, 1.0 ]
	},
	'inswapper_128_fp16':
	{
		'type': 'inswapper',
		'url': 'https://github.com/facefusion/facefusion-assets/releases/download/models/inswapper_128_fp16.onnx',
		'path': resolve_relative_path('../.assets/models/inswapper_128_fp16.onnx'),
		'template': 'arcface_128_v2',
		'size': (128, 128),
		'mean': [ 0.0, 0.0, 0.0 ],
		'standard_deviation': [ 1.0, 1.0, 1.0 ]
	},
	'simswap_256':
	{
		'type': 'simswap',
		'url': 'https://github.com/facefusion/facefusion-assets/releases/download/models/simswap_256.onnx',
		'path': resolve_relative_path('../.assets/models/simswap_256.onnx'),
		'template': 'arcface_112_v1',
		'size': (256, 256),
		'mean': [ 0.485, 0.456, 0.406 ],
		'standard_deviation': [ 0.229, 0.224, 0.225 ]
	},
	'simswap_512_unofficial':
	{
		'type': 'simswap',
		'url': 'https://github.com/facefusion/facefusion-assets/releases/download/models/simswap_512_unofficial.onnx',
		'path': resolve_relative_path('../.assets/models/simswap_512_unofficial.onnx'),
		'template': 'arcface_112_v1',
		'size': (512, 512),
		'mean': [ 0.0, 0.0, 0.0 ],
		'standard_deviation': [ 1.0, 1.0, 1.0 ]
	},
	'uniface_256':
	{
		'type': 'uniface',
		'url': 'https://github.com/facefusion/facefusion-assets/releases/download/models/uniface_256.onnx',
		'path': resolve_relative_path('../.assets/models/uniface_256.onnx'),
		'template': 'ffhq_512',
		'size': (256, 256),
		'mean': [ 0.0, 0.0, 0.0 ],
		'standard_deviation': [ 1.0, 1.0, 1.0 ]
	}
}
OPTIONS : Optional[OptionsWithModel] = None


def get_frame_processor() -> Any:
	global FRAME_PROCESSOR

	with thread_lock():
		while process_manager.is_checking():
			sleep(0.5)
		if FRAME_PROCESSOR is None:
			model_path = get_options('model').get('path')
			FRAME_PROCESSOR = onnxruntime.InferenceSession(model_path, providers = apply_execution_provider_options(facefusion.globals.execution_device_id, facefusion.globals.execution_providers))
	return FRAME_PROCESSOR


def clear_frame_processor() -> None:
	global FRAME_PROCESSOR

	FRAME_PROCESSOR = None


def get_model_initializer() -> Any:
	global MODEL_INITIALIZER

	with thread_lock():
		while process_manager.is_checking():
			sleep(0.5)
		if MODEL_INITIALIZER is None:
			model_path = get_options('model').get('path')
			model = onnx.load(model_path)
			MODEL_INITIALIZER = numpy_helper.to_array(model.graph.initializer[-1])
	return MODEL_INITIALIZER


def clear_model_initializer() -> None:
	global MODEL_INITIALIZER

	MODEL_INITIALIZER = None


def get_options(key : Literal['model']) -> Any:
	global OPTIONS

	if OPTIONS is None:
		OPTIONS =\
		{
			'model': MODELS[frame_processors_globals.face_swapper_model]
		}
	return OPTIONS.get(key)


def set_options(key : Literal['model'], value : Any) -> None:
	global OPTIONS

	OPTIONS[key] = value


def register_args(program : ArgumentParser) -> None:
	if has_execution_provider('coreml') or has_execution_provider('openvino'):
		face_swapper_model_fallback = 'inswapper_128'
	else:
		face_swapper_model_fallback = 'inswapper_128_fp16'
<<<<<<< HEAD
	group_frame_processors = find_argument_group(program, 'frame processors')
	if group_frame_processors:
		group_frame_processors.add_argument('--face-swapper-model', help = wording.get('help.face_swapper_model'), default = config.get_str_value('frame_processors.face_swapper_model', face_swapper_model_fallback), choices = frame_processors_choices.face_swapper_set.keys())
		face_swapper_pixel_boost_choices = suggest_face_swapper_pixel_boost_choices(program)
		group_frame_processors.add_argument('--face-swapper-pixel-boost', help = wording.get('help.face_swapper_pixel_boost'), default = config.get_str_value('frame_processors.face_swapper_pixel_boost', get_first(face_swapper_pixel_boost_choices)), choices = face_swapper_pixel_boost_choices)
		facefusion.jobs.job_store.register_step_keys([ 'face_swapper_model', 'face_swapper_pixel_boost' ])
=======
	face_swapper_model = get_argument_value('--face-swapper-model') or face_swapper_model_fallback
	face_swapper_pixel_boost_choices = frame_processors_choices.face_swapper_set.get(face_swapper_model) #type:ignore[call-overload]
	program.add_argument('--face-swapper-model', help = wording.get('help.face_swapper_model'), default = config.get_str_value('frame_processors.face_swapper_model', face_swapper_model_fallback), choices = frame_processors_choices.face_swapper_set.keys())
	program.add_argument('--face-swapper-pixel-boost', help = wording.get('help.face_swapper_pixel_boost'), default = config.get_str_value('frame_processors.face_swapper_pixel_boost', get_first(face_swapper_pixel_boost_choices)), choices = face_swapper_pixel_boost_choices)
	facefusion.job_store.register_step_args([ 'face_swapper_model', 'face_swapper_pixel_boost' ])
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275


def apply_args(program : ArgumentParser) -> None:
	args = program.parse_args()
	frame_processors_globals.face_swapper_model = args.face_swapper_model
	frame_processors_globals.face_swapper_pixel_boost = args.face_swapper_pixel_boost
<<<<<<< HEAD

=======
>>>>>>> 04385b9a6e4bd5450d6f698e9b9ae040a6d66275
	if args.face_swapper_model == 'blendswap_256':
		facefusion.globals.face_recognizer_model = 'arcface_blendswap'
	if args.face_swapper_model in [ 'ghost_256_unet_1', 'ghost_256_unet_2', 'ghost_256_unet_3' ]:
		facefusion.globals.face_recognizer_model = 'arcface_ghost'
	if args.face_swapper_model in [ 'inswapper_128', 'inswapper_128_fp16' ]:
		facefusion.globals.face_recognizer_model = 'arcface_inswapper'
	if args.face_swapper_model in [ 'simswap_256', 'simswap_512_unofficial' ]:
		facefusion.globals.face_recognizer_model = 'arcface_simswap'
	if args.face_swapper_model == 'uniface_256':
		facefusion.globals.face_recognizer_model = 'arcface_uniface'


def pre_check() -> bool:
	download_directory_path = resolve_relative_path('../.assets/models')
	model_url = get_options('model').get('url')
	model_path = get_options('model').get('path')

	if not facefusion.globals.skip_download:
		process_manager.check()
		conditional_download(download_directory_path, [ model_url ])
		process_manager.end()
	return is_file(model_path)


def post_check() -> bool:
	model_url = get_options('model').get('url')
	model_path = get_options('model').get('path')

	if not facefusion.globals.skip_download and not is_download_done(model_url, model_path):
		logger.error(wording.get('model_download_not_done') + wording.get('exclamation_mark'), NAME)
		return False
	if not is_file(model_path):
		logger.error(wording.get('model_file_not_present') + wording.get('exclamation_mark'), NAME)
		return False
	return True


def pre_process(mode : ProcessMode) -> bool:
	if not has_image(facefusion.globals.source_paths):
		logger.error(wording.get('choose_image_source') + wording.get('exclamation_mark'), NAME)
		return False
	source_image_paths = filter_image_paths(facefusion.globals.source_paths)
	source_frames = read_static_images(source_image_paths)
	for source_frame in source_frames:
		if not get_one_face(source_frame):
			logger.error(wording.get('no_source_face_detected') + wording.get('exclamation_mark'), NAME)
			return False
	if mode in [ 'output', 'preview' ] and not is_image(facefusion.globals.target_path) and not is_video(facefusion.globals.target_path):
		logger.error(wording.get('choose_image_or_video_target') + wording.get('exclamation_mark'), NAME)
		return False
	if mode == 'output' and not in_directory(facefusion.globals.output_path):
		logger.error(wording.get('specify_image_or_video_output') + wording.get('exclamation_mark'), NAME)
		return False
	if mode == 'output' and not same_file_extension([ facefusion.globals.target_path, facefusion.globals.output_path ]):
		logger.error(wording.get('match_target_and_output_extension') + wording.get('exclamation_mark'), NAME)
		return False
	return True


def post_process() -> None:
	read_static_image.cache_clear()
	if facefusion.globals.video_memory_strategy == 'strict' or facefusion.globals.video_memory_strategy == 'moderate':
		clear_model_initializer()
		clear_frame_processor()
	if facefusion.globals.video_memory_strategy == 'strict':
		clear_face_analyser()
		clear_content_analyser()
		clear_face_occluder()
		clear_face_parser()


def swap_face(source_face : Face, target_face : Face, temp_vision_frame : VisionFrame) -> VisionFrame:
	model_template = get_options('model').get('template')
	model_size = get_options('model').get('size')
	pixel_boost_size = unpack_resolution(frame_processors_globals.face_swapper_pixel_boost)
	pixel_boost_total = pixel_boost_size[0] // model_size[0]
	crop_vision_frame, affine_matrix = warp_face_by_face_landmark_5(temp_vision_frame, target_face.landmark_set.get('5/68'), model_template, pixel_boost_size)
	crop_masks = []
	temp_vision_frames = []

	if 'box' in facefusion.globals.face_mask_types:
		box_mask = create_static_box_mask(crop_vision_frame.shape[:2][::-1], facefusion.globals.face_mask_blur, facefusion.globals.face_mask_padding)
		crop_masks.append(box_mask)
	if 'occlusion' in facefusion.globals.face_mask_types:
		occlusion_mask = create_occlusion_mask(crop_vision_frame)
		crop_masks.append(occlusion_mask)
	pixel_boost_vision_frames = implode_pixel_boost(crop_vision_frame, pixel_boost_total, model_size)
	for pixel_boost_vision_frame in pixel_boost_vision_frames:
		pixel_boost_vision_frame = prepare_crop_frame(pixel_boost_vision_frame)
		pixel_boost_vision_frame = apply_swap(source_face, pixel_boost_vision_frame)
		pixel_boost_vision_frame = normalize_crop_frame(pixel_boost_vision_frame)
		temp_vision_frames.append(pixel_boost_vision_frame)
	crop_vision_frame = explode_pixel_boost(temp_vision_frames, pixel_boost_total, model_size, pixel_boost_size)
	if 'region' in facefusion.globals.face_mask_types:
		region_mask = create_region_mask(crop_vision_frame, facefusion.globals.face_mask_regions)
		crop_masks.append(region_mask)
	crop_mask = numpy.minimum.reduce(crop_masks).clip(0, 1)
	temp_vision_frame = paste_back(temp_vision_frame, crop_vision_frame, crop_mask, affine_matrix)
	return temp_vision_frame


def apply_swap(source_face : Face, crop_vision_frame : VisionFrame) -> VisionFrame:
	frame_processor = get_frame_processor()
	model_type = get_options('model').get('type')
	frame_processor_inputs = {}

	for frame_processor_input in frame_processor.get_inputs():
		if frame_processor_input.name == 'source':
			if model_type == 'blendswap' or model_type == 'uniface':
				frame_processor_inputs[frame_processor_input.name] = prepare_source_frame(source_face)
			else:
				frame_processor_inputs[frame_processor_input.name] = prepare_source_embedding(source_face)
		if frame_processor_input.name == 'target':
			frame_processor_inputs[frame_processor_input.name] = crop_vision_frame

	with conditional_thread_semaphore():
		crop_vision_frame = frame_processor.run(None, frame_processor_inputs)[0][0]

	return crop_vision_frame


def prepare_source_frame(source_face : Face) -> VisionFrame:
	model_type = get_options('model').get('type')
	source_vision_frame = read_static_image(facefusion.globals.source_paths[0])

	if model_type == 'blendswap':
		source_vision_frame, _ = warp_face_by_face_landmark_5(source_vision_frame, source_face.landmark_set.get('5/68'), 'arcface_112_v2', (112, 112))
	if model_type == 'uniface':
		source_vision_frame, _ = warp_face_by_face_landmark_5(source_vision_frame, source_face.landmark_set.get('5/68'), 'ffhq_512', (256, 256))
	source_vision_frame = source_vision_frame[:, :, ::-1] / 255.0
	source_vision_frame = source_vision_frame.transpose(2, 0, 1)
	source_vision_frame = numpy.expand_dims(source_vision_frame, axis = 0).astype(numpy.float32)
	return source_vision_frame


def prepare_source_embedding(source_face : Face) -> Embedding:
	model_type = get_options('model').get('type')

	if model_type == 'ghost':
		source_embedding = source_face.embedding.reshape(1, -1)
	elif model_type == 'inswapper':
		model_initializer = get_model_initializer()
		source_embedding = source_face.embedding.reshape((1, -1))
		source_embedding = numpy.dot(source_embedding, model_initializer) / numpy.linalg.norm(source_embedding)
	else:
		source_embedding = source_face.normed_embedding.reshape(1, -1)
	return source_embedding


def prepare_crop_frame(crop_vision_frame : VisionFrame) -> VisionFrame:
	model_type = get_options('model').get('type')
	model_mean = get_options('model').get('mean')
	model_standard_deviation = get_options('model').get('standard_deviation')

	if model_type == 'ghost':
		crop_vision_frame = crop_vision_frame[:, :, ::-1] / 127.5 - 1
	else:
		crop_vision_frame = crop_vision_frame[:, :, ::-1] / 255.0
	crop_vision_frame = (crop_vision_frame - model_mean) / model_standard_deviation
	crop_vision_frame = crop_vision_frame.transpose(2, 0, 1)
	crop_vision_frame = numpy.expand_dims(crop_vision_frame, axis = 0).astype(numpy.float32)
	return crop_vision_frame


def normalize_crop_frame(crop_vision_frame : VisionFrame) -> VisionFrame:
	model_template = get_options('model').get('type')
	crop_vision_frame = crop_vision_frame.transpose(1, 2, 0)

	if model_template == 'ghost':
		crop_vision_frame = (crop_vision_frame * 127.5 + 127.5).round()
	else:
		crop_vision_frame = (crop_vision_frame * 255.0).round()
	crop_vision_frame = crop_vision_frame[:, :, ::-1]
	return crop_vision_frame


def get_reference_frame(source_face : Face, target_face : Face, temp_vision_frame : VisionFrame) -> VisionFrame:
	return swap_face(source_face, target_face, temp_vision_frame)


def process_frame(inputs : FaceSwapperInputs) -> VisionFrame:
	reference_faces = inputs.get('reference_faces')
	source_face = inputs.get('source_face')
	target_vision_frame = inputs.get('target_vision_frame')

	if facefusion.globals.face_selector_mode == 'many':
		many_faces = get_many_faces(target_vision_frame)
		if many_faces:
			for target_face in many_faces:
				target_vision_frame = swap_face(source_face, target_face, target_vision_frame)
	if facefusion.globals.face_selector_mode == 'one':
		target_face = get_one_face(target_vision_frame)
		if target_face:
			target_vision_frame = swap_face(source_face, target_face, target_vision_frame)
	if facefusion.globals.face_selector_mode == 'reference':
		similar_faces = find_similar_faces(reference_faces, target_vision_frame, facefusion.globals.reference_face_distance)
		if similar_faces:
			for similar_face in similar_faces:
				target_vision_frame = swap_face(source_face, similar_face, target_vision_frame)
	return target_vision_frame


def process_frames(source_paths : List[str], queue_payloads : List[QueuePayload], update_progress : UpdateProgress) -> None:
	reference_faces = get_reference_faces() if 'reference' in facefusion.globals.face_selector_mode else None
	source_frames = read_static_images(source_paths)
	source_face = get_average_face(source_frames)

	for queue_payload in process_manager.manage(queue_payloads):
		target_vision_path = queue_payload['frame_path']
		target_vision_frame = read_image(target_vision_path)
		output_vision_frame = process_frame(
		{
			'reference_faces': reference_faces,
			'source_face': source_face,
			'target_vision_frame': target_vision_frame
		})
		write_image(target_vision_path, output_vision_frame)
		update_progress(1)


def process_image(source_paths : List[str], target_path : str, output_path : str) -> None:
	reference_faces = get_reference_faces() if 'reference' in facefusion.globals.face_selector_mode else None
	source_frames = read_static_images(source_paths)
	source_face = get_average_face(source_frames)
	target_vision_frame = read_static_image(target_path)
	output_vision_frame = process_frame(
	{
		'reference_faces': reference_faces,
		'source_face': source_face,
		'target_vision_frame': target_vision_frame
	})
	write_image(output_path, output_vision_frame)


def process_video(source_paths : List[str], temp_frame_paths : List[str]) -> None:
	frame_processors.multi_process_frames(source_paths, temp_frame_paths, process_frames)
