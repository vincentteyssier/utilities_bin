import os
import shutil

origin_path = r"C:\tmp\Face_dataset\KDEF_and_AKDEF\AKDEF"
dest_afraid=r"C:\tmp\Face_dataset\FinalDataset\Afraid"
dest_angry=r"C:\tmp\Face_dataset\FinalDataset\Angry"
dest_disgusted=r"C:\tmp\Face_dataset\FinalDataset\Disgusted"
dest_happy=r"C:\tmp\Face_dataset\FinalDataset\Happy"
dest_neutral=r"C:\tmp\Face_dataset\FinalDataset\Neutral"
dest_sad=r"C:\tmp\Face_dataset\FinalDataset\Sad"
dest_surprised=r"C:\tmp\Face_dataset\FinalDataset\Surprised"   

# AF01AFFL

i=0
j=0
for root, dirs, files in os.walk(origin_path):
    for file in files:
        if file.endswith('.jpg') or file.endswith('.JPG') or file.endswith('.jpeg') or file.endswith('.JPEG'):
            emotion_code = file[1:3]
            file = os.path.join(root, file)
            if (emotion_code == 'AF'):
                shutil.copy(file, dest_afraid)
                j=j+1
            elif (emotion_code == 'AN'):
                shutil.copy(file, dest_angry)
                j=j+1
            elif (emotion_code == 'DI'):
                shutil.copy(file, dest_disgusted)
                j=j+1
            elif (emotion_code == 'HA'):
                shutil.copy(file, dest_happy)
                j=j+1
            elif (emotion_code == 'NE'):
                shutil.copy(file, dest_neutral)
                j=j+1
            elif (emotion_code == 'SA'):
                shutil.copy(file, dest_sad)
                j=j+1
            elif (emotion_code == 'SU'):
                shutil.copy(file, dest_surprised)
                j=j+1
            else:
                print(file)

            i = i + 1
            if (i==10):
                print ('Emotion code:')
                print (emotion_code)
                print (file)
print (i)
print (j)