import { useParams } from "react-router-dom";

const VideoPage = ({}) => {
  const { videoId } = useParams();
  console.log(videoId);
  return <div><VideoPage/></div>;
};

export default VideoPage;
