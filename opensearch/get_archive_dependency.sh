#!/bin/bash

if [ $# -ne 2 ]
  then
    echo "Illegal number of parameters"
    echo "Usage: $0 PACKAGE deb/rpm"
    exit 1
fi

package=$1
version=$2

if [ "$version" != "deb" ] && [ "$version" != "rpm" ]; then
    echo "Unknown OS version. Use deb or rpm"
    exit 1
fi

#get url to download package
if [ "$version" = "deb" ]; then
    url=$(grep -A4 ${package}: archive_ext_packages.yml | grep -m 1 deb_url | awk '{ print $2 }')
    filename=$(grep -A4 ${package}: archive_ext_packages.yml | grep -m 1 deb_name | awk '{ print $2 }')
elif [ "$version" = "rpm" ]; then
    url=$(grep -A4 ${package}: archive_ext_packages.yml | grep -m 1 rpm_url | awk '{ print $2 }')
    filename=$(grep -A4 ${package}: archive_ext_packages.yml | grep -m 1 rpm_name | awk '{ print $2 }')
fi

if [ ! -z "$url" ]; then
    curl -o $filename -L $url;
else
    echo "Error: $package not found";
fi