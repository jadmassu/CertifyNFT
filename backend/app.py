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

# Recipient's Name: [Enter the recipient's name]
    # Training Date: [Enter the date of the training]
    # Duration: [Enter the duration of the training]
    # Trainer's Name: [Enter the name of the trainer]
    # Topics Covered: [List the topics covered during the training]
    # Additional Details (optional): [Include any other relevant details]
  
    # Certificate of Completion
    # This is to certify that [Recipient's Name] has successfully completed the [Training Name] conducted on [Training Date]. The training lasted [Duration] and covered the following topics:
    #     -testtrining
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
    line_thickness = 2
    underline_thickness = 1

    req = urllib.request.urlopen(image)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    cv2.putText(img,"text", (800, 50), font,font_scale, font_color,5,cv2.LINE_AA)
    cv2.putText(img,"Certificate", (800,130), font,font_scale, font_color,5,cv2.LINE_AA)
    cv2.putText(img,"of Completion", (800, 200), font,font_scale, font_color,5,cv2.LINE_AA)
    
 

    # Add recipient's name
    name_position = (800, 200)  
    cv2.putText(img, "Recipient's Name: " + recipient_name, name_position, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, font_scale, font_color)
    text_size, _ = cv2.getTextSize(recipient_name, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, font_scale, line_thickness)
    underline_y = name_position[1] + text_size[1] + underline_thickness
    underline_start = (name_position[0], underline_y)
    underline_end = (name_position[0] + text_size[0], underline_y)
    cv2.line(image, underline_start, underline_end, font_color, underline_thickness)
    
    text_position = (800, 200)
    cv2.putText(img, "For completing online softer development course " , text_position, font, font_scale, font_color, line_thickness)

    # Add training date
    date_position = (800, 300)
    cv2.putText(img, "Completion Date: " + training_date, date_position, font, font_scale, font_color, line_thickness)

   

    # Add trainer's name
    trainer_position = (800, 500)
    cv2.putText(img, "Trainer's Name: " + trainer_name, trainer_position, font, font_scale, font_color, line_thickness)

    # Add additional details
  
    # Display the generated certificate image

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    