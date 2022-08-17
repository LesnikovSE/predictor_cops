import speech_recognition as sr
import os
import time

path = os.getcwd()
# ./speech
path_wav = os.path.join(path, 'opus_to_wav\wav')


list_name_wav = [f for f in os.listdir(os.chdir(path_wav)) if os.path.isfile(f)]
list_path_wav = [os.path.join(path_wav, f) for f in os.listdir(os.chdir(path_wav)) if os.path.isfile(f)]

os.chdir(path)

recog = sr.Recognizer()
list_speech_to_text = []

for i, file in enumerate(list_path_wav[:]):
    print('{} Распознаем файл {}'.format(i, list_name_wav[i - 1]))
    sample_audio = sr.AudioFile(file)
    try:
        with sample_audio as audio_file:
            # Обработка шума
            recog.adjust_for_ambient_noise(audio_file)
            # передать объект audio_content методу recognize_google() объекта класса Recognizer()
            audio_content = recog.record(audio_file)

        list_speech_to_text.append([list_name_wav[i - 1][0:10], list_name_wav[i - 1][11:-4],
                                    recog.recognize_google(audio_content, language='ru-RU')])
        time.sleep(1)
    except Exception:
        print('Ошибка файла - ', i + 1, file)
        continue

with open('whatsapp_speech.txt', 'w', encoding='utf-8') as file:
    for row in list_speech_to_text:
        file.write(f'{row},\n')
    file.close()
