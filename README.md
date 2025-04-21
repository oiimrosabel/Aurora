# Aurora

**A simple, modern and elegant muOS theme.**

## Notice

**Aurora** now boasts a **brand-new layout** on the main menu. If you prefer the **old layout**, with all the buttons on
the main
menu visible, you can try [**OneTwo**](https://github.com/bulkh/OneTwo), a remake of the old Aurora, made by **bulkh** (
thank you a lot !).

## Links

- [**Aurora on muOS's community forum**](https://community.muos.dev/t/pixie-aurora/)
- [**OneTwo on muOS's community forum**](https://community.muos.dev/t/pixie-onetwo/)

## Installation

### From the **Releases** page

1. Head over to the [**Releases** page](https://github.com/oiimrosabel/Aurora/releases)
2. Find the most recent release
3. Download the zip with the variant you want
4. Move it to `/MUOS/theme/` (on the `SD2`, or `SD1` if you use only one card)
5. Apply the theme from the **Theme Picker**
6. (Optional) Choose a variant from the **Customization** menu

### From source

> [!IMPORTANT]
> Before you start, bear in mind every action described here must be done on a **Linux distro** (or **WSL**) or **macOS
** with a recent enough version of **Python** (>= Python 3.12).

> [!IMPORTANT]
> This repo uses Git LFS. If you need to clone or fork the project, you'll need to install it on your system. More info
> can be
>
found [here](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage).

> [!CAUTION]
> This method may produce broken themes, as this repo contains untested code. If you don't mind that, or want to tinker
> with the tools I made, go ahead :3.

1. Clone this repo.

```bash
git clone https://github.com/oiimrosabel/Aurora.git
```

2. Change to project root.

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

This theme officially support muOS's grid layout for the **Explore** page. From **Pixie** onwards, the grid icons are
automatically installed on your system upon selecting the theme.

### Regarding alternative icons

Some icons have alternate versions you can find in `MUOS/info/catalogue/Folder/grid/__alts`. To set them, follow those
steps :

- **Move** the images in its parent folder (`MUOS/info/catalogue/Folder/grid/`)
- **Rename** the images accordingly, if not already prompted by your OS's file explorer

## Support for custom box art

In case you have some box art images you generated with Skraper or Scrappy, you may need to tweak the menu's disposition
a bit to make everything fit. No need to edit the theme for that, you can use overrides. More info about it can be
found [here](https://muos.dev/help/artwork#theme-overrides-for-artwork).

Also, for those who wants a template/box art set to go with that theme, you can check out **md9000**'s work here :

- [**Forum link**](https://community.muos.dev/t/custom-full-screen-box-art-for-aurora-theme-psx-gba-gbc-arcade/219)
- [**Google Drive link**](https://drive.google.com/drive/folders/169m7HGCJHYHG8wPEBulqniYe066Gieqg?usp=sharing)

## Troubleshooting

### My screen is blank / My system got bricked

That probably means the theme didn't get extracted correctly. To resolve this issue, follow those steps :

- **Shut down** your device by pressing the following button combination : <kbd>L2</kbd> + <kbd>R2</kbd> + <kbd>
  SELECT</kbd>

> [!WARNING]
> Never use the **Reset** button on the side of your device, as it is known to corrupt the OS's filesystem. Prefer using
> the hotkey shown above, also referred to as the "Safe Shutdown" hotkey.

- **Eject the SD card** on which the themes are loaded, and connect it to a computer
- **Delete** the folder `MUOS/theme/active/`
- **Plug back the SD card** in your device and turn it on, muOS's default theme should be set
- **Re-apply** Aurora from the **Theme Picker**

### The **Explore** menu is empty

That probably means something went wrong during the installation process. To resolve this issue, follow those steps :

- **Re-apply** the theme with the **Theme Picker**

### Some icons in the **Explore** menu boasts a "?" icon

That "?" icon is a fallback icon, which means, during the installation, the cion didn't get associated correctly with
the folder. This can happen for a variety of reasons. To resolve this issue, follow those steps :

- **Go** in `MUOS/info/catalogue/Folder/grid/`
- **Locate** the icon you want to associate with each unrecognized folders
- **Rename** it by said folder's name

### I can't activate Grid Mode on the "Applications" and "Collections" pages

This is by design, as I haven't made any icons for those menus. If you have your own set of icons, and want to activate
Grid Mode anyway, follow those steps :

- **Go** into `SD[1|2]/MUOS/theme/active/scheme/`
- **Delete** `muxcollect.ini` and/or `muxapp.ini`

Note that this change won't be overwritten after switching to another variant, but will if you re-apply Aurora from the
Theme Picker.

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
    - on the https://community.muos.dev/t/pixie-aurora/ (`@oiimrosabel`)

... with the error message, I'll help you troubleshoot the issue.
