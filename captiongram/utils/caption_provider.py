import  os
from PIL import Image
from flask import url_for, current_app

from .model_inference import model_prediction
#from .model import evaluate

def generate_caption(image_name):
    """
    Takes the image name
    pillow image instance is made and send for the model infernce
    reutrns the resulting caption
    """
    picture_path = os.path.join(current_app.root_path, 'static/temp', image_name)
    
    #result=" ".join(evaluate(picture_path)[:-1])+"."

    result=model_prediction(picture_path)
    
    return result


