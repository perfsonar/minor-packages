#
# Makfile for extrenal RPMs
#

#Determine package format
PACKAGE_FORMAT = none
ifneq ($(wildcard /etc/redhat-release),)
	PACKAGE_FORMAT = rpm
else ifneq ($(wildcard /etc/debian_version),)
	PACKAGE_FORMAT=deb
else
	$(error Unable to determine the package format on this system.)
endif

default: build


build:
	bash get_archive_dependency.sh geoip-database-extra $(PACKAGE_FORMAT)
	bash get_archive_dependency.sh opensearch $(PACKAGE_FORMAT)
	bash get_archive_dependency.sh opensearch-dashboards $(PACKAGE_FORMAT)
	bash get_archive_dependency.sh logstash-oss $(PACKAGE_FORMAT)


install-products:
ifndef PRODUCTS_DEST
	$(error PRODUCTS_DEST is not defined)
else
ifneq ($(wildcard /etc/redhat-release),)
	cp *.rpm $(PRODUCTS_DEST)
endif
endif


uninstall dump:
	@echo Unable to do a $@ for this package.
	@false


clean:
	rm -f *.$(PACKAGE_FORMAT)
