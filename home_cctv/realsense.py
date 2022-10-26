import time
from threading import Thread
from queue import Queue

import cv2
import numpy as np
import pyrealsense2 as rs


class RealSense:
    def __init__(self):
        self.pipeline = rs.pipeline()
        config = rs.config()
        # config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)
        config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
        # config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

        self.pipeline.start(config)

    def get_numpy_color_image(self):
        frames = self.pipeline.wait_for_frames()
        frames = frames.get_color_frame()
        frames = np.asanyarray(frames.get_data())

        return frames

    def stop(self):
        self.pipeline.stop()


# def realsense_capture(frame_queue, realsense):
#     while True:
#         color_image = realsense.get_numpy_color_image()

#         frame_queue.put(color_image)
        

# def drawing(frame_queue):
#     cv2.namedWindow('Stream', cv2.WINDOW_NORMAL)
#     cv2.resizeWindow('Stream', 640, 480)
#     while True:
#         st = time.time()
#         frame = frame_queue.get()
        
#         cv2.imshow('Stream', frame)
#         print(f'\r{1/(time.time()-st):.2f} FPS', end='')
        
#         if cv2.waitKey(1) == 27:
#             break
        
#     cv2.destroyAllWindows()


# def calc():
#     num = 0
    
#     start_time = time.time()
#     while True:
#         num += 1
        
#         if num > 1000000:
#             break
#     print(num)
#     print(f'{time.time() - start_time:.2f} sec')

        
# if __name__ == '__main__':
#     frame_queue = Queue(maxsize=1)    
#     realsense = RealSense()
    
#     Thread(target=realsense_capture, args=(frame_queue, realsense)).start()
#     # Thread(target=realsense_capture).start()
#     Thread(target=drawing, args=(frame_queue,)).start()
#     # Thread(target=calc).start()
    