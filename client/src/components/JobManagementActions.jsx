import { Box, Button } from "@mui/material";
import PropTypes from "prop-types";

function JobManagementActions({ onSave, onCancel }) {
  return (
    <Box sx={{ display: "flex", gap: 2, justifyContent: "flex-end" }}>
      <Button variant="contained" color="primary" onClick={onSave}>
        Save
      </Button>
      <Button variant="outlined" color="secondary" onClick={onCancel}>
        Cancel
      </Button>
    </Box>
  );
}

JobManagementActions.propTypes = {
  onSave: PropTypes.func.isRequired,
  onCancel: PropTypes.func.isRequired,
};

export default JobManagementActions;
