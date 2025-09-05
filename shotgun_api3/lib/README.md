# Lib Submodules

## Flow Production Tracking Modules

### sgutils

`sgutils` contains utility functions for string handling, encoding, and other common operations used throughout the shotgun_api3 package.

### sgtimezone

`sgtimezone` contains classes for easing the conversion between the server (UTC) timezone and client timezone.

### mockgun

Mockgun is a Flow Production Tracking API mocker. It's a class that has got *most* of the same
methods and parameters that the Flow Production Tracking API has got. Mockgun is essentially a
Flow Production Tracking *emulator* that (for basic operations) looks and feels like Flow Production Tracking.

The primary purpose of Mockgun is to drive unit test rigs where it becomes
too slow, cumbersome or non-practical to connect to a real Flow Production Tracking. Using a
Mockgun for unit tests means that a test can be rerun over and over again
from exactly the same database state. This can be hard to do if you connect
to a live Flow Production Tracking instance.

## Modern Dependencies

As of version 3.8.4+, this package uses modern system dependencies instead of bundled libraries:

- **HTTP Client**: `requests` (thread-safe, modern)
- **SSL Certificates**: System `certifi` package (automatic security updates)
- **Parsing**: System `pyparsing` package
- **Python Support**: Python 3.8+ only (no more compatibility layers)

This approach provides better security, thread safety, and maintainability compared to the
previous bundled dependency model.
