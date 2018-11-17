import cv2
import os

# input file
input_file = 'video/input.mp4'
# output file format
output_format = "img_r_{:d}.jpg"
# output directory
output_folder = 'output_folder'
# framer ratio
fratio = 20

# TODO : easier to use in next update
output_height = None
ouptut_width = None

def extractFrames(pathIn, pathOut):
    os.mkdir(pathOut)
 
    cap = cv2.VideoCapture(pathIn)
    count = 0
    framer = 1
 
    while (cap.isOpened()):
 
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret == True:
            
            # Uncomment below to resize the image by half
            frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) 

            # Uncomment below to rezise by fixed size
            # frame = cv2.resize(frame, (100, 50)) 

            # Ucomment below to use scipy module for resize
            # frame = scipy.misc.imresize(image, 0.5)

            if(framer % fratio == 0):
                print('Read %d frame: ' % count, ret)
                cv2.imwrite(os.path.join(pathOut, output_format.format(count)), frame)  # save frame as JPEG file
                count += 1
            framer +=1
        else:
            break
 
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
 
def main():
    extractFrames(input_file, output_folder)
 
if __name__=="__main__":
    main()