# P4 Getting started

> This function is not yet developed and still requires the external plug-in P4-Utils


## Install `P4-Utils` -> Manual Installation

P4-Utils is an extension to *Mininet* that makes P4 networks easier to build, run and debug. P4-utils is strongly
inspired by [p4app](https://github.com/p4lang/p4app). Here we only provide a quick summary of the main information
about P4-Utils. **Check out the [online documentation](https://nsg-ethz.github.io/p4-utils/index.html)
for more details about P4-Utils installation and usage.**

If you have already installed all the [requirements](#requirements), you can simply
install P4-Utils using the following commands:

```bash
git clone https://github.com/nsg-ethz/p4-utils.git
cd p4-utils
sudo ./install.sh
```

> **Attention!**  
> The install script will use `pip -e` to install the project in editable mode, meaning that every time you update the files
> in this repository, either by pulling or doing local edits, the changes will automatically take place without the need of
> installing the package again.

If you want to uninstall run:

```bash
sudo ./uninstall.sh
```

This will remove all the scripts that were added to `/usr/bin` as well as uninstall the python package using `pip`.

### Requirements

P4-Utils depends on the following programs in the given order:

1. [PI LIBRARY REPOSITORY](https://github.com/p4lang/PI) **is required only for topologies with
   P4Runtime switches**
2. [BEHAVIORAL MODEL (bmv2)](https://github.com/p4lang/behavioral-model)
3. [p4c](https://github.com/p4lang/p4c)
4. [Mininet](https://github.com/mininet/mininet)
5. [FRRouting](https://github.com/FRRouting/FRR) **is required 
   only for topologies with routers**

Since the installation process is long and cumbersome, **we provide a [Bash script](./install-tools)
that automatically installs the dependencies.**



# References

- [P4-Open-Source-Programming-Language](https://p4.org/)<br>
- [ComNetsEmu](https://git.comnets.net/public-repo/comnetsemu)<br>
- [p4-utils](https://github.com/nsg-ethz/p4-utils)from NSG.<br> 
- [mininet](https://mininet.org/)<br>
- [tutorials](https://github.com/p4lang/tutorials) from p4lang.<br>
- [p4-learning](https://github.com/nsg-ethz/p4-learning) from Networked Systems Group (NSG), a research group in Computer Networks at ETH Zürich.<br>
- [p4-demos](https://github.com/osinstom/p4-demos) from Tomasz Osiński.<br>