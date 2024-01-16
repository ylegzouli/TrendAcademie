import { useState, useEffect } from "react";

import BottomNav from "./components/BottomNav";
import VideoCard from "./components/VideoCard";

function App() {
  const [videos, setvideos] = useState([]);

  const getVideos = (length) => {
    let newVideos = Array.from(Array(length).keys());
    setvideos((oldVideos) => [...oldVideos, ...newVideos]);
  };

  useEffect(() => {
    getVideos(3);
  }, []);

  return (
    <main>
      <div className="slider-container">
        {videos.length > 0 ? (
          <>
            {videos.map((video, id) => (
              <VideoCard
              key={id}
              index={id + 1}
              lastVideoIndex={videos.length - 1}
              getVideos={getVideos}
          />
            ))}
          </>
        ) : (
          <>
            <h1>Nothing to show here</h1>
          </>
        )}
      </div>

      <BottomNav />
    </main>
  );
}

export default App;
