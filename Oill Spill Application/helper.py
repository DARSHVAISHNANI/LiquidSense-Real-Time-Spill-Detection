from ultralytics import YOLO
import time
import streamlit as st
import cv2
from pytube import YouTube
from twilio.rest import Client
import settings


def load_model(model_path):
    """
    Loads a YOLO object detection model from the specified model_path.

    Parameters:
        model_path (str): The path to the YOLO model file.

    Returns:
        A YOLO object detection model.
    """
    model = YOLO(model_path)
    return model


def display_tracker_options():
    display_tracker = st.radio("Display Tracker", ('Yes', 'No'))
    is_display_tracker = True if display_tracker == 'Yes' else False
    if is_display_tracker:
        tracker_type = st.radio("Tracker", ("bytetrack.yaml", "botsort.yaml"))
        return is_display_tracker, tracker_type
    return is_display_tracker, None


def _display_detected_frames(conf, model, st_frame, image, is_display_tracking=None, tracker=None):
    """
    Display the detected objects on a video frame using the YOLOv8 model.

    Args:
    - conf (float): Confidence threshold for object detection.
    - model (YoloV8): A YOLOv8 object detection model.
    - st_frame (Streamlit object): A Streamlit object to display the detected video.
    - image (numpy array): A numpy array representing the video frame.
    - is_display_tracking (bool): A flag indicating whether to display object tracking (default=None).

    Returns:
    None
    """

    # Resize the image to a standard size
    image = cv2.resize(image, (720, int(720*(9/16))))

    # Display object tracking, if specified
    if is_display_tracking:
        res = model.track(image, conf=conf, persist=True, tracker=tracker)
    else:
        # Predict the objects in the image using the YOLOv8 model
        res = model.predict(image, conf=conf)

    # # Plot the detected objects on the video frame
    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   use_column_width=True
                   )
    
def play_webcam(conf, model):
    """
    Plays a webcam stream. Detects Objects in real-time using the YOLOv8 object detection model.

    Parameters:
        conf: Confidence of YOLOv8 model.
        model: An instance of the YOLOv8 class containing the YOLOv8 model.

    Returns:
        None

    Raises:
        None
    """
    source_webcam = settings.WEBCAM_PATH
    count = 0  # Initial count to detect change immediately
    count_placeholder = st.empty()
    j = 1
    # is_display_tracker, tracker = display_tracker_options()
    
    if st.sidebar.button('Detect Objects'):
        try:
            vid_cap = cv2.VideoCapture(source_webcam)
            st_frame = st.empty()
            while vid_cap.isOpened(): 
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(conf, model, st_frame, image)
                    results = model(image)
                    for result in results:
                        boxes = list(result.boxes.shape)  # Boxes object for bounding box outputs

                    if boxes[0] > 0:
                            if count < 2:
                                count += 1
                                message = client.messages.create(
                                    body='''############ Alert ############
            Please Check the Ware House facility in Zone-1 area. There is an Oil spill.''',
                                    from_='whatsapp:+14155238886',  # Twilio phone number
                                    to='whatsapp:+917621023723'  # Recipient's phone number
                                )
                                count_placeholder.info(f"Spill detected! Message sent with SID: {message.sid}")
                            else:
                                count_placeholder.info(f"Spill detected!")
                    else:
                        count_placeholder.info(f"No spill detected. => {j}")
                        j += 1

                else:
                    vid_cap.release()
                    break
                
        except Exception as e:
            st.sidebar.error("Error loading webcam: " + str(e))

account_sid = 'AC8faa1d1b34626cd229aa3848ee2ebd63'
auth_token = 'c75e51379c543a5c63f4b7718609f65f'

client = Client(account_sid, auth_token)

def play_stored_video(conf, model):
    """
    Plays a stored video file. Tracks and detects objects in real-time using the YOLOv8 object detection model.

    Parameters:
        conf: Confidence of YOLOv8 model.
        model: An instance of the YOLOv8 class containing the YOLOv8 model.

    Returns:
        None

    Raises:
        None
    """

    source_vid = st.sidebar.selectbox("Choose a video...", settings.VIDEOS_DICT.keys())

    # is_display_tracker, tracker = display_tracker_options()

    with open(settings.VIDEOS_DICT.get(source_vid), 'rb') as video_file:
        video_bytes = video_file.read()
    # if video_bytes:
        # st.video(video_bytes)
        
    if st.sidebar.button('Detect Video Objects'):
        try:
            vid_cap = cv2.VideoCapture(str(settings.VIDEOS_DICT.get(source_vid)))
            st_frame = st.empty()
            count_placeholder = st.empty()
            j = 1
            count = 0  # Initial count to detect change immediately

            while vid_cap.isOpened():
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(conf, model, st_frame, image)
                    results = model(image)
                    for result in results:
                        boxes = list(result.boxes.shape)  # Boxes object for bounding box outputs

                    if boxes[0] > 0:
                            if count < 2:
                                count += 1
                                message = client.messages.create(
                                    body='''############ Alert ############
            Please Check the Ware House facility in Zone-1 area. There is an Oil spill.''',
                                    from_='whatsapp:+14155238886',  # Twilio phone number
                                    to='whatsapp:+917621023723'  # Recipient's phone number
                                )
                                count_placeholder.info(f"Spill detected! Message sent with SID: {message.sid}")
                            else:
                                count_placeholder.info(f"Spill detected!")
                    else:
                        count_placeholder.info(f"No spill detected. => {j}")
                        j += 1
                else:
                    vid_cap.release()
                    break
                
        except Exception as e:
            st.sidebar.error("Error loading video: " + str(e))