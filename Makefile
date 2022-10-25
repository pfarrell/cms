
post:
	@PYTHONPATH=cms bin/new_post

build: clean
	@PYTHONPATH=cms bin/gen_site dist
	@cp -R site/assets/* dist/
	@cp site/*.html dist/

clean:
	@rm -rf dist/css dist/img dist/js
	@rm -f dist/*

black:
	@PYTHONPATH=cms black cms bin

deploy: build
	@rsync -e 'ssh -p 10022' -avz dist/* pfarrell@patf.net:/var/www/cms/
