import {
  Box,
  Typography,
  Grid,
  Button,
  CircularProgress,
  Paper,
} from "@mui/material";
import JobDescriptionForm from "../components/JobDecriptionForm";
import JobManagementActions from "../components/JobManagementActions";
import { useState } from "react";
import ApiJobManagement from "../utils/api/job_management";
import ApiCandidateManagement from "../utils/api/candidate_managemet";
import RenderTop5Candidate from "../components/RenderTop5Candidate";
import ApiMatching from "../utils/api/matching";
import { toast } from "react-toastify";
import PropTypes from "prop-types";

function JobManagement() {
  const [jobDescription, setJobDescription] = useState("");
  const [jobData, setJobData] = useState(null);
  const [loading, setLoading] = useState(false); // Trạng thái tải
  const [top5Candidates, setTop5Candidates] = useState([]); // Danh sách top 5 candidates

  const handleSave = async () => {
    try {
      const response = await ApiJobManagement.postExtractJobInfor({
        description: jobDescription,
      });
      if (!response.success) {
        toast.error(response.message);
        return;
      }
      setJobData(response.data);
    } catch (error) {
      console.error("Error saving job information:", error);
    }
  };

  const handleCancel = () => {
    setJobDescription("");
    setJobData(null);
  };

  const handleMatching = async () => {
    setLoading(true); // Bắt đầu tải
    try {
      if (!jobData) {
        toast.error("Please save the job description first.");
        return;
      }

      // Lấy danh sách candidates từ API
      const candidates = await ApiCandidateManagement.getAllCandidates();
      console.log("Candidates:", candidates);

      // Sử dụng Promise.all để gọi API đồng thời cho tất cả các candidates
      const matchingPromises = candidates.data.map(async (candidate) => {
        try {
          const response = await ApiMatching.postMatching({
            Candidate: candidate,
            JobDescription: jobData,
          });

          if (!response.success) {
            toast.error(
              `Error matching for ${candidate.name}: ${response.message}`
            );
          }
        } catch (error) {
          toast.error(`Error matching for ${candidate.name}: ${error.message}`);
          console.error(`Error matching for ${candidate.name}:`, error);
        }
      });

      // Chờ tất cả các yêu cầu hoàn thành
      await Promise.all(matchingPromises);

      toast.success("Matching process completed.");

      // Lấy top 5 candidates sau khi matching
      const top5Response = await ApiMatching.getTopKMatching(jobData._id);
      if (top5Response.success) {
        console.log(top5Response.data)
        setTop5Candidates(top5Response.data); // Cập nhật top 5 candidates
      } else {
        toast.error("Error fetching top 5 candidates.");
      }
    } catch (error) {
      console.error("Error during matching:", error);
      toast.error("An error occurred during the matching process.");
    } finally {
      setLoading(false); // Kết thúc tải
    }
  };

  return (
    <Box sx={{ padding: 2 }}>
      <Typography variant="h4" gutterBottom>
        Job Management
      </Typography>
      <Grid container spacing={2}>
        {/* Left part: Job management form */}
        <Grid item xs={12} md={6}>
          <Paper height="100%">
            <Box sx={{ padding: 2 }}>
              <JobDescriptionForm
                onDescriptionChange={setJobDescription}
                jobDescription={jobDescription}
              />
            </Box>
            <Box sx={{ padding: 2 }}>
              <JobManagementActions
                onSave={handleSave}
                onCancel={handleCancel}
              />
            </Box>
            <Button
              variant="contained"
              color="primary"
              onClick={handleMatching}
              sx={{ marginTop: 2 }}
              disabled={!jobData || loading}
            >
              {loading ? (
                <CircularProgress size={24} color="inherit" />
              ) : (
                "Top 5 Candidates"
              )}
            </Button>
          </Paper>
        </Grid>

        {/* Right part: Display job description and other relevant information */}
        <Grid item xs={12} md={6}>
          {/* Bạn có thể hiển thị thông tin jobData hoặc candidates ở đây nếu cần */}
          <Paper height="100%">
            {top5Candidates && (
              <RenderTop5Candidate top5Candidates={top5Candidates} />
            )}
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
}

RenderTop5Candidate.propTypes = {
  top5Candidates: PropTypes.array.isRequired,
};

export default JobManagement;
