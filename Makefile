
post:
	@PYTHONPATH=cms bin/new_post

build: clean
	@PYTHONPATH=cms bin/gen_site dist
	@cp -R site/assets/* dist/

clean:
	@rm -rf dist/css dist/img dist/js
	@rm -f dist/*

black:
	@PYTHONPATH=cms black cms bin
