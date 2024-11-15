from crewai import Crew,Process
from tasks import plan,write,edit
from agents import planner,writer,editor
from IPython.display import Markdown


crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=2
)


result = crew.kickoff(inputs={"topic": "Smart cities and urban planning"})