# Info about Fas-Plate.py file
This is a very basic form of the code for so called number plate detector .\
For this basic problem faced maybe that you need to download the haarcascade .xml file that i have inlcuded.\
Also you will have to install pytesseract library and add it to the PATH of your computer.

## The code does major task although the major points of improvement are as follows :-
>We will have to take front view image of number plate.(The car plate is still identified though there,s a trouble in identifying the number.)\
>We can always warp the images using existing opencv tools to change the perpective when the image is not head on)\
>pytesseract is not the best in identifying text fro images we can use other ml based models to do that.

## To run the code give a image path file of head-on car numberplate from car to it and it will print the number on plate of car.
Though I had some trouble in installing pytesseract to my laptop so considering that scenario I am attatching the imput and output (with code) as well.
