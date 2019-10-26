test:
	docker-compose -f docker-compose.test.yml run --rm api pytest -v ./tests/test_autocheckin_task.py

.PHONY: all