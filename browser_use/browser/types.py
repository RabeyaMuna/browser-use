# centralize imports for browser typing

import sys
from typing import TYPE_CHECKING, Any

from patchright._impl._errors import TargetClosedError as PatchrightTargetClosedError
from patchright.async_api import Browser as PatchrightBrowser
from patchright.async_api import BrowserContext as PatchrightBrowserContext
from patchright.async_api import ElementHandle as PatchrightElementHandle
from patchright.async_api import FrameLocator as PatchrightFrameLocator
from patchright.async_api import Page as PatchrightPage
from patchright.async_api import Playwright as Patchright
from patchright.async_api import async_playwright as _async_patchright
from playwright._impl._errors import TargetClosedError as PlaywrightTargetClosedError
from playwright.async_api import Browser as PlaywrightBrowser
from playwright.async_api import BrowserContext as PlaywrightBrowserContext
from playwright.async_api import ElementHandle as PlaywrightElementHandle
from playwright.async_api import FrameLocator as PlaywrightFrameLocator
from playwright.async_api import Page as PlaywrightPage
from playwright.async_api import Playwright as Playwright
from playwright.async_api import async_playwright as _async_playwright

# Define types to be Union[Patchright, Playwright]
Browser = PatchrightBrowser | PlaywrightBrowser
BrowserContext = PatchrightBrowserContext | PlaywrightBrowserContext

# Page type - use Union but add accessibility attribute via TYPE_CHECKING
# The accessibility property exists on both PlaywrightPage and PatchrightPage
# but is not in the type stubs, so we need to tell the type checker about it
if TYPE_CHECKING:
	from typing import Protocol, runtime_checkable

	@runtime_checkable
	class _PageWithAccessibility(PatchrightPage, PlaywrightPage, Protocol):
		"""Protocol that combines Page types with accessibility property"""

		@property
		def accessibility(self) -> Any: ...

	# Use the union - pyright will check each type in the union
	# The _PageWithAccessibility protocol is added to tell pyright about the accessibility property
	Page = PatchrightPage | PlaywrightPage | _PageWithAccessibility
else:
	Page = PatchrightPage | PlaywrightPage

ElementHandle = PatchrightElementHandle | PlaywrightElementHandle
FrameLocator = PatchrightFrameLocator | PlaywrightFrameLocator
Playwright = Playwright
Patchright = Patchright
PlaywrightOrPatchright = Patchright | Playwright
TargetClosedError = PatchrightTargetClosedError | PlaywrightTargetClosedError

async_patchright = _async_patchright
async_playwright = _async_playwright

from playwright._impl._api_structures import (
	ClientCertificate,
	Geolocation,
	HttpCredentials,
	ProxySettings,
	StorageState,
	ViewportSize,
)

# fix pydantic error on python 3.11
# PydanticUserError: Please use `typing_extensions.TypedDict` instead of `typing.TypedDict` on Python < 3.12.
# For further information visit https://errors.pydantic.dev/2.10/u/typed-dict-version
if sys.version_info < (3, 12):
	from typing_extensions import TypedDict

	# convert new-style typing.TypedDict used by playwright to old-style typing_extensions.TypedDict used by pydantic
	ClientCertificate = TypedDict('ClientCertificate', ClientCertificate.__annotations__, total=ClientCertificate.__total__)
	Geolocation = TypedDict('Geolocation', Geolocation.__annotations__, total=Geolocation.__total__)
	ProxySettings = TypedDict('ProxySettings', ProxySettings.__annotations__, total=ProxySettings.__total__)
	ViewportSize = TypedDict('ViewportSize', ViewportSize.__annotations__, total=ViewportSize.__total__)
	HttpCredentials = TypedDict('HttpCredentials', HttpCredentials.__annotations__, total=HttpCredentials.__total__)
	StorageState = TypedDict('StorageState', StorageState.__annotations__, total=StorageState.__total__)
