from enum import Enum


class ToolName(str, Enum):
    LLM = "llm"
    RAG = "rag"
    WEB = "web"
    JAVA = "java"


class Intent(str, Enum):
    GENERAL = "general"
    SPRING_BOOT = "spring_boot"
    DEBUG = "debug"
    DSA = "dsa"
    WEB_SEARCH = "web_search"
    RAG = "rag"


class Status(str, Enum):
    INITIALIZED = "initialized"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"