# PyKitMoney

Display Starling Kite information on an e-paper display connected to a Raspberry Pi Zero.

## Introduction 

We live in an increasingly cashless society and, moving with the times, my son has a [Starling Kite account](https://www.starlingbank.com/current-account/kite-debit-card-for-kids/) rather than physical pocket money. My dilemma was that he's only 7 and doesn't have his own smartphone to check his balance and transactions. Nothing a bit of Python and a Raspberry Pi can't sort out, right?

![A photo of a Raspberry Pi Zero running PyKitMoney](/docs/pizero.jpeg)

This README goes through the steps to take this code and turn it into a (hopefully) working pocket money display. I've found that guides to anything Raspberry Pi go out of date quickly so be sure to consult other sources (the official Raspberry Pi website, Stack Overflow and Google) if anything doesn't make sense or doesn't work. If everything goes smoothly, total setup time should be 1-2 hours and cost about £50.

I am not an experienced Python programmer so my apologies to any professional Python coders who read my code. 🙈

> [!NOTE]
> This is very much a _it works for me_ kind of hobby project. You will need a moderate amount of technical knowledge to problem solve any issues that arise.

This project was partially inspired by this [cool weather display](https://blog.polarizedions.net/posts/2020-11-25-make-a-weather-display/). Many thanks to [PolarizedIons](https://github.com/PolarizedIons) for giving me the motivation that I needed.

## Shopping List

What you need:

1. A [Raspberry Pi Zero 2 W (with header)](https://thepihut.com/products/raspberry-pi-zero-2?variant=43855634497731). It should be technically possible to run this project on a Raspberry Pi Zero WH but I came across a lot of issues with python library compatibility, possibily due to it being 32-bit. 
1. An [e-paper screen](https://thepihut.com/products/2-13-e-paper-hat-for-raspberry-pi-250-x-122). I went for the Waveshare 2.13" E-Paper HAT+ as it attaches straight to the Raspberry Pi Zero's header and has several compatible cases available for it. If you're feeling fancy, colour displays are also available in this size and resolution.
1. A [case](https://thepihut.com/products/pi-zero-case-for-waveshare-2-13-eink-display). There's also an option for [a case with the e-paper display already built in](https://thepihut.com/products/2-13-touchscreen-e-paper-display-case-for-raspberry-pi-zero). Both work well so it depends on what aesthetic you're going for or what's in stock.
1. A [Raspberry Pi Zero power supply](https://thepihut.com/products/raspberry-pi-zero-uk-power-supply). Which one you go for is going to depend on your country and which Pi Zero you chose.
1. A microSD card (I went with a Sandisk 32GB card - don't worry about getting the one with Pi OS pre-installed as we can't use the pre-configured settings to run in headless mode).
1. (Optional) A **down** right-angle micro USB adapter (otherwise the power supply cable pokes out of the top at a funny angle).
1. A Kite account with Starling Bank. Hopefully this one is obvious? :)

I'm not affiliated with Pi Hut but I've linked to their store as that's where I ordered from.

What you don't need:

* A microHDMI adapter
* Any microUSB dongles or adapters

We're going to run the Raspberry Pi Zero in headless mode so these are redundent.

## Setting up the Raspberry Pi Zero

### Use Rapsberry Pi Imager to flash the SD card

1. Download [Raspberry Pi Imager](https://www.raspberrypi.com/software/) to the desktop OS of your choice.
1. Choose the default Raspberry Pi OS. The Raspberry Pi Zero WH needs the 32-bit version whereas the Raspberry Pi Zero 2 can run the 64-bit version. After selecting your device, the imaging software should show you only compatible options. It should, it theory, be possible to use the lite version of Raspberry Pi OS but I've never gotten it to work with the required Python libraries.
1. Click next and choose to edit settings.
1. Enter all of the details - device hostname, login name, login password, WiFi details, enable ssh, timezone, etc.
1. Click Save and away you go.

[Official guide](https://www.raspberrypi.com/documentation/computers/getting-started.html#raspberry-pi-imager).
 
### Boot your Raspbery Pi

1. (Optional) Build the case. 
1. Insert the microSD card into your Raspberry Pi Zero.
1. Connect the power supply to boot the Raspberry Pi Zero.

A green light will began to flash intermittedly. Give the device 30 seconds and it should be reachable via ssh.

### Set up your Raspberry Pi

Use your favourite ssh tool to remotely log in to your Raspberry Pi using the username and password you set when creating the image. Now the real fun begins. 

The first thing to do is to update your Pi:
 
```bash
sudo apt-get update
```
```bash
sudo apt-get upgrade
```

You will also need to install and configure git:

```bash
sudo apt install git
```
```bash
git config --global user.name "<your name>"
```
```bash
git config --global user.email "<your e-mail address>"
```

You may wish to also install the text editior of your choice.

Python should be included by default but you can test by running:

```bash
python --version
```

This project was written using Python 3.11.2. Hopefully you've got something similar, otherwise you'll need to get into the world of [pyenv](https://github.com/pyenv/pyenv) and configuring different python versions.

### Enable the SPI

This project requires the Serial Peripheral Interface to be enabled on your Raspberry Pi. I found that it was turned off by default on my Pi Zero. You can enable it as follows:

1. Run `sudo raspi-config`
1. Select "Interfacing Options"
1. Select "SPI"
1. Select yes when it asks you to enable SPI

A reboot shouldn't be required.

### Create Starling developer account

In order to talk to Starling's API, you will need to create an access token. This access token gives permissions-based access to your bank account.

> [!WARNING]
> The generated access token will give access to your _real_ bank account. Be sure to give it only read access.

You can [follow the official guide](https://developer.starlingbank.com/docs#accessing-your-own-starling-bank-account-1) for setting up an account and generating an access token. The access token needs the following scope:

* `account:read`
* `account-list:read`
* `savings-goal-transfer:read`
* `space:read`
* `transaction:read`

Do not give the access token any additional permissions.

### Download and configure PyKitMoney

PyKitMoney can be cloned from this repository:

```bash
git clone https://github.com/AaronTunney/PyKitMoney.git
```

Once cloned, enter the project directory: 

```bash
cd PyKitMoney/
```

Two pieces of information need to be configured - the child's name and access token. Enter the child's name by opening `resources/settings.json` and entering your child's name. This name will be used both to find the Kite account and is displayed on the e-paper display.

Next, open `resources/accesstoken.txt` and paste the access token you generated earlier. The project is now configured for your child!

If you've bought anything other than V3 of the 2.13" e-paper display linked to earlier (Pi Hut helpfully specifies which version it currently has in stock), you will also need to modify the following line in `epaper_drawing.py`:

```python
epd = epaper.epaper('epd2in13_V3').EPD()    
```

The next step is to return to the root project directory and create a Python virtual environment. The virtual environment keeps all of PyKitMoney's depedencies separate from your main Python environment.

```bash
python3 -m venv .venv
```

This may take 10 seconds on a Pi Zero so don't worry if the terminal output pauses. You can then activate the virtual environment:

```bash
source .venv/bin/activate
```

You will notice that there's two requirements files in PyKitMoney's directory. The default one contains all of the dependencies for the project. `requirements_dev.txt` contains only the cross-platform libaries so that the majority of the project can be written and debugged on a desktop machine running macOS, Windows or Linux. Install the default requirements:

```bash
pip install -r requirements.txt 
```

You can now test using:

```bash
python main.py 
```

The command will run but error if you haven't entered an access token yet. If the access token is present and properly configured, you should see your child's account appear on the e-paper display! The drawing code is very basic. You may wish to open `epaper_drawing.py` and slightly tweak the layout to get all of the text to align and show at a sensible font size.

You can exit the virtual enviroment by running the following command:

```bash
deactivate
```

### Set up the systemd job

Finally, PyKitMoney needs to be set up so that it will be periodically executed. This is done by creating a systemd job.

An example PyKitMoney service is included in the `/service`. Open `pykitmoney.service` and look for a line like:

```bash
ExecStart=<full project path>/.venv/bin/python3 <full project path>/main.py
```

Enter the full path to your project (e.g. `/home/kate/development/PyKitMonkey`) in the two places where it's needed. If you wish, you can open `pykitmoney.timer` and change how often it runs. The default is once per hour.

You can now copy these files to the appropriate directory:

```bash
sudo cp service/pykitmoney.* /etc/systemd/system/
```

Run the following commands to start (starts the service) and enable (starts again at boot) the service:

```bash
sudo systemctl daemon-reload
```
```bash
sudo systemctl start pykitmoney
```
```bash
sudo systemctl enable pykitmoney
```

You can check the status of the systemd job at any time using the following command:

```bash
systemctl status pykitmoney
```

### Sit back and relax

Enjoy several more years of your child not owning a smartphone. :)
