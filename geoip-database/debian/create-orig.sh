#!/bin/sh

if [ ! -x /usr/bin/unzip ]; then
	echo "You need the unzip package, to run this script."
	exit 1
fi

V4="http://geolite.maxmind.com/download/geoip/database/GeoIPCountryCSV.zip"
V6="http://geolite.maxmind.com/download/geoip/database/GeoIPv6.csv.gz"
CITY="http://geolite.maxmind.com/download/geoip/database/GeoLiteCity_CSV/GeoLiteCity-latest.zip"
ASN="http://download.maxmind.com/download/geoip/database/asnum/GeoIPASNum2.zip"

OLDDIR=$(pwd)
TMPDIR=$(mktemp -d)
DATE=$(date +'%Y%m%d')

cd ${TMPDIR}

wget ${V4} -O v4.csv.zip
wget ${V6} -O v6.csv.gz
wget ${CITY} -O city.csv.zip
wget ${ASN} -O asn.csv.zip

gunzip v6.csv.gz
unzip v4.csv.zip
unzip city.csv.zip
unzip asn.csv.zip

mkdir ${TMPDIR}/geoip-database-${DATE}

mv GeoIPCountryWhois.csv ${TMPDIR}/geoip-database-${DATE}/
mv v6.csv ${TMPDIR}/geoip-database-${DATE}/
mv GeoLiteCity_*/GeoLiteCity*.csv ${TMPDIR}/geoip-database-${DATE}
mv GeoIPASNum2.csv ${TMPDIR}/geoip-database-${DATE}

tar -cJf geoip-database_${DATE}.orig.tar.xz geoip-database-${DATE}
mv geoip-database_${DATE}.orig.tar.xz ${OLDDIR}/../geoip-database_${DATE}.orig.tar.xz

cd ${OLDDIR}
rm -rf ${TMPDIR}

echo "Saved tarball: ${OLDDIR}/../geoip-database_${DATE}.orig.tar.xz"

exit 0
