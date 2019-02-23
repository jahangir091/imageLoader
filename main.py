#!/usr/bin/python

import urllib
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


def getImageUrls(file_name):
    """
    This function takes input the file name
    which contains the urls for images and returns a list of
    urls.
    :param file_name: string type name of url file.
    :return: list of urls.
    """

    # if no file_name, return empty list
    if not file_name:
        return []

    file_path = os.path.join(PROJECT_ROOT, file_name)
    with open(file_path) as url_file:
        urls = url_file.readlines()

    # Close opend file
    url_file.close()

    return urls


def saveImages(file_name):
    """
    This function takes image urls as imput argument
    and downloads images of mentioned urls
    and saves them into images directory.
    :param urls: images urls
    :return:
    """
    # get images urls
    image_urls = getImageUrls(file_name)
    if not image_urls:
        print "sorry, the file does not contains any urls"
        return

    # define directory where images will be saved
    download_directory = os.path.join(PROJECT_ROOT, 'images')
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    # save images for each url
    print 'Please wait, downloading images...'
    for url in image_urls:
        try:
            urllib.urlretrieve(url, 'images/' + url.split('/')[-1])
        except Exception as e:
            print 'Could not download image from url: ' + url
            print e

    print 'Images download completed'


if __name__ == "__main__":
    saveImages(sys.argv[1])
