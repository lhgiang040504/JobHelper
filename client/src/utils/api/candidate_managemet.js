import axios from "../axios";

class CandidateManagement {
  postExtractCVInfor = async (options = {}) => {
    try {
      const response = await axios.post("candidates/extract_cv_info", options);
      return response;
    } catch (error) {
      console.error("Error in postExtractCVInfor:", error);
      throw error; // Bạn có thể ném lỗi này ra ngoài hoặc xử lý theo cách khác.
    }
  };

  postCreateCandidate = async (options = {}) => {
    try {
      const response = await axios.post("candidates/create_candidate", options);
      return response;
    } catch (error) {
      console.error("Error in postCreateCandidate:", error);
      throw error;
    }
  };

  getAllCandidates = async () => {
    try {
      const response = await axios.get("candidates/get_all_candidates");
      return response;
    } catch (error) {
      console.error("Error in getAllCandidates:", error);
      throw error;
    }
  };

  getCandidateById = async (id) => {
    try {
      const response = await axios.get(`candidates/get_candidate/${id}`);
      return response;
    } catch (error) {
      console.error(`Error in getCandidateById for ${id}:`, error);
      throw error;
    }
  };

  deleteCandidate = async (id) => {
    try {
      const response = await axios.delete(`candidates/delete/${id}`);
      return response;
    } catch (error) {
      console.error(`Error in deleteCandidate for ${id}:`, error);
      throw error;
    }
  };
}

const ApiCandidateManagement = new CandidateManagement();
export default ApiCandidateManagement;
