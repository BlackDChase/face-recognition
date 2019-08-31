from PIL import Image
import glob


image_list=[]
def import_photoes():
    for foldername in glob.glob('dataset/IIT2018*'):
        for filename in glob.glob('dataset/'+ foldername+'/*.jpeg'):
            image=Image.open(filename)
            image_list[foldername].append(image)
    
import_photoes()

