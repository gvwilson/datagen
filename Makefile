# Manage datagen project.

.DEFAULT: commands

PYTHON = uv run python
PYTHON_M = uv run python -m
SRC = datagen

## commands: show available commands
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## clean: clean up build artifacts
clean:
	@find . -name '*~' -delete

## format: reformat code
format:
	${PYTHON_M} ruff format ${SRC}

## lint: check the code format and typing
lint:
	${PYTHON_M} ruff check ${SRC}
