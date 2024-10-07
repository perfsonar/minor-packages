#
# Makfile for extrenal RPMs
#

#Determine package format
PACKAGE_FORMAT = none
ifneq ($(wildcard /etc/redhat-release),)
	PACKAGE_FORMAT = rpm
else ifneq ($(wildcard /etc/debian_version),)
	PACKAGE_FORMAT = deb
else
	$(error Unable to determine the package format on this system.)
endif

#PRODUCTS_DEST := ../unibuild-repo
#$(PRODUCTS_DEST)::
#	mkdir -p $@

# Standard directories and files
TOP := $(CURDIR)

UNIBUILD_DIR := unibuild-work
TO_CLEAN += $(UNIBUILD_DIR)

# Where patches live

# Where the build happens
BUILD_DIR := $(UNIBUILD_DIR)/build
$(BUILD_DIR)::
	mkdir -p $@
TO_BUILD += $(BUILD_DIR)

# Where the finished products go
PRODUCTS_DIR := $(UNIBUILD_DIR)/products
$(PRODUCTS_DIR):
	mkdir -p $@
TO_BUILD += $(PRODUCTS_DIR)

# Build log
BUILD_LOG := unibuild-log
TO_CLEAN += $(BUILD_LOG)

# A place to create temporary files
TMP_DIR := $(UNIBUILD_DIR)/tmp
$(TMP_DIR):
	mkdir -p $@


default: build


build:: $(PRODUCTS_DIR) $(BUILD_DIR)
	bash get_archive_dependency.sh geoip-database-extra $(PACKAGE_FORMAT)
	bash get_archive_dependency.sh opensearch $(PACKAGE_FORMAT)
	bash get_archive_dependency.sh opensearch-dashboards $(PACKAGE_FORMAT)
	bash get_archive_dependency.sh logstash-oss $(PACKAGE_FORMAT)
	mv *.$(PACKAGE_FORMAT) $(PRODUCTS_DIR)


install-products:
ifndef PRODUCTS_DEST
	$(error PRODUCTS_DEST is not defined)
else ifneq ($(wildcard /etc/redhat-release),)
	cp $(PRODUCTS_DIR)/*.rpm $(PRODUCTS_DEST)
else ifneq ($(wildcard /etc/debian_version),)
	cp $(PRODUCTS_DIR)/*.deb $(PRODUCTS_DEST)
endif


uninstall dump:
	@echo Unable to do a $@ for this package.
	@false


clean:
	rm -f *.$(PACKAGE_FORMAT)
	rm -rf $(PRODUCTS_DEST)
