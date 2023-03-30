import axios from "axios";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import VideoPlayer from "../../components/VideoPlayer/VIdeoPlayer";

const VideoPage = ({}) => {
  const { videoId } = useParams();
  const [video, setVideo] = useState(null)

  async function fetchVIdeo(){
    const api_key = "AIzaSyACDkhVL41ty7K077xwrNiTYj6KKsdizoQ"
    const response = await axios.get(`https://youtube.googleapis.com/youtube/v3/videos?part=snippet&id=${videoId}&key=${api_key}`)
  setVideo('Video stuff',response.data.items[0]);
}

  useEffect(()=>{
    fetchVIdeo()
  }, [videoId]) 

  console.log(videoId);
  return video && (<div><VideoPlayer videoId={videoId} video={video}/></div>);
};

export default VideoPage;
