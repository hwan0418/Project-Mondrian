import torch
from PIL import Image
from lavis.models import load_model_and_preprocess

# Generate text caption for image in string, especially objects within the image.
def objects(device, raw_image):
	model, vis_processors, _ = load_model_and_preprocess(name="blip_caption", model_type="large_coco", is_eval=True, device=device)
	image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
	caption = model.generate({"image": image})[0]
	return caption

# Generate spatial, temporal details of image in string.
def spatiotemporal(device, raw_image):
    model, vis_processors, txt_processors = load_model_and_preprocess(name="blip_vqa", model_type="vqav2", is_eval=True, device=device)
    questions = ["Which place is this image taken?", "How is the weather in this image?"]
    image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
    dtls = []
    for question in questions:
        q = txt_processors["eval"](question)
        dtls.append(model.predict_answers(samples={"image": image, "text_input": q}, inference_method="generate")[0])
    return dtls
    
    
def caption(imgdir):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    raw_image = Image.open(imgdir).convert("RGB")
    res = []
    res.append(objects(device, raw_image))
    res+=spatiotemporal(device, raw_image)
    return res
    
if __name__=="__main__":
    path = input("Pass me the file path of image! : ")
    cap = caption(path)
    print(cap)
