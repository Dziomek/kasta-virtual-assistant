<p align="center">
  <img src="https://user-images.githubusercontent.com/72970978/166124613-df2ae0d7-1f7c-4d03-bbcb-97fc9ead719d.png" alt="logo" width="200"/>
</p>
<div align="center">
    <p><h1>Kasta VA Virtual Assistant</h1></p>
</div>
This is a application in the graphical user interface resembling Siri or the Google assistant in its operation. It has been equipped with many functions, e.g. reading the weather from the API, telling jokes and even saving notes to the database and sending them to an e-mail or phone.

Uses speech recognition to take your commands and process them appropriately. Kasta answers by voice and writes the answer on the screen.

## Motivation

Creating something that we can use on dayli basics esspesially playing music, getting newest weather and newes reports.
Thanks to this project we learned a lot of python modules. Also we gain practical knowladge
of connecting a MySQL database and APIs.
In our apliaction we use database which was created on Google Cloud Platform.

Thanks to this project, we took our python programming skills to the next level.
## Installation

Install Kasta VA with pip:

```bash
  pip install -r requirement.txt

```

If there is a problem with pyaudio installation, use the commands below:

```bash
  pip install pipwin
  pipwin install pyaudio

```
#### Executing program
To execute Kasta VA run main.py

#### Warning! 
The application only works when the database is turned on. When the database is turned off, please contact the authors to turn it on. Thank you for your understanding.
## Documentation

In progress

### Graphical User Interface
* [Splash Screen](#Splash-Screen)
* [Login Page](#Log-In)
* [Regsiter](#Register)
* [One time password](#otp)
* [Main window](#main)

### Kasta VA Features

* [Greetings](#greetings)
* [Acknowledgment](#acknowledgment)
* [Help](#help)
* [Date](#date)
* [General response](#generalresponse)
* [headortails](#headsortails)
* [Jokes](#jokes)
* [News](#news)
* [Create Note](#createnote)
* [Read Note](#readnote)
* [Send Note via email](#sendNoteViaEmail)
* [Send Note via SMS](#sendNoteViaSms)
* [Open Application](#openApp)
* [Weather](#weather)
* [Wikipedia](#wikipedia)
* [WolframAlpha](#wolfram)
* [Open Youtube video](#youtube)
* [Rock paper scisorrs](#rockpapperscissors)
* [Search in google](#googleSearch)







## Splash Screen
The splash screen is used to load all modules in the application
<p align="center">
  <img src="https://user-images.githubusercontent.com/72970978/166832470-4874afe3-3d69-4bff-90f4-7be91b38836a.png" alt="splash"/>
</p>

## Log In
Log in takes place by entering an e-mail and password. The password is saved in the database as a hash.
The Login Page returns information about the correct data entry, wrong password and the lack of completion of all fields.
When the account is not confirmed after clicking log in, we are asked to enter OTP.
<p align="center">
  <img src="https://user-images.githubusercontent.com/72970978/166832472-41f582a8-6a58-42d7-948a-3943d4dc8ee2.png" alt="login"/>
</p>

## Register
The password is encrypted and saved to the database.
After registering the user, the e-mail associated with the account receives a one-time password that must be entered to activate the account.
<p align="center">
  <img src="https://user-images.githubusercontent.com/72970978/166832467-395f812f-ef98-4b69-8f5e-c8505e117b0d.png" alt="register"/>
</p>




## Authors

- [@ Jakub Niećko](https://github.com/nieckojakub)
- [@ Dominik Ziomek](https://github.com/Dziomek)

