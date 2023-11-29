FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

WORKDIR /dst/

RUN apt update
RUN apt install -y python3-pip git

RUN pip install --upgrade pip
RUN pip install ffmpeg 
RUN pip install ffmpeg-python
RUN pip install --upgrade git+https://github.com/huggingface/transformers.git accelerate datasets[audio]

COPY ./mp3/ /dst/mp3/
COPY ./Whisper.py /dst/Whisper.py

CMD [ "python3", "Whisper.py" ]