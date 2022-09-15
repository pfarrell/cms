
post:
	PYTHONPATH=cms bin/new_post

gen-site:
	PYTHONPATH=cms python bin/gen_site.py

clean:
	rm site/*.post

