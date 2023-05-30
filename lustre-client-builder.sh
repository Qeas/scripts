#!/usr/bin/env bash
 
set -o nounset
set -o xtrace
set -o errexit
set -o pipefail

yum install -y libtool m4 automake git redhat-lsb-core flex bison libcurl-devel python3-devel kernel-devel kernel-tools \
 kernel-headers openmpi openmpi-devel rpm-build cmake gcc libnl3-devel libudev-devel make pkgconfig valgrind-devel keyutils-libs \
 kernel-abi-whitelists kernel-rpm-macros keyutils-libs-devel libselinux-devel
dnf install -y mpich-devel
dnf --enablerepo=powertools install -y libmount-devel libyaml-devel

if (( $# == 0 )); then
        LUSTRE_VERSION='2.15.2'
else
        LUSTRE_VERSION="$1"
fi

OS_VENDOR=$(lsb_release -i | awk '{print tolower($NF)}')
OS_VERSION=$(lsb_release -r | awk '{print tolower($NF)}')

if [[ ! -d lustre-release ]]; then
        git clone https://github.com/lustre/lustre-release.git
fi

cd lustre-release
git fetch --all
git checkout $LUSTRE_VERSION
sh autogen.sh
 
if [[ -f Makefile ]]; then
        make clean distclean
fi

# sudo yum install flex
# sudo yum install bison
./configure --disable-maintainer-mode --disable-doc --disable-tests --disable-server --disable-snmp
make rpms

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



./lustre-client-builder.sh





yum install -y libtool m4 automake git redhat-lsb-core flex bison libcurl-devel python3-devel kernel-devel kernel-tools \
 kernel-headers openmpi openmpi-devel rpm-build cmake gcc libnl3-devel libudev-devel make pkgconfig valgrind-devel keyutils-libs \
 kernel-abi-whitelists kernel-rpm-macros keyutils-libs-devel libselinux-devel
dnf install -y mpich-devel
dnf --enablerepo=powertools install -y libmount-devel libyaml-devel



   63  yum install libnl-genl
   64  yum install openssl-devel

   73  um install cmake gcc libnl3-devel libudev-devel make pkgconfig valgrind-devel
   74  yum install cmake gcc libnl3-devel libudev-devel make pkgconfig valgrind-devel
   75  ./lustre-client-build.sh 2.15.1
   76  ls lustre-release/
   77  yum install libyaml-dev
   78  yum install libyaml-devel
   79  dnf install libyaml-devel
   80  dnf --enablerepo=powertools install libyaml-devel
   81  ./lustre-client-build.sh 2.15.1
   82  yum install rpmbuild
   83  dnf --enablerepo=powertools install rpmbuild
   84  rpmbuild
   85  ./lustre-client-build.sh 2.15.1
   86  kernel_module_package_buildreqs
   94  rpm -U --reinstall kmod-lustre-client-2.15.1-1.el8.x86_64.rpm lustre-client-2.15.1-1.el8.x86_64.rpm
   95  rpm -q --provides -p
   96  rpm -q --provides -p kmod-lustre-client-2.15.1-1.el8.x86_64
   97  uname -a
   98  yum kernel-tools
   99  yum install kernel-tools
  100  rpm -U --reinstall kmod-lustre-client-2.15.1-1.el8.x86_64.rpm lustre-client-2.15.1-1.el8.x86_64.rpm
  101  