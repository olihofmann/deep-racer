def reward_function(params):

    wheels_on_track = params["all_wheels_on_track"]
    steps = params["steps"]
    progress = params["progress"]
    progess_percent = progress / steps * 100
    speed = params["speed"]

    distance_from_center = params["distance_from_center"]
    track_width = params["track_width"]
    away_from_center_percent = distance_from_center / track_width
    
    if (wheels_on_track and steps > 0 and away_from_center_percent < 0.3):
        reward = progess_percent + speed**2
    else:
        reward = .01
    
    return float(reward)