from transformers import AutoConfig, AutoImageProcessor, AutoModelForCausalLM

from .configuration_mineru2 import Mineru2QwenConfig
from .image_processing_mineru2 import Mineru2ImageProcessor
from .modeling_mineru2 import Mineru2QwenForCausalLM

AutoConfig.register(Mineru2QwenConfig.model_type, Mineru2QwenConfig)
AutoModelForCausalLM.register(Mineru2QwenConfig, Mineru2QwenForCausalLM)
AutoImageProcessor.register(Mineru2QwenConfig, slow_image_processor_class=Mineru2ImageProcessor)
