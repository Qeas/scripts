#!/usr/bin/python2.7
"""
This program takes debian architecture as a parameter and returns
10 packages that have the most files associated to them.
"""
import exceptions
import gzip
import os
import sys

from six.moves import urllib


def main(argv):
    if not argv[1:]:
        msg = ('Debian architecture must be passed as an argument, '
               'for example: %s amd64') % sys.argv[0]
        raise exceptions.BaseException(msg)

    base_url = 'http://ftp.uk.debian.org/debian/dists/stable/main/'
    file_name = 'Contents-%s.gz' % argv[1]
    file_path = os.path.join(os.getcwd(), file_name)
    url = '%s%s' % (base_url, file_name)
    print 'Downloading %s' % file_name
    urllib.request.urlretrieve(url, file_path)

    print 'Unzipping %s' % file_name
    with gzip.open(file_path, 'rb') as f:
        file_content = f.read()
        print len(file_content)
    print os.getcwd()

    modules_dict = {}
    with open('test', 'r') as infile:
        for line in infile:
            deb_file, deb_module = line.split()
            if modules_dict.get(deb_module):
                if deb_file not in modules_dict[deb_module]:
                    modules_dict[deb_module].append(deb_file)
            else:
                modules_dict[deb_module] = [deb_file]

    sorted_dict = sorted(
        modules_dict.items(), key=lambda x: len(x[1]), reverse=True)
    for i in sorted_dict[:10]:
        print '%-35s%i' % (i[0], len(i[1]))


if __name__ == '__main__':
    main(sys.argv)
