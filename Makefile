install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

package-uninstall:
	python3 -m pip uninstall hexlet-code || True

lint:
	poetry run flake8 brain_games

deploy: package-uninstall install build publish package-install
