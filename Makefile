
test: install
	python3 -m pytest nerdy

clean:
	py3clean .
	rm -rf dist

install:
	sudo pip3 install -e .
