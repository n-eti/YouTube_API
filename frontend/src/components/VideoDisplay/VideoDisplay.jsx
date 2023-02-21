import { Link } from "react-router-dom";

const VideoDisplay = ({data}) => {
    console.log(data)
  return (
    <div>
      <Link to="/"> 
      <img src={data.snippet.thumbnails.medium.url} alt="" />
      <h4>{data.snippet.title}</h4> </Link>
    </div>
  );
};

export default VideoDisplay;
