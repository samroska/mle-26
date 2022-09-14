FROM python:3.8.9
LABEL description="Sam Roska ML26"
ADD model-app/ /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r packages.txt
EXPOSE 1313
CMD ["uvicorn", "api.predict:app","--host","0.0.0.0", "--port", "1313"]