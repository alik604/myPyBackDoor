# myPyBackDoor
> "back door" written in python 

## Getting Started 
```python

python server.py

python slave.py 

```
Tested on the same computer, you will need your PC's hostname and/or IP addr  


## Usage
press X and follow on screen instructions to do Y
  - 1: View Current Working Dir
  - 2: View custom Dir
  - 3: Download File 
  - 4: Delete File 
  - 5: Delete Dir  
  - 6: Create File 
  - 7: Return ipconfig (TODO...) // so we can spoof our target MAC address  
  - 8: Execute custom CMD command 
  - 9: "Shut it down" -MC Hammer 
  - 10: Get wifi Password list 



 ## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## Inspiration 
+ Mr. robot
+ https://github.com/quasar/QuasarRAT
+ https://github.com/nathanlopez/Stitch

## Expansion  

I wont get around to any of these... I am too busy with learning _ML for Security_. The first two suggestion will likely be their own mini-project, which I won't get around to integrating into myPyBackDoor    

* Capture video with web cam, and send (via FTP?). record IFF a human face is in view of camera (via OpenCV), this part is partially done. see my openCV projects DIR. 

* record mic, and conveter to text and transmit 

* [Hijack chrome passwords (pretty easy to do). This compontent is done here, but is easy to integrate in](https://github.com/alik604/chromePasswordThieve)

  * [Tutorial 1](<https://github.com/ProgrammedBoi/password-stealer/blob/master/stealer.pyw>)
  * [Tutorial 2](<https://github.com/ProgrammedBoi/password-proof-of-concept/blob/master/pass_stealer.py>)
*  [Tutorial 3](https://raw.githubusercontent.com/byt3bl33d3r/chrome-decrypter/master/chrome_decrypt.py)
* search for a file call "wallet.dat"💯😈💹 // %100 evil makes money 

* turn this into a proper [rat](https://en.wikipedia.org/wiki/Remote_access_trojan)
  + Bypass antivirus 
  + Sample [1](https://github.com/nathanlopez/Stitch)
  + Sample [2](https://github.com/n1nj4sec/pupy)


+ add in my Python Keylogger
+ add in my DoS client 
  - make more effective. 



## License
[MIT](https://choosealicense.com/licenses/mit/)


## Related projects
1. [CMPT 318: Cyber Security](https://github.com/alik604/Classes/tree/master/CMPT318)
    - [Presenation on Anomaly Detection](https://github.com/alik604/Classes/blob/master/CMPT318/CMPT_318_Presentation.pdf) 
2. [chromePasswordThieve](https://github.com/alik604/chromePasswordThieve)
    - Grab passwords saved in chrome and email them out 
    - [Blog post](https://alik604.github.io/chromePasswordThieve/index.html)
3. [bandwidth-hog](https://github.com/alik604/bandwidth-hog)
    - Download a file many times, but do not save the data. Useful for stressing out a network... possibly your own
