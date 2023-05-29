from diffusers import AudioLDMPipeline
import torch

def txt2aud(prompt):

    repo_id = "cvssp/audioldm-s-full-v2"
    pipe = AudioLDMPipeline.from_pretrained(repo_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    audio = pipe(prompt, num_inference_steps=10, audio_length_in_s=5.0).audios[0]

    return audio
