import pytest
from unittest.mock import MagicMock, patch
from src.client import chat, load_prompt


def test_load_prompt_returns_string():
    content = load_prompt("assistant")
    assert isinstance(content, str)
    assert len(content) > 0


def test_load_prompt_missing_file():
    with pytest.raises(FileNotFoundError):
        load_prompt("nonexistent_prompt")


@patch("src.client.build_client")
def test_chat_returns_text(mock_build):
    mock_response = MagicMock()
    mock_response.content = [MagicMock(text="Hello from Claude")]
    mock_client = MagicMock()
    mock_client.messages.create.return_value = mock_response
    mock_build.return_value = mock_client

    result = chat("Hi")
    assert result == "Hello from Claude"


@patch("src.client.build_client")
def test_chat_with_system_prompt_uses_cache_control(mock_build):
    mock_response = MagicMock()
    mock_response.content = [MagicMock(text="ok")]
    mock_client = MagicMock()
    mock_client.messages.create.return_value = mock_response
    mock_build.return_value = mock_client

    chat("Hi", system_prompt="You are an assistant.")

    call_kwargs = mock_client.messages.create.call_args.kwargs
    system = call_kwargs["system"]
    assert system[0]["cache_control"] == {"type": "ephemeral"}


def test_build_client_raises_without_api_key(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    from src.client import build_client
    with pytest.raises(EnvironmentError):
        build_client()
