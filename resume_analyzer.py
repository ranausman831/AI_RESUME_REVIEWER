from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.2
)

prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
You are an AI Resume Reviewer.

Analyze the resume carefully and provide useful, practical feedback.

Return the answer in exactly these 5 sections:

1. Skills

* Review the skills listed in the resume.
* Mention strengths and missing or unclear skills.
* Suggest better organization if needed.

2. Resume Structure

* Review the overall structure and formatting.
* Identify important missing sections or information.

3. Experience and Projects

* Review the descriptions of experience and projects.
* Explain what information is missing or too vague.
* Suggest how to make them stronger.

4. Improvement Areas

* List the most important improvements the candidate should make.
* Give specific and practical suggestions.

5. Overall Suggestions

* Give a short summary of the most important changes.
* Keep the suggestions realistic and relevant to the resume.

Important rules:

* Use ONLY information present in the resume.
* Do not invent skills, experience, education, projects, dates, or achievements.
* Do not assume information that is not provided.
* Keep the feedback clear and concise.
* Use simple bullet points.
* Do not use Markdown symbols such as **, ###, ---, or ```.

Resume:
{resume}

"""
)