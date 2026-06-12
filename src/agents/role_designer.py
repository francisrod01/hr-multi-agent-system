"""Role Designer - generates role description using RAG and LLM."""

from src.agents.base import BaseAgent
from src.tools.rag_retriever import RAGRetriever
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from src.core.settings import settings


class RoleDesignerAgent(BaseAgent):
    async def run(self, state: dict) -> dict:
        self.log_start(state)
        topic = state["topic"]
        research = "\n".join(state.get("research_notes", []))

        # Retrieve benefits context
        retriever = RAGRetriever()
        benefits_context = retriever.retrieve_context(topic, k=3)

        # LLM generation
        llm = ChatOpenAI(model=settings.llm_model, temperature=0.7)
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert HR role designer. Output a JSON object."),
            ("user", f"""
Topic: {topic}
Research: {research}
Benefits available: {benefits_context}

Generate a job role with:
- title
- summary (2-3 sentences)
- key_responsibilities (3-5 bullet points)
- required_skills (3-5)
- recommended_benefits (2-4 from the list above)

Return valid JSON.
""")
        ])
        chain = prompt | llm
        response = await chain.ainvoke({})

        # Simple extraction (in production, use structured output)
        return {
            "drafted_role": {"raw": response.content},
            "role_description": response.content
        }
