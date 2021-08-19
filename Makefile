.PHONY: pip tests plots clean .check_version

pip: clean .check_version
	python setup.py bdist_wheel
	twine upload dist/*

tests plots:
	$(MAKE) -C $@

clean:
	rm -Rf build dist plotgen.egg-info __pycache__

.check_version:
	@[ "$$(grep version setup.py | grep -Eo '[0-9]+\.[0-9]+\.[0-9]+')" = "$$(grep __version__ plotgen | grep -Eo '[0-9]+\.[0-9]+\.[0-9]+')" ] || { echo "Version mismatch between plotgen and setup.py!" && exit 1; }


