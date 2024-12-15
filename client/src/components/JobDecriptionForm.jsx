import { Paper, TextField, Typography } from "@mui/material";
import PropTypes from "prop-types";

function JobDescriptionForm({jobDescription, onDescriptionChange }) {
  return (
    <Paper sx={{ padding: 2, marginBottom: 2 }}>
      <Typography variant="h6" gutterBottom>
        Job Description
      </Typography>
      <TextField
        label="Enter Job Description"
        variant="outlined"
        fullWidth
        multiline
        rows={4}
        value={jobDescription}
        onChange={(e) => onDescriptionChange(e.target.value)}
      />
    </Paper>
  );
}

JobDescriptionForm.propTypes = {
  onDescriptionChange: PropTypes.func.isRequired,
  jobDescription: PropTypes.string.isRequired,
};

export default JobDescriptionForm;
