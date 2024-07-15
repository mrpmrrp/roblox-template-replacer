
from PIL import Image
from os import mkdir, listdir, remove, path
from time import sleep

Directories = ['input', 'output']
for directory in Directories:
    if path.isdir(directory) != True:
        mkdir(directory)
        print(f'Created {directory}')

def ClearOutputFolder():
    path = 'output'
    files = listdir(path)

    for file in files:
        remove(f'{path}/{file}')

def GetInputFiles():
    path = 'input'
    files = listdir(path)

    Files = []
    for file in files:
        Files.append(f'{path}/{file}')
    return Files

def ApplyTemplate(path):
    template = Image.open('template.png')

    input = Image.open(path)
    output = Image.new('RGBA', template.size)

    output.paste(input)
    output.paste(template, (0,0), template)
    output.save(path.replace('input', 'output'))

if __name__ == '__main__':
    ClearOutputFolder()
    
    sleep(.3)

    InputFiles = GetInputFiles()
    for file in InputFiles:
        ApplyTemplate(file)