help:
	@echo 'Makefile for inori                      '
	@echo '                                        '
	@echo 'Usage:                                  '
	@echo '   make install    install as a package '
	@echo '   make uninstall  uninstall inori      '

install:
	python setup.py install --record install.record
	@echo
	@echo "Install finished."

uninstall:
	cat install.record | xargs rm -rf
	@echo
	@echo "Uninstall finished."
