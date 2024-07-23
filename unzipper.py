from zipfile import ZipFile
from pydub import AudioSegment 



def unzip(path):
    with ZipFile(path, 'r') as object:
        object.extractall(path ="C:\\Users\\jingh\\Desktop\\AudioAugmentation")
        sound = AudioSegment.from_mp3(audioinput) 
        sound.export(output_file, format="wav") 