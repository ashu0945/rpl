from crewai import Task
from tools import tool
from agents import research_analyst,research_editor

# Research task
research_task = Task(
  description=(
    "Identify comprehensive and most suitable top 10 research papers in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
  ),
  expected_output='List of research papers',
  tools=[tool],
  agent=research_analyst,
)

# Writing task with language model configuration
edit_task = Task(
  description=(
    "Choose best part from the top 10 research papers and Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industries."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=research_editor,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)