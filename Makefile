THRIFT=thrift

develop:
	python setup.py develop
	@echo
	@echo "Install finished"

install:
	python setup.py install --record install.record
	@echo
	@echo "Install finished"

uninstall:
	cat install.record | xrags rm -rf
	@echo
	@echo "Uninstall finished"
