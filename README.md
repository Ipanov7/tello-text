# Tello Text
```
 ______    ____       ______        __
/_  __/__ / / /__    /_  __/____ __/ /_
 / / / -_) / / _ \    / / / -_) \ / __/
/_/  \__/_/_/\___/   /_/  \__/_\_\__/

    A text-based DJI Tello Emulator
```
## About
A DJI Tello text-based emulator. Listens to an UDP port and executes a subset of Tello commands. It is based on a fork of [tello_sim](https://github.com/Fireline-Science/tello_sim) and relies on [plotext](https://github.com/piccolomo/plotext) to plot data on a terminal.

## Why
I needed a way to execute integration tests quickly and reliably, without the hassle (and potential harm) of connecting to a real Tello. Text-based plots allow to easily visualize the flight route.

## Usage
Use Docker to build this image `docker build -t tello-text .`

In order to properly simulate the connection interface of a Tello, it is necessary to expose an UDP port when running the image

`docker run -p 18889:18889/upd -it tello-text`

If the emulator was started correctly it will log the following message

```
Connecting...
Emulator listening on 0.0.0.0:18889
```

It is now possible to test commands, for example by using a UDP client `nc -u localhost 18889`

## Supported commands
Tello commands are text-based. Any emulation session will be started/reset with `command` and terminated with `halt`.

Tello Text supports the following commands:

| Command  | Drone action  |
|----------|:-------------:|
| command |  setup drone/reset flight data |
| takeoff |  drone takes off |
| land | drone lands |
| up `z` | moves up for `z` cm|
| down `z` | moves down for `z` cm|
| left `y` | moves left for `y` cm|
| right `y` | moves right for `y` cm|
| forward `x` | moves forward for `x` cm|
| back `x` | moves back for `x` cm|
| cw `deg` | rotates clockwise for `deg` degrees |
| cw `deg` | rotates counter-clockwise for `deg` degrees |
| flip `dir` | flips in a direction (`l`, `r`, `b` or `f`) |
| halt | Closes connection and stops emulator |

## Improvements
Some possible improvements are:
* expand command set
* add cli support
* export flight data

## Disclaimer
No Tello was harmed while hacking this repo.