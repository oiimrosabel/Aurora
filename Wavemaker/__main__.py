from loguru import logger

from Wavemaker.binder.Binder import Binder
from Wavemaker.node.Node import Node

variants = ["Moon", "Cloud", "Blossom", "DMG", "Dolphin", "Midnight"]
supportedResolutions = ["640x480"]
defaultVariant = variants[0]  # Moon

root = Node(__file__).container().back()

auroraFolder = root.go("Aurora")
resourcesFolder = root.go("resources")
variantsFolder = root.go("variants")
destFolder = root.go("dist").makeDir()


def defineActive():
	activeLocation = auroraFolder.go("active.txt")
	activeLocation.write(defaultVariant)
	logger.success(f"Default variant ({defaultVariant}) defined.")


def zipAssets():
	zipLocation = auroraFolder.go("assets.muxzip")
	zipLocation.delete()
	consoleIcons = resourcesFolder.go("consoleIcons")
	consoleIcons.zip(zipLocation.path(), "muxzip")
	logger.success("Assets zipped.")


def createSchemesForVariants():
	colorsDataFolder = resourcesFolder.go(["data", "colors"])
	globalSchemeTemplate = resourcesFolder.go(["schemes", "global.ini"])
	for variant in variants:
		colorsDataFile = colorsDataFolder.go(f"{variant}.toml")
		globalSchemeFile = variantsFolder.go(
			[variant, "theme", "active", "scheme", "global.ini"]
		)
		result = Binder(
			template=globalSchemeTemplate.read(),
			data=colorsDataFile.read(),
		).mix()
		globalSchemeFile.write(result)
		logger.success(f"Schemes created for {variant}.")


def copyActive():
	defaultVariantFolder = variantsFolder.go(
		[defaultVariant, "theme", "active"]
	)
	defaultVariantFolder.mergeInto(auroraFolder.path(), overwrite=True)
	logger.success(f"Default variant ({defaultVariant}) copied.")


def setOverlays():
	overlaysFolder = resourcesFolder.go("overlays")
	for resolution in supportedResolutions:
		imagesFolder = auroraFolder.go([resolution, "image"])
		overlayImage = overlaysFolder.go(f"{resolution}.png")
		_, newImage = overlayImage.copy(imagesFolder.path())
		newImage.rename("overlay.png", True)
	logger.success("Overlays set.")


def createSchemesForResolutions():
	resolutionsDataFolder = resourcesFolder.go(["data", "resolutions"])
	defaultSchemeTemplate = resourcesFolder.go(["schemes", "default.ini"])
	for resolution in supportedResolutions:
		resolutionsDataFile = resolutionsDataFolder.go(f"{resolution}.toml")
		defaultSchemeFile = (
			auroraFolder.go([resolution, "scheme"]).makeDir().go("default.ini")
		)
		result = Binder(
			template=defaultSchemeTemplate.read(),
			data=resolutionsDataFile.read(),
		).mix()
		defaultSchemeFile.write(result)
		logger.success(f"Schemes created for {resolution}.")


def copyMuxSchemes():
	schemesFolder = resourcesFolder.go("schemes")
	muxSchemes = schemesFolder.path().glob("mux*.ini")
	activeSchemesFolder = auroraFolder.go("scheme")
	for scheme in muxSchemes:
		Node(scheme).copy(activeSchemesFolder.path())
	logger.success(f"Schemes copied in {activeSchemesFolder.path().name}.")


def zipVariants():
	auroraVariantFolder = auroraFolder.go("alternate")
	for variant in variants:
		srcVariant = variantsFolder.go(variant)
		dstZip = auroraVariantFolder.go(f"{variant}.muxzip")
		srcVariant.zip(dstZip.path(), "muxzip")
		logger.success(f"{variant} variant zipped.")


def copyGif():
	gifFile = resourcesFolder.go("gifs").go("preview.gif")
	auroraDefaultPreviewFolder = auroraFolder.go("640x480").makeDir()
	gifFile.copy(auroraDefaultPreviewFolder.path())
	logger.success("Gif copied.")


def zipAurora():
	auroraFolder.zip(destFolder.go("Aurora.muxthm").path(), "muxthm")
	logger.success("Aurora zipped.")


if __name__ == "__main__":
	defineActive()
	zipAssets()
	createSchemesForVariants()
	copyActive()
	setOverlays()
	createSchemesForResolutions()
	copyMuxSchemes()
	zipVariants()
	copyGif()
	zipAurora()
