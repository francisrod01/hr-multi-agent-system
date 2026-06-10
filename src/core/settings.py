"""Pydantic settings management for the HR multi-agent system"""

from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore" # -- ignore extra env vars (like langchain_tracing_v2)
    )

    # OpenAI
    openai_api_key: Optional[str] = None

    # Tavily search
    tavily_api_key: Optional[str] = None

    # Slack
    slack_bot_token: Optional[str] = None
    slack_channel_id: Optional[str] = None

    # Observability
    langchain_tracing_v2: bool = False
    langchain_api_key: Optional[str] = None

    # Vector DB
    chrome_persist_dir: str = "./data/benefits_db"

    # Model names
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-V2"
    llm_model: str = "gpt-4o-mini" # Start cheap, upgrade to gpt-4o later

    # Application
    environment: str = "development" # development, staging, production
    log_level: str = "INFO"


settings = Settings() # Singleton instance
