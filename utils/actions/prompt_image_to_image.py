from api.api_helpers import generate_image_by_prompt_and_image
import json


def prompt_image_to_image(workflow, model_image_path, cloth_image_path, load_ootd_param, save_previews=False):
    prompt = json.loads(workflow)
    id_to_class_type = {id: details['class_type'] for id, details in prompt.items()}

    ootd_key = [key for key, value in id_to_class_type.items() if value == 'OOTDGenerate'][0]
    prompt.get(ootd_key)['inputs']['category'] = load_ootd_param

    load_image_keys = [key for key, value in id_to_class_type.items() if value == 'LoadImage']

    if len(load_image_keys) >= 2:
        model_image_key = load_image_keys[0]
        cloth_image_key = load_image_keys[1]

        # Set model_image path
        model_image_filename = model_image_path.split('/')[-1]
        prompt.get(model_image_key)['inputs']['image'] = model_image_filename

        # Set cloth_image path
        cloth_image_filename = cloth_image_path.split('/')[-1]
        prompt.get(cloth_image_key)['inputs']['image'] = cloth_image_filename

    generate_image_by_prompt_and_image(prompt, './output/', model_image_filename, cloth_image_filename, save_previews)