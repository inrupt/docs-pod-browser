# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
GIT_BRANCH    :=$(shell git rev-parse --abbrev-ref HEAD)
BUILDDIR      = build/${GIT_BRANCH}
SPHINXOPTS    = -d $(BUILDDIR)/doctrees -c .
SOURCECOPYDIR = $(BUILDDIR)/source/
DOCS_ASSETS   = build/docs-assets

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCECOPYDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help clean Makefile migrate html linkcheck dirhtml

clean:
	if [ -d $(BUILDDIR) ]; then rm -rf $(BUILDDIR) ; fi;
	
	if [ -d $(DOCS_ASSETS) ]; then rm -rf $(DOCS_ASSETS) ; fi;

linkcheck: Makefile migrate
	@$(SPHINXBUILD) -M $@ "$(SOURCECOPYDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

migrate: clean
	mkdir -p $(SOURCECOPYDIR)

	git clone https://github.com/inrupt/docs-assets.git $(DOCS_ASSETS)

   # Copying to SOURCECOPYDIR instead of copying source dir to BUILDDIR
   # in case someone forgets to backslash after build/

	cp -R $(SOURCEDIR)/* $(SOURCECOPYDIR)

linkcheck:
	@$(SPHINXBUILD) -M $@ "$(SOURCECOPYDIR)" "$(BUILDDIR)" -c . $(O) 

html: Makefile migrate

	@$(SPHINXBUILD) -M $@ "$(SOURCECOPYDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) 

dirhtml: Makefile migrate

	@$(SPHINXBUILD) -M $@ "$(SOURCECOPYDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile migrate
	@$(SPHINXBUILD) -M $@ "$(SOURCECOPYDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

