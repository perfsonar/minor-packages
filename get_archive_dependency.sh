#!/bin/bash

if [ $# -ne 2 ]
  then
    echo "Illegal number of parameters"
    echo "Usage: $0 PACKAGE DEB/RPM"
    exit 1
fi

package=$1
version=$2

if [ "$version" != "DEB" ] && [ "$version" != "RPM" ]; then
    echo "Unknown OS version. Use DEB or RPM"
    exit 1
fi

if [ "$package" = "opensearch" ] || [ "$package" = "dashboards" ]; then
    #docker-compose -p minor-packages -f opensearch/docker-compose.yml up --build --no-start $package
    #docker cp minor-packages_${package}_1:/usr/share/opensearch/artifact/. ./
    #docker-compose -p minor-packages -f opensearch/docker-compose.yml down -v
    if [ "$package" = "opensearch" ]; then
        curl -o opensearch-1.2.3.x86_64.rpm -L http://monipe-central.rnp.br:8002/opensearch-1.2.3-linux-x64.rpm
    else
        curl -o opensearch-dashboards-1.2.0.x86_64.rpm -L http://monipe-central.rnp.br:8002/opensearch-dashboards-1.2.0-linux-x64.rpm
    fi
else
    #get url to download package
    if [ "$version" = "DEB" ]; then
        url=$(grep -A4 ${package}: archive_ext_packages.yml | grep -m 1 deb_url | awk '{ print $2 }')
        filename=$(grep -A4 ${package}: archive_ext_packages.yml | grep -m 1 deb_name | awk '{ print $2 }')
    elif [ "$version" = "RPM" ]; then
        url=$(grep -A4 ${package}: archive_ext_packages.yml | grep -m 1 rpm_url | awk '{ print $2 }')
        filename=$(grep -A4 ${package}: archive_ext_packages.yml | grep -m 1 rpm_name | awk '{ print $2 }')
    fi

    if [ ! -z "$url" ]; then
        curl -o $filename -L $url;
    else
        echo "Error: $package not found";
    fi
fi