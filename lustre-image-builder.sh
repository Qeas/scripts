#!/usr/bin/env bash
 
set -o nounset
set -o xtrace
set -o errexit
set -o pipefail
 
if (( $# == 0 )); then
        LUSTRE_VERSION='2.12.5'
else
        LUSTRE_VERSION="$1"
fi
 
OS_VENDOR=$(lsb_release -i | awk '{print tolower($NF)}')
OS_VERSION=$(lsb_release -r | awk '{print tolower($NF)}')
 
if [[ ! -d lustre-release ]]; then
        git clone git://git.whamcloud.com/fs/lustre-release.git
fi
 
cd lustre-release
git fetch --all
git checkout $LUSTRE_VERSION
sh autogen.sh
 
if [[ -f Makefile ]]; then
        make clean distclean
fi
 
./configure --disable-maintainer-mode --disable-doc --disable-tests --disable-server --disable-snmp
make debs
 
LUSTRE_MODULES=$(ls kmod-lustre-client-${LUSTRE_VERSION}*.rpm)
LUSTRE_CLIENT=$(ls lustre-client-${LUSTRE_VERSION}*.rpm)
 
rpm -U --reinstall $LUSTRE_MODULES $LUSTRE_CLIENT
 
cat >Dockerfile<<EOF
FROM ${OS_VENDOR}:${OS_VERSION}
WORKDIR $PWD
COPY $LUSTRE_CLIENT .
RUN rpm -i --nodeps $LUSTRE_CLIENT
RUN rm -f $LUSTRE_CLIENT
EOF
 
docker build -f Dockerfile -t "${OS_VENDOR}-${OS_VERSION}-lustre:${LUSTRE_VERSION}" .
rm -f Dockerfile
