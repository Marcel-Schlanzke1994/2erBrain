from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Config:
    database_url: str = "sqlite:///:memory:"
    log_level: str = "INFO"

    @classmethod
    def from_env(cls) -> "Config":
        return cls(os.getenv("DATABASE_URL", "sqlite:///:memory:"), os.getenv("LOG_LEVEL", "INFO"))
