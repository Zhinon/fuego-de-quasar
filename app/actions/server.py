from app.actions import (
    topsecret,
    topsecret_split,
)


ACTIONS_MAP = {
    # Topsecret
    'post_get_coords_and_message': topsecret.GetCoordsAndMessageAction,
    # Topsecret_split
    'get_coords_and_message_split': topsecret_split.GetCoordsAndMessageSplit,
    'post_message_and_distance_split': topsecret_split.PostMessageAndDistanceSplit,
}
