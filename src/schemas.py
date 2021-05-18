from pydantic import BaseModel


class Offer(BaseModel):
    sdp: str
    type: str
    video_transform: str = None
