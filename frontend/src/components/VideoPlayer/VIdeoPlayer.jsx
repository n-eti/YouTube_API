import { useParams } from "react-router-dom";

const VideoPlayer = ({videoId}) => {
// let {videoId} = useParams();

  return (
    <div className='video-player'>
      <iframe
        src={`https://www.youtube.com/embed/${videoId}`}
      ></iframe>
      <h3></h3>
    </div>
  );
};

export default VideoPlayer;
