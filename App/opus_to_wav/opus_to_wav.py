import subprocess
import shlex
import os

opus_path = os.getcwd()
print('path is:\n', opus_path, '\n')

# install temp files directory
os.chdir('temp_opus')

list_temp_opus_file = [f for f in os.listdir(os.getcwd()) if os.path.isfile(f)]
# print(list_temp_opus_file)

os.chdir(opus_path)

for file_name in list_temp_opus_file:
    print(f'Декодируем файл - {file_name}')
    cmd = "opusdec.exe"
    args = shlex.split(f'opusdec temp_opus/{file_name} wav/{file_name[15:-5]}.wav')
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.communicate()[0]

print('Декодирование временных файлов законченно..')
