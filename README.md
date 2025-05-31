# check-unifi-controller
Checkmk special agent for checking unifi controller 

**ATTENTION START**

This is a FORK of the original special agent by bashclub. The fork contains a conversion to CheckMK's 2.3.0 API that's also used in 2.4.0. I (mbunkus) will not provide an MKP for this as I have no intention of maintaining the special agent. This fork's sole purpose is to offer others who're willing to maintain the special agent a version already converted to the 2.3.0 API & to save the maintainers some time. Please, go ahead & use this converted version in any way you see fit.

Additionally this fork contains a handful of fixes we had to implement in order to get it to run on our end.

Note that I have not tried this on an actual CheckMK 2.4.0 installation, only on 2.3.0 instances.

**ATTENTION END**

### Usage:
Login into your checkmk instnace user on your checkmk server (e.g. via SSH).
Download and install the checkmk agent:
~~~
wget https://github.com/bashclub/check-unifi-controller/releases/download/v0.87/unifi_controller-0.87.mkp
mkp install ./unifi_controller-0.87.mkp
~~~

### Configure Agent
Login into your checkmk website and go to "Setup" -> "Agents" -> "Other integrations" (Datasource programs). Under the category "Hardware" click on "Unifi Controller via API" and create a new rule.
Fill in the credentials of your Unifi controller, set the HTTPS Port, define the site name (if other than default), check "Ignore certificate validation" if using a self signed certificate, select Hostname or IP for storing piggyback data.
Under "Conditions" assign an "Explicit host" with your Unifi Controller Machine.
The agent will carry piggyback data for switches and access points and you can create new hosts to monitor, where piggyback data will be assignesd on exact match (IP or hostname).
