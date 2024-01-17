import { useState, useEffect } from "react";

// import BottomNav from "./components/BottomNav";
import VideoCard from "./components/VideoCard";

function App() {
  const [videos, setVideos] = useState([]);
  useEffect(() => {
  const videoUrls = [
    "http://127.0.0.1:8000/videos/0",
    "http://127.0.0.1:8000/videos/1",
    "http://127.0.0.1:8000/videos/2",
    "http://127.0.0.1:8000/videos/3",
    "http://127.0.0.1:8000/videos/4",
    "http://127.0.0.1:8000/videos/5",
    "http://127.0.0.1:8000/videos/6",
    "http://127.0.0.1:8000/videos/7",
    "http://127.0.0.1:8000/videos/8",
  ];

  const videoObjects = videoUrls.map((url, index) => ({
    id: index,
    video_files: url,
    user: { name: "Unknown", url: "#" } // Adjust as needed
  }));

  setVideos(videoObjects);
  }, []);

return (
  <main>
    <div className="slider-container">
      {videos.length > 0 ? (
        videos.map((video, id) => (
          <VideoCard
            key={id}
            index={id}
            author={video.user.name}
            videoURL={video.video_files}
            authorLink={video.user.url}
          />
        ))
      ) : (
        <h1>Nothing to show here</h1>
      )}
    </div>

    {/* <BottomNav /> */}
  </main>
);
}

export default App;