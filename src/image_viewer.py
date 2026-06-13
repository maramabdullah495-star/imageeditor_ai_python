import cv2


def show_image():

    img = cv2.imread('../images/employee.png')

    cv2.imshow('Image Viewer', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
