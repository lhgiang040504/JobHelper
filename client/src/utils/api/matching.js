import axios from "../axios";

class Matching {
     postMatching = async (options = {}) => {
          try {
               const response = await axios.post("/jobresumematching/createJobResumeMatching", options);
               return response;
          } catch (error) {
               console.error("Error in postMatching:", error);
          }
     }
     getTopKMatching = async (job_id) => {
          try {
               const response = await axios.get(`/jobresumematching/getTopKJobResumeMatching/${job_id}`);
               return response;
          } catch (error) {
               console.error("Error in getTopKMatching:", error);
          }
     }
}

const ApiMatching = new Matching();
export default ApiMatching;