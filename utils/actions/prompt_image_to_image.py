from api.api_helpers import generate_image_by_prompt_and_image
import json

def prompt_image_to_image(workflow, image1_path, image2_path, ootd_pipeline_option, save_previews=False):
  prompt = json.loads(workflow)

  load_image_nodes = [node for node in prompt['nodes'] if node['type'] == 'LoadImage']

  if len(load_image_nodes) < 2:
    raise ValueError("Workflow must contain at least two LoadImage nodes")

  load_image_nodes[0]['widgets_values'][0] = image1_path.split('/')[-1]
  load_image_nodes[1]['widgets_values'][0] = image2_path.split('/')[-1]

  ootd_pipeline_node = next(node for node in prompt['nodes'] if node['type'] == 'LoadOOTDPipelineHub')
  ootd_pipeline_node['widgets_values'][0] = ootd_pipeline_option

  generate_image_by_prompt_and_image(prompt, './output/', image1_path, image2_path, save_previews)