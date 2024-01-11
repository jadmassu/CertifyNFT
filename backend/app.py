from flask import Flask, request
import cv2
import config.config as config
import connection
from openai import OpenAI
import urllib.request
import numpy as np
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = config.POSTGRES_URI
# db = SQLAlchemy()
# db.init_app(app)
# with app.app_context():
#     db.create_all()


@app.route('/')
def hello():
    return connection.create_table() 



    
@app.route('/certificate', methods=['GET', 'POST'])
def certificate():
    if request.method == 'GET':
        return generate_certificate()
    else:
        return show_the_login_form()


def generate_certificate():


    client = OpenAI(api_key=config.key_api)

    response = client.images.generate(
    model="dall-e-3",
    prompt= """
    a white background and add an edge blue color simple line  
    """
,
    size="1792x1024",
    quality="standard",
    n=1,
    )
    
    image_url = response.data[0].url 
    add_info(image_url)
    print(image_url)
    return image_url

def add_info(image):
    recipient_name = "recipient_name"
    training_date = "training_date"
    duration = "duration"
    trainer_name = "trainer_name"
    topics_covered = "topics_covered"
    additional_details = "additional_details"
    
    
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    font_color = (0, 0, 0)  # Black color
    line_thickness = 3
    underline_thickness = 2
    x_axis = 550

    req = urllib.request.urlopen(image)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    cv2.putText(img,"Oracle", (800, 160), font,2, font_color,3,cv2.LINE_AA)
    cv2.putText(img,"Certificate ", (x_axis,300), font,5, font_color,3,cv2.LINE_AA)
    cv2.putText(img,"of Completion", (650,400), font,3, font_color,3,cv2.LINE_AA)
    
  
    
 

    # Add recipient's name
    name_position = (650, 500)  
    cv2.putText(img,  recipient_name, name_position, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 3, font_color)
    text_size, _ = cv2.getTextSize(recipient_name, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, line_thickness)
    underline_y = name_position[1] + text_size[1] + underline_thickness
    underline_start = (name_position[0], underline_y)
    underline_end = (name_position[0] + text_size[0], underline_y)
    cv2.line(img, underline_start, underline_end, font_color, underline_thickness)
    
    text_position = (x_axis, 600)
    cv2.putText(img, "For completing online softer development course " , text_position, font, font_scale, font_color, 4)

    # Add training date
    date_position = (100, 900)
    date_text_position = (100, 950)
    
    cv2.putText(img, training_date, date_position, font, font_scale, font_color, line_thickness,cv2.LINE_AA)
    cv2.putText(img, "Completion Date", date_text_position, font, font_scale, font_color, line_thickness,cv2.LINE_AA)
    
    


   

    # Add trainer's name
    trainer_position = (1300, 900)
    trainer_text_position = (1300, 950)
    
    cv2.putText(img,trainer_name, trainer_position, font, font_scale, font_color, line_thickness,cv2.LINE_AA)
    cv2.putText(img, "Trainer", trainer_text_position, font, font_scale, font_color, line_thickness,cv2.LINE_AA)
    



    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    