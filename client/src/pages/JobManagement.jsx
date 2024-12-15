import { Box, Typography } from "@mui/material";
import JobDescriptionForm from "../components/JobDecriptionForm";
import JobManagementActions from "../components/JobManagementActions";
import { useState } from "react";
import ApiJobManagement from "../utils/api/job_management";
import { toast } from "react-toastify";

function JobManagement() {
  const [jobDescription, setJobDescription] = useState("");

  const handleSave = async () => {
    try {
      console.log("Saving job information:", jobDescription);
      const response = await ApiJobManagement.postExtractJobInfor({
        description: jobDescription,
      });
      console.log("API Response:", response);
      if (!response.success) {
        toast.error(response.message);
        return;
      }
    } catch (error) {
      console.error("Error saving job information:", error);
    }
  };

  const handleCancel = () => {
    setJobDescription("");
  };

  return (
    <Box sx={{ padding: 2 }}>
      <Typography variant="h4" gutterBottom>
        Job Management
      </Typography>
      <JobDescriptionForm onDescriptionChange={setJobDescription} jobDescription={jobDescription} />
      <JobManagementActions onSave={handleSave} onCancel={handleCancel} />
    </Box>
  );
}

export default JobManagement;
