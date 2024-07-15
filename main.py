
from PIL import Image
from os import listdir, remove
from time import sleep

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