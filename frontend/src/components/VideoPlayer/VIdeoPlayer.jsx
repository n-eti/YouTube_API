import { useParams } from "react-router-dom";
import React from 'react';


const VideoPlayer = ({videoId, video}) => {
console.log('The video',video)
  return (
    <div className='video-player'>
      <iframe
        src={`https://www.youtube.com/embed/${videoId}`}
      ></iframe>
      <h3>{video.snippet.title}</h3>
      <p>video description</p>
    </div>
  );
};

export default VideoPlayer;
