import os
import re
import sys
import urllib.request


def extract_urls(filename):
    """Returns a list of the url addresses from the given log file,
    extracting the host name from the file name itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    file = open(filename, 'r', encoding="utf8")
    text = file.read()
    if (filename == "log_suspect1.cyberbit.log"):
        url_codes = re.findall('/cyberbit/[\w\-]+\.jpg', text)
    elif (filename == "log_suspect2.cyberbit.log"):
        url_codes = re.findall('/cyberbit/[\w\-]+[\w\-]+\.jpg', text)
    for i in range(len(url_codes)):
        x = url_codes[i]
        url_codes[i] = 'http://cyber-blich-7.bitballoon.com/'+x
    url_codes = set(url_codes)
    if (filename == "log_suspect1.cyberbit.log"):
        url_codes = sorted(url_codes)
    elif (filename == "log_suspect2.cyberbit.log"):
        url_codes = sorted(url_codes, key=lambda x: x.split("-")[4])
    url_codes = list(url_codes)
    return url_codes

    #raise NotImplementedError()
def get_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local file names img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    for i in range(len(img_urls)):
        x = dest_dir+"{}.jpg"
        urllib.request.urlretrieve(img_urls[i], x.format(i))
    #f = open(dest_dir+"index.html")
    newfile = open(dest_dir+"index.html", "w")
    bodyoffile = '<html><body> </body></html>'
    newlistimg = ""
    for i in range(len(img_urls)):
        basestr = '<img src="' + dest_dir  +'{}.jpg">'.format(i)
        newlistimg +=basestr
    bodyoffile = bodyoffile.replace(" ", newlistimg)
    newfile.write(bodyoffile)
    newfile.close()
    os.startfile(dest_dir+'index.html')
    #raise NotImplementedError()


def main():
    args = sys.argv[1:]

    if not args:
        print ('use this way: [--todir dir] log-file-path ')
        sys.exit(1)

    to_dir = ''
    if args[0] == '--todir':
        to_dir = args[1]
        args = args[2:]

    img_urls = extract_urls(args[0])

    if to_dir:
        get_images(img_urls, to_dir)
    else:
        print ('\n'.join(img_urls))


if __name__ == '__main__':
    main()

