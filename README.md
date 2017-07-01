# temperature_to_es
Raspberry PI temperature monitor that sends temperature data to elasticsearch

## Requirements
+ A Raspberry PI
+ A Maxim DS18B20 temperature sensor (with 4K7/10K pull-up resistor)


## Instructions

Configure the sensor as:

![raspi_ds18b20](https://user-images.githubusercontent.com/5869991/27763696-60742c5a-5e80-11e7-93b8-d1a570704689.jpg)

Then run the ansible playbook on your Raspberry PI:

```no-highlight
ansible-playbook -i hosts site.yml -u root --ask-pass
```

<i><b>Note:</b> The first time this is run, the PI will reboot!</i>
