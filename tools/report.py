from langchain.tools import StructuredTool #tool that can accept multiple arguments
from pydantic.v1 import BaseModel

def write_report (filename, html):
    with open(filename, 'w') as f:
        f.write(html)

class WriteReportArgs(BaseModel):
    filename:str
    html:str

write_report_tool = StructuredTool.from_function(
    name="write_report",
    description="Write an html file to disk. Use this tool when a user asks to create a report",
    func=write_report,
    args_schema=WriteReportArgs
)