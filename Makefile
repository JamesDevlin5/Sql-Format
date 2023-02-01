
lex.py:
	curl -sSLO "https://raw.githubusercontent.com/dabeaz/ply/master/src/ply/lex.py"

test:
	pytest test_fmt.py

.PHONY: test
