TOOL = ../../tools/corriges.py

W2 = w2_slicing.py w2_if.py w2_for.py w2_strings.py
W3 = w3_marine_dict.py w3_marine_set.py w3_decode_zen.py w3_if.py
W4 = w4_files.py w4_pgcd.py w4_functional.py w4_comprehensions.py w4_fun_args.py 

WEEKS=2 3 4

SOURCES = $(foreach week,$(WEEKS),$(W$(week)))

all: $(foreach week, $(WEEKS), corriges-w$(week).tex) corriges.tex

corriges.tex: $(SOURCES) 
	$(TOOL) -o $@ $(SOURCES)
corriges.pdf: corriges.tex
	pdflatex corriges.tex

define week_target
corriges-w$(1).tex: $(W$(1))
	$(TOOL) -o corriges-w$(1).tex $(W$(1))

corriges-w$(1).pdf: corriges-w$(1).tex
	pdflatex corriges-w$(1).tex

clean::
	rm -f corriges-w$(1).tex corriges-w$(1).pdf
endef


$(foreach week, $(WEEKS), $(eval $(call week_target,$(week))))
