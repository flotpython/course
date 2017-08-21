# publish the test directory in data/ under the three formats

NAME = diskusage-spam

all: data

spam-tar: clean
	tar cf ../data/$(NAME).tar spam/

spam-tgz: clean
	tar czf ../data/$(NAME).tgz spam/

spam-zip: clean
	zip ../data/$(NAME).zip $(shell find spam)

clean:
	find spam -name .du | xargs rm


data: spam-tar spam-tgz spam-zip

.PHONY: data clean spam-tar spam-tgz spam-zip


snapshot: force
	rm -rf snapshot
	mkdir snapshot
	tar -C snapshot -xf ../data/$(NAME).tar 

force:


size-help help-size:
	python -c "from diskusage import *; help(HumanReadableSize)" > size.help
cache-help help-cache:
	python -c "from diskusage import *; help(Cache)" > cache.help
toplevel-help help-toplevel:
	python -c "from diskusage import *; help(ToplevelDir)" > toplevel.help
main-help help-main:
	python -c "from diskusage import *; help(main)" > main.help

help: help-size help-cache help-toplevel help-main
