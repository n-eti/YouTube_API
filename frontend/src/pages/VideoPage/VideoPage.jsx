import { useParams } from "react-router-dom";

const VideoPage = ({}) => {
  const { videoId } = useParams();
  console.log(videoId);
  return <div>Video Page</div>;
};

export default VideoPage;
