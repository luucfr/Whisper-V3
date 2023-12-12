FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

WORKDIR /dst/

RUN apt update
RUN apt install -y python3-pip git ffmpeg

RUN pip install --upgrade git+https://github.com/huggingface/transformers.git accelerate datasets[audio] ffmpeg ffmpeg-python

COPY ./mp3/ /dst/mp3/
COPY ./Whisper.py /dst/Whisper.py

CMD [ "python3", "Whisper.py" ]
