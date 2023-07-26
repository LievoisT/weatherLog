## Weather Station Setup
* https://shop.ecowitt.com/products/gw1100
* https://shop.ecowitt.com/products/ws68

### Explanation
* The gw1100 hosts a wifi hotspot that your device will need to connect to
* once connected to the hotspot you can get the current weather data using this address: http://192.168.4.1/get_livedata_info
* The script as written creates a csv file for each day and records the wind speed and direction once per minute
* if you want other weather info as well you can see what each of the id numbers corresponds to
  * https://wiki.ledhed.net/index.php?title=Ecowitt_GW1000

### Run on startup
* you can use the service file to set this up to run automatically if you use systemd.  
  * Check that the paths in the service file are correct for your setup  
`ExecStart=python3 path_to_weatherLogger.py`
and
`WorkingDirectory=path_to_folder_to_save_csv_files`
  * move the service file to /etc/systemd/system/
  * enable and start the program so that it runs when you start up
    * `sudo systemctl daemon-reload`  
    * `sudo systemctl enable weather_logger.service`
    * `sudo systemctl start weather_logger.service`


email: tlievois@gmail.com
