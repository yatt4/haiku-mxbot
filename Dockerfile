FROM python
WORKDIR /usr/local/haiku-mxbot

RUN pip install --upgrade pip
RUN pip install --no-cache-dir simplematrixbotlib nltk dotenv

COPY haiku-detector-strict.py .

RUN useradd -m haiku && chown -R haiku /usr/local/haiku-mxbot
USER haiku

CMD ["python3", "./haiku-detector-strict.py"]



