from transformers import AutoTokenizer, AutoModelForCausalLM
from watermark_detector import WatermarkDetector

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

detector = WatermarkDetector(model, tokenizer, device="cpu")
