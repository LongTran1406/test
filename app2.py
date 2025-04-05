# from diffusers import StableDiffusionPipeline
# import torch
from flask import Blueprint, render_template, request
import matplotlib.pyplot as plt

second = Blueprint('second', __name__, static_folder="static", template_folder="templates")

@second.route('/image_generator')
def image_generator():
    return render_template('image_generator.html')

# class ImageGenerator:
#     def __init__(self, model_path):
#         self.device = "cuda" if torch.cuda.is_available() else "cpu"
#         self.model_path = model_path
#         self.pipeline = StableDiffusionPipeline.from_pretrained(model_path, torch_dtype=torch.float16).to(self.device)
    
#     def generate_image(self, prompt):
#         with torch.no_grad():
#             image = self.pipeline(prompt).images[0]
#         return image
    
#     def display_image(self, image):
#         plt.imshow(image)
#         plt.axis('off')
#         plt.show()

#     def save_image(self, image, filename):
#         image.save(filename)

# @second.route('/generate', methods=['POST'])
# def generate():
#     prompt = request.form['prompt']
#     model_path = "D:\sentiment_app\dreamlike-photoreal-2.0"
#     generator = ImageGenerator(model_path)
#     image = generator.generate_image(prompt)
#     filename = "output.png"
#     generator.save_image(image, filename)
#     return render_template('image_geerator.html', filename=filename)