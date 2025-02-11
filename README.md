# <span style="color:deepskyblue"> Real-time Object Detection and Tracking with YOLOv8 (nano, small ,medium), YOLOv9 (c), YOLOv10 (nano, small ,medium) & Streamlit </span>

This repository is an extensive open-source project showcasing the seamless integration of **object detection and tracking** using **YOLOv8** (object detection algorithm), along with **Streamlit** (a popular Python web application framework for creating interactive web apps). The project offers a user-friendly and customizable interface designed to detect and track objects in real-time video streams from sources such as RTSP, as well as static videos and images.


## <span style="color:deepskyblue">WebApp Demo on Streamlit Server</span>

Thank you team [Streamlit](<https://github.com/streamlit/streamlit>) for the community support for the cloud upload. 

This app is can run on Streamlit local!!! You can check the local demo 
[yolov8-streamlit-detection](https://localhost/8501)

## <span style="color:deepskyblue"> Tracking With Object Detection Demo</span>

https://github.com/DARSHVAISHNANI/LiquidSense-Real-Time-Spill-Detection/blob/b9783ded7695b11c273c901932b65a3101730aa5/Github%20Document%20Readme%20File/Jetson%20Xavier%20Setup%20Video.mp4


## Demo Pics

### Home page

<img src="https://github.com/DARSHVAISHNANI/LiquidSense-Real-Time-Spill-Detection/blob/1a73b4a994e449362be9110bb9ef49a2a12874c6/Github%20Document%20Readme%20File/image-5.png">

### Page after uploading an image and object detection

<img src="https://github.com/DARSHVAISHNANI/LiquidSense-Real-Time-Spill-Detection/blob/b9783ded7695b11c273c901932b65a3101730aa5/Github%20Document%20Readme%20File/image-3.png" >

## Requirements

Python 3.6+
YOLOv8
Streamlit

```bash
pip install ultralytics streamlit pytube
```

## Installation

- Clone the repository: git clone [<https://github.com/DARSHVAISHNANI/LiquidSense-Real-Time-Spill-Detection.git>](https://github.com/DARSHVAISHNANI/LiquidSense-Real-Time-Spill-Detection.git)
- Change to the repository directory: `cd Oil-Spill-Detection-System`
- Create `weights`, `videos`, and `images` directories inside the project.
- Download the pre-trained YOLOv8 weights from (<https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt>) and save them to the `weights` directory in the same project.

## Usage

- Run the app with the following command: `streamlit run app.py`
- The app should open in a new browser window.

### ML Model Config

- Select task (Detection, Segmentation)
- Select model confidence
- Use the slider to adjust the confidence threshold (25-100) for the model.

One the model config is done, select a source.

## Detection in Videos

- Create a folder with name `videos` in the same directory
- Dump your videos in this folder
- In `settings.py` edit the following lines.

```python
# video
VIDEO_DIR = ROOT / 'videos' # After creating the videos folder

# Suppose you have four videos inside videos folder
# Edit the name of video_1, 2, 3, 4 (with the names of your video files) 
VIDEO_1_PATH = VIDEO_DIR / 'video_1.mp4' 
VIDEO_2_PATH = VIDEO_DIR / 'video_2.mp4'
VIDEO_3_PATH = VIDEO_DIR / 'video_3.mp4'
VIDEO_4_PATH = VIDEO_DIR / 'video_4.mp4'

# Edit the same names here also.
VIDEOS_DICT = {
    'video_1': VIDEO_1_PATH,
    'video_2': VIDEO_2_PATH,
    'video_3': VIDEO_3_PATH,
    'video_4': VIDEO_4_PATH,
}

# Your videos will start appearing inside streamlit webapp 'Choose a video'.
```

- Click on `Detect Video Objects` button and the selected task (detection/segmentation) will start on the selected video.

### Detection on RTSP

- Select the RTSP stream button
- Enter the rtsp url inside the textbox and hit `Detect Objects` button

## Acknowledgements

This app uses [YOLOv8](<https://github.com/ultralytics/ultralytics>) for object detection algorithm and [Streamlit](<https://github.com/streamlit/streamlit>) library for the user interface.

### Disclaimer

Please note this project is intended for educational purposes only and should not be used in production environments.

**Hit star ⭐ if you like this repo!!!**
