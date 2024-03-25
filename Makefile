start:
	docker-compose -f docker-compose.yml up -d --remove-orphans

run: start
	docker-compose -f docker-compose.yml exec qa_ollama_python uvicorn app:app --host 0.0.0.0 --port 5000

bash: start
	docker-compose -f docker-compose.yml exec qa_ollama_python bash

setup: start
	docker-compose -f docker-compose.yml exec qa_ollama_server ollama pull mistral
	docker-compose -f docker-compose.yml exec qa_ollama_python pip install --no-cache-dir -r src/requirements.txt
