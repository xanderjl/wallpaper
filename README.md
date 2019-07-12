# wallpaper

This was a fun weekend project to grab images from https://source.unsplash.com 

Once you enter your search terms in the terminal window, It downloads a random 2560x1440 image related to your query from unsplash to whichever directory you have the .exe in. It then applies that image as your wallpaper to any number of monitors you have connected. Once the wallpaper has changed, it deleted the image file from your current directory and closes out the program.

## Instructions

wallpaper.exe will launch a terminal window that will ask you to input some sort of theme. You can add multiple values by using comma separated values like this:
```
Input a theme (i.e. nature): green,forest
```

Please note that there **cannot be any spaces in your input.** You'll have to use something like:
```
Input a theme (i.e. nature): red,neon-lights
```

Your wallpaper will be deleted and turned black if you enter:

```
Input a theme (i.e. nature): green, forest
```
or 
```
green, street car
```

## Open Source

This program currently only works on windows machines, but I've left the source code to be tinkered with. See what you can make with it and enjoy using my answer to choice paralysis.
