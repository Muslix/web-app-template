# Makefile für Investment-Tracker Projekt

install:
	@echo "Installing backend dependencies..."
	pip install -r backend/requirements.txt
	@echo "Installing frontend dependencies..."
	cd frontend && npm install

backend-install:
	@echo "Installing backend dependencies..."
	pip install -r backend/requirements.txt

backend-run:
	@echo "Starting Flask backend..."
	cd backend && flask run

frontend-run:
	@echo "Starting Vue frontend..."
	cd frontend && npm run dev

start:
	@echo "Starting both frontend and backend..."
	make -j2 backend-run frontend-run

migrate:
	@echo "Running database migrations..."
	cd backend && flask db upgrade
