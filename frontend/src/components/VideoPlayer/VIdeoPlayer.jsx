import { useParams } from "react-router-dom";

const VideoPlayer = ({}) => {
let {videoId} = useParams();

  return (
    <div>
      <iframe
        id="ytplayer"
        width="640"
        height="360"
        src={`https://www.youtube.com/embed/${videoId}`}
        frameborder="0"
      ></iframe>
    </div>
  );
};

export default VideoPlayer;
