#   IMPORTS

from PIL import Image

#VARIABLES

DIRECTORIO = "/Users/pablo/Desktop/Programacion/Python/CC1002/"

# FUNCIONES  

def insertMix(mainColour,secretColour,nDigits):

    main = mainColour - (mainColour%(2**nDigits))
    secret = secretColour // (2**(8-nDigits))

    return main + secret

def revealColour(mixedColour, nDigits):
    return (mixedColour%(2**nDigits))* 2**(8-nDigits)

def encriptSteganography(base, secret, criptBits = 3 ,outputName='tempSten.png'):
    Base = Image.open(base,'r')
    Secret = Image.open(secret,'r')
    
    bWidth,bHeight = Base.size
    sWidth,sHeight = Secret.size

    xProp = sWidth/bWidth
    yProp = sHeight/bHeight

    for x in range(bWidth):
        for y in range(bHeight):
            (bR,bG,bB,_) = Base.getpixel((x,y))
            (sR,sG,sB) = Secret.getpixel((int(x*xProp),int(y*yProp)))
            
            newColour = (insertMix(bR,sR,criptBits),insertMix(bG,sG,criptBits),insertMix(bB,sB,criptBits))
            Base.putpixel((x,y),newColour)
    
    Base.save(DIRECTORIO + outputName)
    
    return

def decriptSteganography(encripted, criptBits = 3, outputName='tempSten.png'):
    file = Image.open(encripted,'r')

    width,height = file.size

    for x in range(width):
        for y in range(height):
            eR,eG,eB,_ = file.getpixel((x,y))
            
            decriptedColours = (revealColour(eR,criptBits),revealColour(eG,criptBits),revealColour(eB,criptBits))
            file.putpixel((x,y),decriptedColours)

    file.save(DIRECTORIO + outputName)

    return 

#   MAIN
def main():

    mode = input('Elija el modo a operar (Escriba el número)\n\t1. Encriptar\n\t2. Desencriptar\n')

    if int(mode) == 1:
        IMAGEN = DIRECTORIO + input('\nEscriba el nombre del archivo base (sin olvidar terminación .png)\n')
        SECRET = DIRECTORIO + input('\nEscriba el nombre del archivo secreto (sin olvidar terminación .png)\n')
        BITS = int(input('\nEscriba el número de bits con que quiere encriptar el archivo\n'))
        OUTPUT = input('\nEscriba el nombre del archivo de salida (sin olvidar terminación .png)\n')
        
        encriptSteganography(IMAGEN,SECRET,criptBits=BITS,outputName=OUTPUT)

    if int(mode) == 2:
        IMAGEN = DIRECTORIO + input('\nEscriba el nombre del archivo encriptado (sin olvidar terminación .png)\n')
        BITS = int(input('\nEscriba el número de bits con que el archivo fue encriptado\n'))
        OUTPUT = input('\nEscriba el nombre del archivo de salida (sin olvidar terminación .png)\n')

        decriptSteganography(IMAGEN,criptBits=BITS,outputName=OUTPUT)

main()
