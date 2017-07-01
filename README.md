# temperature_to_es
Raspberry PI temperature monitor that sends temperature data to elasticsearch

## Requirements
+ A Raspberry PI
+ A Maxim DS18B20 temperature sensor (with 4K7/10K pull-up resistor).  


## Instructions

Configure the sensor as:

![raspi_ds18b20](https://user-images.githubusercontent.com/5869991/27763696-60742c5a-5e80-11e7-93b8-d1a570704689.jpg)

Alternatively, pre-built versions are available on ebay, which makes this a lot easier:

![ds18b20_built](https://user-images.githubusercontent.com/5869991/27763881-2a9513ca-5e84-11e7-98b2-c13a46b4e3d3.png)


Then put edit the hosts file with your PIs IP address and Elasticsearch host IP, and run the ansible playbook:

```no-highlight
ansible-playbook -i hosts site.yml -u root --ask-pass
```

<i><b>Note:</b> The first time this is run, the PI will reboot!</i>
