from pathlib import Path

from griptape.structures import Agent
from griptape.tools import FileManagerTool

# Initialize the FileManagerTool tool with the current directory as its base
file_manager_tool = FileManagerTool()

# Add the tool to the Agent
agent = Agent(tools=[file_manager_tool])

# Directly create a file named 'sample1.txt' with some content
filename = "sample1.txt"
content = "This is the content of sample1.txt"

Path(filename).write_text(content)

# Now, read content from the file 'sample1.txt' using the agent's command
agent.run("Can you get me the sample1.txt file?")
