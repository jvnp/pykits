# imports
import os
 
# setup your directory
directory = 'processor'

# Main function to rename multiple files
def main():
    i = 0
     
    for filename in os.listdir(directory):
        dst = "image" + str(i) + ".jpg"
        src = directory + '/' + filename
        dst = directory + '/' + dst
         
        # rename process
        os.rename(src, dst)
        i += 1
 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()