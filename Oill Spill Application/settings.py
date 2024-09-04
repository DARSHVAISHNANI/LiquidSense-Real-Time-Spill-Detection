from pathlib import Path
import sys

# Get the absolute path of the current file
FILE = Path(__file__).resolve()
# Get the parent directory of the current file
ROOT = FILE.parent
# Add the root path to the sys.path list if it is not already there
if ROOT not in sys.path:
    sys.path.append(str(ROOT))
# Get the relative path of the root directory with respect to the current working directory
ROOT = ROOT.relative_to(Path.cwd())

# Sources

VIDEO = 'Video'
WEBCAM = 'Webcam'

SOURCES_LIST = [VIDEO, WEBCAM]


# Videos config
VIDEO_DIR = ROOT / 'videos'
VIDEOS_DICT = {

    'video_5': VIDEO_DIR / '00004.mp4',
    'video_4': VIDEO_DIR / '00015.mp4',
    'video_1': VIDEO_DIR / 'video_1.mp4',
    'video_2': VIDEO_DIR / 'video_2.mp4',
    'video_3': VIDEO_DIR / 'video_3.mp4',
    'video_6': VIDEO_DIR / '00010.mp4',
    'video_7': VIDEO_DIR / '00026.mp4'
}

# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'C:/Users/darsh/Desktop/Main Documents Folder/AI Hackethron/Model/best.pt'
# In case of your custome model comment out the line above and
# Place your custom model pt file name at the line below 
# DETECTION_MODEL = MODEL_DIR / 'my_detection_model.pt'

# Webcam
WEBCAM_PATH = 0
