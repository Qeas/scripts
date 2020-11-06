#!/usr/bin/python2.7
"""
This program takes debian architecture as a parameter and returns
10 packages that have the most files associated to them.
"""
import exceptions
import gzip
import os
import sys
import urllib


def main(argv):
    """
    argv: parameters passed via command line
    """

    # check for incorrect input
    architectures = ['amd64', 'arm64', 'armel', 'armhf', 'i386', 'mips',
        'mips64el', 'mipsel', 'ppc64el', 's390x']
    if len(argv) < 2:
        msg = ('Debian architecture must be passed as an argument, '
               'for example: %s amd64') % argv[0]
        raise exceptions.BaseException(msg)
    if argv[1] not in architectures:
        msg = ('Architecture must be one of %s') % architectures
        raise exceptions.BaseException(msg)

    # download contents file
    base_url = 'http://ftp.uk.debian.org/debian/dists/stable/main/'
    file_name = 'Contents-%s.gz' % argv[1]
    file_path = os.path.join(os.getcwd(), file_name)
    url = '%s%s' % (base_url, file_name)
    print 'Downloading %s' % file_name
    urllib.urlretrieve(url, file_path)

    # unzip content
    print 'Unzipping %s' % file_name
    with gzip.open(file_path, 'rb') as data:
        file_content = data.read()

    # count files associated with each module in a hash table
    modules_dict = {}
    for line in file_content.split('\n'):
        splitted_line = line.split()
        # some files are not associated with any module, skip those
        if len(splitted_line) > 1:
            deb_module = splitted_line[-1]
            if modules_dict.get(deb_module):
                modules_dict[deb_module] += 1
            else:
                modules_dict[deb_module] = 1

    # sort by amount of files
    sorted_dict = sorted(
        modules_dict.items(), key=lambda x: x[1], reverse=True)
    for i in sorted_dict[:10]:
        print '%-35s%i' % (i[0], i[1])
    os.remove(file_path)

if __name__ == '__main__':
    main(sys.argv)
