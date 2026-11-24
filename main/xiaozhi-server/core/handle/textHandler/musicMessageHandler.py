from typing import Any, Dict

from core.handle.textMessageHandler import TextMessageHandler
from core.handle.textMessageType import TextMessageType
from plugins_func.functions.play_netease import music_command


class MusicTextMessageHandler(TextMessageHandler):
    """Direct player commands from the kiosk: no model, no TTS."""

    @property
    def message_type(self) -> TextMessageType:
        return TextMessageType.MUSIC

    async def handle(self, conn, msg_json: Dict[str, Any]) -> None:
        action = (msg_json.get("action") or "").strip()
        value = msg_json.get("value", "")
        if action not in ("pause", "resume", "next", "prev", "stop", "seek",
                          "status", "lyrics", "playlists", "play_playlist", "playlist_tracks", "play_playlist_track", "play_index", "queue"):
            return
        await music_command(conn, action, value)
