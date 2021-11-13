default: clean

clean:
	find . -name '*.pyc' -exec rm -rf {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.egg-info' -exec rm -rf {} +
	rm -rf dist/ build/ .pytest_cache/

format:
	isort src/yrouter_websockets tests examples
	black src/yrouter_websockets tests examples
	flake8 src/yrouter_websockets tests examples
