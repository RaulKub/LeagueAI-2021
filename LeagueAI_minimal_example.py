from LeagueAI_helper import input_output, LeagueAIFramework, detection
import time
import cv2



####### Params ######
# Show the AI view or not:
show_window = True
# Output window size
output_size = int(3440/3), int(1440/3)
# To record the desktop use:
IO = input_output(input_mode='desktop', SCREEN_WIDTH=1920, SCREEN_HEIGHT=1080)
# If you want to use the webcam as input use:
#IO = input_output(input_mode='webcam')
# If you want to use a videofile as input:
#IO = input_output(input_mode='videofile', video_filename='videos/eval.mp4')
####################

LeagueAI = LeagueAIFramework(config_file="C:\\Users\\Raul\\OneDrive\\Escritorio\\TFG\\version dev\\LeagueAI-development\\cfg\\yolov3.cfg", weights="C:\\Users\\Raul\\OneDrive\\Escritorio\\TFG\\version dev\\LeagueAI-development\\weights\\yolov3_adaptado.weights", names_file="C:\\Users\\Raul\\OneDrive\\Escritorio\\TFG\\version dev\\LeagueAI-development\\cfg\\obj-8.names", classes_number = 8, resolution=int(1440/1.5), threshold = 0.75, cuda=True, draw_boxes=True)


while True:
    start_time = time.time()
    # Get the current frame from either a video, a desktop region or webcam (for whatever reason)
    dim = (500,500)
    frame = IO.get_pixels(dim)
    # Get the list of detected objects and their positions
    # Model
   
    objects = LeagueAI.get_objects(frame)
    print("{} detected objects: ".format(len(objects)))
    for o in objects:
        # Print out the returned objects
        o.toString()
        # Example to validate if the returned objects are correct:
        # Draw rectangles arount the objects and a center point, you can use the draw_boxes=False to turn the frameworks boxes off
        cv2.circle(frame, (int(o.x), int(o.y)), 5, (255,0,0), -1)
        cv2.rectangle(frame, (int(o.x_min), int(o.y_min)), (int(o.x_max), int(o.y_max)), (255, 0, 0), 4)


    """
    Here you can do stuff with the detected objects and the other data from above.
    This file just provides the minimal working version on which you can start building your own bots.
    If you need some inspiration check out my Vayne bot which should be included in the repository.
    Lets build something cool!
    """

    # Write fps
    cycle_time = time.time()-start_time
    cv2.putText(frame, "FPS: {}".format(str(round(1/cycle_time,2))), (10, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255), 2)
    # Show the AI view, rescale to output size
    if show_window:
        frame = cv2.resize(frame, output_size)
        cv2.imshow('LeagueAI', frame)
        if (cv2.waitKey(25) & 0xFF == ord('q')):
            cv2.destroyAllWindows()
            break