import providers
from providers.base import ProviderProfile

MODEL_MAPPING = {
    # Gemini 3.7 series (Hybrid reasoning with dynamic/thinking levels)
    "gemini-3.7-flash": "gemini-3.5-flash-low",
    "gemini-3.7-flash-thinking": "gemini-3.5-flash-low",

    # Claude 4.6 series
    "claude-opus-4-6-thinking": "claude-opus-4-6-thinking",
    "claude-opus-4-6": "claude-opus-4-6-thinking",
    "claude-sonnet-4-6-thinking": "claude-sonnet-4-6",
    "claude-sonnet-4-6": "claude-sonnet-4-6",

    # Gemini 3.1 & 3.5 & 2.5 series
    "gemini-3.1-pro-high": "gemini-3.1-pro-low",
    "gemini-3.1-pro-low": "gemini-3.1-pro-low",
    "gemini-3.5-flash": "gemini-3.5-flash-low",
    "gemini-3-flash": "gemini-3-flash",
    "gemini-2.5-flash": "gemini-2.5-flash",
    
    # Standard compatibility aliases
    "claude-3-5-sonnet-latest": "claude-sonnet-4-6",
    "claude-3-5-sonnet-20241022": "claude-sonnet-4-6",
    "claude-3-5-sonnet-20240620": "claude-sonnet-4-6",
    "claude-3-opus-20240229": "claude-opus-4-6-thinking",
    "claude-3-5-haiku-latest": "claude-sonnet-4-6",
}

class AntigravityProfile(ProviderProfile):
    def fetch_models(
        self,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: float = 8.0,
        **kwargs
    ) -> list[str] | None:
        return list(MODEL_MAPPING.keys())

antigravity = AntigravityProfile(
    name="antigravity",
    aliases=("agy",),
    display_name="Google Antigravity",
    description="Query Gemini and Claude models directly using your Google OAuth accounts pool",
    signup_url="https://github.com/mrhisyammm/opencode-antigravity-auth",
    env_vars=("ANTIGRAVITY_API_KEY", "ANTIGRAVITY_BASE_URL"),
    base_url="http://127.0.0.1:8999/v1",
    auth_type="api_key",
    default_aux_model="gemini-3.7-flash",
    fallback_models=tuple(MODEL_MAPPING.keys()),
)

providers.register_provider(antigravity)
