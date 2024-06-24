# Arrays of Images Editor

*Can edit arrays of images easy and fast. Can be started from command line or with .exe file.*

 
1. ```CONTENT```<a name="CONTENT"></a>

    1. [Content](#CONTENT)
    1. [Filters](#FILTERS)
    1. [Actions](#ACTIONS)
    1. [Usage](#USAGE)
    1. [Files in repository](#FILESINREPOSITORY)
    1. [About source code](#ABOUTSOURCECODE)


1. ```FILTERS```<a name="FILTERS"></a> 

    1. ```1 or r``` —- rotate right

    1. ```2 or l``` — rotate left

    1. ```3 or b``` — blur

    1. ```4 or w``` — black and white

    1. ```5 or m``` — mirror

    1. ```6``` — sharpen

    1. ```7 or d``` — detail


1. ```ACTIONS```<a name="ACTIONS"></a> 

    1. ```8 or h``` — help action

    1. ```0 or s``` — save


1. ```USAGE```<a name="USAGE"></a> 
    
    1. Start ```PhotoEditing.exe.```
    1. Input paths to files or/and folders containing files. Input 0 to finish input:
        ```
        E:\12.jpg
        E:\FolderWithFiles\
        0
        ```
    1. Input sequences of actions:
        
        ```
        76dm3
        6
        78
        h
        ```
    1. The progress bar ```|###—|``` is visible, when there are a lot of images and actions.
    1. To save input s or 0. Then input path to folder, where edited files will be saved.
        ```
        E:\
        ```
        Your files will be in ```E:\PhotoEditing_output\```
    1. After saving press ```Enter``` to close window.


1. ```FILES IN REPOSITORY```<a name="FILESINREPOSITORY"></a> 

    1. ```README.md``` — manual.

    1. ```PhotoEditing.py``` — source code.

    1. ```PhotoEditing.exe``` — exe application.


1. ```ABOUT SOURCE CODE```<a name="ABOUTSOURCECODE"></a> 

    1. Libraries: ```PIL```, ```os.```

    1. Functions ```saving — detail``` are for filters.

    1. ```printDocs``` — prints short manual.

    1. ```progress``` — prints progress bar.

    1. ```photoes``` — array of images.

    1. ```img1``` — current image.