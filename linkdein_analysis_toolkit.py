from abc import ABC
from typing import List
from superagi.tools.base_tool import BaseTool, BaseToolkit, ToolConfiguration
from LINKDEIN_TOOL.tools import LinkdeinAnalysTool
from superagi.types.key_type import ToolConfigKeyType

class LinkdeinAnalysisToolkit(BaseToolkit, ABC):
    name: str = "Linkdein Analysis Toolkit"
    description: str = "Linkdein Analysis Tool kit is used to scrape linkdein"

    def get_tools(self) -> List[BaseTool]:
        return [
            LinkdeinAnalysTool(),
        ]

    def get_env_keys(self) -> List[ToolConfiguration]:
        return []
