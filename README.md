# Visby

A lightweight web application designed for collecting and visualizing biometric data, built for personal daily use and experimentation with cloud deployment. Developed as a 40-hour challenge to explore the effectiveness of current LLMs in development.

### Short term goals
- [x] Simple backend in Python FastAPI framework
- [x] [Swagger](https://github.com/swagger-api/swagger-ui) API documentation
- [x] Docker containerization
- [x] [Superset](https://github.com/apache/superset) data visualization
- [x] CI/CD flow
- [x] ~~GCP~~ Heroku deployment
- [ ] Tests: unit, integration, e2e

### Long term goals
- [x] Web UI using ~~Node.js~~ [Dash](https://dash.plotly.com/)
- [ ] ~~Android app in Flutter~~

## Instalation
```
pip install visby
uvicorn visby.main:app --host 0.0.0.0 --port 8000
```

## Usage
To explore the API, simply start the application and go to http://localhost:8000/docs in your browser. This will open the interactive Swagger API documentation, allowing you to view available endpoints, make test requests, and see sample responses.

## Contact
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin&logoColor=white&style=flat-square)](hlinkedin.com/in/klawikowski-jakub)
[![Email](https://img.shields.io/badge/Email-Contact%20Me-blue?logo=gmail&logoColor=white&style=flat-square)](mailto:klawik.j@gmail.com)
