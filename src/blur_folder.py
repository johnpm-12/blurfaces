
from pathlib import Path
import auto_blur_image
import auto_blur_video
import subprocess
import argparse

import os



def main(args):
    rootdir = args.input_directory

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:

            #checks if already processed
            if "blurred" in file:
                continue

            if file.endswith(".img") or file.endswith(".jpg") or file.endswith(".jpg") :
                inputImage = os.path.join(subdir, file)

                name, ext = os.path.splitext(inputImage)
                outputImage = "{name}-blurred{ext}".format(name=name, ext=ext)
                #checks if already processed
                if (os.path.isfile(inputImage) and  os.path.isfile(outputImage)):
                    continue

                #calls and runs the subprocess
                modelPath= "../face_model/face.pb"
                cmd = f"python auto_blur_image.py --input_image {inputImage} --output_image {outputImage} --model_path {modelPath} --threshold 0.7"
                process = subprocess.Popen(cmd, shell=True)

            if file.endswith(".mp4")  :
                inputImage = os.path.join(subdir, file)
                name, ext = os.path.splitext(inputImage)
                outputImage = "{name}-blurred{ext}".format(name=name, ext=ext)

                #checks if already processed
                if (os.path.isfile(inputImage) and  os.path.isfile(outputImage)):
                    continue

                #calls and runs the subprocess
                modelPath= "../face_model/face.pb"
                cmd = f"python auto_blur_video.py --input_video {inputImage} --output_video {outputImage} --model_path {modelPath} --threshold 0.1"
                print(cmd)
                process = subprocess.Popen(cmd, shell=True)
            else:
                continue
    exit()


if __name__ == "__main__":
    # creating argument parser
    parser = argparse.ArgumentParser(description='Input Directory parameter')

    # adding arguments
    parser.add_argument('-i',
                        '--input_directory',
                        help='Path to your folder of images',
                        type=str,
                        required=True)
    args = parser.parse_args()

    # if input image path is invalid then stop
    assert os.path.isdir(args.input_directory), 'Invalid input directory'



    main(args)
