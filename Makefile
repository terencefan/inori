THRIFT=thrift

help:
	@echo 'Makefile for inori                       '
	@echo '                                         '
	@echo 'Usage:                                   '
	@echo '    make build      build thrift files   '
	@echo '    make develop    make a develop env   '
	@echo '    make install    install as a package '
	@echo '    make uninstall  uninstall inori      '

clean:
	rm -rf inori/*/sdk/*

requirements:
	pip install -r requirements.txt

build: clean
	$(THRIFT) -out inori/ems/sdk --gen py:new_style,utf8strings inori/ems/ems.thrift
	@echo
	@echo "Build finished."

develop: requirements build
	python setup.py develop
	@echo
	@echo "Install finished"

install: requirements build
	python setup.py install --record install.record
	@echo
	@echo "Install finished"

uninstall:
	cat install.record | xrags rm -rf
	@echo
	@echo "Uninstall finished"
