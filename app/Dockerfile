FROM python:3.7.3
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install requests
RUN pip install -U flask-cors
RUN pip install python-dotenv 
ENV FLASK_HOST=0.0.0.0
ENV WEATHERMAP_API_KEY=d4450502dc2d565c203526c49b66b8cc
ENV FLASK_ENV=development
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["server.py"]