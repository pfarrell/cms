
post:
	@PYTHONPATH=cms bin/new_post

gen-site:
	@PYTHONPATH=cms bin/gen_site

clean:
	rm build/*

black:
	PYTHONPATH=cms black cms bin
