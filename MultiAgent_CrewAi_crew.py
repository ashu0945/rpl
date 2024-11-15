from crewai import Crew,Process
from tasks import research_task,edit_task
from agents import research_analyst,research_editor
from IPython.display import Markdown

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[research_analyst,research_editor],
    tasks=[research_task,edit_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'Smart cities and urban planning'})

Markdown(result)

#print(result)