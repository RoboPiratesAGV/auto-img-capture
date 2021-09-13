# Import essential libraries
import requests
import cv2
import numpy as np
import imutils
import argparse
import time

arg_parser = argparse.ArgumentParser(description="Starts capturing images. \nCommand Syntax:\n\n\tpython3 main.py --url http://<IPv4>:<PORTNUMBER>")
arg_parser.add_argument('--url',
                        dest='url',
                        required=True,
                        type=str,
                        help='https url of the launched IP Webcam')

args = arg_parser.parse_args()
# assigning args to vars
url = f"{args.url}/shot.jpg"

# READING LAST SAVED IMAGE NUMBER
last_saved_file = open("LAST_SAVED.txt", "r")
LAST_SAVED_INDEX = int(last_saved_file.read())

# VARS
IMAGE_WIDTH = 500
IMAGE_HEIGHT = 400
SAVE_PATH = "./storage/"
INDEX = LAST_SAVED_INDEX + 1


# While loop to continuously fetching data from the Url
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=IMAGE_WIDTH, height=IMAGE_HEIGHT)
    cv2.imshow("Data_Input", img)
    cv2.imwrite(f"{SAVE_PATH}/{INDEX}.jpg", img)
    INDEX += 1

    # WRITING CURRENT SAVED IMAGE NUMBER
    last_saved_file = open("LAST_SAVED.txt", "w")
    last_saved_file.write(str(INDEX))

    # Press Esc key to exit
    if cv2.waitKey(1) == 27:
        break

    time.sleep(1)

cv2.destroyAllWindows()