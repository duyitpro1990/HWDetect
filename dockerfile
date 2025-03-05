FROM python:3.12
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6  -y
WORKDIR /home/duyitpro90/hwdetect
COPY . .
RUN pip install -r requirement.txt
CMD ["python", "app.py"]