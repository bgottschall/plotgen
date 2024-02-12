.PHONY: pip tests plots clean .check_version

pip: dist
	twine upload dist/*

dist: setup.py plotgen
	rm -f dist/*
	python3 $(firstword $^) bdist_wheel

tests plots:
	$(MAKE) -C $@

clean:
	rm -Rf build dist plotgen.egg-info __pycache__
