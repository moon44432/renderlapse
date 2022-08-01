# renderlapse: Create timelapse video from Minecraft world backups

This program creates a timelapse video from your Minecraft world backups. It requires Chunky to render a screenshot of each of the worlds, and ffmpeg to concatenate screenshots into a video.

## Prepare World Backups

You should prepare backups in a same directory for a batch rendering. Each backup should be a *full* Minecraft world which can playable in Minecraft without any modification. If your world is separated into multiple dimensions (e.g. `world`, `world_nether`, `world_the_end`), you can take just one dimension you'd like to render.

Each backup should be nested in a folder named `world-yymmdd`!

The structure of the directory should be like this:
```
..
└ world-170101
  └ world
    └ level.dat
    └ ...
└ world-170205
└ world-170316
└ world-170409
└ world-170520
└ ...
```

## Prepare JSON file (requires Chunky!)

## Rendering

## Troubleshooting