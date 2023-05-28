import torch
import subprocess
from PIL import Image
from lavis.models import load_model_and_preprocess

def img2txt(imgdir):
	device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
	raw_image = Image.open(imgdir).convert("RGB")
	model, vis_processors, _ = load_model_and_preprocess(name="blip_caption", model_type="large_coco", is_eval=True, device=device)
	image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
	caption = model.generate({"image": image})[0]
 
	return caption
