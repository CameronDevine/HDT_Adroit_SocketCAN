.PHONY: dist clean upload upload-test

dist:
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/*

upload-test:
	twine upload dist/* --repository-url https://test.pypi.org/legacy/

clean:
	rm -rf dist build AdroitComs.egg-info
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete
