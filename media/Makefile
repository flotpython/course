SVGS = $(shell git ls-files *.svg)
PNGS = $(subst .svg,.png,$(SVGS))

all: $(PNGS)

%.png: %.svg
	cairosvg -o $@ -f png $*.svg


list:
	@echo SVGS=$(SVGS)
	@echo PNGS=$(PNGS)

clean:
	rm -f $(PNGS)
