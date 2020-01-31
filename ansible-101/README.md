1. Download and install Vagrant (https://www.vagrantup...­)
2. Download and install VirtualBox (https://www.virtualbo...­)
3. Create directory meetups
4. With favorite editor create file 'Vagrantfile'
5. Place parameters below in Vagrantfile

``` bash


####################

Vagrant.configure("2") do |config|

config.vm.define :controller do |controller|
controller.vm.box = "ansible/tower"
controller.vm.network :private_network, ip: "10.0.0.10"
controller.vm.hostname = "controller"
end

config.vm.define :linux do |linux|
linux.vm.box = "centos/7"
linux.vm.network :private_network, ip: "10.0.0.11"
linux.vm.hostname = "linux"
end

config.vm.define :linux2 do |linux2|
linux2.vm.box = "centos/7"
linux2.vm.network :private_network, ip: "10.0.0.12"
linux2.vm.hostname = "linux2"
end

end
################

```

6. Start virtual machines (vagrant up --provider virtualbox)
7. Ping vms in Vagrantfile to verify connectivity.
8. ssh to controller (vagrant ssh controller) to collect Tower url and credentials
Log into the web interface here:

https://10.42.0.42/...­

``` bash
Username: admin
Password: <admin_password>

```

9. Download Tower license (https://www.ansible.c...­)

10. Collect license from email and copy/paste to a file
11. Access Tower web interface and upload license.
12. You should see Tower dashboard
13. Shutdown vm (vagrant -halt)
