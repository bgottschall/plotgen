.PHONY: pip wheel pip_upload tests plots clean .check_version

pip: clean .check_version 
	$(MAKE) wheel
	$(MAKE) pip_upload

wheel:
	python setup.py bdist_wheel

pip_upload:
	twine upload dist/*

tests plots:
	$(MAKE) -C $@

clean:
	rm -Rf build dist plotgen.egg-info __pycache__

.check_version:
	@[ "$$(grep version setup.py | grep -Eo '[0-9]+\.[0-9]+\.[0-9]+')" = "$$(grep __version__ plotgen | grep -Eo '[0-9]+\.[0-9]+\.[0-9]+')" ] || { echo "Version mismatch between plotgen and setup.py!" && exit 1; }


