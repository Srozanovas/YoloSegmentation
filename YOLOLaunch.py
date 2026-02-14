import ultralytics
import time
import cv2
import models as m





# Create resizable window for each frame



def launchYolo(model, network, networkVersion):


    windowName = m.getWindowName(network, networkVersion) 
    cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(windowName, 1080, 720)


    videoPath = m.getVideoSource()
    deviceName = m.getDeviceName()
   # model.set_classes(["person"])
    prev_time = 0
    for r in model(0 if videoPath == "webCam" else videoPath, stream=True, device=deviceName, imgsz=480, vid_stride=1, classes = 0):
        frame = r.plot()  # nupiešia box'us + maskes ant kadro

        current_time = time.time()
        fps = 1 / (current_time - prev_time) if prev_time != 0 else 0
        prev_time = current_time

        # Užrašome FPS ant kadro
        cv2.putText(frame, f"FPS: {fps:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow(windowName, frame)
        # q - uždaryti
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.waitKey(0)        
    cv2.destroyAllWindows()
    cv2.destroyAllWindows()