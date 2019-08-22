# Simulator Prototype


Prerequisite, to have installed **Ansible**

###### $ sudo ansible-playbook main.yml -i host
###### $ docker exec -it master /bin/bash
###### $ docker rm -f attacker2 attacker1 master



              tcpdump [ -AbdDefhHIJKlLnNOpqStuUvxX# ] [ -B buffer_size ]
               [ -c count ]
               [ -C file_size ] [ -G rotate_seconds ] [ -F file ]
               [ -i interface ] [ -j tstamp_type ] [ -m module ] [ -M secret ]
               [ --number ] [ -Q in|out|inout ]
               [ -r file ] [ -V file ] [ -s snaplen ] [ -T type ] [ -w file ]
               [ -W filecount ]
               [ -E spi@ipaddr algo:secret,...  ]
               [ -y datalinktype ] [ -z postrotate-command ] [ -Z user ]
               [ --time-stamp-precision=tstamp_precision ]
               [ --immediate-mode ] [ --version ]
               [ expression ].



###### Limit  the number of packets to capture 
```
sudo tcpdump -c 20
```
              
##### Capture only TCP packets
    sudo tcpdump 'tcp'
  
  or   
  ###### sudo tcpdump 'type protocol'


##### Save and read files
###### Save
    sudo tcpdump -w paquetes.dump
###### Read
    sudo tcpdump -r paquetes.dump

##### Filter records with source and destination IP
###### To Capture packets from a source IP
    sudo tcpdump -i eth0 src 192.168.1.1
###### You can monitor packets from a destination IP
    sudo tcpdump -i eth0 dst 192.168.1.1



######  https://www.tcpdump.org/manpages/tcpdump.1.html
######  http://lextoumbourou.github.io/blog/posts/packet-capturing-in-parallel-ansible/
######  https://picodotdev.github.io/blog-bitix/2014/11/integracion-entre-ansible-y-docker/
######  https://www.linuxito.com/gnu-linux/nivel-medio/1214-mover-archivos-entre-hosts-con-ansible
######  http://toroid.org/ansible-parallel-dispatch
