apt update
apt install -y python3-pip git ffmpeg

pip install --upgrade git+https://github.com/huggingface/transformers.git accelerate datasets[audio] ffmpeg ffmpeg-python