.PHONY: install dev seed test lint clean

install:
	pip install -e .

dev:
	pip install -e ".[dev]"

seed:
	python scripts/seed_rag.py

test:
	pytest tests/ -v

lint:
	ruff check src/ scripts/
	black --check src/ scripts/

format:
	black src/ scripts/

clean:
	rm -rf data/benefits_db/
	rm -rf __pycache__ .pytest_cache .mypy_cache .ruff_cache

run-rag-test:
	python -C "from src.tools.rag_retriever import RAGRetriever; r=RAGRetriever(); print(r.retrieve_context('health insurance'))"
