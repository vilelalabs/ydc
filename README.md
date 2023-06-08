# YDC - Youtube Downloader and Converter

## Description
This is a simple script to download and convert youtube videos to mp3.

## Fast install & run
```bash
git clone
cd ydc
pip install -r requirements.txt
python3 ydc.py
```
---

## Usage
Run in CLI:

```bash
python3 ydc.py
```
A prompt will ask you for youtube video url. 
```bash
Enter the url of the video you want to download: 
```
Paste the url and press enter. The video will be downloaded (if file is big can take a lot of time, *be patient with you blank shell!*) and converted to mp3. The mp3 file will be saved in the same directory as the script with the name music1.mp3

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Notes
- This script was made for educational purposes only. I am not responsible for any misuse of this script.

## Future Improvements
- [ ] output folder
- [ ] Try to a progress bar during the video download
- [ ] Add GUI
- [ ] Integrate with [audio-music-divider](https://github.com/vilelalabs/audio-music-divider) in same (third) application

---

## Requirements (if "fast" commands isn't enough to work)
before install moviepy, follow the instructions in this link: [moviepy requirements](https://zulko.github.io/moviepy/install.html)
Then, install the following packages:
```
pip install pytube moviepy glob
```