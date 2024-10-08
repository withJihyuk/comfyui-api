from utils.actions.load_workflow import load_workflow
from api.api_helpers import clear
import sys

from utils.actions.prompt_image_to_image import prompt_image_to_image


def main():
  try:
    workflow = load_workflow('./workflows/workflow.json')
    model_image_path = "./model_1.png"
    cloth_image_path = "./cloth_1.jpg"
    prompt_image_to_image(workflow, model_image_path, cloth_image_path, "Upper body", save_previews=True)
  except Exception as e:
    print(f"An error occurred: {e}")
    exit_program()


def exit_program():
    print("Exiting the program...")
    sys.exit(0)

def clear_comfy():
    clear(True, True)

main()
