from browser_use.logging_config import setup_logging

logger = setup_logging()

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from browser_use.agent.prompts import SystemPrompt
	from browser_use.agent.service import Agent
	from browser_use.agent.views import ActionModel, ActionResult, AgentHistoryList
	from browser_use.browser import Browser, BrowserConfig, BrowserContext, BrowserContextConfig, BrowserProfile, BrowserSession
	from browser_use.controller.service import Controller
	from browser_use.dom.service import DomService

__all__ = [
	'Agent',
	'Browser',
	'BrowserConfig',
	'BrowserSession',
	'BrowserProfile',
	'Controller',
	'DomService',
	'SystemPrompt',
	'ActionResult',
	'ActionModel',
	'AgentHistoryList',
	'BrowserContext',
	'BrowserContextConfig',
]


def __getattr__(name: str):
	if name == 'SystemPrompt':
		from browser_use.agent.prompts import SystemPrompt
		return SystemPrompt
	if name == 'Agent':
		from browser_use.agent.service import Agent
		return Agent
	if name in ('ActionModel', 'ActionResult', 'AgentHistoryList'):
		from browser_use.agent.views import ActionModel, ActionResult, AgentHistoryList
		return {'ActionModel': ActionModel, 'ActionResult': ActionResult, 'AgentHistoryList': AgentHistoryList}[name]
	if name in ('Browser', 'BrowserConfig', 'BrowserContext', 'BrowserContextConfig', 'BrowserProfile', 'BrowserSession'):
		from browser_use.browser import Browser, BrowserConfig, BrowserContext, BrowserContextConfig, BrowserProfile, BrowserSession
		return {
