def reward_function(params):

    wheels_on_track = params["all_wheels_on_track"]
    steps = params["steps"]
    progress = params["progress"]
    progess_percent = progress / steps * 100
    speed = params["speed"]
    
    if (wheels_on_track and steps > 0):
        reward = progess_percent + speed
    else:
        reward = .01
    
    return float(reward)