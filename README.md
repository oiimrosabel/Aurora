# Aurora

**A simple, modern and elegant muOS theme.**

## Installation

### From the **Releases** page

1. Head over to the **Releases** page : [link](https://github.com/oiimrosabel/Aurora/releases)
2. Find the most recent release
3. Download the zip with the variant you want
4. Move it to `/MUOS/theme/` (on the `SD2`, or `SD1` if you use only one card)
5. Apply the theme from the **Theme Picker**
6. (Optional) Choose a variant from the **Customization** menu

### From source

> [!IMPORTANT]
> Before you start, bear in mind every action described here must be done on a **Linux distro** (or **WSL**) or **macOS** with a recent enough version of **Python** (>= Python 3.12).

> [!IMPORTANT]
> This repo uses Git LFS. If you need to clone or fork the project, you'll need to install it on your system. More info can be found [here](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage).

> [!CAUTION]
> This method may produce broken themes, as this repo contains untested code. If you don't mind that, or want to tinker with the tools I made, go ahead :3.

1. Clone this repo :

```bash
git clone https://github.com/oiimrosabel/Aurora.git
```

2. Change to project root :

```bash
cd ./Aurora/
```

3. Execute the generation script.

```bash
python3 -m Wavemaker
```

4. Head over to the `dist` folder at the root of the project. You should find a file named `Aurora.muxthm`.
5. Move the zip to the correct folder, as indicated above (from the 4th instruction onwards).

#### TL;DR

For convenience, you can copy-paste the following script into a `.sh` file and execute it using `bash`, or paste it
directly in the terminal and hit <kbd>Enter</kbd>:

```bash
git clone https://github.com/oiimrosabel/Aurora.git
cd ./Aurora
python3 -m Wavemaker
cd dist
ls
```

## Grid support

This theme officially support muOS's grid layout for the **Explore** page. From **Pixie** onwards, the grid icons are automatically installed on your system upon selecting the theme.

## Troubleshooting

### Your screen is blank and/or your system gets bricked

That probably means the theme didn't get extracted correcly. To resolve this issue, follow those steps :
- **Shut down** your device by pressing the following button combination : <kbd>L2</kbd> + <kbd>R2</kbd> + <kbd>SELECT</kbd>

> [!WARNING]
> Never use the **Reset** button on the side of your device, as it is known to corrupt the OS's filesystem. Prefer using the hotkey shown above, also referred to as the "Safe Shutdown" hotkey.

- **Eject the SD card** on which the themes are loaded, and connect it to a computer
- **Delete** the folder `MUOS/theme/active/`
- **Plug back the SD card** in your device and turn it on, muOS's default theme should be set
- **Re-apply** Aurora from the **Theme Picker**

Just in case, here's the quote I used to link to before : 
> Please go into your `MUOS/theme/active` folder and remove everything in there, your system should now boot, and you
> can choose a different (not broken) theme. - [Harry](https://hmcneill46.github.io/muOS-MinUIfied-Theme-Generator/)

### An error occurred during the generation phase

- Make sure the version of Python you're using is recent enough. Also, make sure you're using `python3` instead of
  `python` in the command prompt.
    - If you're unsure, execute `python3 --version` (or `python --version` if the former yields an error).
- Make sure the message is an actual error. Some are just warns, meant to ease out debugging. Errors are usually
  prefixed by `⨉ ERROR` (and not `⚠ NOTICE`). Note that warnings should only appear if the `-v` or `--verbose` is set.
    - Errors usually appears before the script stops. If you're using `bash`, execute `echo $?` to see the script's
      return code. If it's `0`, that means the script worked properly.
- If none of these steps solved your issue, send me a message...
	- on Discord by DMs (`@oiimrosabel`)
	- on the muOS forum ([here](https://community.muos.dev/t/pixie-aurora/))

... with the error message, I'll help you troubleshoot the issue.

### The **Explore** menu is empty

That probably means something went wrong during the installation process. Please re-apply **Aurora** with the **Theme Picker**.

### I can't activate Grid Mode on the "Applications" and "Collections" pages
This is by design, as I haven't made any icons for those menus. If you have your own set of icons, and want to activate Grid Mode anyway, go into `SD[1|2]/MUOS/theme/active/scheme/` and delete `muxcollect.ini` and/or `muxapp.ini`. Note that this change won't be overwritten after switching to another variant, but will if you re-apply Aurora from the Theme Picker.
