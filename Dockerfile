FROM python:buster

WORKDIR /camera_api

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY camera_lines.py .

CMD ["python", "camera_lines.py"]