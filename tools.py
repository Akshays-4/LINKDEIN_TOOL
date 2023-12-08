from typing import Type, Optional

from pydantic import BaseModel, Field

from superagi.helper.webpage_extractor import WebpageExtractor
from superagi.llms.base_llm import BaseLlm
from superagi.tools.base_tool import BaseTool


class LinkdeinAnalysSchema(BaseModel):
    website_url: str = Field(
        ...,
        description="Valid website url without any quotes.",
    )


class LinkdeinAnalysTool(BaseTool):
    """
    Web Scraper tool

    Attributes:
        name : The name.
        description : The description.
        args_schema : The args schema.
    """
    llm: Optional[BaseLlm] = None
    name = "LinkdeinAnalysTool"
    description = (
        "Used to scrape Linkdein urls and extract specific text content"
    )
    args_schema: Type[BaseModel] = LinkdeinAnalysSchema

    class Config:
        arbitrary_types_allowed = True

    def _execute(self, website_url: str) -> tuple:
        """
        Execute the Web Scraper tool.

        Args:
            website_url : The website url to scrape.

        Returns:
            The text content of the website.
        """
        content = WebpageExtractor().extract_with_bs4(website_url)
        max_length = len(' '.join(content.split(" ")[:600]))
        return content[:max_length]