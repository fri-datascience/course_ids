FROM python:3.11.1-bullseye

WORKDIR /app

ENV JUPYTER_DIR '/jupyter-data'
ENV JUPYTER_PASSWORD 'Geslo.01'

RUN pip install notebook==7.0.6 pandas==2.1.3

EXPOSE 8888

ENTRYPOINT jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser \
            --NotebookApp.token=${JUPYTER_PASSWORD} --allow-root --notebook-dir=${JUPYTER_DIR}