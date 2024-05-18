#!/usr/bin/env python3
from sch import codex, bookmark, command, Command

TAGS = ["public", "music", "radio"]

stations = {
    "kexp": (
        "https://kexp.org/",
        "https://kexp-mp3-128.streamguys1.com/kexp128.mp3",
        "https://kexp.org/schedule/",
        "https://kexp.org/playlist/",
        "kexp independent radio, seattle",
    ),
    "wpfw": (
        "https://wpfwfm.org/radio/",
        "https://streams.pacifica.org:9000/wpfw_128",
        "https://wpfwfm.org/radio/programming/schedule-grid",
        "https://wpfwfm.org/radio/programming/playlists",
        "wpfw independent radio, dc",
    ),
    "wrir": (
        "https://www.wrir.org/",
        "https://live.wrir.org",
        "https://www.wrir.org/schedule/",
        "",
        "wrir independent radio, richmond",
    ),
}


def radio_station_command(
    url: str, stream_url: str, schedule_url: str, playlist_url: str, short_help: str
) -> Command:
    command = bookmark(url, short_help)
    command.add_bookmark("radio", stream_url, "internet radio stream")
    command.add_bookmark("schedule", schedule_url, "station schedule")
    command.add_bookmark("playlist", playlist_url, "current playlist")
    command.add_bookmark(
        "bcast", f"broadcasts://play?address={stream_url}", "broadcasts app stream"
    )

    return command


for station, config in stations.items():
    # TODO: This is not properly propagating the tags down to the "generic"
    # and tagless commands yielded by radio_station_command.
    codex.add_command(radio_station_command(*config), station, tags=TAGS)


codex.add_bookmark(
    "bcast",
    "https://apps.apple.com/us/app/broadcasts/id1469995354",
    "broadcasts internet radio app for iOS/macOS",
    tags=TAGS,
)
