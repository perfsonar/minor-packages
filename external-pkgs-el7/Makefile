#
# Makfile for extrenal RPMs
#

# TODO: This is a bit of a hack that should go away with CentOS 7.

default: build


build install:
	@echo No $@ to do here.


install-products:
ifndef PRODUCTS_DEST
	$(error PRODUCTS_DEST is not defined)
else
	cp *.rpm $(PRODUCTS_DEST)
endif


uninstall dump:
	@echo Unable to do a $@ for this package.
	@false


clean:
	rm -rf $(TO_CLEAN) *~
