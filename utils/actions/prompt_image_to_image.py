from api.api_helpers import generate_image_by_prompt_and_image
import json


def prompt_image_to_image(workflow, model_image_path, cloth_image_path, category, save_previews=False):
  prompt = json.loads(workflow)

  prompt["1"]['inputs']['image'] = model_image_path.split('/')[-1]
  prompt["4"]['inputs']['image'] = cloth_image_path.split('/')[-1]

  prompt["10"]['inputs']['type'] = category

  generate_image_by_prompt_and_image(prompt, './output/', model_image_path, cloth_image_path, save_previews)