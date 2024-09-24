from api.api_helpers import generate_image_by_prompt
from utils.helpers.randomize_seed import generate_random_15_digit_number
from api.open_websocket import open_websocket_connection
import json
def prompt_to_image(workflow, model_image_path, cloth_image_path, save_previews=False):
  prompt = json.loads(workflow)

  model_loader = [node for node in prompt['nodes'] if node['id'] == 1 and node['type'] == 'LoadImage'][0]
  model_filename = model_image_path.split('/')[-1]
  model_loader['widgets_values'][0] = model_filename

  cloth_loader = [node for node in prompt['nodes'] if node['id'] == 4 and node['type'] == 'LoadImage'][0]
  cloth_filename = cloth_image_path.split('/')[-1]
  cloth_loader['widgets_values'][0] = cloth_filenameㅌ

  generate_image_by_prompt(prompt, './output/', save_previews)
