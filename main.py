from utils.video_utils import read_video, save_video
from trackers import Tracker
import cv2
from team_assigner import TeamAssigner
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

def main():
    # Read Video
    video_frames = read_video('input_videos/08fd33_4.mp4')

    # Initialize Tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='stubs/track_stubs.pkl')

    # # save cropped image of a player
    # for track_id, player in tracks['players'][0].items():
    #     print(track_id,player)
    #     bbox = player['bbox']
    #     print(bbox)
    #     frame = video_frames[0]
    #     # crop bbox from frame
    #     cropped_image = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]
    #     #save the cropped image
    #     cv2.imwrite(f'outpot_videos/cropped_img.jpg', cropped_image)
    #     break

    # Interpolate Ball Positions
    tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])

    # Assign Player Teams
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], 
                                    tracks['players'][0])
    
    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num],   
                                                 track['bbox'],
                                                 player_id)
            tracks['players'][frame_num][player_id]['team'] = team 
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

    


    # Draw output 
    ## Draw object Tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks)

     # Save video
    save_video(output_video_frames, 'output_videos/output_video_interpolate_ball_positions.avi')

if __name__ == '__main__':

    main()