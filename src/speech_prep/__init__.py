"""
Speech Prep - Audio preprocessing toolkit for speech-to-text applications.

This package provides tools to prepare audio files for speech-to-text processing,
including silence detection and removal, speed adjustment, and format conversion.
"""

from ._version import __version__
from .core import SoundFile
from .exceptions import (
    AudioPropertiesError,
    FFmpegError,
    FileValidationError,
    SilenceDetectionError,
    SpeechPrepError,
)

__all__ = [
    "SoundFile",
    "SpeechPrepError",
    "FFmpegError",
    "FileValidationError",
    "AudioPropertiesError",
    "SilenceDetectionError",
    "__version__",
]
