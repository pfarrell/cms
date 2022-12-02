
post:
	@PYTHONPATH=cms bin/new_post

build: clean
	@PYTHONPATH=cms bin/gen_site dist
	@cp -R assets/* dist/
	@cp site/*.html dist/
	@cp site/*.pdf dist/

build-prod: clean
	@PYTHONPATH=cms bin/gen_prod_site dist
	@cp -R assets/* dist/
	@cp site/*.html dist/
	@cp site/*.pdf dist/

clean:
	@rm -rf dist/css dist/img dist/js dist/lib
	@rm -f dist/*

black:
	@PYTHONPATH=cms black cms bin

deploy: build-prod
	@rsync -e 'ssh -p 7822' -avz dist/* patfnet@mi3-ss121.a2hosting.com:/home/patfnet/public_html/
