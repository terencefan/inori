help:
	@echo 'Makefile for inori                      '
	@echo '                                        '
	@echo 'Usage:                                  '
	@echo '   make install    install as a package '
	@echo '   make uninstall  uninstall inori      '

requirements:
	pip install -r requirements.txt

build: requirements
	bower install

develop: build
	python setup.py develop
	@echo
	@echo "Install finished"

install: build
	python setup.py install --record install.record
	@echo
	@echo "Install finished."

uninstall:
	cat install.record | xargs rm -rf
	@echo
	@echo "Uninstall finished."
