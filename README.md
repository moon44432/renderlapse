# renderlapse: Create timelapse video from Minecraft world backups

[![A 8-Year Timelapse of Minecraft MoonServer](http://img.youtube.com/vi/wACIDyN1eAw/0.jpg)](https://youtu.be/wACIDyN1eAw)  
This program creates a timelapse video from your Minecraft world backups. It uses Chunky to generate screenshots of each of the worlds, and ffmpeg to concatenate screenshots into a video.

## Preparing World Backups

You should prepare backups in the same directory for a batch rendering. Each backup should be a *full* Minecraft world which can be played in Minecraft without any modification. If your world is separated into multiple dimensions (e.g. `world`, `world_nether`, `world_the_end`), you can take just one dimension you'd like to render.

Every backup should be contained within a folder named `world-yymmdd`!

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

## Preparing JSON file (requires Chunky)

Create a preset JSON scene file so that Chunky can reuse it to render multiple worlds with the same camera angle and settings.

![](assets/chunkytutorial.png)

1. Load one of your backup worlds.
2. Select chunks to render. **If you want to shoot a timelapse from the very beginning of your world, it might not be enough with only one preset. If that's the case, see 9.**
3. Load selected chunks.
4. Canvas size. 1920 * 1080 is recommended.
5. Un-check all entities.
6. Set the camera. You can do this in Render Preview tab as well.
7. Set target SPP(Samples Per Pixel). 64 or above is recommended.
8. Save the scene.
9. **Be careful - Chunky throws an error or produces weird artifacts when it tries to render empty chunks. If your early backups are not big enough to completely fill the scene's chunk range, just duplicate the scene and manually reduce the chunk range to fit in older worlds.**

## Rendering (requires Chunky & ffmpeg)

### Rendering frames: ```render```, ```ren```

```python renderlapse.py --chunky-root CHUNKY_ROOT [--chunky-jar CHUNKY_JAR] [--scene-dir SCENE_DIR] --scene-name SCENE_NAME render --backup-dir BACKUP_DIR --world WORLD [--jre-path JRE_PATH] [--jre-mem JRE_MEM] [--jre-arg JRE_ARG] [--chunky-arg CHUNKY_ARG]```.  
Brackets around a parameter indicate that it is optional. For help, type ```python renderlapse.py render -h```.

### Generating video: ```genvideo```, ```vid```

```python renderlapse.py --chunky-root CHUNKY_ROOT [--chunky-jar CHUNKY_JAR] [--scene-dir SCENE_DIR] --scene-name SCENE_NAME genvideo [--ffmpeg-path FFMPEG_PATH] [--ffmpeg-arg FFMPEG_ARG] [--framerate FRAMERATE] [--vid-path VID_PATH] [--frame-duration FRAME_DURATION] [--sync]```.  
Brackets around a parameter indicate that it is optional. For help, type ```python renderlapse.py genvideo -h```.

## Troubleshooting

### Chunky throws ```java.lang.NullPointerException: Cannot invoke "String.equals(Object)" because the return value of "se.llbit.chunky.world.Chunk.getVersion()" is null```  

This error occurs when Chunky attempts to render chunks that have not been generated. It happens when you try to render an early backup which is smaller than the preset chunk range. See (9) at **Preparing JSON file**.
