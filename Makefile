test:
	pytest src

type-check:
	mypy src/

ci: type-check test