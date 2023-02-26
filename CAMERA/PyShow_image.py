#!/usr/bin/python3
##
import cv2
import sys

def take_input(img):
    image = cv2.imread(img, cv2.IMREAD_COLOR)
    """
    # shows blak & white
    image = cv2.imread(imgf, 2) # or 2=cv2.IMREAD_GRAYSCALE
    ret, data = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    """
    while True:
        cv2.imshow("PyImage", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

def help():
    print("""
    #######################################################
    # Usage:\tDisplay images
    #\t-h, --help\t\t dospaly this help message
    #\t!takes only 1 argument [image_path] or [-h,--help]
    # Example:
    #\t\t./PyShow_image.py [image.jpg]
    #\t\t./PyShow_image.py -h
    # Important:
    #\t press ( q ) button to exit.
    #\t or CTRL-c (^c)
    #######################################################
            """)


def check_args(args):
    if len(args) != 2 or args[1] == "-h" or args[1] == "--help":
        help()
        sys.exit(0)
    else:
        try:
            take_input(args[1])
        
        except:
            sys.exit(0)


check_args(sys.argv)



