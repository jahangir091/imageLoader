# imageLoader
ImageLoader is a simple python script that takes a text file as input argument which contains urls for images and the script is responsible for downloading and saving them in local drive in a directory named **'images'**.

# Instructions:

open terminal in your machine(ubuntu recommended)

type: *git clone https://github.com/jahangir091/imageLoader* and hit enter.

a directory named **imageLoader** will be cloned to your machine.

Then run the command: ***virtualenv env***
This command will create a python virtual environment.

Now activate the environment by typing: ***source env/bin/activate***

This command will activate your virual environment.

Now go through the directory **imageLoader** by typing: *cd imageLoader*

Now type: '***python main.py images.txt***' in your terminal and hit enter.

Here '**images.txt**' is the file name which contains images urls to be downloaded.

After hitting enter the python program will start executing and you will see a message 
in your terminla like this: ***Please wait, downloading images...***

Hence download has been started.

After a moment when the images download completes, you will see another message 
like: ***Images download completed***

Now you will see a newly created directory named '**images**' where you have cloned the project.

All the images are downloaded and stored in this images directory.
