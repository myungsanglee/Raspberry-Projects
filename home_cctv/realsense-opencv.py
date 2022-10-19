import time
from threading import Thread
from queue import Queue

import cv2
import numpy as np
import pyrealsense2 as rs

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)

# pipeline.start(config)

# cv2.namedWindow('Stream', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('Stream', 640, 480)
# num = 0
# start_time = time.time()
# while True:
#     start_time = time.time()
#     frames = pipeline.wait_for_frames()
#     color_frame = frames.get_color_frame()
#     color_image = np.asanyarray(color_frame.get_data())
    
#     cv2.imshow('Stream', color_image)
    
#     # print(f'\r{1/(time.time() - start_time):.1f} FPS', end='')
#     num += 1
#     if num > 1000000:
#         print(f'{time.time() - start_time:.2f} sec')
#         break
    
#     key = cv2.waitKey(1)
#     if key == 27:
#         break
    
# cv2.destroyAllWindows()
# pipeline.stop()


def realsense_capture(frame_queue):
    pipeline.start(config)
    
    # cv2.namedWindow('Stream', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('Stream', 640, 480)
    
    while True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        color_image = np.asanyarray(color_frame.get_data())

        frame_queue.put(color_image)
        
    #     cv2.imshow('Stream', color_image)
        
    #     if cv2.waitKey(1) == 27:
    #         break
    
    # cv2.destroyAllWindows()

def drawing(frame_queue):
    cv2.namedWindow('Stream', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Stream', 640, 480)
    while True:
        st = time.time()
        frame = frame_queue.get()
        
        cv2.imshow('Stream', frame)
        print(f'\r{1/(time.time()-st):.2f} FPS', end='')
        
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()

def calc():
    num = 0
    
    start_time = time.time()
    while True:
        num += 1
        
        if num > 1000000:
            break
    print(num)
    print(f'{time.time() - start_time:.2f} sec')

        
if __name__ == '__main__':
    frame_queue = Queue(maxsize=1)    
    
    Thread(target=realsense_capture, args=(frame_queue,)).start()
    # Thread(target=realsense_capture).start()
    Thread(target=drawing, args=(frame_queue,)).start()
    # Thread(target=calc).start()