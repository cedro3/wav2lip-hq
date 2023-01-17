# --- picup frame ---
import cv2
import os
def save_frame(video_name, video_folder, pic_folder):  
    # setting
    #video_folder = 'examples/videos' 
    #pic_folder ='pic'  
    frame_num = 10
    # content
    video_path = video_folder + '/' + video_name
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
    ret, frame = cap.read()
    result_path = pic_folder + '/' + os.path.splitext(video_name)[0]+'.jpg'
    if ret:
        cv2.imwrite(result_path, frame)

# --- display_movie ---
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
def display_movie(folder, name):
    fig = plt.figure(figsize=(30, 60))
    files = sorted(os.listdir(folder))
    for i, file in enumerate(files):
        if file=='.ipynb_checkpoints':
           continue
        if file=='.DS_Store':
           continue
        img = Image.open(folder+'/'+file)    
        images = np.asarray(img)
        ax = fig.add_subplot(10, 5, i+1, xticks=[], yticks=[])
        image_plt = np.array(images)
        ax.imshow(image_plt)
        ax.set_xlabel(name[i], fontsize=30)
    fig.tight_layout()               
    plt.show()
    plt.close()

# --- video_2_images
import cv2 
def video_2_images(video_file, image_dir, image_file):  

    # Initial setting
    i = 0
    interval = 1
    length = 1800  # リミッター
    
    cap = cv2.VideoCapture(video_file)
    fps = cap.get(cv2.CAP_PROP_FPS)  # fps取得

    while(cap.isOpened()):
        flag, frame = cap.read()  
        if flag == False:  
                break
        if i == length*interval:
                break
        if i % interval == 0:    
           cv2.imwrite(image_dir+image_file % str(int(i/interval)).zfill(6), frame)
        i += 1 
    cap.release()
    return fps, i, interval
        
# --- display_mp4 ---
from IPython.display import display, HTML, clear_output

def display_mp4(path):
    from base64 import b64encode
    mp4 = open(path,'rb').read()
    data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
    display(HTML("""
    <video width=700 controls>
        <source src="%s" type="video/mp4">
    </video>
    """ % data_url))
    #print('Display finished.')  ###


# --- display_pic ---
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
import glob
def display_pic(folder):
    fig = plt.figure(figsize=(30, 60))
    files = sorted(glob.glob(folder+'/*.jpg'))
    for i, file in enumerate(files):
        img = Image.open(file)    
        images = np.asarray(img)
        ax = fig.add_subplot(10, 5, i+1, xticks=[], yticks=[])
        image_plt = np.array(images)
        ax.imshow(image_plt)
        name = os.path.basename(file)
        ax.set_xlabel(name, fontsize=30)  
        fig.tight_layout()             
    plt.show()
    plt.close()


# --- reset_folder ---
import shutil

def reset_folder(path):
    if os.path.isdir(path):
      shutil.rmtree(path)
    os.makedirs(path,exist_ok=True)
    
    
# --- get_sampling_rate --- 
import wave

def get_rate(file_path):
    wf = wave.open(file_path, "r")
    fs = wf.getframerate()
    return fs
