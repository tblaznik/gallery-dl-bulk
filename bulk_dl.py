import gallery_dl
import os


def read_source(file):
    urls = []
    with open(file, 'r') as inpt1:
        for line in inpt1.readlines():
            if 'http' in line:
                line = line.strip('\n')
                urls.append(line)
            else:
                pass
        print(len(urls), ' URLs read from input file.')
    file.close()
    return urls


def download(url_list):
    for url in url_list:
        try:
            command = 'gallery-dl ' + url
            print('Attempting to download: ', url)
            os.system(command)
        except Exception:
            print('Download failed.')
            pass


def main():
    urls = read_source('input.txt')
    download(urls)


if __name__ == '__main__':
    main()
