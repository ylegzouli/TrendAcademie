import { useRef, useState, useEffect } from "react";

import useIsInViewport from "../useIsInViewport";

const VideoCard = ({
  index,
  author,
  videoURL,
  authorLink,
  lastVideoIndex,
  getVideos,
}) => {
  const videoRef = useRef();
  const isInViewport = useIsInViewport(videoRef);
  const [loadNewVidsAt, setloadNewVidsAt] = useState(lastVideoIndex);
  const vid = videoURL;
  if (isInViewport) {
    setTimeout(() => {
      videoRef.current.play();
    }, 1000);

    if (loadNewVidsAt === Number(videoRef.current.id)) {
      setloadNewVidsAt((prev) => prev + 1);
      getVideos(3);
    }
  }

  const togglePlay = () => {
    let currentVideo = videoRef.current;
    if (currentVideo.paused) {
      currentVideo.play();
    } else {
      currentVideo.pause();
    }
  };

  useEffect(() => {
    if (!isInViewport) {
      videoRef.current.pause();
    }
  }, [isInViewport]);

  return (
    <div className="slider-children">
      <video
        muted
        className="video"
        ref={videoRef}
        onClick={togglePlay}
        id={index}
        autoPlay
      >
        <source src={vid} type="video/mp4" />
      </video>
      <div className="video-content" onClick={togglePlay}>
        <p>@{author}</p>
      </div>
    </div>
  );
};

export default VideoCard;