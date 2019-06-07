# Ansible Inventories 

Ajay Chenampara

Twitter/Github : @termlen0

--next--


# Today's presentation

- Introduction

- Static inventories

- Nested inventories

- Group and Host variables

- Better managing inventory vars

- Dynamic inventories


--next--



# Introduction

<img src="media/images/language.svg" />



--next--


## The Ansible ecosystem - Playbooks

<img src="media/images/how-ansible-works-diagram-02.svg" />

--next--




## The Ansible ecosystem - Inventories
<img src="media/images/how-ansible-works-diagram-05.svg" />

--next--



## Understanding inventory
<div class="columns">
    <div class="col">
<pre>
```
10.1.1.2
192.168.1.2
core1.nw.com
core2.nw.com
access1.nw.com
access2.nw.com
```</pre>


<pre>```

leaf[1:10]
core[A:D]

```</pre>
</div>
<div>
</div>


--next--


## Inventory - Groups

<div class="columns">
    <div class="col">
    There is always a group called **"all"** by default
<pre>
```
[atl]
10.1.1.2
192.168.1.2
    
[core]
core1.nw.com
core2.nw.com
    
[access]
access1.nw.com
access2.nw.com
```</pre>

</div>

<div>
Groups can be nested
<pre>
```
[DC:children]
core
access

[east-coast:children]
DC
atl

[atl]
10.1.1.2
192.168.1.2
    
[core]
core1.nw.com
core2.nw.com
    
[access]
access1.nw.com
access2.nw.com
```</pre></div>


--next--

## Inventory - variables

<div class="columns">
    <div class="col">

<pre>
```
[all:vars]
ansible_username=admin
ansible_password=pa55w0rd
snmp_ro=public123
snmp_rw=private123

[east-coast:vars]
ntp_server=10.99.99.99
anycast=169.1.1.1

[DC:children]
core
access

[east-coast:children]
DC
atl

[atl]
10.1.1.2 snmp_ro=atl123 
192.168.1.2
    
[core]
core1.nw.com snmp_ro=corepub123 snmp_rw=corepri123
core2.nw.com
    
[access]
access1.nw.com ansible_username=localadmin
access2.nw.com 
```</pre>
</div>
<div> 
<p>- Group variables apply for all devices in that group </p>
<p>- Host variables apply to the host and overrides group vars </p>
</div> 



--next--

## Group vars and host vars

- Organize variables out of inventory files
- **`group_vars`** and **`host_vars`** directory
- Structure of the directory is important


``` bash
.
├── debug_demo.inv
├── debug_demo.yaml
├── group_vars
│   ├── all.yaml
│   └── east_coast
│       ├── anycast.yaml
│       └── ntp.yaml
└── host_vars
    ├── access1.nw.com.yaml
    └── core1.nw.com
        └── snmp.yaml

```

--next--


## Dynamic inventories

- Leverage existing source of truth
- Inventory file should be executable
- Ansible supports dynamic and static inventories simultaneously


``` bash
ansible-playbook -i dynamic_inv.py playbook.yaml
```

--next--

## Discussion
