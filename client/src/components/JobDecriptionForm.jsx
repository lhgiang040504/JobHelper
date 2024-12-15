import { TextField } from "@mui/material";
import PropTypes from "prop-types";

function JobDescriptionForm({ jobDescription, onDescriptionChange }) {
  return (
    <>
      <TextField
        label="Enter Job Description"
        variant="outlined"
        fullWidth
        multiline
        rows={6} // Tăng số hàng để người dùng có không gian lớn hơn để nhập liệu
        value={jobDescription}
        onChange={(e) => onDescriptionChange(e.target.value)}
        sx={{ resize: "vertical" }} // Cho phép người dùng thay đổi chiều cao nếu cần
      />
    </>
  );
}

JobDescriptionForm.propTypes = {
  onDescriptionChange: PropTypes.func.isRequired,
  jobDescription: PropTypes.string.isRequired,
};

export default JobDescriptionForm;
