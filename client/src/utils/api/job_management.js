import axios from "../axios";

class JobManagement {
     postExtractJobInfor = async (options = {}) => {
          try {
               const response = await axios.post("jobs/extract_job_info", options);
               return response;
          } catch (error) {
               console.error("Error in postExtractJobInfor:", error);
               throw error;
          }
     }
}

const ApiJobManagement = new JobManagement();
export default ApiJobManagement;