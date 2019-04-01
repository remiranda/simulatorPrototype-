# Simulator Prototype
prerequisite, to have installed ansible

##### $ sudo ansible-playbook main.yml -i host
##### $ docker exec -it master /bin/bash
##### $ docker rm -f attacker2 attacker1 master

 ###### Limit  the number of packets to capture 
              sudo tcpdump -c 20.
              
              
##### Capture only TCP packets
    sudo tcpdump 'tcp'
  
  or   
  ###### sudo tcpdump 'type protocol'
