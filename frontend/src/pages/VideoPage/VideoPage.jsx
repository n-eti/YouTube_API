import { useParams } from "react-router-dom";
import VideoPlayer from "../../components/VideoPlayer/VIdeoPlayer";

const VideoPage = ({}) => {
  const { videoId } = useParams();
  console.log(videoId);
  return <div><VideoPlayer/></div>;
};

export default VideoPage;
