# FFMPEG w/ NVENC & CUDA Support

1. Dependencies:
    
    - Have CUDA / CUDNN already working (10.2 req'd on driver 440 as of writing)
    - YASM: `sudo apt-get install yasm`

2. Clone the FFMPEG git repo: `git clone https://git.ffmpeg.org/ffmpeg.git`

3. `cd ffmpeg`

4. `./configure --enable-cuda-sdk --enable-cuvid --enable-nvenc --enable-nonfree --enable-libnpp --extra-cflags=-I/usr/local/cuda/include --extra-ldflags=-L/usr/local/cuda/lib64`

5. Move FFPMEG to your `bin` to make it always accessible: `sudo mv ./ffmpeg /usr/local/bin/ffmpeg`

6. Test using `ffmpeg -y -hwaccel cuvid -c:v h264_cuvid -vsync 0 -i <input.mp4> -vf scale_npp=1920:1072 -vcodec h264_nvenc <output0.264> -vf scale_npp=1280:720 -vcodec h264_nvenc <output1.264>`
