from PIL import Image, ImageFilter
import os


# Docs
def printDocs():
    print("---Filters---")
    print("1 or r -- rotate right")
    print("2 or l -- rotate left")
    print("3 or b -- blur")
    print("4 or w -- black and white")
    print("5 or m -- mirror")
    print("6 -- sharpen")
    print("7 or d -- detail")
    print("---Actions---")
    print("8 or h -- help action")
    print("0 or s -- save")
    print("-------------")
    print()


printDocs()
print("input names of files: ")
print("(input 0 to finish)")


def saving(img, dir, k):
    img.save(dir + str(k) + ".jpg")


def rotateRight(img):
    return img.rotate(90, expand=True)


def rotateLeft(img):
    return img.rotate(-90, expand=True)


def blurring(img):
    return img.filter(ImageFilter.BLUR)


def blackWhite(img):
    return img.convert("L")


def mirror(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)


def sharpen(img):
    return img.filter(ImageFilter.SHARPEN)


def detail(img):
    return img.filter(ImageFilter.DETAIL)


# Progess bar
def progress(n):
    s = ""
    for i in range(n):
        s += "#"
    for i in range(10 - n):
        s += "-"
    if n == 10:
        print(f"\rProgress: |{s}|")
    print(f"\rProgress: |{s}|", end="\r")


name = ""
photoes = []
while True:
    name = input()
    if name == "0":
        break
    if (".jpg" in name) | (".png" in name):
        photoes.append(Image.open(name))
    else:
        for i in os.listdir(name):
            if (".jpg" in i) | (".png" in i):
                photoes.append(Image.open(name + i))


# Choose action
c = False
while True:
    print("input action or array of action: ")
    b = input()
    b.replace(" ", "")
    max = (len(b) * len(photoes)) // 10
    count = 0

    for i in b:
        for j in range(len(photoes)):
            img1 = photoes[j]
            match i:
                case "0" | "s":
                    c = True
                    break
                case "1" | "r":
                    img1 = rotateRight(img1)
                case "2" | "l":
                    img1 = rotateLeft(img1)
                case "3" | "b":
                    img1 = blurring(img1)
                case "4" | "w":
                    img1 = blackWhite(img1)
                case "5" | "m":
                    img1 = mirror(img1)
                case "6":
                    img1 = sharpen(img1)
                case "7" | "d":
                    img1 = detail(img1)
                case "8" | "h":
                    printDocs()
                    break
            photoes[j] = img1
            if max > 1:
                if count % max == 0:
                    progress(count // max)
                count += 1

    if c:
        print("output directory: ")
        dir = input()
        dir += "PhotoEditing_output\\"
        if not os.path.isdir(dir):
            os.mkdir(dir)
        for k in range(len(photoes)):
            saving(photoes[k], dir, k)
        print(f"Files will be in {dir}")
        break
print("Press 'Enter' to stop programm...")
p = input()
