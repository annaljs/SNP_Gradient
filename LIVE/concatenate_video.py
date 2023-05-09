def concate(video_clip_path, nums, output_path, method="compose"):
    """Concatenates several video files into one video file
    and save it to `output_path`. Note that extension (mp4, etc.) must be added to `output_path`
    `method` can be either 'compose' or 'reduce':
        `reduce`: Reduce the quality of the video to the lowest quality on the list of `video_clip_paths`.
        `compose`: type help(concatenate_videoclips) for the info"""
    # create VideoFileClip object for each video file
    video_clip_paths=[]
    nums = int(nums)
    '''for n in range( 1, nums + 1 ) : 
        path =  video_clip_path[0] + str(n) + ".avi"
        video_clip_paths += [path]
        path = ""
        print(n)
    '''
    for i in range( 1, nums+1 ): # num_iter
        path = ""
        path = os.path.join( video_clip_path[0], "{}.avi".format(i))
        print(path)
        video_clip_paths += [path]



    clips = [VideoFileClip(c) for c in video_clip_paths]
    if method == "reduce":
        print("reduce")
        # calculate minimum width & height across all clips
        min_height = min([c.h for c in clips])
        min_width = min([c.w for c in clips])
        # resize the videos to the minimum
        clips = [c.resize(newsize=(min_width, min_height)) for c in clips]
        # concatenate the final video
        final_clip = concatenate_videoclips(clips)
    elif method == "compose":
        print("compose")
        # concatenate the final video with the compose method provided by moviepy
        for c in clips :
            print(clips)
        final_clip = concatenate_videoclips(clips, method="compose")
    # write the output video file
    final_clip = speedx(final_clip, factor=20)
    final_clip.write_videofile(output_path)


if __name__ == "__main__":
    import argparse
    from moviepy.editor import *
    from moviepy.video.fx.all import *
    parser = argparse.ArgumentParser(
        description="Simple Video Concatenation script in Python with MoviePy Library")
    parser.add_argument("-c", "--clips", nargs="+",
                        help="List of audio or video clip paths")
    parser.add_argument("-n", "--nums", 
                        help="numbers of audio or video clip ")
    parser.add_argument("-r", "--reduce", action="store_true", 
                        help="Whether to use the `reduce` method to reduce to the lowest quality on the resulting clip")
    parser.add_argument("-o", "--output", help="Output path")
    args = parser.parse_args()
    clips = args.clips
    nums = args.nums
    output_path = args.output
    reduce = args.reduce
    method = "reduce" if reduce else "compose"
    concate(clips, nums, output_path, method)