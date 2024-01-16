import { useRef, useState } from "react";

import useIsInViewport from "../useIsInViewport";

const VideoCard = ({ index, lastVideoIndex, getVideos }) => {
  const elementRef = useRef();
  const isInViewport = useIsInViewport(elementRef);
  const [loadNewVidsAt, setloadNewVidsAt] = useState(lastVideoIndex);

  if (isInViewport) {
    if (loadNewVidsAt === Number(elementRef.current.id)) {
      // increase loadNewVidsAt by 2
      setloadNewVidsAt((prev) => prev + 2);
      getVideos(3);
    }
  }

  return (
    <div className="slider-children">
      <div
        ref={elementRef}
        id={index}
        style={{
          justifyContent: "center",
          alignItems: "center",
          display: "flex",
          height: "100%",
        }}
      >
        <h1>Video {index}</h1>
      </div>
    </div>
  );
};

export default VideoCard;