import os


def _make_tts_fn():
    def tts_fn(
        model: str, text: str, voice: str | None, speed: float | None, params: dict
    ) -> dict:
        from tts_webui_extension.parler_tts.api import tts

        return tts(
            text=text,
            description=params.get("description", "A neutral voice."),
            model_name=params.get("model_name", "parler-tts/parler-tts-mini-v1"),
            attn_implementation=params.get("attn_implementation", "eager"),
            compile_mode=params.get("compile_mode", None),
        )

    return tts_fn


def register():
    try:
        if os.environ.get("OPENAI_PROXY_HOST"):
            register_unsafe_outprocess()
        else:
            register_unsafe_inprocess()
    except Exception as e:
        print(f"Error registering Parler-TTS API adapter: {e}")
        print("Parler-TTS TTS will not be available on the OpenAI API.")


def register_unsafe_inprocess():
    from tts_webui_extension.openai_tts_api.services.tts_adapter_registry import (
        register_tts_adapter,
    )

    register_tts_adapter("parler-tts", _make_tts_fn())


def register_unsafe_outprocess():
    from tts_webui_extension.openai_tts_api.harness import setup_oai_server

    setup_oai_server(
        tts_fn=_make_tts_fn(),
        get_voices_fn=lambda model: [],
        model="parler-tts",
    )